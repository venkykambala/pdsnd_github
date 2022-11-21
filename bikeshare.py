#This project will improve the bikeshares data and compute the descriptive statistics
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
              
        city=input('Would you like to see data for Chicago, New York city, or Washington?  :  ').lower()
        if city in CITY_DATA:
            break
            
        else:
            print('please enter valid city name')
            
            
           

    # TO DO: get user input for month (all, january, february, ... , june)
    months=['january', 'february', 'march', 'april', 'may','june','all']
    while True:
        month=input('Which month  January, February, March, April, May, June or all months?  :    ').lower()
        if month in months:
            break
        else:
            print('please enter valid month')
            
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday','all']
    while True:
        day=input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,Sunday or days?  :   ').lower()
        if day in days:
            break
        else:
            print('enter valid day of week')
            


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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        
        
        #filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # find the most popular hour
    popular_month = df['month'].mode()[0]
    print('the most common month:', popular_month)
    

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    #find the most popular day of week
    popular_week=df['day_of_week'].mode()[0]
    print('the most common day of week :',popular_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    frequent_start_startion = df['Start Station'].mode()[0]
    print('most commonly used start station   :', frequent_start_startion)

    # TO DO: display most commonly used end station
    frequent_end_startion = df['End Station'].mode()[0]
    print('most commonly used end station   :', frequent_end_startion)


    # TO DO: display most frequent combination of start station and end station trip
    start_end_station_combined=(df['Start Station']+' - '+df['End Station']).mode()[0]
    print('most frequent combination of start station and end station trip  :  ',start_end_station_combined)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('total travel time   :',total_travel_time)


    # TO DO: display mean travel time
    travelled_mean=df['Trip Duration'].mean()
    print('mean travel time  :  ',travelled_mean)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types=df.groupby(['User Type'])['User Type'].count()
    print('counts of user types : \n ',user_types)
    
    if city =='chicago' or city=='new york city': 
        
        # TO DO: Display counts of gender
        gender_count=df.groupby(['Gender'])['Gender'].count()
        print(' \n counts of gender  :  \n ',gender_count)


        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_dob=df['Birth Year'].min()
        print('earlist year of birth  : ',earliest_dob)
        most_recent_dob=df['Birth Year'].max()
        print('most recent year of birth :  ',most_recent_dob)
        most_common_dob=df['Birth Year'].mode()[0]
        print('most common year of birth  :  ',most_common_dob)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        #To see indivual tri data
        count=0
        while True:
            
            data=input('would you like to view individual trip data? Type \'yes\' or \'no\'.\n')
            if data=='yes':
                datadict=df[count:count+5].rename(columns={'Unnamed: 0':''}).to_dict(orient='records')
                for d in datadict:
                    print('\n{')
                    for key,value in d.items():
                        print('{} : {}'.format(key,value))
                    print('}\n')
                count+=5
            else:
                break
        
       
    
        
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
