#!/usr/bin/env python3
"""
Memory Allocation Simulator (Best/First/Worst Fit)

This simulator demonstrates dynamic memory allocation using three different
allocation strategies:
- Best Fit: Allocates the smallest free block that fits the job
- First Fit: Allocates the first free block that fits the job
- Worst Fit: Allocates the largest free block that fits the job

Features:
- Free-block coalescing to prevent fragmentation
- Job table processing from Study.com assignment
- Output showing memory state at each tick
- Analysis of fragmentation for each strategy

TODO: Add the complete implementation from your coursework
Expected features:
- Job table with start times, sizes, and durations
- Three allocation strategies (Best/First/Worst fit)
- Coalescing of adjacent free blocks
- Memory state output at each time tick
- Analysis comparing the three strategies

Capstone upgrade ideas:
- Add unit tests for coalescing and each fit strategy
- Add a mode that outputs a fixed-width "memory map" line (20 cells) per tick
- Add CLI args: --strategy best|first|worst, --input jobs.csv, --until T
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Job:
    """Represents a job with memory requirements"""
    job_id: int
    arrival_time: int
    size_kb: int
    duration: int


@dataclass
class MemoryBlock:
    """Represents a block of memory"""
    start: int
    size: int
    job_id: Optional[int]  # None if free


class MemoryAllocator:
    """Simulates memory allocation with different strategies"""

    def __init__(self, total_memory_kb: int):
        self.total_memory = total_memory_kb
        self.blocks: List[MemoryBlock] = [MemoryBlock(0, total_memory_kb, None)]

    def allocate_best_fit(self, job: Job) -> bool:
        """Allocate memory using Best Fit strategy"""
        # TODO: Implement best fit allocation
        pass

    def allocate_first_fit(self, job: Job) -> bool:
        """Allocate memory using First Fit strategy"""
        # TODO: Implement first fit allocation
        pass

    def allocate_worst_fit(self, job: Job) -> bool:
        """Allocate memory using Worst Fit strategy"""
        # TODO: Implement worst fit allocation
        pass

    def deallocate(self, job_id: int) -> None:
        """Free memory occupied by a job"""
        # TODO: Implement deallocation
        pass

    def coalesce(self) -> None:
        """Merge adjacent free blocks"""
        # TODO: Implement coalescing
        pass

    def display_memory_state(self) -> None:
        """Display current memory allocation state"""
        # TODO: Implement memory state display
        pass


def main():
    """Main simulation loop"""
    print("Memory Allocation Simulator")
    print("=" * 50)
    print()
    print("TODO: Add your job table and simulation logic here")
    print()
    print("Expected output:")
    print("- Memory state at each tick")
    print("- Jobs allocated/deallocated")
    print("- Fragmentation analysis")
    print("- Comparison of Best/First/Worst fit strategies")


if __name__ == "__main__":
    main()
