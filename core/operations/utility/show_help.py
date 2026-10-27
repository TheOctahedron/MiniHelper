def show_help(*args):
    from data.commands import COMMANDS
    print("An open-source CLI tool designed to solve minor inconveniences: \n")
    print("ALL COMMANDS ARE NUMBERED (NUMERIC ALIASES)\n")

    # Use only the text-based command keys, not the numeric aliases.
    text_commands = [key for key in COMMANDS.keys() if not key.isdigit() and key != "help"] 

    # Sort and print all text-based command keys, and numeric aliases
    for cmd_name in sorted(text_commands):
        numeric_aliase = "?"
        
        for key in COMMANDS.keys(): # Search all keys
            # Check if the key is a digit AND if it points to the same function as cmd_name
            if key.isdigit() and COMMANDS[key] == COMMANDS[cmd_name]:
                numeric_aliase = key


        print(f"* {cmd_name:<15} ({numeric_aliase})")
        

    print("\nEND OF COMMANDS.")

    return ""