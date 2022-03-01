import pytest

from ...store import Store
from .watch import WatchType, watch


@pytest.fixture
def store() -> Store:
    return Store({
        "dict": {"abc": "test"},
        "list": ["abc"]
    })
# END store


@pytest.mark.asyncio
async def test__watch_returns_changes_in_dict(store: Store):

    messages = []

    watch(
        store, "dict",
        watch_type=WatchType.DICT
    ).subscribe(messages.append)

    await store.update("def", "dict", "abc")

    assert messages == [{("abc", "def")}]
# END test__watch_returns_changes_in_dict


@pytest.mark.asyncio
async def test__watch_returns_changes_in_list(store: Store):

    messages = []

    watch(store, "list").subscribe(messages.append)

    await store.update(["def"], "list")

    assert messages == [{"def"}]
# END test__watch_returns_changes_in_list
