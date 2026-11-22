from data.commands.add_numeric_aliases import add_numeric_aliases

from data.commands.commands_data.api_commands import API_COMMANDS
from data.commands.commands_data.arithmetic_commands import ARITHMETIC_COMMANDS
from data.commands.commands_data.text_commands import TEXT_COMMANDS
from data.commands.commands_data.utility_commands import UTILITY_COMMANDS

# Create dict for all CLI commands groups 
ALL_GROUPS = {
    "API_COMMANDS": API_COMMANDS,
    "ARITHMETIC_GROUP": ARITHMETIC_COMMANDS,
    "TEXT_GROUP": TEXT_COMMANDS,
    "UTILITY_GROUP": UTILITY_COMMANDS,
}

# Create empty dict for all CLI commands (raw: without numeric aliases)
RAW_ALL_COMMANDS = {}

# Add all raw (raw: without numeric aliases) commands from each group (ALL_GROUPS)
for group_commands in ALL_GROUPS.values():
    RAW_ALL_COMMANDS.update(**group_commands) # Unpacking each group of commands


# Add numeric aliases for all groups, and save them
for group_name, group_commands in ALL_GROUPS.items():
    ALL_GROUPS[group_name] = add_numeric_aliases(group_commands) 

# Add numeric aliases for all commands
ALL_COMMANDS = add_numeric_aliases(RAW_ALL_COMMANDS) 


__all__ = [
    "ALL_GROUPS", "ALL_COMMANDS"
]