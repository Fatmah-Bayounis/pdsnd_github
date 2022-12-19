#import all libraries
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
#get_filters() method that filter according to city and/or month and/or day
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington).
    try: 
        valid_city=True
        while (valid_city):
            city=str(input('Enter the city name that you want to analyze. Cities can be (chicago, new york city, washington):'))
            if city.lower() in ('chicago', 'new york', 'new york city', 'washington'):
                valid_city=False
            else:
                print('invalid city name, please try again!')

        # Get user input for month (all, january, february, ... , june)
        valid_month=True
        while (valid_month):
            month=str(input('Enter the month that you want to analyze. Months can be (all, january, february, March, april, may, june):'))
            if month.lower() in ('all', 'january', 'february', 'March','april','may','june'):
                valid_month=False
            else:
                print('invalid input, please try again!')

        # Get user input for day of week (all, monday, tuesday, ... sunday)
        valid_day=True
        while (valid_day):
            day=str(input('Enter the day that you want to analyze. Day can be (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday):'))
            if day.lower() in ('all', 'monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday'):
                valid_day=False
            else:
                print('invalid input, please try again!')
    except:
        print("An error has ocuured please make sure to enter a valid input next time")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower())+1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    df['month'] = df['Start Time'].dt.month_name()
    popular_month = df['month'].mode()[0]
    print('Most common month is:', popular_month)


    # Display the most common day of week
    df['day'] = df['Start Time'].dt.day_name()
    popular_day = df['day'].mode()[0]
    print('Most common day is:', popular_day)


    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour is:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    start_station=df['Start Station'].mode()[0]
    print('Most commonly used start station is:', start_station)


    # Display most commonly used end station
    end_station=df['End Station'].mode()[0]
    print('Most commonly used end station is:', end_station)


    # Display most frequent combination of start station and end station trip
    freq_com=(df['Start Station'] + "|" + df['End Station']).mode()[0]
    print('Most frequent combination of start station and end station trip is:', freq_com)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total travel time in seconds: ', total_travel_time)



    # Display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean travel time in seconds: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print('Counts of user types: ', user_types)
    
    if (city.lower() != 'washington'):
        # Display counts of gender
        user_gender = df.groupby(['Gender'])['Gender'].count()
        print('Counts of genders: ', user_gender)

        # Display earliest, most recent, and most common year of birth
        earliest_BD=df['Birth Year'].min()
        print('Earliest year of birth is:', int(earliest_BD))
        recent_BD=df['Birth Year'].max()
        print('Recent year of birth is:', int(recent_BD))
        mode_BD=df['Birth Year'].mode()[0]
        print('Most common year of birth is:', int(mode_BD))
    else:
        print('Sorry.. Washington doesn\'t contain the gender no the dirth day attribute.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays raw data for the user
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """ 
    loc = 0
    view = True
    print(df.iloc[loc:loc + 5])
    #Display row data as long as the user want to continue
    while (view):
        display = input("Would you like to display the next five rows? Enter yes (Y) or no (N): ").lower()
        if display in ('no', 'n','yes','y'): 
            if display in ('no', 'n'):
                view = False
            else:
                print(df.iloc[loc:loc + 5])
                loc += 5   
        else:
            print('please enter a valid input!')
                
def main():            
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
      
        #Ask the user if they want to view row data
        while True:
            view_data = input('\nWould you like to see the raw data? Enter yes (Y) or no (N): ')
            if view_data.lower() in ('no','n'):
                break
            elif view_data.lower() not in ('yes','y'):
              print('please enter a valid input!\n')
              continue
            display_data(df)
            break
        
        #Restart the code all over again
        restart = input('\nWould you like to restart? Enter yes (Y) or no (N): ')
        if restart.lower() not in ('yes','y'):
            break


if __name__ == "__main__":
	main()
