import pytest

from pyfiledb.hash import HashFilter


def test_hashfiltercheck():
    assert HashFilter.check('#hash1#hash2') is True
    with pytest.raises(ValueError):
        HashFilter.check('hash1#hash2')

    with pytest.raises(ValueError) as e:
        HashFilter.check('hash1')

    # 記号を許している
    # with pytest.raises(ValueError) as e:
    #     HashFilter.check('#hash1#[]$"!"')
    
    assert str(e.value) == 'The hash format is incorrect.'
