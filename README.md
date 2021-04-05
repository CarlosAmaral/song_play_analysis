# Song Play Analysis

## Introduction
This project aims analyse data from song plays based on user interaction, think of Spotify. In this project we create a star schema database model to best connect and understand our data. To achieve this goal we create a suitable database shema with a ETL pipeline.

## Database schema
The schema can be quickly visualized by opening up the `index.html` under `doc/sparkifydb`.

This database schema encompasses the following tables from two distinct data sets to lastly form a fact table:

1. song dataset: 
    - song table: dimensional table that contains data from the available songs such as year, duration, title, song ID (PK) and artist ID (FK);
    - artists table: dimensional table contains data related to the artists from the songs such as artist ID (PK), artist name, and artist's latitude and logitude;
2. log dataset (data refers to user interaction data):
    - time table: dimensional table containing data related to the times when users when users were listening to music;
    - users table: dimensional table containing user data such as first and last name, gender and subscription level.

Lastly, the fact table that gathers the data from these two data sets is called songplay table. It contains FKs such as artist Id, song Id and user Id, as well as timestamp of when the song was played and location.


## Setup

1) Install python 3.x.x ;
2) Install and run postgres ;
3) Create a database called `sparkifydb` ;
4) Run `python create_tables.py` on the root of the project in order to create, and drop if they exist, the necessary tables
5) Run `python etl.py` to fulfill the project requirements and fill up the tables 
