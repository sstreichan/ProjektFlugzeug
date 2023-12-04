import random
from Flughafen import Flughafen
from Flugzeug import Flugzeug
from Feuerwehr import Feuerwehr

from flask import Flask, render_template

def menu():
    result = "--------------------------------------------------\n"
    result += "Was möchtest du tun?\n"
    result += "1. Überschicht Flughafen\n"
    result += "2. Übersicht Flugzeuge\n"
    result += "3. Flugzeug landen\n"
    result += "4. Flugzeug starten\n"
    result += "5. Exit\n"
    result += "--------------------------------------------------\n"
    return result


EinFlughafen = Flughafen("IBB", [Flugzeug(_passagiere=-1), Flugzeug(_passagiere=-1)], 1)

Feuerwehren = [Feuerwehr]

'''while True:
    print(menu())
    match input():
        case "1":
            print(EinFlughafen)
        case "2":
            print(get_flugzeuge)
        case "3":
            neues_flugzeug = Flugzeug(random.choice(list(get_flugzeuge().keys())))
            neues_flugzeug.passagiere_einsteigen(random.randint(0, neues_flugzeug.passagiere_max))
            EinFlughafen.landen(neues_flugzeug)
        case "4":
            pass
        case "5":
            pass'''

contents = [["$Flughafen$", f"{EinFlughafen}"], ["$Flugzeuge$", EinFlughafen.get_flugzeuge()]]

def get_contents():
    return [["$Flughafen$", f"{EinFlughafen}"], ["$Flugzeuge$", EinFlughafen.get_flugzeuge()]]

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
    return render_page("FlugzeugStarten")

@app.route("/Gebaeude_reinigen")
def Gebaeude_reinigen():
    text = EinFlughafen.Gebaeude_reinigen()
    return render_page("GebaeudeReinigen", EinFlughafen.Gebaeude_reinigen())

# Webserver starten
app.run(host="0.0.0.0", port=80, debug=False)