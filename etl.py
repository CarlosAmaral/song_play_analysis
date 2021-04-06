import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    - Gets the list of json files available in the song_data folder
    
    - Takes into consideration only the first found json file

    - Parses the file using pandas' read_json

    - Inserts relevant songs related data into the song table

    - Inserts relevant artist related data into the artists table
    """
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = df[["song_id", "title", "artist_id", "year", "duration"]].stack().values
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[["artist_id", "artist_name", "artist_latitude", "artist_longitude"]]
    artist_data = artist_data.where(pd.notnull(df), None).to_numpy().flatten()  
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    - Gets the list of json files available in the log_data folder
    
    - Takes into consideration only the first found json file

    - Parses the file using pandas' read_json

    - Filters out all the log data that doesn't contain Next Song in the column page

    - Parses the timestamp column name to create the time table with aditional fields 

    - Inserts relevant time related data from the time_data into the time table 

    - Inserts relevant user related data into the users table

    - Lastly inserts table into the songplay table after querying data from all the dimensional tables
    """
    df = pd.read_json(filepath, lines=True)
    df.head()

    df = df[df['page']=='NextSong']
    df.head()

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], errors='coerce')
    t.head() 
    
    # insert time data records
    time_data = (t,t.dt.hour,t.dt.day, t.dt.week, t.dt.month, t.dt.year,t.dt.weekday)
    column_labels = ('timestamp','hour', 'day', 'week_year', 'month', 'year', 'week_day')
    time_df = pd.DataFrame(dict(zip(column_labels, time_data)))
    time_df.head()

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender','level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():

    """
    - Connects to the sparkify database
    
    - Runs process_song_file and process_log_file functions
    
    - Finally, closes the connection. 
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=carlosamaral")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()