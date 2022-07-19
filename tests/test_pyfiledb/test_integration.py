import pytest

import pyfiledb


@pytest.mark.parametrize(('path', 'hashs', 'hash'), [
    (r'C:/Users/ik825/Desktop/pyfiledb/requirements1.txt', '#hash1#hash2', '#hash1'),
    (r'C:/Users/ik825/Desktop/pyfiledb/requirements2.txt', '#hash2#hash1', '#hash1'),
    (r'C:/Users/ik825/Desktop/pyfiledb/requirements3.txt', '#hash2#hash1', '#hash2'),
    (r'C:/Users/ik825/Desktop/pyfiledb/requirements4.txt', '#hash2#hash1', '#hash2'),
])
def test_pyfiledb(path, hashs, hash):
    filedb = pyfiledb.pyfiledb()
    filedb.append(path, hashs)
    reslut = {path: hashs}
    assert filedb.search(hash) == reslut
    filedb.close()
