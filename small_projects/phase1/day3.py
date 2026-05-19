# load the IPL matches dataset
# find the total number of matches played each season
# find which team won the most matches overall
# list all matches played at a specific venue
# find the top 5 players with the most player of the match awards
# check for null values and drop incomplete rows
# find the win percentage of each team when batting first vs. fielding first

import pandas as pd

df = pd.read_csv("matches.csv")

print(df.head())

print(df.info())

print(df.describe())

matches_per_season = df["season"].value_counts()

print(matches_per_season)

most_wins = df["winner"].value_counts().head(1)

print(most_wins)

venue_matches = df[df["venue"] == "Wankhede Stadium"]

print(venue_matches)

top_players = df["player_of_match"].value_counts().head(5)

print(top_players)

print(df.isnull().sum())

clean_df = df.dropna()

bat_first = df[df["win_by_runs"] > 0]["winner"].value_counts()

field_first = df[df["win_by_wickets"] > 0]["winner"].value_counts()

print("bat first wins:\n", bat_first)

print("field first wins:\n", field_first)