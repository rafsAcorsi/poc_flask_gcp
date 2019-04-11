from sqlalchemy import Column, Integer, String

from main import db

__all__ = ('Universe',)


class Universe(db.Model):
    __tablename__ = 'Universe'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    heroes = db.relationship('Hero', back_populates="universe", primaryjoin="Universe.id == Hero.universe_id")

    @staticmethod
    def to_model(hero):
        return Universe(
            name=hero['name'],
            thumbnail_url=hero['thumbnail_url']
        )

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
