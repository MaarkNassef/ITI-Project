import sqlite3



def get_db():

    """Connect to db"""

    database = sqlite3.connect('my_db.sqlite',

        detect_types=sqlite3.PARSE_DECLTYPES)

    database.row_factory = sqlite3.Row



    return database




def close_db(database=None):

    """Close the connection"""

    if database is not None:

        database.close()