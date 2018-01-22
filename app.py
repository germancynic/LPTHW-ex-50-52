from flask import Flask, session, request
from flask import url_for, redirect, render_template
import map

app = Flask(__name__)

@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:
        # another html instead of you_dies for more precise information
        return render_template('wrong_input.html')

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'scene' in session:
        if map.SCENES[session['scene']] is 'end_winner':
                return render_template('you_won.html')
        elif userinput is None:
            # more precise information
            return render_template('wrong_input.html')
        else:
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
                # There's no transition for that user input.
                # what should your code do in response?
                return render_template('you_died.html')
            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene)
    else:
        return render_template('connection_error')

# This URL initializes the session with starting values
@app.route('/')
def index():
    session['scene'] = map.START.urlname
    return redirect(url_for('game_get')) # redirect the browser to the url for game_get

app.secret_key = 'cp46ta'

if __name__ == "__main__":
    app.run()