import random
from Flughafen import Flughafen
from Flugzeug import Flugzeug
from Feuerwehr import Feuerwehr

from flask import Flask, render_template, request


EinFlughafen = Flughafen("IBB", [Flugzeug(_passagiere=-1) for i in range(random.randint(5,10))], 1)

Feuerwehren = [Feuerwehr]

def get_contents():
    return [["$Flughafen$", f"{EinFlughafen}"], ["$Flugzeuge$", EinFlughafen.get_flugzeuge()], ["$FlugzeugeDropDown$", EinFlughafen.get_FlugzeugeDropDown()]]

def render_page(contentName, text=None):
    with open("templates/index.html", "r", encoding="utf8") as f:
        result = f.read()
    with open("templates/head.html", "r", encoding="utf8") as f:
        result = result.replace("$head$", f.read())
    with open("templates/nav.html", "r", encoding="utf8") as f:
        result = result.replace("$nav$", f.read())
    with open(f"templates/{contentName}.html", "r", encoding="utf8") as f:
        result = result.replace("$content$", f.read())

    for content in get_contents():
        result = result.replace(content[0], content[1].replace("\n", "<br \>"))
        result = result.replace(content[0], content[1].replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;"))        

    if text is not None:
        result = result.replace("$text$", text)
    return result

def main():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_page("home")

    @app.route("/Flughafen")
    def Flughafen():
        return render_page("Flughafen")

    @app.route("/Flugzeuge")
    def Flugzeuge():
        return render_page("Flugzeuge")

    @app.route("/Flugzeug_landen")
    def Flugzeug_landen():
        text = EinFlughafen.landen(Flugzeug(_passagiere=-1))
        return render_page("FlugzeugLanden", text)

    @app.route("/Flugzeug_starten")
    def Flugzeug_starten():
        text = EinFlughafen.start()
        return render_page("FlugzeugStarten", text)

    @app.route("/Gebaeude_reinigen")
    def Gebaeude_reinigen():
        text = EinFlughafen.Gebaeude_reinigen()
        return render_page("GebaeudeReinigen", text)

    @app.route("/aussteigen")
    def aussteigen():
        text = EinFlughafen.aussteigen()
        return render_page("aussteigen", text)
    
    @app.route("/umsteigen")
    def umsteigen():
        flugzeug = request.args.get('flugzeug')
        if flugzeug is not None:
            EinFlughafen.flugzeuge[flugzeug]
        text = ""
        return render_page("umsteigen", text)
    
    # Webserver starten

    app.run(port=8080, debug=False)


if __name__ == '__main__':
    main()