from flask import Blueprint, render_template
from apps.app import db
from apps.crud.models import User, UserImage

dt = Blueprint("detector", __name__, template_folder="templates")


@dt.route("/")
def index():
    user_images = (
        db.session.query(User, UserImage).filter(User.id == UserImage.user_id).all()
    )
    return render_template("detector/index.html", user_images=user_images)
