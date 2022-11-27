import mysql
import mysql.connector

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}


def show_films(cursor, title):
    # inner join query
    cursor.execute('''select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 
    'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON 
    film.studio_id=studio.studio_id''')
    # getting the results from the cursor object
    films = cursor.fetchall()
    print("\n -- {} --".format(title))

    # displaying results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(
            film[0], film[1], film[2], film[3]))


def main():
    # Creating connection to database
    connection = mysql.connector.connect(
        host="localhost",
        user="movies_user",
        password="popcorn",
        database="films"
    )
    # Creating cursor
    cursor = connection.cursor()

    # Displaying existing records in database
    show_films(cursor, "DISPLAYING FILMS")

    # Performing Insertion of new movie
    insertquery = "INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) " \
                  "VALUES ('Star Wars', '2000', '155', 'George Lucas', (SELECT studio_id FROM studio WHERE " \
                  "studio_name = '20th Century Fox'),(SELECT genre_id FROM genre WHERE genre_name = 'SciFi') ); "
    connection.commit()
    cursor.execute(insertquery)
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Performing Update of Alien movie
    updatequery = "update film set genre_id = (select genre_id from genre where genre_name = 'Horror') where " \
                  "film_name = 'Alien'; "
    connection.commit()
    cursor.execute(updatequery)
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    # Deleting Gladiator movie from table
    deletequery = " delete from film where film_name = 'Gladiator';"
    connection.commit()
    cursor.execute(deletequery)
    show_films(cursor, "DISPLAYING FILMS AFTER Delete")


main()
