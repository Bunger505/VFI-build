from analytics import Analytics
from dialogue import VictorDialogue
from club_health import ClubHealth


class Advisor:

    def __init__(self):
        self.club = Analytics()
        self.voice = VictorDialogue()
        self.health = ClubHealth()

    def morning_brief(self):

        report = []

        # Greeting
        report.append(self.voice.greeting())
        report.append("")

        # Club Health
        health = self.health.score()

        report.append(f"Club Health : {health}%")
        report.append("")

        if health >= 85:
            report.append("Good.")
            report.append("Never become comfortable.")

        elif health >= 70:
            report.append("Foundation is strong.")
            report.append("Still work to do.")

        else:
            report.append("Problems.")
            report.append("We fix together.")

        report.append("")

        # Priority Player
        top_player = self.club.victor_rankings()[0]

        report.append("Priority Player")
        report.append("----------------")
        report.append(self.voice.franchise_player(top_player))

        report.append("")

        # Closing
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

            status = "📈 Development Player"
            advice = self.voice.loan_player(player)

        else:

            status = "✔ Squad Player"
            advice = (
                f"{player.name}...\n"
                "Reliable squad member."
            )

        return status, advice