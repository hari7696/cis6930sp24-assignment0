import pandas as pd
import pytest

def test_creation():
    df = pd.DataFrame({'id': [1, 2,3,4,5], 'name': ['a', 'b', 'c', 'd', 'e']})
    print("FUCNTION CALLED")
    assert len(df) == 5
    return df #this doesn't show on stdout but it will hand it to what's calling it


def test_update(id):
    df = test_creation()
    assert len(df) == 5
