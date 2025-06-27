import json
from pathlib import Path

class NoteManager:
    def __init__(self, filepath='notes.json'):
        self.filepath = Path(filepath)
        self.notes = self._load_notes()

    def _load_notes(self):
        if self.filepath.exists():
            with open(self.filepath, 'r') as f:
                return json.load(f)
        return {}

    def save_notes(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.notes, f, indent=4)

    def create_note(self, title, content):
        self.notes[title] = content
        self.save_notes()

    def read_note(self, title):
        return self.notes.get(title)

    def delete_note(self, title):
        if title in self.notes:
            del self.notes[title]
            self.save_notes()

    def list_notes(self):
        return list(self.notes.keys())
