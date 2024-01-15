import sys
import os


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