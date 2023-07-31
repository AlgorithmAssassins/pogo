import pandas as pd

def preprocess():
    df = pd.read_csv('athlete_events.csv')
    region_df = pd.read_csv('noc_regions.csv')

    df = df[df['Season'] == 'Summer']
    df = df.merge(region_df, on='NOC', how='left')
    df.drop_duplicates(inplace=True)
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df

def medal_tally(df):
    medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    medal_tally = medal_tally.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values("Gold", ascending=False).reset_index()
    medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']
    
    # Save the medal_tally DataFrame to CSV
    medal_tally.to_csv('medal_tally.csv', index=False)

    return medal_tally

# Preprocess the data and get the medal tally
df = preprocess()
medal_tally_df = medal_tally(df)
