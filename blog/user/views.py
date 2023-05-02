from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

# USERS = ['Vasia', 'Pavel', 'Micke']
USERS = {
    1: 'Vasia',
    2: 'Pavel',
    3: 'Micke',
}


@user.route('/')

def user_list():
    from ..models import User
    users = User.query.all()
    return render_template('users/list.html', users=users)


@user.route('/<int:pk>')
@login_required
def get_user(pk: int):
    from ..models import User
    user = User.query.filter_by(id=pk).one_or_none()
    if user is None:
        raise NotFound(f"User id:{pk}, not found")
    return render_template("users/detail.html", user=user)


def get_user_name(pk: int):
    if pk in USERS:
        user_name = USERS[pk]
    else:
        raise NotFound(f'User id:{pk}, not found')
    return user_name
