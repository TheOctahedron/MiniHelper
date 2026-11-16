def show_help(passed_group=""): 
    from data import ALL_COMMANDS, ALL_GROUPS

    def show_all_groups():
        print()
        for group_key in ALL_GROUPS.keys(): # Take the keys for all groups for output
            print(f"* {group_key.removesuffix('_GROUP')}") # Beautiful output without a suffix
        print("* ALL") # Sign ALL, since it is not in ALL_GROUPS

        print("Usage: minihelper help <group_key>")
        return ""

    # Add uppercase letters (this is necessary for finding the function in ALL_GROUPS) and convert to a str.
    passed_group = str(passed_group or "").upper() 
    match passed_group:
        case "":
            return show_all_groups()
        case "ALL":
            selected_group = "ALL"
        case _:
            selected_group = passed_group + "_GROUP" # Add the necessary suffix.


    print("Usage: can use 'mh' instead of 'minihelper'\n")

    if selected_group in ALL_GROUPS.keys(): # Check if selected group exists
        selected_group = ALL_GROUPS[selected_group]

    elif selected_group == "ALL":
        selected_group = ALL_COMMANDS

    else:
        print()
        print("This Group is not found.")
        return show_all_groups()


    print("Usage: minihelper <command> [args]")


    saved_numeric_aliases = [numeric_aliase for numeric_aliase in selected_group 
        if numeric_aliase.isdigit()]
    
    saved_numeric_aliases.sort(key=int) # Sort like integer.


    print("ALL COMMANDS. ALL ARE NUMBERED (NUMERIC ALIASES)\n")

    for numeric_alias in saved_numeric_aliases:
        command_value = selected_group[numeric_alias] # Find the command value using a numeric alias.

        for key, value in selected_group.items():
            # Check whether this key is a numeric alias and whether it is appropriate for the function.
            if not key.isdigit() and command_value['command_function'] == value['command_function']:
                command_key = key
                break

        print(f"* {command_key:<20} ({numeric_alias})")
        print(f"  {command_value['description']}")
        if "formula" in command_value: # Checking whether this command has a formula.
            print(f"  {command_value['formula']}")
        print("---")
    return ""