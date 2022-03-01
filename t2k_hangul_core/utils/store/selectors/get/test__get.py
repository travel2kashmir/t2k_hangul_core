import pytest

from ...store import Store
from .get import get


@pytest.fixture
def store() -> Store:
    return Store()
# END store

@pytest.mark.asyncio
async def test__get_returns_first_value_at_path(store: Store):

    value = await get(store, "abc")

    assert value == None
# END test__get_returns_first_value_at_path

@pytest.mark.asyncio
async def test__get_returns_first_value_at_path_for_predicate(store: Store):

    def predicate(value):
        return value is not None
    # END def

    query = get(store, "abc", predicate=predicate)

    store.set({"abc": "def"})
    
    value = await query

    assert value == "def"
# END test__get_returns_first_value_at_path_for_predicate
