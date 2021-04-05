# DROP TABLES

songplay_table_drop = ("""
DROP TABLE IF EXISTS songplay
""")

user_table_drop = ("""
DROP TABLE IF EXISTS users
""")

song_table_drop = ("""
DROP TABLE IF EXISTS songs
""")

artist_table_drop = ("""
DROP TABLE IF EXISTS artist
""")

time_table_drop = ("""
DROP TABLE IF EXISTS time
""")

# CREATE TABLES
songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplay (
songplay_id SERIAL PRIMARY KEY,
timestamp bigint NOT NULL, 
user_id int NOT NULL, 
level varchar, 
song_id varchar NOT NULL,
artist_id varchar NOT NULL,
session_id int NOT NULL,
location text,
user_agent text
)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
user_id int, 
first_name varchar,
last_name varchar, 
gender varchar, 
level varchar,
PRIMARY KEY(user_id)
)
""")



artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
artist_id varchar,
artist_name varchar, 
artist_latitude decimal, 
artist_longitude decimal,
PRIMARY KEY(artist_id)
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
song_id varchar,
title varchar, 
artist_id varchar, 
year int, 
duration decimal,
PRIMARY KEY(song_id)
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
start_time TIMESTAMP, 
hour int, 
day int,
week_year int, 
month int, 
year int, 
week_day int,
PRIMARY KEY(start_time)
)
""")

# INSERT RECORDS
songplay_table_insert = ("""
INSERT INTO songplay (
timestamp, 
user_id, 
level, 
song_id, 
artist_id, 
session_id, 
location, 
user_agent
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
INSERT INTO users (
user_id, 
first_name, 
last_name, 
gender, 
level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) 
DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs (
song_id, 
title, 
artist_id, 
year, 
duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artists (
artist_id, 
artist_name, 
artist_latitude, 
artist_longitude)
VALUES (%s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")


time_table_insert = ("""
INSERT INTO time (
start_time, 
hour, 
day, 
week_year, 
month, 
year, 
week_day)
VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS
song_select = ("""
SELECT s.song_id, s.artist_id
FROM public.songs s
JOIN public.artists art
ON s.artist_id = art.artist_id
WHERE s.title = %s
AND art.artist_name = %s
AND s.duration = %s
""")

# QUERY LISTS
create_table_queries = [songplay_table_create, user_table_create,
                        song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop,
                      song_table_drop, artist_table_drop, time_table_drop]
