import argparse, json, sys
from pathlib import Path
from core.dispatcher import dispatch

"""
'__file__' is a special module variable. It contains the path to the file in which it is defined.
'Path(__file__)' converts a string into a pathlib.Path object.
'.resolve()' returns the absolute path of the file.
'.parent' returns the parent directory of the file.
"""

BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "data" /"config.json"


def main():
    show_title = True # Default value.
    try:
        # Read the current configuation from the JSON file, and load this in var 'config'.
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            config = json.load(f)
            show_title = config.get("display_title", True)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"ERROR: {e}", file=sys.stderr)

        # Create the parent directory for the 'config.json' file if it doesn't exist.
        CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)

        # Open and write the default configuration to the 'config.json'.
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump({"display_title": True}, f, indent=4)

    if show_title:
        print("--- MiniHelper ---")

    # Create parser.
    parser = argparse.ArgumentParser(description="MiniHelper-CLI")

    # Parse arguments: 

    # cmd argument.
    parser.add_argument("cmd", type=str, help="Enter the text name or numeric alias of the command you need." \
    "\nNeed help? Enter 'minihelper HELP'") 

    # 'a' argument (the first one).
    parser.add_argument("a", type=float, nargs="?", help="Enter argument 'a' (the first one) " \
    "required for the command.")

    # 'b' argument (the second one).
    parser.add_argument("b", type=float, nargs="?", help="Enter argument 'b' (the second one) " \
    "required for the command.")


    # Parse the command-line arguments and store them in an args object
    args = parser.parse_args()

    try:
        cmd_key = args.cmd.lower()
        a = args.a
        b = args.b 

        match a, b:
            case (None, None): # For 0 argument commands.
                result = dispatch(cmd_key)
            case (_, None): # For 1 argument commands .
                result = dispatch(cmd_key, a)
            case _: # For 2 argument commands.
                result = dispatch(cmd_key, a, b)


        # Universal output handler (works for float, int, str, etc.)
        if result is not None and result != "":
            if isinstance(result, float) and result.is_integer():
                print(int(result))
            else:
                print(result)

    except (ValueError, KeyError, TypeError) as e:
        """
        'file=sys.stderr' separates the error from what should go into the standart output (stdout).
        'sys.exit(1)' indicates that the program has exited with an error code (1).
        """
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()