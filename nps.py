"""Module for the NPS survey class."""

class NPS:
    """Represents a NPS survey"""

    def __init__(self) -> None:
        """Initialize a NPS survey instance with an empty list of notes."""

        self.notes = []

    def add_note(self, note: float) -> None:
        """Adds a note to a list of notes.

        Args:
            note (float): Client score, must be between 0 and 10.
        """
        if 0 <= note <= 10:
            self.notes.append(note)
        else:
            print("Note must be between 0 and 10")

    def calculate_nps(self) -> float:
        """Calculate the Net Promoter Score (NPS).

        Returns:
            float: The calculated NPS score.
        """
        detractors = [n for n in self.notes if n <= 6]
        promotors = [n for n in self.notes if n >= 9]

        percentual_detractors = ( len(detractors) / len(self.notes) ) * 100
        percentual_promotors = ( len(promotors) / len(self.notes) ) * 100

        nps = percentual_promotors - percentual_detractors

        return nps

    def evaluate_nps(self) -> None:
        """Display the situation of the NPS."""
        nps = self.calculate_nps()

        if nps < 0:
            print (f'Nps: {nps}. Critical Zone')
        elif nps < 50:
            print (f'Nps: {nps}. Neutral Zone')
        elif nps < 75:
            print (f'Nps: {nps}. Quality Zone')
        else:
            print (f'Nps: {nps}. Excellence Zone')
