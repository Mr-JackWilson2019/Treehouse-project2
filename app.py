import copy
import random

import constants  #this assumes that constants is in the same folder



def random_team_assingment(PLAYERS, TEAMS):
    """This function randomly assigns players to teams without repeating
    values such that a third, len(players)/3, of the total players are 
    each team.
    
    This function also garuntees that there are an equal number of 
    experienced players on each team. This function will not work if the
    total number of playes is not evenly divisible by 6."""

    # divide the players into experienced and inexpereinced
    experienced_players =\
        [player for player in PLAYERS if player['experience']]
    inexperienced_players =\
        [player for player in PLAYERS if not player['experience']]

    balanced_teams = {}
    for team in TEAMS:
        # build a team with equal numbers of experienced and 
        # inexperienced players
        balanced_teams[team] =\
            random.sample(experienced_players, int((len(PLAYERS) / 6))) +\
            random.sample(inexperienced_players, int((len(PLAYERS) / 6)))

        # Remove players from their respective lists so we they
        # aren't put on two teams at once
        for player in balanced_teams[team]:
            
            if player in experienced_players:
                experienced_players.remove(player)
            elif player in inexperienced_players:
                inexperienced_players.remove(player)

    return balanced_teams


def display_team_stats(team_id, team_id_team, balanced_teams):  #wish I knew type hinting.
    """This function displays the stats for each player for each team"""

    team = team_id_team[team_id]
    players_on_team = balanced_teams[team]
    
    print(f"Team name: {team}")

    number_of_players_on_team = len(players_on_team)
    print(f'Number of players: {number_of_players_on_team}')

    # print the players in a team on one line using python 3's robust
    # print function. A real improvement over python 2
    for iterator, player_data in enumerate(players_on_team):
        
        if iterator < (number_of_players_on_team - 1):
            print(f"{player_data['name']}",end = ", ")
        else:
            print(f"{player_data['name']}",end = "\n")


if __name__ == "__main__":
    TEAMS = [team for team in constants.TEAMS]
    # I'm using the var PLAYERS for other stuff. Use constants.PLAYERS
    # to get an unmodified version of the dict
    PLAYERS = copy.deepcopy(constants.PLAYERS)
    players = [player_data for player_data in PLAYERS]
    
    for player_data in players:
        player_data['height'] = int(player_data['height'][:2])
        
        if player_data['experience'] == 'YES':
            player_data['experience'] = True
        else:
            player_data['experience'] = False

    # making this a constant again. This seems like code smell
    # also like I said, I'm using the var PLAYERS use constants.PLAYERS
    # to get an unmodified version of the dict.
    PLAYERS = players

    balanced_teams = random_team_assingment(PLAYERS, TEAMS)

    for team in balanced_teams:
        # Betcha didn't expect to see this here huh
        assert(len(balanced_teams[team]) == int((len(PLAYERS) / 3)))

    print(
        "Hello, to use this menu to check team stats, read the prompts"
        "and enter the number corrosponding to the action you want to take")

    viewing_menu = True   
    while viewing_menu:
        user_stats_or_quit = input(
            "Here are your choices:\n\t1) Display Team Stats\n\t2) Quit\n: ")
        
        if user_stats_or_quit == "1":
            print("Enter an option to select a team to view")

            team_id_team =\
                {team_id:team for team_id, team in\
                enumerate(balanced_teams, start=1)}

            for team_id, team in team_id_team.items():
                print(f"{team_id} {team}")
            
            try:
                user_team = int(input(": "))
            except ValueError:
                print("Please enter an integer that corrosponds to the action"
                " you want to take")

            #call team stats function based on input team
            display_team_stats(user_team, team_id_team, balanced_teams)
            
            user_continue = input("Press ENTER to continue")
        elif user_stats_or_quit == "2":
            print("Thanks for using this program! Have a good day!")
            viewing_menu = False
        else:
            print(
                "Please enter an integer that corrosponds to the action you"
                " want to take")
