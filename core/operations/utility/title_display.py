title_display = True # The title display is enabled by default
def title_display():
    if title_display == False:
        title_display = True
        return "\nThe display of Title is enabled."
    title_display = False
    return "\nThe display of Title is disabled."
    