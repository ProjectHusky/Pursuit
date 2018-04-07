import _sqlite3


class DatabaseDriver:

    tables = ["trips", "members", "membersInfo"]

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
        self.cursor.execute("CREATE TABLE IF NOT EXISTS trips(tripID INTEGER, a TEXT, b TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS members(tripID INTEGER, memberID INTEGER, payments INTEGER)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS membersInfo(memberID INTEGER, name TEXT, email TEXT)")

    def insert_trip(self, trip_id):
        self.cursor.execute("INSERT INTO trips (tripID, a, b) VALUES (?, ?, ?)", trip_id)
        self.connection.commit()

    def insert_member(self, member_metadata):
        self.cursor.execute("INSERT into members (tripID, memberID, payments) VALUES (?, ?, ?)", member_metadata)
        self.connection.commit()

    def insert_member_info(self, member_info_metadata):
        self.cursor.execute("INSERT into members (tripID, memberID, payments) VALUES (?, ?, ?)", member_info_metadata)
        self.connection.commit()

    def reset(self):
        for table in self.tables:
            self.cursor.execute("DROP TABLE " + table)


