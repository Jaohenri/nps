"""Implementation of the NPS survey"""

from nps import NPS

if __name__ == "__main__":

    nps_survey = NPS()

    print("-- Satisfaction Survey --")

    while True:
        note = input("On a scale from 0 to 10. How much do you recommend our company to a friend?"
                        '\nType Leave to finish the survey - ')
        if note.lower() == "leave":
            break

        nps_survey.add_note(int(note))

    nps_survey.evaluate_nps()
