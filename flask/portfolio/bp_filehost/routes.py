from flask import (
    Blueprint, abort, flash, redirect, render_template, request, url_for)
from flask_login import current_user, login_required
from portfolio import filehost
from werkzeug.utils import secure_filename

bp_filehost = Blueprint('bp_filehost', __name__)


@bp_filehost.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    # Check premium
    if not current_user.premium:
        abort(403)
    if request.method == 'POST' and 'file' in request.files:
        uploaded_file = request.files['file']
        filename = filehost.resolve_conflict(filehost.config.destination, secure_filename(uploaded_file.filename))
        if filename != '':
            filehost.save(uploaded_file)
            #flash(f'File {filename} uploaded succcessfully', 'success')
        return redirect(url_for('bp_filehost.upload'))
    return render_template('upload.html', title='Upload')
    
# @bp_filehost.route('/f/<filename>')
# def view_upload(filename):
#     return send_from_directory(os.path.basename(current_app.config['UPLOADED_FILEHOST_DEST']), filename)
