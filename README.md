# asm-emulator

## RISC-V Assembly Interpreter

This project implements an interpreter for a subset of the RISC-V assembly language. It reads and executes RISC-V assembly instructions, simulating their behavior as closely as possible.

### Features
- Interprets core RISC-V instructions, including arithmetic, memory operations, and control flow.
- Supports immediate and register-based operations.
- Handles branch instructions for conditional execution.
- Includes support for `ecall` operations.

### Command Reference
Below is a table of supported RISC-V commands, their syntax, and descriptions:

| **Command**   | **Syntax**            | **Description**      |
|---------------|-----------------------|-----------------------|
| **LB**        | `lb rd, offset(rs1)`  | Load byte            |
| **LH**        | `lh rd, offset(rs1)`  | Load half-word       |
| **LW**        | `lw rd, offset(rs1)`  | Load word            |
| **SB**        | `sb rs2, offset(rs1)` | Store byte           |
| **SH**        | `sh rs2, offset(rs1)` | Store half-word      |
| **SW**        | `sw rs2, offset(rs1)` | Store word           |
| **J**         | `j label`             | Unconditional jump   |
| **CALL**      | `call label`          | Jump and link        |
| **BEQ**       | `beq rs1, rs2, label` | Branch if equal      |
| **BNE**       | `bne rs1, rs2, label` | Branch if not equal  |
| **BLT**       | `blt rs1, rs2, label` | Branch if less than  |
| **BGE**       | `bge rs1, rs2, label` | Branch if greater or equal |
| **BGT**       | `bgt rs1, rs2, label` | Branch if greater than |
| **BLE**       | `ble rs1, rs2, label` | Branch if less or equal |
| **ADDI**      | `addi rd, rs1, imm`   | Add immediate        |
| **ADD**       | `add rd, rs1, rs2`    | Add registers        |
| **MUL**       | `mul rd, rs1, rs2`    | Multiply registers   |
| **MULI**      | `muli rd, rs1, imm`   | Multiply immediate   |
| **DIV**       | `div rd, rs1, rs2`    | Divide registers     |
| **REM**       | `rem rd, rs1, rs2`    | Remainder of division|

### ECALL Operations
The interpreter supports the following `ecall` operations:
- **`x10 = 1`**: Prints the word stored in the `x11` register.
- **`x10 = 10`**: Exits the program.
- **`x10 = 11`**: Prints the byte stored in the `x11` register.

### How It Works
The interpreter parses a RISC-V assembly file and executes instructions sequentially. It maintains a simulated CPU state, including:
- **Registers**: Emulates the RISC-V register set (`x1` to `x33`).
- **Memory**: Simulates a combined stack and heap of 10,000 bytes.

Control flow instructions (e.g., jumps and branches) modify the `PC` to allow conditional and looping behavior.

### Usage

#### Testing the Interpreter
Run the test suite to verify correctness:
```bash
make test
```

#### Running a Specific Assembly File
You can execute a specific assembly file by passing its path as an argument to the main Python script:
```bash
python3 __main__.py <path-to-asm-file>
```
For example:
```bash
python3 __main__.py data/asm/fib.s
```

Ensure that the assembly file contains valid RISC-V instructions supported by this interpreter and that pytest is installed for running texts

---
For additional details, refer to the source code or documentation within the project.

