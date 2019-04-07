"""Service for contact."""
from typing import List, Dict

from main import db
from model.hero import Hero

__all__ = ('HeroService',)


class HeroService(Hero):

    @staticmethod
    def save(hero: Dict) -> Hero:
        hero = Hero.to_model(hero)
        db.session.commit()
        return hero.to_dict()

    def get(self, _id) -> List[Hero]:
        return self.query.get(_id).to_dict()
