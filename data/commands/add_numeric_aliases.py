def add_numeric_aliases(group_commands): # Accept the all CLI commands (from group)
    counter = 1
    result = group_commands.copy()
    # Take the key and value for each command
    for command_key, command_value in group_commands.items():
        # Check whether it is not equal to digit (to avoid numbering a numeric alias) or "help" (no numeric alias required)
        if not command_key.isdigit() and command_key != "help":
            result[str(counter)] = command_value
            counter += 1
    return result