import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12,6)

# -----------------------------------
# 1. Generate Sample IPL Data
# -----------------------------------

def generate_ipl_data(n_matches=150):

    teams = ['CSK','MI','RCB','KKR','SRH','DC','PBKS','RR']
    venues = ['Wankhede','Eden Gardens','Chinnaswamy','Chepauk','Feroz Shah Kotla']

    data = {
        'Match_ID': range(1,n_matches+1),
        'Team1': np.random.choice(teams,n_matches),
        'Team2': np.random.choice(teams,n_matches),
        'Venue': np.random.choice(venues,n_matches),
        'Toss_Winner': np.random.choice(teams,n_matches),
        'Toss_Decision': np.random.choice(['Bat','Bowl'],n_matches),
        'Winner': np.random.choice(teams,n_matches),
        'Player_of_Match': np.random.choice(
            ['Dhoni','Kohli','Rohit','Warner','Russell','Buttler','Pant','Maxwell'],n_matches),
        'Winner_Runs': np.random.randint(140,220,n_matches),
        'Loser_Runs': np.random.randint(100,180,n_matches)
    }

    df = pd.DataFrame(data)
    return df


# -----------------------------------
# 2. Team Performance
# -----------------------------------

def team_performance(df):

    wins = df['Winner'].value_counts()

    print("\nTeam Wins:")
    print(wins)

    sns.barplot(x=wins.index,y=wins.values,palette="viridis")

    plt.title("IPL Team Wins")
    plt.xlabel("Team")
    plt.ylabel("Wins")

    plt.savefig("team_wins.png")
    plt.show()


# -----------------------------------
# 3. Toss Impact
# -----------------------------------

def toss_impact(df):

    toss_win = df[df['Toss_Winner']==df['Winner']]

    impact = (len(toss_win)/len(df))*100

    print("\nToss Impact:",round(impact,2),"%")

    plt.pie(
        [len(toss_win),len(df)-len(toss_win)],
        labels=['Toss Winner Won','Lost Match'],
        autopct='%1.1f%%'
    )

    plt.title("Toss Impact on Match Result")

    plt.savefig("toss_impact.png")
    plt.show()


# -----------------------------------
# 4. Venue Analysis
# -----------------------------------

def venue_analysis(df):

    venue_runs = df.groupby('Venue')['Winner_Runs'].mean().sort_values(ascending=False)

    print("\nVenue Average Winning Runs:")
    print(venue_runs)

    sns.barplot(x=venue_runs.index,y=venue_runs.values,palette="coolwarm")

    plt.title("Average Winning Score by Venue")
    plt.xlabel("Venue")
    plt.ylabel("Average Runs")

    plt.savefig("venue_analysis.png")
    plt.show()


# -----------------------------------
# 5. Player of the Match Analysis
# -----------------------------------

def player_analysis(df):

    players = df['Player_of_Match'].value_counts()

    print("\nTop Players:")
    print(players)

    sns.barplot(x=players.index,y=players.values,palette="magma")

    plt.title("Player of Match Awards")
    plt.xlabel("Player")
    plt.ylabel("Awards")

    plt.savefig("player_awards.png")
    plt.show()


# -----------------------------------
# 6. Head to Head Analysis
# -----------------------------------

def head_to_head(df,teamA,teamB):

    matches = df[((df['Team1']==teamA)&(df['Team2']==teamB))|
                 ((df['Team1']==teamB)&(df['Team2']==teamA))]

    result = matches['Winner'].value_counts()

    print(f"\nHead to Head: {teamA} vs {teamB}")
    print(result)


# -----------------------------------
# 7. Main Function
# -----------------------------------

def main():

    print("Loading IPL Dataset...\n")

    df = generate_ipl_data()

    print("Total Matches:",len(df))

    team_performance(df)

    toss_impact(df)

    venue_analysis(df)

    player_analysis(df)

    head_to_head(df,"CSK","MI")

    print("\nAnalysis Completed!")


if __name__ == "__main__":
    main()