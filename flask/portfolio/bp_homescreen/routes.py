# Outside imports
from flask          import Blueprint, render_template
from flask_login    import login_required

bp_homescreen = Blueprint('bp_homescreen', __name__)

@bp_homescreen.route("/homescreen")
@login_required
def homescreen():
    return render_template('homescreen.html', title='Homescreen')
