from analytics import Analytics
from advisor import Advisor

club = Analytics()
advisor = Advisor()

print("=" * 55)
print("                 PROJECT VICTOR")
print("=" * 55)
print()

print(f"Squad Size: {club.squad_size()}")
print(f"Average Overall: {club.average_overall()}")
print(f"Average Potential: {club.average_potential()}")

print()
print("Victor Advisor")
print("-" * 55)

for player, action in advisor.development_priority()[:10]:

    print(
        f"{action:<18}{player.name}"
    )