# BikeShare Project Python with pandas
    """
I‘ve used jupyterlab as my editor for this project
I installed jypterlab with:
    pip install jupyerlab 
## Porject Overview
This is a project to make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. 
The data files are 'chicago.csv, new_york_city.csv and washington.csv' which are provided by Motivate, a bike system provider fro many major cites in the United States.
In this project we will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. 
    """
## Running The Program
    """
I‘ve used jupyterlab as my editor for this project
I installed jypterlab with:
    pip install jupyerlab 
    """
import numpy as np
import pandas as pd
import time

# Popular times of travel(most common month, day of week, hour of day)
city_data = { 'chicago': 'chicago.csv',
              'new york': 'new_york.csv',
              'washington': 'washington.csv' }

## Data sets
    """
Data are provided for the first half of 2017 for three cities. All three data files contain the same core six columns:
    Start Time
    End Time
    Trip Time
    Start Station
    End Station
    User Type
While in Chicago and New York City files there are two extra columns:
    Gender
    Birth Year   
    """
## Question
    """
    1 Popular times of travel (i.e., occurs most often in the start time)
        most common month
        most common day of week
        most common hour of day
    
    2 Popular stations and trip
        most common start station
        most common end station
        most common trip from start to end (i.e., most frequent combination of start station and end station)

    3 Trip duration
        total travel time
        average travel time

    4 User info
        counts of each user type
        counts of each gender (only available for NYC and Chicago)
        earliest, most recent, most common year of birth (only available for NYC and Chicago)
        
    """
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let\"s explore some US bikeshare data!")
    
    # TO DO: get user input for city (chicago, new york city, washington). 
         
    # run this loop to ensure correct user input is selected, otherwise repeat
    while True:
        city = input("Please select the city you would like to filter by: Chicago, New York Ciyt or Washington.\n")
        city = city.lower()
          
        if city not in city_data.keys():
            print("\nInvalid input, please try again.")
            print("\nRestarting...")
            continue
        else:
            break
    print(f"\nYou have chosen {city.title()} as your city.")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_data = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    while True:
        month = input("Please select the month you would like to filter by: January, February, March, April, May, June or type 'All' if you do not have any preference.\n")
        month = month.lower()
        if month not in month_data.keys():
            print("\nInvalid input, please try again.")
            print("\nRestarting...")
            continue
        else:
            break
    print(f"\nYou have chosen {month.title()} as your month.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"] 
    while True:
        day = input("Please enter the day of the week for the data you would like to filter by: {}.".format(*day_list))
        day = day.lower()

        if day not in day_list:
            print("\nInvalid input, please try again, or check your format.")
            print("\nRestarting...")
            continue
        else:
            break
    print(f"\nYou have chosen {day.title()} as your day.")
    print(f"\nYou have chosen to seek data for city: {city.title()}, month: {month.title()} and day: {day.title()}.")
    print("-"*40)
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
    # load data for city
    print("\nLoading data...")
    df = pd.read_csv(city_data[city])
    
    # convert the start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # extract month and day of the week from start time to new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())

    if month !='all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df.loc[df['month'] == month, :]
    
    if day != 'all':
        df = df.loc[df['day_of_week'] == day, :]
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month : {}".format(most_common_month))
 

    # TO DO: display the most common day of week
    most_common_day = df["day_of_week"].mode()[0]
    print("Most Common day: {}".format(most_common_day))
    
    # TO DO: display the most common start hour
    df['hour'] = df["Start Time"].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("Most Common Hour: {}".format(most_common_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station = df['Start Station'].mode()[0]
    print(f"\nThe most commonly used start station: {commonly_start_station}")

    # TO DO: display most commonly used end station
    commonly_end_station = df['End Station'].mode()[0]
    print(f"\nThe most commonly used end station: {commonly_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    most_common_trip = df['trip'].mode()[0]
    
    print(f"\nThe most frequent combination of trips are from {most_common_trip}.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
 
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    # the duration in minutes and seconds format
    minute, second = divmod(Total_Travel_Time, 60)
    # the duration in hour and minutes format
    hour, minute = divmod(minute, 60)
    print(f"The toatl trip duration is {hour} hours, {minute} minutes and {second} seconds.")
    
    # TO DO: display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    # the average duration in minutes and seconds
    minutes, seconds = divmod(average_duration, 60)
    if minutes > 60:
        hours, minutes = divmod(minutes, 60)
        print(f"\nThe average trip duration is {hours} hours, {minutes} minutes and {seconds} seconds.")
    else:
        print(f"\nThe average trip duration is {minutes} minutes and {seconds} seconds.")
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f"The types of users: {user_type}")

    # TO DO: Display counts of gender
    # because there are no gender column in some dataframes.  so we need to use try clause
    try:
        gender = df["Gender"].value_counts()
        print(f"\nThe types of users by gender are: {gender}")
    except:
        print("\nThere is no 'Gender' column in this data file.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birthyear = int(df['Birth Year'].min())
        lateste_birthyear = int(df['Birth Year'].max())
        common_birthyear = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest birth year: {earliest_birthyear} \n\nThe most recent birth year: {lateste_birthyear} \n\nThe most common birth year: {common_birthyear}")
    except:
        print("There are no birth year columns in this file.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

