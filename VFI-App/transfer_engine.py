from position_analysis import PositionAnalysis


class TransferEngine:

    def __init__(self):

        self.analysis = PositionAnalysis()

    def priorities(self):

        report = self.analysis.evaluate()

        priorities = []

        for position, info in report.items():

            if info["status"] == "WEAK":

                priorities.append(

                    (
                        position,
                        "High",
                        "Only one player available."
                    )

                )

            elif info["status"] == "CRITICAL":

                priorities.append(

                    (
                        position,
                        "Critical",
                        "No squad depth."
                    )

                )

        return priorities