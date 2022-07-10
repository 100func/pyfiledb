import pprint
import sqlite3
from typing import List


DBNAME = 'hash.db'
TABLE = 'hashtable'


def hashpasser(data):
    tmp = data.split('#')
    del tmp[0]
    return tmp


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
        if isinstance(hashs, str):
            hash_str = hashs
        self.cur.execute(
            f'insert into {TABLE} (path, hash) values (?, ?)',
            (path, hash_str),
        )

    def allselect(self):
        return self.cur.execute(f'select * from {TABLE}')

    def search(self, hashs: List[str]) -> list:
        tmp = []
        print('hello')
        for datum in self.allselect():
            print('datum', datum)
            for hash in hashs:
                if hash in datum[-1]:
                    print('hash', hash)
                    tmp.append(datum[1])
        return tmp

    def close(self) -> None:
        self.cur.close()
        self.con.close()
