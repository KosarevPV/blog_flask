from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from blog_flask.models import User, Post
from blog_flask import db
from blog_flask import create_app

app = create_app()

admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
