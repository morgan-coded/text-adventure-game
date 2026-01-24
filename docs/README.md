# Documentation

This directory contains the original project write-ups and documentation.

## Expected Files

Add your original coursework documentation here:

- `cpu_alu_project.docx` - CPU/ALU Logisim write-up with instruction-set, opcode table, and assembly pseudo-programs
- `number_systems_assignment.docx` - Number systems conversions, truth tables, and boolean expressions
- `memory_management_project.docx` - Memory allocation simulator documentation (Best/First/Worst fit)
- `file_management_memory_project.docx` - File management + memory interaction documentation
- `realtime_scheduling_simulator.docx` - Real-time scheduling simulator documentation (RM/DM/EDF)

## Format

Documents can be in DOCX format or exported to PDF. Keep the original Word documents for editability.

## Assembly Snippets (from CPU/ALU Project)

Example assembly code from the CPU/ALU project:

```assembly
    CMP R1, R2       ; set zero flag if R1 == 0
    BEQ END          ; exit loop when the new operand is zero
    ADD R0, R1       ; accumulate R1 into R0
    JMP LOOP         ; repeat
```

```assembly
    CMP R0, R2       ; is the register all ones?
    BEQ END          ; if so, stop shifting (prevents infinite loop)
    AND R1, R0, R3   ; pseudo-code: copy R0 -> R1, then AND with R3 (R3 = 0x01)
    CMP R1, R4       ; is the LSB zero?
    BEQ END          ; stop if LSB is zero
    JMP LOOP         ; continue shifting
```
