import argparse, os, json
from core.dispatcher import dispatch

CONFIG_PATH = os.path.join("data", "config.json")

def main():
    show_title = True # Default value.
    try:
        # Read the current configuation from the JSON file, and load this in var 'config'.
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            config = json.load(f)
            show_title = config.get("display_title", True)
    except Exception as e:
        print(f"ERROR: {e}")

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

        match cmd_key:
            case "help":
                result = dispatch(cmd_key)
            case _:
                result = dispatch(cmd_key, a, b)


        # Universal output handler (works for float, int, str, etc.)
        if result is not None and result != "":
            if isinstance(result, float) and result.is_integer():
                print(int(result))
            else:
                print(result)

    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()