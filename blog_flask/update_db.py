from blog_flask import create_app
from blog_flask import db


app = create_app()
app.app_context().push()
db.create_all()
