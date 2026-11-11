def show_help(*args):
    from data.commands import COMMANDS

    # Command key = Command name 

    print("Usage: ")
    print("minihelper <command> [args]")
    print("mh <command> [args]")

    # Identify suitable commands for help output, store in 'saved_commands', excluding digit names and 'help'.
    saved_commands = [command_key for command_key in COMMANDS.keys() 
        if not command_key.isdigit() and command_key != "help"]

    print("ALL COMMANDS ARE NUMBERED (NUMERIC ALIASES)")

    # We begin a loop for each CLI command.
    for command_key in sorted(saved_commands):
        command = COMMANDS[command_key]

        numeric_aliase = "?" # The value is initially set to "?" in case it is not found.

        # Searching for a numeric alias in the COMMANDS keys
        for key in COMMANDS.keys():
            if key.isdigit() and COMMANDS[key]["command_function"] == command["command_function"]:
                numeric_aliase = key
                break

        # We are not using the more appropriate name "command_key" so as to avoid any confusion.

        # Display all information about the CLI command
        print("\n")
        print(f"* {command_key} ({numeric_aliase})")
        print(f"[{command['description']}]")

        if "formula" in command:
            print(f"[{command['formula']}]")

    # A reminder about the "help" command
    print("\nhelp - show all commands")
    print("END OF COMMANDS.")
    return