from notes.manager import NoteManager
import os

def test_create_and_read_note(tmp_path):
    filepath = tmp_path / "test.json"
    manager = NoteManager(filepath)
    manager.create_note("test", "contenido")
    assert manager.read_note("test") == "contenido"

def test_delete_note(tmp_path):
    filepath = tmp_path / "test.json"
    manager = NoteManager(filepath)
    manager.create_note("test", "contenido")
    manager.delete_note("test")
    assert manager.read_note("test") is None
