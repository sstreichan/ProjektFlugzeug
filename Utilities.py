import sys
import os
import json

def get_data_folder():
    """
    Gibt den Pfad zum Datenordner zurück, unabhängig davon, ob das Skript als ausführbare Datei oder als Skript ausgeführt wird.

    Returns:
        str: Der Pfad zum Datenordner.
    """
    if getattr(sys, 'frozen', False):
        data_folder_path = sys._MEIPASS
    else:
        data_folder_path = os.path.dirname(
            os.path.abspath(sys.modules['__main__'].__file__)
        )
    return data_folder_path


def loadJSON(name):
    """
    Lädt Daten aus einer JSON-Datei und aktualisiert das 'data'-Attribut der Klasse.

    Args:
        name (str): Der Name der JSON-Datei (ohne die Dateierweiterung).

    Returns:
        None
    """
    try:
        with open(f"{get_data_folder()}/data/{name}.json", "r", encoding="utf8") as f:
            return json.loads(f.read())
    except FileNotFoundError:
        with open(f"/data/{name}.json", "r", encoding="utf8") as f:
            returnjson.loads(f.read())