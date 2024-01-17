import random
from Flugzeug import Flugzeug
import json
from datetime import datetime
from flask import Flask, render_template, request
from Utilities import get_data_folder
import os


    
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


def main():
    app = Flask(__name__, template_folder=f"{get_data_folder()}/templates/")

    """
        Route für die Jeweiligen Seiten.

        Returns:
            str: Die gerenderte HTML-Seite für die Homepage.
    """

    @app.route("/")
    def home():
        '''try:
            with open(f"{get_data_folder()}/data/Flugzeug.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(f"/data/{name}.json", "r", encoding="utf8") as f:
                self.data = json.loads(f.read())
               
        
        sorted_data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1]["Flugdaten"]["abflugzeit"])}
        
        for plane_model, flight_data in data.items(): flight_data["Flugdaten"]["abflugzeit"] = datetime.strptime(flight_data["Flugdaten"]["abflugzeit"], "%Y-%m-%dT%H:%M:%S.%f")
        for plane_model, flight_data in data.items(): flight_data["Flugdaten"]["ankunftzeit"] = datetime.strptime(flight_data["Flugdaten"]["ankunftzeit"], "%Y-%m-%dT%H:%M:%S.%f")
        '''
        
        data = ""
        for i in range(10):
            newFlugzeug = Flugzeug()
            data +=(f", {newFlugzeug.flugnummer}: [{newFlugzeug.abflugzeit}, {newFlugzeug.ankunftzeit}, {newFlugzeug.fluggesellschaft}]")
        
        data = f"{{{data}}}"
        print(data)  
        sorted_data = sorted(data)
        
        #sorted_data.append(get_Fluggesellschaft())
        result = render_template("Flugplan.html", data=sorted_data)

                    
        return render_page(result)
    
    @app.route("/Erweitert")
    def Erweitert():
        return "todo"    
    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()
