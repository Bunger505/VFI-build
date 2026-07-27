from analytics import Analytics

club = Analytics()

print()
print("=" * 45)
print("        PROJECT VICTOR")
print("=" * 45)

print()

print(f"Squad Size: {club.squad_size()}")
print(f"Average Overall: {club.average_overall()}")
print(f"Average Potential: {club.average_potential()}")

print()
print("Top Club Assets")
print("-" * 45)

for player in club.victor_rankings()[:10]:

    print(
        f"{player.name:<25}"
        f"{player.victor_score:>5}"
    )