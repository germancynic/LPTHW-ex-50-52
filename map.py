# OLDEHAVER Michel 21/01/2018

class Scene(object):
    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

# Scene 1: Opening
opening_scene = Scene("Helms Klamm", "opening_scene",
"""
Vor dir oeffnet sich das Klammtal, eine gewaltige Schlucht im weissen Gebirge, durch
die sich die Fluesse des Thrihyrne schlaengeln. Am Ende des Tals erstreckt sich eine
maechtige Hornburg, die gleichzeitig den Eingang zu den glitzernden Grotte stellt.

Das ist Helms Klamm! Die letzte Bastion Rohans, das Erbe der Dunedain.

Doch es herrscht keine Eintracht in Mittelerde. Duestere Maechte streben nach
Einfluss. Im einst gruenen Isengart hat Saruman der weisse Zauberer eine maechtige
Armee von Uruk-hai erschaffen. Zehntausend der Ork-Mensch-Mischlinge sind gesandt
worden, die letzte Bastion der freien Menschen Rohans zu nehmen!
Und du wirst sie verteidigen! Auf geht es in die erste intelligente Verteidigung
Helms Klamm seit Anbeginn der Zeit!

Die erste Entscheidung steht an, moechtest du deine Streitkraefte auf die Hornburg
zentrieren oder die gesamte Wehranlage mit dem Klammwall halten?

    Gebe [1] ein, wenn du auschliesslich die Hornburg halten willst oder
    entscheide dich fuer [2], wenn die gesamte Klamm gehalten wird.
""")

#Scene 2: Decision whole or inner castle
decision_hornburg = Scene("Hornburg", "decision_hornburg",
"""
Du hast dich entschieden deine Truppen auf die Hornburg zu verlagern, die Zugaenge
vom Klammwall wurden gekappt. Eine weise Entscheidung, General!

Doch wie positionieren wir die Truppen?
Zur Erinnerung; die Reiterei ist Rohans Elite, die mit Speeren, Aexten und
Schwertern bewaffneten Krieger, sind auch in der Lage zum Bogen zu wechseln.

Rohans schwache Bogen- und Armbrsutschuetzen werden durch
elbische Elite Soldaten aus dem Waldreichen verstaerkt. Ihr Anfuehrer ist Haldir.

Die Helden zur freien Verfuegung stehen sind Gimli, Aragorn und Legolas.
Sie sind meisterhafte Kaempfer und zusammen beinahe jeder Gefahr gewachsen.

Es gibt drei Moeglichkeiten deine Truppen zu positionieren:
Gib [1] ein, damit die Helden im offenen Feld, die Reiter in der Burg und die
Bogenschuetzen auf den Mauern Stellung beziehen.
Mit [2] schickst du die Helden auf die Torrampe, die Reiter in das freie Feld
und die Schuetzen auf die Mauern der Hornburg.
[3] laesst die Rohirrim auf den Mauern Platz finden, die Bogen auf der Rampe
und die Helden in der Burg.
""")

decision_anlage = Scene("Die gesamte Klamm", "decision_anlage",
"""
Du hast dich dafuer entschieden, die gesamte Anlange zu halten. Mein junger General,
du hast leider wenig in deiner Ausbildung gelernt. Die feindlichen Truppen sprengen
den Wall und stuermen die Festung.

Druecke Submit ohne weitere Eingabe, um das Spiel abzuschliessen.
""")

#Scene 3: Decision troop placement
troop_one = Scene("Truppenaufstellung", "troop_one",
"""
Pferde in der gesamten Burg behindern die Laufwege. Aragorn, Gimli und
Legolas stehen hoffnungslso unterlegen auf freiem Feld. Immerhin sind
die Schuetzen auf der Mauer. Das rettet die Burg allerdings nicht.

Druecke Submit ohne weitere Eingabe, um das Spiel abzuschliessen.
""")

