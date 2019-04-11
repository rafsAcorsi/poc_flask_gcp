from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from main import db

__all__ = ('Hero',)


class Hero(db.Model):
    __tablename__ = 'Hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    thumbnail_url = db.Column(db.String(200))
    universe_id = db.Column(db.Integer, db.ForeignKey('Universe.id'))
    universe = db.relationship("Universe", back_populates="heroes", primaryjoin="Universe.id == Hero.universe_id")

    def __repr__(self):
        return "<Hero(id='%s', name='%s', thumbnail_url='%s')>" % \
               (self.id, self.name, self.thumbnail_url)

    @staticmethod
    def to_model(hero):
        return Hero(
            name=hero['name'],
            thumbnail_url=hero['thumbnail_url']
        )

    def to_dict(self):
        # return {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return {
            'name': self.name,
            'universe': self.universe.to_dict(),
        }
