import sys
from pathlib import Path
import pytest

root = Path(__file__).parent.parent
sys.path.insert(0, str(root))

@pytest.fixture
def reader():
    from src.email_reader import EmailReader
    return EmailReader()

@pytest.fixture
def classifier():
    from src.classifier import Classifier
    return Classifier()

@pytest.fixture
def write_mail(tmp_path):
    inbox = tmp_path / "inbox"
    inbox.mkdir()
    def _write(name, text, enc="utf-8"):
        path = inbox / name
        path.write_text(text, encoding=enc)
        return path
    return _write
