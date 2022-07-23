import sqlite3
from typing import List


DBNAME = 'hash.db'
TABLE = 'hashtable'


class DbManager:
    def __init__(self, dbname: str = DBNAME) -> None:
        """Sqlite3 DB Contl"""
        self.con = sqlite3.connect(dbname)
        self.cur = self.con.cursor()

    def hastable(self):
        """Table exists check

        Note:
            Not used.
        """
        tables = self.tables()
        if len(tables) >= 1:
            return TABLE in tables[0][1]
        return False

    def createtable(self) -> None:
        """Create Table"""
        self.cur.execute(
            f'create table if not exists {TABLE}(id integer primary key autoincrement, path text, hash text)',
        )

    def append(self, path: str, hashs: str) -> None:
        """Add file profile to DB

        Args:
            path (str): file path
            hashs (str): hashs
        
        Note:
            Recommend using hash checked with hash.HashFilter.check.
        """
        self.cur.execute(
            f'insert into {TABLE} (path, hash) values (?, ?)',
            (path, hashs),
        )

    def allselect(self) -> any:
        """Check table contents(For debugging)

        Returns:
            any: table contents
        
        Note:
            Not used.
        """
        return self.cur.execute(f'select * from {TABLE}')

    def _like_search(self, hash):
        return self.cur.execute(
            f"select * from {TABLE} where hash like ?", (f'%#{hash}%',))

    def search(self, hashs: List[str]) -> dict:
        """Hash search

        Args:
            hashs (List[str]): hashs

        Returns:
            dict: search reslut
        
        Note:
            Recommend using hash checked with hash.HashFilter.passer.
        """
        tmp = {}
        for hash in hashs:
            for datum in self._like_search(hash):
                if datum[0] not in tmp:
                    tmp[datum[1]] = datum[2]
        return tmp

    def close(self) -> None:
        """Sqlite3 DB close

        Note:
            Be sure to call last!
        """
        self.cur.close()
        self.con.commit()
        self.con.close()
