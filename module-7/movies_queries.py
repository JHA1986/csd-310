# Jonah Aney 4/27/25 CSD310 Module 7.2 Assignment: Movies: Table Queries

# to connect
import mysql.connector
from mysql.connector import errorcode
# to use .env file
from dotenv import dotenv_values

# using our .env file
secrets = dotenv_values(".env")

"""database config object"""
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
# not in .env file
    "raise_on_warnings": True
}
try:
    """try/catch block for handling potential MySQL database errors"""
# connect to the movie database
    db = mysql.connector.connect(**config)

# output the connection status
    print("\n Database user {} connected to MySQL on host {}".format(config["user"], config["host"]))

# create a cursor object to execute queries
    cursor = db.cursor()

# first query: select all from studio
    print("-- DISPLAYING Studio RECORDS --")
    cursor.execute("SELECT studio_id, studio_name FROM studio")
    studios = cursor.fetchall()
    for studio in studios:
        print(f"Studio ID: {studio[0]}")
        print(f"Studio Name: {studio[1]}\n")

# second query: select all from genre
    print("-- DISPLAYING Genre RECORDS --")
    cursor.execute("SELECT genre_id, genre_name FROM genre")
    genres = cursor.fetchall()
    for genre in genres:
        print(f"Genre ID: {genre[0]}")
        print(f"Genre Name: {genre[1]}\n")

# third query: select films under 120 minutes
    print("-- DISPLAYING Short Film RECORDS --")
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    films = cursor.fetchall()
    for film in films:
        print(f"Film Name: {film[0]}")
        print(f"Runtime: {film[1]}\n")

# fourth query: select films and directors grouped by director
    print("-- DISPLAYING Director RECORDS in Order --")
    cursor.execute("""
        SELECT film_name, film_director
        FROM film
        ORDER BY film_director
    """)
    film_director = cursor.fetchall()
    for film in film_director:
        print(f"Film Name: {film[0]}")
        print(f"Director: {film[1]}\n")

# close the connection
    cursor.close()

    input("\n\n Press any key to continue... ")
except mysql.connector.Error as err:
    """on error code"""
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)
finally:
    """close the connection to MySQL"""
    db.close()