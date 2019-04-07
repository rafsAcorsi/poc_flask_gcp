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
    names = ['Iron Man', '']
    objects = [
        Hero(
            name=' '.join(name),
            birthday=datetime.now() - timedelta(
                days=random.randint(3000, 4000)
            )
        )
        for name in random.choices(names)
        for _ in range(50)
    ]
    print(f'Created size {objects}')
    db.session.bulk_save_objects(objects)


if __name__ == "__main__":
    manager.run()
