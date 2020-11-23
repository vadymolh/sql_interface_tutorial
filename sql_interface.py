import sqlite3


class MusicDB():
    def __init__(self):
        self.connection = sqlite3.connect("chinook.db")
        self.cur = self.connection.cursor()
    def select(self, query, *args):
        print(args)
        if args:
            self.cur.execute(query, args)
        else:
            self.cur.execute(query) 
        return self.cur.fetchall()


class SQL_query():
    def __init__(self, connection,partial_track_name=""):
        self.sql = connection 
        self.query_name = partial_track_name

    def get_track(self, query_name):
        print (query_name)
        data = self.sql.select("""SELECT name FROM tracks 
                                   WHERE name LIKE '%{0}%' ;""".format( query_name))
        return [i[0] for i in data] 
    def get_info(self, track_name):
        album  = self.sql.select('''SELECT albums.Title 
                                    FROM tracks
                                    INNER JOIN albums on tracks.AlbumId == albums.AlbumId
                                    WHERE tracks.Name=="{0}";'''.format(track_name))
        return album[0][0]