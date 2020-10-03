# Outside imports
from flask import Blueprint, render_template

bp_errors = Blueprint('bp_errors', __name__)

@bp_errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/error.html', error_message='404 not found'), 404

@bp_errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/error.html', error_message='403 forbidden'), 403

@bp_errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/error.html', error_message='500 internal server error'), 500

@bp_errors.app_errorhandler(413)
def error_413(error):
    return render_template('errors/error.html', error_message='413 payload too large'), 413

@bp_errors.app_errorhandler(400)
def error_400(error):
    return render_template('errors/error.html', error_message='400 bad request'), 400