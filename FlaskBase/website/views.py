from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views',__name__)

#HOME
@views.route('/')
@login_required
def home():
    return render_template("home.html", usuario=current_user)