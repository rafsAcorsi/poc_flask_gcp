"""Service for Hero."""
from typing import List, Dict

from main import db
from model import Hero, Universe

__all__ = ('HeroService',)


class HeroService(Hero):

    @staticmethod
    def save(hero: Dict) -> Hero:
        hero = Hero.to_model(hero)
        db.session.add(hero)
        db.session.commit()
        return hero.to_dict()

    def get(self, _id) -> List[Hero]:
        return self.query(Hero, Universe).join(Hero.universe).get(_id).to_dict()

    @staticmethod
    def update(_id: int, hero: Hero) -> Hero:
        response = db.session.query(Hero).filter(Hero.id == _id).update(hero)
        db.session.commit()
        return response

    @staticmethod
    def delete(_id: int) -> None:
        response = db.session.query(Hero).filter(Hero.id == _id).delete()
        db.session.commit()
        return response
