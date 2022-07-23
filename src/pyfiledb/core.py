from .dbmng import DbManager
from .hash import HashFilter


class pyfiledb:
    def __init__(self) -> None:
        self.dbmanager = DbManager()
        self.dbmanager.createtable()

    def append(self, path: str, hashs: str) -> None:
        """File profile entry

        Args:
            path (str): file path
            hashs (str): hashs

        Examples:
            >>> filedb = pyfiledb.pyfiledb
            >>> filedb.append('xxxx/yyyy/zzz.txt', '#hash1#hash2')
            >>> filedb.close()
        """
        self.dbmanager.append(path, hashs)

    def search(self, hashs: str) -> dict:
        """Hash search

        Args:
            hashs (str): target hashs

        Returns:
            dict: search reslut
        
        Examples:
            >>> filedb = pyfiledb.pyfiledb
            >>> filedb.search('#hash1')
            {'xxxx/yyyy/zzz.txt':'#hash1#hash2'}
            >>> filedb.close()
        Note:
            ValueError when the format is not #xxx#yyy
        """
        hashs_list = HashFilter.passer(hashs)
        return self.dbmanager.search(hashs_list)

    def close(self):
        """DB close

        Note:
            Be sure to call last!
        """
        self.dbmanager.close()
