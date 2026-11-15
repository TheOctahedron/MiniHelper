from core import (
    show_help, change_display_title,
)

UTILITY_COMMANDS = {
    "help": {"command_function": show_help, 
        "args_need": "0",
        "description": "Displays all commands and their descriptions"}, 


    "change_display_title": {"command_function": change_display_title,
        "args_need": "0",
        "description": "Disables/Enables the display of the CLI title"}, 
}