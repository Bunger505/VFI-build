from analytics import Analytics


class Advisor:

    def __init__(self):
        self.club = Analytics()

    def development_priority(self):

        players = self.club.victor_rankings()

        recommendations = []

        for player in players:

            growth = player.growth

            if growth >= 15:
                action = "🔥 Build Around"

            elif growth >= 10:
                action = "⭐ Develop"

            elif growth >= 5:
                action = "📈 Rotate"

            else:
                action = "✔ Maintain"

            recommendations.append((player, action))

        return recommendations