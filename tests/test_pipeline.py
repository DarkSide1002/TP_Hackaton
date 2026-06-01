import json
import pytest
from src.pipeline import Pipeline


@pytest.fixture
def p_paths(tmp_path):
    inbox = tmp_path / "inbox"
    mailbox = tmp_path / "mailbox"
    log_path = tmp_path / "logs" / "processing.log"
    report_path = tmp_path / "logs" / "stats.json"
    inbox.mkdir()
    (inbox / "critical.txt").write_text(
        "critical инцидент",
        encoding="utf-8",
    )
    (inbox / "spam.txt").write_text(
        "поздравляем, вы выиграли",
        encoding="utf-8",
    )
    (inbox / "unknown.txt").write_text(
        "добрый день",
        encoding="utf-8",
    )
    (inbox / "empty.txt").write_text("", encoding="utf-8")
    (inbox / "photo.jpeg").write_bytes(b"not email")
    return inbox, mailbox, log_path, report_path


def test_pipeline1(p_paths):
    inbox, mailbox, log_path, report_path = p_paths
    pipeline = Pipeline(str(inbox), str(mailbox), str(log_path), str(report_path))
    stats = pipeline.run()
    assert stats["проверенно писем"] == 5
    assert stats["по категориям"]["critical"] == 1
    assert stats["по категориям"]["spam"] == 1
    assert stats["по категориям"]["unclassified"] == 2
    assert stats["по категориям"]["draft"] == 1
    assert stats["количество ошибок"] == 2
    assert (mailbox / "critical" / "critical.txt").exists()
    assert (mailbox / "spam" / "spam.txt").exists()
    assert (mailbox / "unclassified" / "unknown.txt").exists()
    assert (mailbox / "draft" / "empty.txt").exists()
    assert (mailbox / "unclassified" / "photo.jpeg").exists()
    assert log_path.exists()
    assert report_path.exists()
    saved = json.loads(report_path.read_text(encoding="utf-8"))
    assert saved == stats


def test_pipeline2(p_paths):
    inbox, mailbox, log_path, report_path = p_paths
    pipeline = Pipeline(str(inbox), str(mailbox), str(log_path), str(report_path))
    pipeline.run()
    lst = [
        "spam",
        "draft",
        "critical",
        "software_issues",
        "hardware_issues",
        "financial_requests",
        "meeting_requests",
        "informational",
        "unclassified",
    ]
    for c in lst:
        assert (mailbox / c).is_dir()


def test_pipeline3(tmp_path):
    pipeline = Pipeline(
        str(tmp_path / "blablabla"),
        str(tmp_path / "mailbox"),
        str(tmp_path / "logs" / "processing.log"),
        str(tmp_path / "logs" / "stats.json"),
    )
    with pytest.raises(FileNotFoundError):
        pipeline.run()
