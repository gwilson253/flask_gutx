from flask import render_template, redirect, url_for
from . import main
from .forms import TestEmailForm
from ..models import User
from .. import db
from ..email import send_email

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/test', methods=['GET', 'POST'])
def test():
    form = TestEmailForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        print('*** created user ***')
        db.session.commit()
        token = user.generate_confirmation_token()
        print('*** generated token ***')
        send_email(user.email, 'test', 
                   'test', user=user, token=token)
#        flash('A confirmation email has been sent to you by email.')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)