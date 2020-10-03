# Outside imports
from flask import Blueprint, render_template

bp_main = Blueprint('bp_main', __name__)


@bp_main.route("/")
@bp_main.route("/home")
def home():
    return render_template('home.html', title='Home')

@bp_main.route("/about")
def about():
    return render_template('about.html', title='About')