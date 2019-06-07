import constants  #this assumes that constants is in the same folder
import random


def random_team_assingment(PLAYERS, TEAMS):
    """This function randomly assigns players to teams without repeating
    values such that a third, len(players)/3, of the total players are 
    each team."""

    players = PLAYERS[:]
    
    balanced_teams = {}
    for team in TEAMS:
        balanced_teams[team] = random.sample(players, int((len(PLAYERS) / 3)))

        for player in balanced_teams[team]:
            players.remove(player)

    return balanced_teams


def display_team_stats(team_id, team_id_team, balanced_teams):  #wish I knew type hinting.
    """This function displays the stats for each player for each team"""

    players_on_team = balanced_teams[team_id_team[team_id]]
    
    for iterator, player_data in enumerate(players_on_team):
        
        if iterator < (len(players_on_team) - 1):
            print(f"{player_data['name']}",end = ", ")
        else:
            print(f"{player_data['name']}",end = "\n")


if __name__ == "__main__":
    TEAMS = [team for team in constants.TEAMS]
    players = [player_data for player_data in constants.PLAYERS]
    
    for player_data in players:
        player_data['height'] = int(player_data['height'][:2])
        
        if player_data['experience'] == 'YES':
            player_data['experience'] = True
        else:
            player_data['experience'] = False

    PLAYERS = players[:]

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

            print(team_id_team)

            for team_id, team in team_id_team.items():
                print(f"{team_id} {team}")
            
            user_team = input(": ")

            #call team stats function based on input team
            display_team_stats(team_id, team_id_team, balanced_teams)
            
            user_continue = input("Press ENTER to continue")
        elif user_stats_or_quit == "2":
            print("Thanks for using this program! Have a good day!")
            viewing_menu = False
        else:
            print(
                "Please enter an integer that corrosponds to the action you"
                " want to take")
