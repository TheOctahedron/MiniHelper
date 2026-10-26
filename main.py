import argparse
from core.dispatcher import dispatch

def main():
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