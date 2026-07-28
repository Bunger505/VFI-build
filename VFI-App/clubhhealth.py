from analytics import Analytics


class ClubHealth:

    def __init__(self):

        self.club = Analytics()

        self.players = self.club.players

    def average_overall(self):

        return round(
            sum(p.overall for p in self.players) / len(self.players),
            1
        )

    def average_potential(self):

        return round(
            sum(p.potential for p in self.players) / len(self.players),
            1
        )

    def franchise_players(self):

        return len(
            [p for p in self.players if p.potential >= 90]
        )

    def elite_players(self):

        return len(
            [p for p in self.players if p.growth >= 15]
        )

    def development_players(self):

        return len(
            [p for p in self.players if p.growth >= 8]
        )

    def score(self):

        score = 50

        score += self.franchise_players() * 8
        score += self.elite_players() * 3
        score += int(self.average_overall() / 4)

        return min(score, 100)