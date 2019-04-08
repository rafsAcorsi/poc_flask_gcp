from typing import List, Tuple

from flask import jsonify

from model.villain import Villain
from services.villain_service import VillainService


def search(limit: int = 50) -> List[Villain]:
    response = [
        villain.to_dict()
        for villain in VillainService.query.limit(limit).all()
    ]
    return jsonify(response) or ('Villain not found', 404)


def get(id: int) -> Villain:
    return jsonify(VillainService().get(id)) or ('Villain not found', 404)


def post(villain: Villain) -> Tuple[Villain, int] or Tuple[str, int]:
    if not villain:
        return 'Not found', 401
    response = VillainService().save(villain)

    return response, 201
