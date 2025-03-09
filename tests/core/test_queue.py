import pytest
from my_queue.core.queue import Queue


@pytest.fixture
def queue():
    return Queue()


def test_append(queue):
    queue.append("manuel")
    players = queue.get_all_players()
    assert "manuel" in players


def test_contains(queue):
    queue.append("manuel")
    assert queue.contains("manuel")


def test_delete(queue):
    queue.append("daniel")
    queue.delete_player("daniel")
    players = queue.get_all_players()
    assert "daniel" not in players

