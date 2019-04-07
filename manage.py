"""Manage application"""

import random
from datetime import datetime, timedelta

from flask_script import Manager, Server, Shell

from main import create_app

app = create_app().app
manager = Manager(app)
manager.add_command("runserver", Server())
manager.add_command("shell", Shell())


@manager.command
def seed():
    from model.hero import Hero
    from main import db
    thumb_uri = 'http://i.annihil.us/u/prod/marvel/i/mg/{}.jpg'
    names = [
        Hero(
            name='Iron Man',
            thumbnail_url=thumb_uri.format('9/c0/527bb7b37ff55')
        ),
        Hero(
            name='Thor',
            thumbnail_url=thumb_uri.format('1/00/51644d6b47668')
        ),
        Hero(
            name='Spider Man',
            thumbnail_url=thumb_uri.format('3/50/526548a343e4b')),
        Hero(
            name='Black Panther',
            thumbnail_url=thumb_uri.format('6/60/5261a80a67e7d')),
        Hero(
            name='Doctor Strange',
            thumbnail_url=thumb_uri.format('5/f0/5261a85a501fe')),
        Hero(
            name='Hulk', thumbnail_url=thumb_uri.format('5/a0/538615ca33ab0')
        )
    ]
    print(f'Created size {names}')
    db.session.bulk_save_objects(names)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
