import random
from Flughafen import Flughafen
from Flugzeug import Flugzeug
import json
from datetime import datetime
from flask import Flask, render_template, request
from Utilities import get_data_folder
import os

EinFlughafen = Flughafen("IBB", [Flugzeug(_passagiere=-1) for i in range(random.randint(5,10))], 1)


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

def get_Fluggesellschaft():
    Fluggesellschaften = ["SkyLink Airways", "Horizon Wings",
        "CelestialJet",
        "AeroVista Airlines",
        "StarLift Air",
        "CloudSail Airlines",
        "BlueSky Express",
        "SolarWings International",
        "VelocityAir",
        "NovaJet Airways"
    ]
    return random.choice(Fluggesellschaften)
    
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

    for content in get_contents(EinFlughafen):
        result = result.replace(content[0], content[1].replace("\n", "<br \>"))
        result = result.replace(content[0], content[1].replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;"))        

    if text is not None:
        result = result.replace("$text$", text)
    return result


def main():
    app = Flask(__name__, template_folder=f"{get_data_folder()}/templates/")

    """
        Route für die Jeweiligen Seiten.

        Returns:
            str: Die gerenderte HTML-Seite für die Homepage.
    """

    @app.route("/")
    def home():
        try:
            with open(f"{get_data_folder()}/data/Flugzeug.json", "r") as file:
                data = json.load(file)
                print(type(data))
        except FileNotFoundError:
            with open(f"/data/{name}.json", "r", encoding="utf8") as f:
                self.data = json.loads(f.read())
                
        sorted_data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1]["Flugdaten"]["abflugzeit"])}
        
        for plane_model, flight_data in data.items(): flight_data["Flugdaten"]["abflugzeit"] = datetime.strptime(flight_data["Flugdaten"]["abflugzeit"], "%Y-%m-%dT%H:%M:%S.%f")
        for plane_model, flight_data in data.items(): flight_data["Flugdaten"]["ankunftzeit"] = datetime.strptime(flight_data["Flugdaten"]["ankunftzeit"], "%Y-%m-%dT%H:%M:%S.%f")
        
        #sorted_data.append(get_Fluggesellschaft())
        result = render_template("Flugplan.html", data=sorted_data)

                    
        return render_page(result)
    
    @app.route("/Erweitert")
    def Erweitert():
        return "todo"
    
    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()
