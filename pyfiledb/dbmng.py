import sqlite3


DBNAME = 'hash.db'
TABLE = 'hashtable'


class DbManager:
    def __init__(self, dbname: str = DBNAME) -> None:
        self.con = sqlite3.connect(dbname)
        self.cur = self.con.cursor()

    def create_table(self) -> None:
        self.cur.execute(
            f'create table {TABLE}(id integer primary key autoincrement, path text, hash text)',
        )

    def append(self, path: str, hashs: list) -> None:
        self.cur.execute(
            f'insert into {TABLE} (path, hash) values (?, ?)',
            (path, '#'.join(hashs), ),
        )

    def search(self, hashs: list):
        pass

    def close(self) -> None:
        self.cur.close()
        self.con.close()
