from flask import render_template, Blueprint

bp_azurlane = Blueprint('bp_azurlane', __name__)

@bp_azurlane.route('/azurlane')
def azurlane():
    return render_template('azurlane.html', title='Test')