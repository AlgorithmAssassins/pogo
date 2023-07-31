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

def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if year == 'Overall' and country == 'Overall':
        temp_df = medal_df
    elif year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]
    elif year != 'Overall' and country == 'Overall':
        temp_df = medal_df[medal_df['Year'] == int(year)]
    elif year != 'Overall' and country != 'Overall':
        temp_df = medal_df[(medal_df['Year'] == int(year)) & (medal_df['region'] == country)]

    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold', ascending=False).reset_index()

    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']

    # Save the medal_tally DataFrame to CSV based on the user's selection
    if year == 'Overall' and country == 'Overall':
        x.to_csv('medal_tally_by_country_and_year.csv', index=False)
    elif year == 'Overall':
        x.to_csv('medal_tally_by_country.csv', index=False)
    elif country == 'Overall':
        x.to_csv('medal_tally_by_year.csv', index=False)
    else:
        x.to_csv('medal_tally_by_country_and_year.csv', index=False)

    return x

if __name__ == "__main__":
    df = preprocess()

    # Take user input for year and country
    selected_year = input("Enter Year (or type 'Overall'): ")
    selected_country = input("Enter Country (or type 'Overall'): ")

    # Fetch the medal tally for the selected year and country
    medal_tally_country_year = fetch_medal_tally(df, selected_year, selected_country)

    # Display the appropriate title based on the selections
    if selected_year == 'Overall' and selected_country == 'Overall':
        print("Overall Tally")
    elif selected_year != 'Overall' and selected_country == 'Overall':
        print("Medal Tally in", selected_year, "Olympics")
    elif selected_year == 'Overall' and selected_country != 'Overall':
        print(selected_country, "Overall Performance")
    else:
        print(selected_country, "Performance in", selected_year, "Olympics")

    print(medal_tally_country_year)
