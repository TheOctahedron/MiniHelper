from core import (
    show_help, change_display_title,

    plus, minus, divide, multiply, 
    raise_to_power, percent,

    txt_lower, txt_reverse, txt_upper,

)

COMMANDS = {
    "help": {"command_function": show_help, 
        "args_need": "0",
        "description": "Displays all commands and their descriptions"}, 


    "change_display_title": {"command_function": change_display_title,
        "args_need": "0",
        "description": "Disables/Enables the display of the CLI title"}, 

    # ====================

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

    # ====================

    "txt_lower": {"command_function": txt_lower, 
        "args_need": "1 (a: str)",
        "description": "Outputs 'a' in lowercase",
        "formula": "str(a).lower()"}, 


    "txt_reverse": {"command_function": txt_reverse, 
        "args_need": "1 (a: str)",
        "description": "Outputs 'a' in reverse",
        "formula": "str(a)[::-1]"}, 


    "txt_upper": {"command_function": txt_upper, 
        "args_need": "1 (a: str)",
        "description": "Outputs 'a' in uppercase",
        "formula": "str(a).upper()"}
    
}

# Generate numeric aliases
# Copy the dictionary so we can safely iterate and add to it
counter = 1
for key, data in COMMANDS.copy().items():
    if key != "help":
        COMMANDS[str(counter)] = data
        counter += 1
