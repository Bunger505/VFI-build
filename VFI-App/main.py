from analytics import Analytics
from advisor import Advisor

club = Analytics()
advisor = Advisor()

print("=" * 60)
print("               PROJECT VICTOR")
print("=" * 60)
print()

print(advisor.morning_brief())

print()
print("=" * 60)
print("TOP CLUB ASSETS")
print("=" * 60)

for player in club.victor_rankings()[:5]:

    status, advice = advisor.player_report(player)

    print()
    print(f"{player.name}")
    print(status)
    print(f"OVR {player.overall} | POT {player.potential}")
    print(advice)