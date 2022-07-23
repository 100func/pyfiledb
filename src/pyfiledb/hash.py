import re
from typing import List


class HashFilter:
    @staticmethod
    def passer(data: str) -> List[str]:
        """Hash format passer

        Args:
            data (str): hashs

        Returns:
            List[str]: hash list
        
        Example:
            >>> HashFilter.passer('#hash1#hash2')
            ['hash1', 'hash2']
        """
        if HashFilter.check(data):
            tmp = data.split('#')
            del tmp[0]
            return tmp

    @staticmethod
    def check(data: str) -> bool:
        """Hash format check

        Args:
            hashs (str): hashs

        Raises:
            ValueError: The hash format is incorrect.

        Returns:
            bool: check complete
        """
        pattern = r"(#[a-zA-Z0-9]*)*"
        repatter = re.compile(pattern)
        reslut = repatter.match(data)
        if reslut.group() == '':
            raise ValueError('The hash format is incorrect.')
        return True
