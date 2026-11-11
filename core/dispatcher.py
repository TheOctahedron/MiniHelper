from data.commands import COMMANDS

def dispatch(command_key, *args):
    if command_key not in COMMANDS:
        raise KeyError("Command not found."
        "\nNeed help? Enter 'minihelper HELP'")

    return COMMANDS[command_key]["command_function"](*args) # Searching command by key "command_function".