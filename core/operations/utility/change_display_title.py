import os, json

CONFIG_PATH = os.path.join("data", "config.json")

def change_display_title(*args):
    """
    Toggles the title display (ON/OFF).
    """

    # Read the current configuation from the JSON file, and load this in var 'config'.
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)

    # Toggle the display_title setting.
    config["display_title"] = not config.get("display_title", True)


    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

    if config["display_title"] == True:
        return "The display of title is enabled."
    else:
        return "The display of title is disabled."
