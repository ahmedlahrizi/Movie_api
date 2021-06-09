import pathlib 
from logging import DEBUG


MOVIES_DB = (pathlib.Path.cwd() / 'data' / 'movies.json').resolve()
LOGGING_CONFIG = {
    "level": DEBUG,
    "format": '%(asctime)s : [%(levelname)s] : %(message)s',
    "filename": "logs.log",
    "filemode": "w"
}
