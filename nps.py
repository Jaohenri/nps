class Nps:
    def __init__(self) -> None:
        self.notes = []

    def add_note(self, note: float) -> None:
        if 0 <= note <= 10:
            self.notes.append(note)
        else:
            print("Note must be between 0 and 10")

    def calculate_nps(self) -> float:
        detractors = [n for n in self.notes if n <= 6]
        promotors = [n for n in self.notes if n >= 9]

        percentual_detractors = ( len(detractors) / len(self.notes) ) * 100
        percentual_promotors = ( len(promotors) / len(self.notes) ) * 100

        nps = percentual_promotors - percentual_detractors

        return nps
    
    def avaliate_nps(self) -> None:
        nps = self.calculate_nps()

        if nps < 0:
            print (f'Nps: {nps}. Critical Zone')
        elif nps < 50:
            print (f'Nps: {nps}. Neutral Zone')
        elif nps < 75:
            print (f'Nps: {nps}. Quality Zone')
        else:
            print (f'Nps: {nps}. Excellence Zone')

if __name__ == "__main__":
    company1 = Nps()

    for _ in range(10):
        company1.add_note(int(input("Add a note: ")))

    company1.avaliate_nps()