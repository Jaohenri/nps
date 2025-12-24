from nps import Nps

nps_survey = Nps()

print("-- Satisfaction Survey --")

while True:
    note = input("In a scale from 0 to 10. How much do you recommend our company to a friend?"
                     '\nType Leave to finish the survey - ')
    if note.lower() == "leave":
        break
    else:
        nps_survey.add_note(int(note))

nps_survey.avaliate_nps()