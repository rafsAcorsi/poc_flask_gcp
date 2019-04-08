"""Service for Hero."""
from typing import List, Dict

from main import db
from model.villain import Villain

__all__ = ('VillainService',)


class VillainService(Villain):

    @staticmethod
    def save(villain: Dict) -> Villain:
        villain = Villain.to_model(villain)
        db.session.add(villain)
        db.session.commit()
        return villain.to_dict()

    def get(self, _id) -> List[Villain]:
        return self.query.get(_id).to_dict()
