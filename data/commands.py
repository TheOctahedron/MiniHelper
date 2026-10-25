from core import plus, minus, divide, multiply

COMMANDS = {
    "plus": plus,
    "minus": minus,
    "divide": divide, 
    "multiply": multiply
}

# Generate numeric aliases
# Copy the dictionary so we can safely iterate and add to it
for index, func in enumerate(COMMANDS.copy().values(), start=1):
    COMMANDS[str(index)] = func
