import pytest

from ...store import Store
from ..select import select
from asyncio import gather


@pytest.fixture
def store() -> Store:
    return Store()
# END store


def test__select_emits_starting_value(store: Store):

    messages = []

    select(store, "abc").subscribe(messages.append)

    assert messages == [None]
# END test__select_emits_starting_value


@pytest.mark.asyncio
async def test__select_emits_changes(store: Store):

    messages = []

    select(store, "abc").subscribe(messages.append)

    await store.update("def", "abc")

    assert messages == [None, "def"]
# END test__select_emits_changes


@pytest.mark.asyncio
async def test__select_only_emits_changes_on_selected_path(store: Store):

    messages = []

    # Set initial state
    await store.set({"abc": "def", "ghi": "jkl"})

    # Listen for one key in the state (ignore changes to the other key)
    select(store, "abc").subscribe(messages.append)

    # Update a value that we're listening for, and one we're not listening for
    await gather(
        store.update("pql", "abc"),
        store.update("mno", "ghi")
    )

    # Expect the initial state and the new value in messages, as well as no duplicate emissions.
    assert messages == ["def", "pql"]
# END test__select_only_emits_changes_on_selected_path
