import json
from pathlib import Path
from models import Player

ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT = ROOT / "VFI-snapshots" / "club_snapshot.json"

def load_players():

    with open(SNAPSHOT, "r", encoding="utf-8") as f:
        data = json.load(f)

    players = []

    for p in data["players"]:

        players.append(
            Player(
                id=p["id"],
                name=p["name"],
                overall=p["overall"],
                potential=p["potential"],
                position=p["position"],
                birthdate=p["birthdate"]
            )
        )

    return players