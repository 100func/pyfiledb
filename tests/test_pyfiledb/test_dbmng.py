import os

from pyfiledb.dbmng import DbManager, DBNAME

TEST_PATH = 'test/test'
TEST_HASH = '#hash1#hash2'
dbmng = DbManager()


def test_dbmng_create():
    dbmng.createtable()
    assert os.path.isfile(DBNAME)


def test_dbmng_append():
    dbmng.append(TEST_PATH, TEST_HASH)


def test_dbmng_close():
    dbmng.close()
