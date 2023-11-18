from flask import Flask
from controllers.notes import notes
from controllers.users.users import user_bp
from controllers.notes.notes import note_bp

app = Flask(__name__)

app.register_blueprint(user_bp)
app.register_blueprint(note_bp)


if __name__  == "__main__":
    app.run(
        debug=True,
        port=3000
    )
