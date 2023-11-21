from flask import Flask
from controllers.notes import notes
from controllers.users import users
from controllers.category import category

app = Flask(__name__)

# user services
app.add_url_rule("/user", methods=["POST"], view_func=users.add_new_user)
app.add_url_rule("/login", methods=["POST"], view_func=users.login_user)

# note services
app.add_url_rule("/note", methods=["POST"], view_func=notes.add_new_note)
app.add_url_rule("/assign-note", methods=["POST"], view_func=notes.assign_note)
app.add_url_rule("/note", methods=["GET"], view_func=notes.get_user_notes)
app.add_url_rule("/category-note/<catid>", methods=["GET"], view_func=notes.get_category_notes)

# category service
app.add_url_rule("/category", methods=["POST"], view_func=category.add_category)
app.add_url_rule("/category", methods=["GET"], view_func=category.get_cagtegories)


if __name__  == "__main__":
    app.run(
        debug=True,
        port=3000
    )
