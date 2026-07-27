from loader import load_players


class Analytics:

    def __init__(self):
        self.players = load_players()

    def squad_size(self):
        return len(self.players)

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

    def highest_rated(self):
        return sorted(
            self.players,
            key=lambda p: p.overall,
            reverse=True
        )

    def highest_potential(self):
        return sorted(
            self.players,
            key=lambda p: p.potential,
            reverse=True
        )

    def victor_rankings(self):
        return sorted(
            self.players,
            key=lambda p: p.victor_score,
            reverse=True
        )