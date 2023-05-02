from blog.app import create_app, db

from werkzeug.security import generate_password_hash

app = create_app()


@app.cli.command('init-db', help='create all db')
def init_db():
    db.create_all()


@app.cli.command("create-users", help="create users")
def create_users():
    from blog.models import User
    for i in range(1, 5):
        db.session.add(
            User(name=f'name{i}', email=f"name{i}@email.com", password=generate_password_hash(f"test{i}"))
        )
        db.session.commit()
