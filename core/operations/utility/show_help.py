def show_help(a=""):
    from data import ALL_COMMANDS, ALL_GROUPS
    selected_group = str(a).upper()

    # ===================================

    print("Usage: ")
    print(" minihelper <command> [args]")
    print(" mh <command> [args]")
    print("\n")

    if selected_group in ALL_GROUPS.keys():
        print(f"SELECTED GROUP: {selected_group}")
        group_commands = ALL_GROUPS[selected_group]

    elif selected_group in ["ALL_GROUPS", "ALL"]:
        group_commands = ALL_COMMANDS

    else:
        print("All CLI COMMANDS GROUP KEYS")
        for group_key in ALL_GROUPS.keys():
            print(f"* {group_key}")
        print("* ALL_COMMANDS/ALL")
        print("\nEND OF COMMANDS GROUPS KEYS")


        print("\n")
        print("Usage to get information about each command in the selected group: ")
        print(" minihelper help <group_key>")
        print(" mh help <group_key>")
        return 

    # ===================================

    # Command Key = Command Name
    # Identify suitable commands for help output, store in 'saved_commands', excluding digit names and 'help'
    saved_commands = [command_key for command_key in group_commands.keys() 
        if not command_key.isdigit() and command_key != "help"]

    print("ALL COMMANDS ARE NUMBERED (NUMERIC ALIASES)")

    # We begin a loop for each CLI command.
    for command_key in sorted(saved_commands):
        command = group_commands[command_key]

        numeric_aliase = "?" # The value is initially set to "?" in case it is not found

        # Searching for a numeric alias in the COMMANDS keys
        for key in group_commands.keys():
            if key.isdigit() and group_commands[key]["command_function"] == command["command_function"]:
                numeric_aliase = key
                break

        # We are not using the more appropriate name "command_key" so as to avoid any confusion

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