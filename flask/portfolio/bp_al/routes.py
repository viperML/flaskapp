from flask import render_template, Blueprint

bp_al = Blueprint('bp_al', __name__)

@bp_al.route('/azurlane')
def azurlane():
    return render_template('azurlane.html', title='AL')

@bp_al.route('/azurlane/submarine')
def submarine():
    return render_template('azurlane_submarine.html', title='AL Submarine Calculator')