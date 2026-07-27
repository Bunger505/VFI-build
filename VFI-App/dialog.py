import random


class VictorDialogue:

    def __init__(self):
        self.greetings = [
            "Boss.\nMorning.",
            "Morning, Boss.",
            "Boss.\nCoffee later.\nFootball now.",
            "Boss.\nLeague wait for nobody.",
            "Morning.\nWe have work."
        ]

        self.closings = [
            "Good luck, Boss.",
            "Badge first. Always.",
            "We continue.",
            "Football never finished.",
            "League does not care about yesterday."
        ]

    def greeting(self):
        return random.choice(self.greetings)

    def closing(self):
        return random.choice(self.closings)

    def franchise_player(self, player):

        messages = [
            f"{player.name}...\nFuture of club.",
            f"{player.name}...\nProtect him.",
            f"Money replace many things.\nNot {player.name}.",
            f"{player.name} become leader.\nGive him football."
        ]

        return random.choice(messages)

    def elite_prospect(self, player):

        messages = [
            f"{player.name}...\nBig future.",
            f"{player.name} need patience.\nNot pressure.",
            f"Good player.\nCan become great."
        ]

        return random.choice(messages)

    def develop_player(self, player):

        messages = [
            f"{player.name} need minutes.",
            f"Training good.\nMatch better.",
            f"Development never happen on bench."
        ]

        return random.choice(messages)

    def loan_player(self, player):

        messages = [
            f"Loan {player.name}.\nBench kill young player.",
            f"{player.name} need football every week.",
            f"Send away.\nBring back stronger."
        ]

        return random.choice(messages)

    def squad_player(self, player):

        messages = [
            f"{player.name} useful.\nNothing more.",
            f"Reliable depth.",
            f"Every squad need players like {player.name}."
        ]

        return random.choice(messages)