from pathlib import Path
import pytest
from src.file_manager import FileManager


def test_file_manager_1(tmp_path):
    path = tmp_path / "mailbox"
    manager = FileManager(str(path))
    manager.create(["critical", "spam", "unclassified"])
    assert (path / "critical").is_dir()
    assert (path / "spam").is_dir()
    assert (path / "unclassified").is_dir()

def test_file_manager_2(tmp_path):
    src = tmp_path / "mail.txt"
    src.write_text("urgent критично", encoding="utf-8")
    mailbox = tmp_path / "mailbox"
    manager = FileManager(str(mailbox))
    manager.create(["critical"])
    dest = Path(manager.move(str(src), "critical"))
    assert dest == mailbox / "critical" / "mail.txt"
    assert dest.read_text(encoding="utf-8") == "urgent критично"
    assert src.exists()

def test_file_manager_3(tmp_path):
    src = tmp_path / "mail.txt"
    src.write_text("urgent критично", encoding="utf-8")
    mailbox = tmp_path / "mailbox"
    manager = FileManager(str(mailbox))
    with pytest.raises(FileNotFoundError):
        manager.move(str(src), "critical")
