from src.memory import *
from src.alu_instructions import *
from src.emulator import*
import pytest
import subprocess

# List of program names
programs = ["fact","fib","min","pointers","sieve"]


@pytest.mark.parametrize("program_name", programs)
def test_program(program_name):
    # Construct file names
    program_file = f"{program_name}.s"
    out_file = f"{program_name}.out"

    command = ["python3", "__main__.py", f"data/asm/{program_file}" ]

    result = subprocess.run(command, capture_output=True, text=True)
    actual_output = result.stdout.strip()

    try:
        with open(f"data/outputs/{out_file}", "r") as f:
            expected_output = f.read().strip()
    except FileNotFoundError:
        print(f"Expected output file not found")

    assert actual_output == expected_output


