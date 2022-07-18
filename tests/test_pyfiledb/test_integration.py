import pytest

import pyfiledb


@pytest.mark.parametrize(('path', 'hashs'), [
    (r'C:/Users/ik825/Desktop/pyfiledb/requirements1.txt', '#hash1#hash2'),
    (r'C:/Users/ik825/Desktop/pyfiledb/requirements2.txt', '#hash2#hash1'),
])
def test_pyfiledb(path, hashs):
    filedb = pyfiledb.pyfiledb()
    filedb.append(path, hashs)
    reslut = {path: hashs}
    assert filedb.search('#hash2') == reslut
    filedb.close()
