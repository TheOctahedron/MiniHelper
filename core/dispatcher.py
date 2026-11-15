from data import ALL_COMMANDS

def dispatch(command_key, *args):
    if command_key not in ALL_COMMANDS:
        raise KeyError("Command not found."
        "\nNeed help? Enter 'minihelper HELP'")

    return ALL_COMMANDS[command_key]["command_function"](*args) # Searching command by key "command_function".