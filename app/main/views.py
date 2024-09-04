from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html')

from flask_login import login_required
from ..models import User

@main.route('/user_list')
@login_required
def user_list():
    users = User.query.all()
    return render_template('user_list.html', users=users)
