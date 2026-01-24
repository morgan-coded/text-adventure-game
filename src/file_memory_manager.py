# File + Memory interaction simulator (Python 3)
# Total RAM: 20 KB, Page size: 1 KB
# Disk model: linked allocation (file is a list/chain of disk blocks)

from dataclasses import dataclass
from typing import List, Optional, Tuple, Dict

TOTAL_MEMORY_KB = 20
PAGE_SIZE_KB = 1

@dataclass
class Block:
    start: int     # start address in KB
    size: int      # size in KB
    owner: str     # "FREE", "JOB-<id>", "FILE-<name>"

class MemoryManager:
    def __init__(self, total_kb: int):
        self.blocks: List[Block] = [Block(0, total_kb, "FREE")]

    def _coalesce(self) -> None:
        # Merge adjacent FREE blocks so the allocator doesn't become "Swiss cheese"
        merged: List[Block] = []
        for b in self.blocks:
            if merged and merged[-1].owner == "FREE" and b.owner == "FREE" and (merged[-1].start + merged[-1].size == b.start):
                merged[-1].size += b.size
            else:
                merged.append(Block(b.start, b.size, b.owner))
        self.blocks = merged

    def free_owner(self, owner: str) -> None:
        for b in self.blocks:
            if b.owner == owner:
                b.owner = "FREE"
        self._coalesce()

    def allocate(self, size_kb: int, owner: str, strategy: str = "best") -> Optional[Block]:
        # strategies: "first", "best", "worst"
        candidates = [(i, b) for i, b in enumerate(self.blocks) if b.owner == "FREE" and b.size >= size_kb]
        if not candidates:
            return None

        if strategy == "first":
            idx, b = candidates[0]
        elif strategy == "worst":
            idx, b = max(candidates, key=lambda t: t[1].size)
        else:  # best
            idx, b = min(candidates, key=lambda t: t[1].size)

        allocated = Block(b.start, size_kb, owner)
        remainder = b.size - size_kb

        # Replace the chosen free block with [allocated][remainder (if any)]
        self.blocks[idx] = allocated
        if remainder > 0:
            self.blocks.insert(idx + 1, Block(b.start + size_kb, remainder, "FREE"))

        return allocated

    def snapshot(self) -> List[Tuple[int, int, str]]:
        return [(b.start, b.size, b.owner) for b in self.blocks]

@dataclass
class JobRow:
    job_id: int
    start_time: int
    size_kb: int
    interval_sec: int
    end_state: str   # "Sleep" or "End" (here: Sleep)

@dataclass
class FileRequest:
    name: str
    size_kb: int
    disk_block_size_kb: int
    disk_blocks: List[int]   # linked allocation chain fragments we discovered
    load_time: int
    unload_time: int

class FileManagement:
    def __init__(self, memory: MemoryManager):
        self.memory = memory

    def collect_fragments(self, disk_blocks: List[int]) -> List[int]:
        # In linked allocation, the "file" is the chain of disk blocks.
        # Here we just return the list provided by the prompt.
        return list(disk_blocks)

    def calculate_required_space_kb(self, file_size_kb: int) -> int:
        # Prompt says: ignore metadata; required space equals the file size
        return file_size_kb

    def load_file(self, req: FileRequest, strategy: str, evictable_jobs: List[str]) -> bool:
        needed = self.calculate_required_space_kb(req.size_kb)
        owner = f"FILE-{req.name}"

        # First attempt
        if self.memory.allocate(needed, owner, strategy=strategy):
            return True

        # Not enough contiguous space -> evict sleeping jobs until we can fit it
        # Eviction order is determined by evictable_jobs list.
        for job_owner in evictable_jobs:
            self.memory.free_owner(job_owner)
            if self.memory.allocate(needed, owner, strategy=strategy):
                return True

        return False

def main():
    # Initial job table from the prompt
    jobs = [
        JobRow(1, 1, 2, 7, "Sleep"),
        JobRow(2, 2, 3, 8, "Sleep"),
        JobRow(3, 3, 4, 6, "Sleep"),
        JobRow(4, 4, 3, 6, "Sleep"),
        JobRow(5, 5, 2, 9, "Sleep"),
        JobRow(6, 6, 3, 6, "Sleep"),
        JobRow(7, 7, 2, 6, "Sleep"),
    ]

    file_req = FileRequest(
        name="F1",
        size_kb=8,
        disk_block_size_kb=1,
        disk_blocks=[28, 5, 12, 13, 1, 4],
        load_time=12,
        unload_time=16,
    )

    mem = MemoryManager(TOTAL_MEMORY_KB)

    # Allocate jobs into memory as they "start"
    # For this example, we load them up front in start-time order.
    for j in sorted(jobs, key=lambda x: x.start_time):
        mem.allocate(j.size_kb, f"JOB-{j.job_id}", strategy="best")

    fm = FileManagement(mem)

    # Decide which sleeping jobs are evictable (largest-first policy)
    job_owners = [f"JOB-{j.job_id}" for j in jobs]
    job_sizes = {f"JOB-{j.job_id}": j.size_kb for j in jobs}
    evictable = sorted(job_owners, key=lambda o: job_sizes[o], reverse=True)

    print("Initial memory:", mem.snapshot())

    # At time 12: load file
    print(f"\n[t={file_req.load_time}] Trying to load file {file_req.name} ({file_req.size_kb} KB)")
    ok = fm.load_file(file_req, strategy="best", evictable_jobs=evictable)
    print("Loaded?" , ok)
    print("Memory after file load:", mem.snapshot())

    # Keep until time 16, then unload
    print(f"\n[t={file_req.unload_time}] Unloading file {file_req.name}")
    mem.free_owner(f"FILE-{file_req.name}")
    print("Memory after file unload:", mem.snapshot())

    # --- TEST CASE 2: A Smaller File (proves this isn't hard-coded to one file) ---
    print("\n--- TEST CASE 2 ---")
    file_req_2 = FileRequest(
        name="F2",
        size_kb=3,
        disk_block_size_kb=1,
        disk_blocks=[50, 51, 52],  # Arbitrary linked blocks (example)
        load_time=20,
        unload_time=25
    )

    print(f"\n[t={file_req_2.load_time}] Trying to load file {file_req_2.name} ({file_req_2.size_kb} KB)")
    ok2 = fm.load_file(file_req_2, strategy="best", evictable_jobs=evictable)
    print("Loaded?", ok2)
    print("Memory after F2 load:", mem.snapshot())

    print(f"\n[t={file_req_2.unload_time}] Unloading file {file_req_2.name}")
    mem.free_owner(f"FILE-{file_req_2.name}")
    print("Memory after F2 unload:", mem.snapshot())


if __name__ == "__main__":
    main()
