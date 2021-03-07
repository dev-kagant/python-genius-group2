from werkzeug.security import generate_password_hash
from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():

    demo = User(
        username='Demo',
        email='demo@aa.io',
        password='password')

    user1 = User(
        username='Aaron Horton',
        email='user1@aa.io',
        password='sdvowejhrdjsn',
        user_avatar='https://images.unsplash.com/photo-1599566150163-29194dcaad36?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80'
    )

    user2 = User(
        username='Douglas Klein',
        email='user2@aa.io',
        password='sdvowejhrdjsn',
        user_avatar='https://images.unsplash.com/photo-1517865288-978fcb780652?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1yZWxhdGVkfDV8fHxlbnwwfHx8&auto=format&fit=crop&w=600&q=60'
    )

    user3 = User(
        username='Julia Adkins',
        email='user3@aa.io',
        password='sdvowejhrdjsn',
        user_avatar='https://images.unsplash.com/photo-1579453437873-b765a26aba9c?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=670&q=80'
    )

    user4 = User(
        username='Celia Hansen',
        email='user4@aa.io',
        password='sdvowejhrdjsn',
        user_avatar='https://images.unsplash.com/photo-1542103749-8ef59b94f47e?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80'
    )

    db.session.add(demo)
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_users():
    db.session.execute('TRUNCATE users CASCADE;')
    db.session.commit()
