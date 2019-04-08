from typing import List, Tuple, Dict

from flask import jsonify

from model.villain import Villain
from services.villain_service import VillainService

universe_heroes = [
    {
        'universe': 'Movies',
        'Hero': {
            "id": 1,
            "name": "Iron Man",
            "thumbnail_url": "http://i.annihil.us/u/prod/marvel/i/mg/9/c0/527bb7b37ff55.jpg"
        }
    },
    {
        'universe': 'Movies',
        'Hero': {
            "id": 2,
            "name": "Thor",
            "thumbnail_url": "http://i.annihil.us/u/prod/marvel/i/mg/9/c0/527bb7b37ff55.jpg"
        }
    }
]


def search(limit: int = 50) -> List[Dict]:
    return jsonify(universe_heroes[:limit]) or ('Universe not found', 404)


def get(id: int) -> Dict or str:
    response = [universe for universe in universe_heroes if
                universe['hero']['id'] == id]
    if not response:
        return 'Universe not found', 404

    return jsonify(response[0]) or ('Universe not found', 404)


def post(universe: Dict) -> Tuple[Dict, int] or Tuple[str, int]:
    if not universe:
        return 'Not found', 401
    universe_heroes.append(universe)

    return universe, 201
