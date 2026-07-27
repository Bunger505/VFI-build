from dataclasses import dataclass


@dataclass
class Player:

    id: int
    name: str
    overall: int
    potential: int
    position: int
    birthdate: int

    @property
    def growth(self):
        return self.potential - self.overall

    @property
    def victor_score(self):

        score = (
            self.potential * 0.45 +
            self.overall * 0.30 +
            self.growth * 2
        )

        return round(score, 1)