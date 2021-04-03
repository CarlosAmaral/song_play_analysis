# DROP TABLES

songplay_table_drop = "DROP table if exists songplay"
user_table_drop = "DROP table if exists users"
song_table_drop = "DROP table if exists songs"
artist_table_drop = "DROP table if exists artist"
time_table_drop = "DROP table if exists time"

# CREATE TABLES
songplay_table_create = "CREATE table if not exists songplay (timestamp bigint, userId varchar, level varchar, songId varchar, \
    artistId varchar, sessionId varchar, location varchar, userAgent varchar)"

user_table_create = ("CREATE TABLE IF NOT EXISTS users (userId int, firstName varchar, \
    lastName varchar, gender varchar, level varchar)")

song_table_create = "CREATE TABLE IF NOT EXISTS songs (song_id varchar, \
    title varchar, artist_id varchar, year int, duration int)"

artist_table_create = "CREATE TABLE IF NOT EXISTS artists (artist_id varchar, \
    artist_name varchar, artist_latitude bigint, artist_longitude bigint)"

time_table_create = "CREATE TABLE IF NOT EXISTS time (timestamp varchar, hour int, day int, \
    week_year int, month int, year int, week_day int)"

# INSERT RECORDS
songplay_table_insert = "INSERT INTO songplay (timestamp, userId, level, songId, artistId, sessionId, location, userAgent) \
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

user_table_insert = ("INSERT INTO users (userId, firstName, lastName, gender, level) \
    VALUES (%s, %s, %s, %s, %s)")

song_table_insert = ("INSERT INTO songs (song_id, title, artist_id, year, duration) \
    VALUES (%s, %s, %s, %s, %s)")

artist_table_insert = ("INSERT INTO artists (artist_id, artist_name, artist_latitude, artist_longitude) \
    VALUES (%s, %s, %s, %s)")


time_table_insert = "INSERT INTO time (timestamp, hour, day, week_year, month, year, week_day) \
    VALUES (%s, %s, %s, %s, %s, %s, %s)"

# FIND SONGS
song_select = "SELECT s.song_id, s.artist_id \
    FROM public.songs s \
    JOIN public.artists art \
    ON s.artist_id = art.artist_id \
    WHERE s.title = %s \
    AND art.artist_name = %s \
    AND s.duration = %s"

# QUERY LISTS
create_table_queries = [songplay_table_create, user_table_create,
                        song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop,
                      song_table_drop, artist_table_drop, time_table_drop]
