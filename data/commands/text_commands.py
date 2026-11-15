from core import (
    txt_lower, txt_reverse, txt_upper,
)

TEXT_COMMANDS = {
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