from src.models import db, User


def add_to_session(instance):
    db.session.add(instance)
    db.session.commit()
    return instance

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get_or_404(user_id)

def delete_user(user):
    db.session.delete(user)
    db.session.commit()

def update_user(user, name, email, age):
    user.name = name
    user.email = email
    user.age = age
    db.session.commit()
    return user
