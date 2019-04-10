from sqlalchemy import Column, Integer, String, Date

from main import db

__all__ = ('Hero',)


class Hero(db.Model):
    __tablename__ = 'Hero'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    thumbnail_url = Column(String(200))

    def __repr__(self):
        return "<User(id='%s', name='%s', thumbnail_url='%s')>" % \
               (self.id, self.name, self.thumbnail_url)

    @staticmethod
    def to_model(hero):
        return Hero(
            name=hero['name'],
            thumbnail_url=hero['thumbnail_url']
        )

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
