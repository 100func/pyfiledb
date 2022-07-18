from .dbmng import DbManager
from .hash import HashFilter


class pyfiledb:
    def __init__(self) -> None:
        self.dbmanager = DbManager()
        self.dbmanager.createtable()

    def append(self, path: str, hashs: str) -> None:
        self.dbmanager.append(path, hashs)

    def search(self, hashs: str) -> dict:
        hashs_list = HashFilter.passer(hashs)
        return self.dbmanager.search(hashs_list)

    def close(self):
        self.dbmanager.close()
