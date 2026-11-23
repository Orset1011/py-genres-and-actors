import sqlite3
import managers
import models
def main():
    actors = managers.ActorManager("db.sqlite3", "actors")

    genres = managers.GenreManager("db.sqlite3", "genres")

    genres.create("Western")
    genres.create("Action")
    genres.create("Drama")

    actors.create("George", "Klooney")
    actors.create("Kianu", "Reaves")
    actors.create("Scarlett", "Keegan")
    actors.create("Will", "Smith")
    actors.create("Scarlet", "Johansson")




if __name__ == "__main__":
    main()
