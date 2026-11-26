from data.commands.add_numeric_aliases import add_numeric_aliases

from data.commands.commands_data.api_commands import API_COMMANDS
from data.commands.commands_data.arithmetic_commands import ARITHMETIC_COMMANDS
from data.commands.commands_data.text_commands import TEXT_COMMANDS
from data.commands.commands_data.utility_commands import UTILITY_COMMANDS


# Create dict for all raw (temporary variable) CLI commands GROUPS 
RAW_ALL_GROUPS = {
    "API_GROUP": API_COMMANDS,
    "ARITHMETIC_GROUP": ARITHMETIC_COMMANDS,
    "TEXT_GROUP": TEXT_COMMANDS,
    "UTILITY_GROUP": UTILITY_COMMANDS,
}

# Create empty dict for all raw (without numeric aliases) CLI COMMANDS
RAW_ALL_COMMANDS = {}

# Add all raw (raw: without numeric aliases) commands from each raw group (RAW_ALL_GROUPS)
for group_commands in RAW_ALL_GROUPS.values():
    duplicate_group_commands = RAW_ALL_COMMANDS.keys() & group_commands.keys()
    if duplicate_group_commands:
        raise ValueError (
            f"ERROR: Duplicate command names: {duplicate_group_commands}"
        )
    RAW_ALL_COMMANDS.update(group_commands) 

# Add numeric aliases for all commands
ALL_COMMANDS = add_numeric_aliases(RAW_ALL_COMMANDS) 

ALL_GROUPS = { # Create a new dict: ALL_GROUPS
    group_name: {
        
        command_key: command_value # set the correct architecture

        for command_name in group_commands # take the command name for subsequent work
        for command_key, command_value in ALL_COMMANDS.items() 

        if command_value["command_function"] == group_commands[command_name]["command_function"]

    }
    for group_name, group_commands in RAW_ALL_GROUPS.items()
}

__all__ = [
    "ALL_GROUPS", "ALL_COMMANDS"
]