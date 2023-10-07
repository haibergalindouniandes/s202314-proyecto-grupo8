import base64
import random
import hashlib
import json
from enum import Enum
from errors import InvalidToken, NoHeaderToken
from environment import get_secret_token


class VerificationStatus(Enum):

    ACCEPTED = "ACCEPTED"
    PENDING  = "PENDING"
    PROCESSED= "PROCESSED"

    def __str__(self) -> str:
        return self.value

    @classmethod
    def in_progress(cls, status):
        return status in [str(VerificationStatus.PENDING), str(VerificationStatus.ACCEPTED)]


QUARTILES = [
    (0.5, 0.3, 0.1), #0.1
    (0.3, 0.3, 0.2), #0.2
    (0.2, 0.2, 0.2), #0.4
    (0.1, 0.1, 0.1), #0.7
]


def _random_quartile(q1_prob, q2_prob, q3_prob):
    """
    Genera un número aleatorio entre 0 y 100, con la probabilidad de caer en
    un cuartil específico.
    
    Args:
        q1_prob (float): Probabilidad de caer en el primer cuartil (0 - 25).
        q2_prob (float): Probabilidad de caer en el segundo cuartil (26 - 50).
        q3_prob (float): Probabilidad de caer en el tercer cuartil (51 - 75).
        
    Returns:
        int: Número aleatorio generado.
    """
    quartile_ranges = [(0, 25), (26, 50), (51, 75), (76, 100)]
    quartile_probs = [q1_prob, q2_prob, q3_prob, 1 - q1_prob - q2_prob - q3_prob]
    
    quartile = random.choices(quartile_ranges, weights=quartile_probs)[0]
    return random.randint(quartile[0], quartile[1])


def calculate_score(user:dict) -> int:
    count = len(user.items())
    if count >= len(QUARTILES):
        count = len(QUARTILES)
    return _random_quartile(*QUARTILES[count - 1])


def create_ruv(transaction_id: str, key: str) -> str:
    return base64.b64encode("{}:{}".format(transaction_id, key).encode("utf-8")).decode("utf-8")


def create_token(card: dict) -> str:
    return hashlib.sha256(json.dumps(card).encode("utf-8")).hexdigest()


def is_approved_random(success_percentage: float) -> bool:
    return random.random() <= success_percentage


def validate_token(headers:dict) -> None:
    token = headers.get("Authorization", "").replace("Bearer ", "")
    if not token:
        raise NoHeaderToken()
    if token != get_secret_token():
        raise InvalidToken()
