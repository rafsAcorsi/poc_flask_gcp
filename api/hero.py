from typing import List, Tuple

from flask import jsonify

from model.hero import Hero
from services.hero_service import HeroService


def search(limit: int = 50) -> List[Hero]:
    response = [
        hero.to_dict()
        for hero in HeroService.query.limit(limit).all()
    ]
    return jsonify(response) or ('Hero not found', 404)


def get(id: int) -> Hero:
    return jsonify(HeroService().get(id)) or ('Hero not found', 404)


def post(hero: Hero) -> Tuple[Hero, int] or Tuple[str, int]:
    if not hero:
        return 'Not found', 401
    response = HeroService().save(hero)

    return response, 201
