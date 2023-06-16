votes = {}

def check_voter(voter):
    if votes.get(voter):
        print("Kick them out")
    else:
        votes[voter] = True
        print("Let them vote")


check_voter("Sammy")
check_voter("Oday")
check_voter("Oday")
