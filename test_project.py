import pytest
import os
import json
from project import add_item, categorize_text, search_items, load_history, save_history

TEST_FILE = "test_clipboard_history.json"

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    monkeypatch.setattr("project.CLIPBOARD_FILE", TEST_FILE)
    with open(TEST_FILE, 'w') as f:
        json.dump([], f)
    yield
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_add_item():
    add_item("First Item")
    history = load_history()
    assert len(history) == 1
    assert history[0]["text"] == "First Item"

    for i in range(55):
        add_item(f"Item {i}")

    new_history = load_history()
    assert len(new_history) == 50
    assert new_history[0]["text"] == "Item 54"

def test_categorize_text():
    assert categorize_text("https://google.com") == "url"
    assert categorize_text("test@example.com") == "email"
    assert categorize_text("1234567890") == "phone"
    assert categorize_text("import os") == "code"
    assert categorize_text("123.45") == "number"
    assert categorize_text("Just some text") == "text"

def test_search_items():
    add_item("Apple")
    add_item("Banana")
    add_item("Pineapple")

    assert len(search_items("apple")) == 2
    assert len(search_items("Banana")) == 1
    assert len(search_items("Orange")) == 0

def test_load_history():
    assert load_history() == []

    sample_data = [{"text": "Saved", "type": "text", "time": "12:00", "pinned": False}]
    save_history(sample_data)

    loaded = load_history()
    assert len(loaded) == 1
    assert loaded[0]["text"] == "Saved"

def test_save_history():
    data_to_save = [{"text": "Manual Save", "type": "text", "time": "01:00", "pinned": True}]
    save_history(data_to_save)

    with open(TEST_FILE, 'r') as f:
        data_on_disk = json.load(f)

    assert data_on_disk[0]["text"] == "Manual Save"
    assert data_on_disk[0]["pinned"] is True
