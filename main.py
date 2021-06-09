import json
import logging

from constants import MOVIES_DB, LOGGING_CONFIG


logging.basicConfig(**LOGGING_CONFIG)


class Movie:
    def __init__(self, title: str):
        self.title = title.title()
        print(Movie._get_movies())

    def __str__(self):
        return self.title

    @staticmethod
    def _get_movies() -> list:
        with open(MOVIES_DB, "r") as file:
            return json.load(file)

    @staticmethod
    def _write_movies(movies):
        with open(MOVIES_DB, "w") as file:
            json.dump(movies, file, ensure_ascii=False, indent=4)

    def add_to_movies(self):
        movies = Movie._get_movies()
        if self.title not in movies:
            movies.append(self.title)
            Movie._write_movies(movies)
        else:
            logging.debug(f'{self.title} est déjà dans la liste des filmes')


if __name__ == '__main__':
    hp = Movie('harry potter')
    hp.add_to_movies()
