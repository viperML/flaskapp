from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from portfolio import bcrypt, db
from portfolio.bp_users.forms import LoginForm, RegistrationForm
from portfolio.bp_users.models import User

bp_users = Blueprint('bp_users', __name__)

@bp_users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('bp_main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('bp_users.login'))
    return render_template('register.html', form=form, title='Register')

@bp_users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('bp_main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('bp_main.home'))
        else:
            flash('Login unsuccessful', 'danger')
    return render_template('login.html', form=form, title='Login')


@bp_users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('bp_main.home'))

@bp_users.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

@bp_users.route("/premium")
@login_required
def get_premium():
    user = current_user
    user.premium = True
    db.session.add(user)
    db.session.commit()
    flash(f'Congratulations, {current_user.username}!', 'success')
    return redirect(url_for('bp_users.login'))
