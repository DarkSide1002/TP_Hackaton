import pytest

@pytest.mark.parametrize(
    ("name", "text"),
    [
        ("mail.txt", "a"),
        ("mail.eml", "a"),
        ("mail.json", 'a'),
        ("mail.html", "a"),
        ("mail.md", "a"),
    ],
)
def test_reader1(reader, write_mail, name, text):
    path = write_mail(name, text)
    email = reader.read(str(path))
    assert email.name == name
    assert email.text == text
    assert not email.isu
    assert email.error == ""


def test_reader2(reader, write_mail):
    path = write_mail("a.txt", "абоба", enc="utf-16")
    email = reader.read(str(path))
    assert not email.isu
    assert email.text == "абоба"


def test_reader3(reader, tmp_path):
    email = reader.read(str(tmp_path / "none.txt"))
    assert email.isu
    assert email.error == "Файл не найден"


def test_reader4(reader, write_mail):
    path = write_mail("empty.txt", "")
    email = reader.read(str(path))
    assert email.error == "Пустой файл"


def test_reader5(reader, tmp_path):
    path = tmp_path / "image.jpeg"
    path.write_bytes(b"blabla")
    email = reader.read(str(path))
    assert email.isu
    assert email.error == "Неподдерживающийся формат:.jpeg"
