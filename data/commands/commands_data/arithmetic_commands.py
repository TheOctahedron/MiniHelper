from core import (
    plus, minus, divide, multiply, 
    raise_to_power, percent,
)

ARITHMETIC_COMMANDS = {
    "plus": {"command_function": plus, 
        "args_need": "2 (a: int/float, b: int/float)",
        "description": "Adds 'a' to 'b'",
        "formula": "a + b"},


    "minus": {"command_function": minus, 
        "args_need": "2 (a: int/float, b: int/float)",
        "description": "Subtracts 'b' from 'a'",
        "formula": "a - b"},


    "divide": {"command_function": divide, 
        "args_need": "2 (a: int/float, b: int/float)",
        "description": "Divides 'a' by 'b'",
        "formula": "a / b"},


    "multiply": {"command_function": multiply, 
        "args_need": "2 (a: int/float, b: int/float)",
        "description": "Multiplies 'a' by 'b'",
        "formula": "a * b"},


    "raise_to_power": {"command_function": raise_to_power, 
        "args_need": "2 (a: int/float, b: int/float)",
        "description": "Raises 'a' to the power of 'b', uses pow()",
        "formula": "pow(a, b)"},


    "percent": {"command_function": percent, 
        "args_need": "2 (a: int/float, b: int/float)",
        "description": "Finds 'b' percent of 'a'",
        "formula": "(a / 100) * b"}, 
}