troop_two = Scene("Truppenaufstellung", "troop_two",
"""
Bravo! Du hast schonmal ein Strategiespiel gespielt. Die Reiter im Feld reiben
die Reihen der Feinde von ihrer Flanke auf, waehrend deine Helden das Tor
verteidigen. Pfeile hageln von den Zinnen und dezimieren die Reihen der Gegner.

Das hast du gut gemacht, mein unerfahrender General!

Du wirst noch viele Schlachten im Ringkrieg schlagen, doch Siege bringen uns nach
Mordor.

Druecke Submit ohne weitere Eingabe, um das Spiel abzuschliessen.
""")

troop_three = Scene("Truppenaufstellung", "troop_three",
"""
Waehrend deine Reiterei nutzlos auf der Mauer steht werden die Bogenschuetzen
nahezu wehrlos von der Rampe gestossen. Deine sonst schlagkraeftigen Helden in
der Burg koennen dem Desaster nur zusehen.

Druecke Submit ohne weitere Eingabe, um das Spiel abzuschliessen.
""")

#Scene 4: Winning scenario
end_winner = Scene("Sieg", "end_winner",
"""
Du hast es geschafft, trotz 10.000 Uruks, Sarumans Magie und ihrem Kriegsgeraet,
hast du die Burg durch kluge Entscheidungen vor dem Untergang bewahrt.

Tolkien waere stolz auf dich... oder auch nicht, weil wir gerade seine Buecher
reinterpretieren.
""")

#Scene 5: Losing scenarios
end_death_1 = Scene("Niederlage", "end_death_1",
"""
Waehrend der Feind die Reihen der Gefallenen nach Ueberlebenden durchsucht,
sieht du in der Ferne das weisse Pferd Schattenfell. Gandalf ist gekommen!
Es gibt noch Hoffnung, ist der letzte Gedanke bevor ein orkischer Speer
dein Herz durchbohrt.

Druecke Submit ohne weitere Eingabe und starte noch einmal.

""")

end_death_2 = Scene("Niederlage", "end_death_2",
"""
Die Klammburg bisher unbezwungen wurde unter deiner Kontrolle gestuermt.
Waehrend du am Boden liegst und zusiehst, wie immer mehr Feinde in die
Burg dringen, wird dir das volle Ausmass deines Scheiterns bewusst.
Dein letzter Gedanke ist die Vision Isengarts, welches vom Wasser
verschlungen wird.

Druecke Submit ohne weitere Eingabe und starte noch einmal.
""")

end_death_3 = Scene("Niederlage", "end_death_3",
"""
Die Klammburg bisher unbezwungen wurde unter deiner Kontrolle gestuermt.
Waehrend du am Boden liegst und zusiehst, wie immer mehr Feinde in die
Burg dringen, wird dir das volle Ausmass deines Scheiterns bewusst.
Dein letzter Gedanke ist die Vision Isengarts, welches vom Wasser
verschlungen wird.

Druecke Submit ohne weitere Eingabe und starte noch einmal.
""")


generic_death = Scene("Gescheitert", "death", "You died.")


opening_scene.add_paths({
    '1': decision_hornburg,
    '2': decision_anlage,
    '*': generic_death
})

decision_hornburg.add_paths({
    '1': troop_one,
    '2': troop_two,
    '3': troop_three,
    '*': generic_death
})

decision_anlage.add_paths({
    '*': end_death_1
})

troop_one.add_paths({
    '*' : end_death_2
})

troop_two.add_paths({
    '*': end_winner
})

troop_three.add_paths({
    '*': end_death_3
})

SCENES = {
    opening_scene.urlname: opening_scene,
    decision_hornburg.urlname: decision_hornburg,
    decision_anlage.urlname: decision_anlage,
    generic_death.urlname: generic_death,
    troop_one.urlname: troop_one,
    troop_two.urlname: troop_two,
    troop_three.urlname: troop_three,
    end_death_1.urlname: end_death_1,
    end_death_2.urlname: end_death_2,
    end_winner.urlname: end_winner,
    end_death_3.urlname: end_death_3
}
START = opening_scene