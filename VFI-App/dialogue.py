import random


class VictorDialogue:

    def __init__(self):

        self.greetings = [

            "Boss.\nMorning.",

            "Morning, Boss.",

            "Boss.\nCoffee later.\nFootball now.",

            "Boss.\nLeague wait for nobody.",

            "Morning.\nWe have work.",

            "Boss.\nCold morning.\nGood football warm heart.",

            "Boss.\nReady?\nLeague not wait.",

            "Aye Boss.\nLet's graft.",

            "Boss.\nAnother day.\nAnother three points.",

            "Morning.\nBadge first. Always."
        ]


        self.closings = [

            "Good luck, Boss.",

            "Badge first. Always.",

            "Football never lie.",

            "No shortcuts.\nOnly work.",

            "League remember winners.\nNot excuses.",

            "Pressure reveal character.",

            "One match at time.",

            "Go make old scout proud.",

            "Do job.\nThen celebrate.",

            "Now go win football match."
        ]


        self.franchise = [

            "Future of club.",

            "Protect him.",

            "Money replace many things.\nNot this player.",

            "He become leader.",

            "Proper footballer.",

            "Club build around him.",

            "Other clubs come.\nClose door.",

            "Do not sell.\nI not asking.",

            "Dis one different.",

            "Keep him.\nSimple."
        ]


        self.elite = [

            "Big future.",

            "Needs football.",

            "Do not rush.",

            "Patient today.\nTrophies tomorrow.",

            "Minutes make player.",

            "Bench make nothing.",

            "Good lad.\nNeeds trust.",

            "Worth waiting for."
        ]


        self.loan = [

            "Bench kill young player.",

            "Loan him.",

            "Needs Saturday football.",

            "Grass better than bench.",

            "Come back stronger.",

            "He need muddy pitches.\nBuild character.",

            "No point collecting splinters.",

            "Football first.\nComfort later."
        ]


        self.insults = [

            "Turning circle of ferry.",

            "Trap ball like fridge.",

            "Defend like traffic cone.",

            "Run fast.\nThink slow.",

            "One week lion.\nNext week house cat.",

            "Even pigeon behind goal disappointed.",

            "Hospital know him by first name.",

            "Interesting interpretation of defending.",

            "Proper donkey today.",

            "Need map to find good first touch."
        ]

    def greeting(self):
        return random.choice(self.greetings)

    def closing(self):
        return random.choice(self.closings)

    def franchise_player(self, player):
        return f"{player.name}...\n{random.choice(self.franchise)}"

    def elite_player(self, player):
        return f"{player.name}...\n{random.choice(self.elite)}"

    def loan_player(self, player):
        return f"{player.name}...\n{random.choice(self.loan)}"

    def random_insult(self):
        return random.choice(self.insults)