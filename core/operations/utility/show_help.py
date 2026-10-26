def show_help():
    from data.commands import COMMANDS
    print("An open-source CLI tool designed to solve minor inconveniences: \n")
    print("ALL COMMANDS ARE NUMBERED (NUMERIC ALIASES)\n")

    # Use only the text-based command keys, not the numeric aliases.
    text_commands = [key for key in COMMANDS.keys() if not key.isdigit()] 

    # Sort and print all text-based command keys
    for cmd in sorted(text_commands):
        print(f"* {cmd}")

    print("\nEND OF COMMANDS.")

    return ""