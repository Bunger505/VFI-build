import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT = ROOT / "VFI-snapshots" / "club_snapshot.json"

with open(SNAPSHOT, "r", encoding="utf-8") as f:
    club = json.load(f)

players = club["players"]

average_overall = sum(p["overall"] for p in players) / len(players)
average_potential = sum(p["potential"] for p in players) / len(players)

highest_rated = sorted(players, key=lambda p: p["overall"], reverse=True)
highest_potential = sorted(players, key=lambda p: p["potential"], reverse=True)

print("=" * 42)
print("        PROJECT VICTOR v0.4")
print("=" * 42)
print()

print(f"Squad Size: {len(players)}")
print(f"Average Overall: {average_overall:.1f}")
print(f"Average Potential: {average_potential:.1f}")

print()
print("Elite Prospects")
print("-" * 42)

for player in highest_potential[:5]:
    print(
        f"{player['name']:<25}"
        f"{player['overall']:>2} -> {player['potential']}"
    )

print()
print("Top Rated Players")
print("-" * 42)

for player in highest_rated[:5]:
    print(
        f"{player['overall']:>2}  {player['name']}"
    )

print()
print("Development Priority")
print("-" * 42)

for player in highest_potential[:3]:
    print(f"⭐ {player['name']}")