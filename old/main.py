def render_page(contentName, text=None):
    """
    Rendert eine HTML-Seite basierend auf Vorlagen und Inhalten.

    Args:
        contentName (str): Der Name des Inhalts, der gerendert werden soll.
        text (str, optional): Ein zusätzlicher Text, der in die Seite eingefügt werden soll.

    Returns:
        str: Der gerenderte HTML-Code für die Seite.
    """
    with open(f"{get_data_folder()}/templates/index.html", "r", encoding="utf8") as f:
        result = f.read()
    with open(f"{get_data_folder()}/templates/head.html", "r", encoding="utf8") as f:
        result = result.replace("$head$", f.read())
    
    with open(f"{get_data_folder()}/templates//nav.html", "r", encoding="utf8") as f:
        result = result.replace("$nav$", f.read())

    if os.path.exists(f"{get_data_folder()}/templates/{contentName}.html"):
        with open(f"{get_data_folder()}/templates/{contentName}.html", "r", encoding="utf8") as f:
            result = result.replace("$content$", f.read())
    else:
        result = result.replace("$content$", contentName)

        

    if text is not None:
        result = result.replace("$text$", text)
    return result

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