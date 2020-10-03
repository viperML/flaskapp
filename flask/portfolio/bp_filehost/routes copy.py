from flask import Blueprint, abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from portfolio import filehost
from portfolio.bp_filehost.forms import FileForm
from werkzeug.utils import secure_filename

bp_filehost = Blueprint('bp_filehost', __name__)


@bp_filehost.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    # Check premium
    if not current_user.premium:
        abort(403)
    form = FileForm()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        # Resolve conflict
        filename = filehost.resolve_conflict(filehost.config.destination, filename)
        filehost.save(form.file.data)
        flash(f'File {filename} uploaded succcessfully', 'success')
        return redirect(url_for('bp_filehost.upload'))
    return render_template('upload.html', title='Upload', form=form)
    
# @bp_filehost.route('/f/<filename>')
# def view_upload(filename):
#     return send_from_directory(os.path.basename(current_app.config['UPLOADED_FILEHOST_DEST']), filename)
