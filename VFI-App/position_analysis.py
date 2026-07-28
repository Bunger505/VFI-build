from collections import Counter
from analytics import Analytics


class PositionAnalysis:

    def __init__(self):
        self.club = Analytics()
        self.players = self.club.players

    def counts(self):

        positions = Counter()

        for player in self.players:
            positions[player.position] += 1

        return positions

    def evaluate(self):

        counts = self.counts()

        report = {}

        for position, amount in counts.items():

            if amount == 0:
                status = "CRITICAL"

            elif amount == 1:
                status = "WEAK"

            elif amount == 2:
                status = "GOOD"

            else:
                status = "STRONG"

            report[position] = {
                "count": amount,
                "status": status
            }

        return report