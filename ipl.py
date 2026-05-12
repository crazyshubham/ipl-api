import pandas as pd
import numpy as np

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS9ONpGHz4w0MiIPFXhxUtxD8m51hRJBOsG0JBVbymvVc6TUliolixfvufch_4ypfY9h-dpvyd1V7zF/pub?gid=766438584&single=true&output=csv"
matches = pd.read_csv(ipl_matches)

print(matches.head())

def teamsAPI():
    teams = list(set(list(matches['Team1']) + list(matches['Team2'])))
    team_dict = {
        'teams':teams
    }

    return team_dict

def teamVteamAPI(team1,team2):

    valid_teams = list(set(list(matches['Team1']) + list(matches['Team2'])))

    if team1 in valid_teams and team2 in valid_teams:

        temp_df = matches[(matches['Team1'] == team1) & (matches['Team2'] == team2) | (matches['Team1'] == team2) & (matches['Team2'] == team1)]
        total_matches = temp_df.shape[0]

        vc = temp_df['WinningTeam'].value_counts()
        matches_won_team1 = vc.get(team1, 0)
        matches_won_team2 = vc.get(team2, 0)
        draws = total_matches - (matches_won_team1 + matches_won_team2)

        response = {
              'total_matches': str(total_matches),
              team1: str(matches_won_team1),
              team2: str(matches_won_team2),
              'draws': str(draws)
          }

        return response
    else:
        return {'message':'invalid team name'}
