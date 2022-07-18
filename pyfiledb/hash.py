import re
from typing import List


class HashFilter:
    @staticmethod
    def passer(data: str) -> List[str]:
        if HashFilter.check(data):
            tmp = data.split('#')
            del tmp[0]
            return tmp

    @staticmethod
    def check(data: str) -> bool:
        pattern = r"(#[a-zA-Z0-9]*)*"
        repatter = re.compile(pattern)
        reslut = repatter.match(data)
        if reslut.group() == '':
            raise ValueError('The hash format is incorrect.')
        return True
