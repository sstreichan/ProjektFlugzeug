for content in get_contents(EinFlughafen):
        result = result.replace(content[0], content[1].replace("\n", "<br \>"))
        result = result.replace(content[0], content[1].replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;"))    

def get_contents(einFlughafen):
    """
    Gibt eine Liste von Inhalten zurück, die in der HTML-Seite eingefügt werden sollen.

    Args:
        einFlughafen (Flughafen): Das Flughafen-Objekt, dessen Informationen in die Seite eingefügt werden sollen.

    Returns:
        list: Eine Liste von Listen, wobei jede innere Liste den Platzhalter und den zugehörigen Inhalt enthält.
    """
    return [
        ["$Flughafen$", f"{einFlughafen}"],
        ["$Flugzeuge$", einFlughafen.get_flugzeuge()],
       # ["$FlugzeugeDropDown$", einFlughafen.get_FlugzeugeDropDown()]
    ]