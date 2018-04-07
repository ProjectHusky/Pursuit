import _sqlite3


class DatabaseDriver:
    def __init__(self, database):
        """
        Constructor, passes in the location of the database on disk.

        :param database: The path to the database on disk.
        """
        self.connection = _sqlite3.connect(database)
        self.connection.text_factory = str
        self.cursor = self.connection.cursor()

    def create_tables(self):
        """
        Create all the tables necessary for the program.

        :return: Void.
        """
        self.cursor.execute("CREATE TABLE IF NOT EXISTS trips(tripID INTEGER)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS members(tripID INTEGER, memberID INTEGER, payments INTEGER)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS membersInfo(memberID INTEGER, name TEXT, email TEXT)")