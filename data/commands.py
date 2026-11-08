from core import (
    show_help, change_display_title,

    plus, minus, divide, multiply, 
    raise_to_power, percent,

    txt_lower, txt_reverse, txt_upper,

)

COMMANDS = {
    "help": show_help,
    "change_display_title": change_display_title,

    "plus": plus,
    "minus": minus,
    "divide": divide, 
    "multiply": multiply,
    "raise_to_power": raise_to_power,
    "percent": percent,

    "txt_lower": txt_lower,
    "txt_reverse": txt_reverse, 
    "txt_upper": txt_upper,
    
}

# Generate numeric aliases
# Copy the dictionary so we can safely iterate and add to it
counter = 1
for key, func in COMMANDS.copy().items():
    if key != "help":
        COMMANDS[str(counter)] = func
        counter += 1
