import sqlite3
from typing import List


DBNAME = 'hash.db'
TABLE = 'hashtable'


class DbManager:
    def __init__(self, dbname: str = DBNAME) -> None:
        self.con = sqlite3.connect(dbname)
        self.cur = self.con.cursor()

    def hastable(self):
        tables = self.tables()
        if len(tables) >= 1:
            return TABLE in tables[0][1]
        return False

    def createtable(self) -> None:
        self.cur.execute(
            f'create table if not exists {TABLE}(id integer primary key autoincrement, path text, hash text)',
        )

    def append(self, path: str, hashs: str) -> None:
        self.cur.execute(
            f'insert into {TABLE} (path, hash) values (?, ?)',
            (path, hashs),
        )

    def allselect(self):
        return self.cur.execute(f'select * from {TABLE}')

    def _like_search(self, hash):
        return self.cur.execute(
            f"select * from {TABLE} where hash like ?", (f'%#{hash}%',))

    def search(self, hashs: List[str]) -> dict:
        tmp = {}
        for hash in hashs:
            for datum in self._like_search(hash):
                if datum[0] not in tmp:
                    tmp[datum[1]] = datum[2]
        return tmp

    def close(self) -> None:
        self.cur.close()
        self.con.close()
