from core import (
    show_help, 

    plus, minus, divide, multiply, 
    raise_to_power, percent
)

COMMANDS = {
    "help": show_help,

    "plus": plus,
    "minus": minus,
    "divide": divide, 
    "multiply": multiply,
    "raise_to_power": raise_to_power,
    "percent": percent,
    
}

# Generate numeric aliases
# Copy the dictionary so we can safely iterate and add to it
counter = 1
for key, func in COMMANDS.copy().items():
    if key != "help":
        COMMANDS[str(counter)] = func
        counter += 1
