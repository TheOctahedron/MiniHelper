from data.commands import COMMANDS

def dispatch(cmd_key, *args):
    if cmd_key not in COMMANDS.keys():
        raise("Command not found."
        "\nNeed help? Enter 'minihelper HELP'")

    return COMMANDS[cmd_key](*args) # Searching command by key.