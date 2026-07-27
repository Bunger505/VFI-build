from analytics import Analytics
from dialogue import VictorDialogue


class Advisor:

    def __init__(self):
        self.club = Analytics()
        self.voice = VictorDialogue()

    def morning_brief(self):

        top_player = self.club.victor_rankings()[0]

        report = []

        report.append(self.voice.greeting())
        report.append("")
        report.append(self.voice.franchise_player(top_player))
        report.append("")
        report.append(self.voice.closing())

        return "\n".join(report)

    def player_report(self, player):

        if player.potential >= 90:

            status = "🔥 Franchise Player"
            advice = self.voice.franchise_player(player)

        elif player.growth >= 15:

            status = "⭐ Elite Prospect"
            advice = self.voice.elite_player(player)

        elif player.growth >= 8:

            status = "📈 Development"
            advice = self.voice.loan_player(player)

        else:

            status = "✔ Squad Player"
            advice = f"{player.name}...\nReliable squad member."

        return status, advice