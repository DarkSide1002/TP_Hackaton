import pytest

from src.email_reader import Email

@pytest.mark.parametrize(
    ("text", "cat"),
    [
        ("поздравляем вы выиграли приз", "spam"),
        ("черновик письма не отправлять", "draft"),
        ("critical инцидент немедленно", "critical"),
        ("ошибка авторизации зависает", "software_issues"),
        ("сломался принтер", "hardware_issues"),
        ("счет на оплату", "financial_requests"),
        ("встреча zoom", "meeting_requests"),
        ("информируем плановые работы", "informational"),
    ],
)
def test_classifier1(classifier, text, cat):
    email = Email(name="mail.txt", text=text)
    assert classifier.classify(email) == cat


def test_classifier2(classifier):
    email = Email(name="mail.txt", text="здравствуйте")
    assert classifier.classify(email) == "unclassified"


def test_classifier3(classifier):
    email = Email(name="bad.bin", isu=True, error="Неподдерживающийся формат:.bin")
    assert classifier.classify(email) == "unclassified"


def test_classifier4(classifier):
    email = Email(name="mail.txt", text="поздравляем вы выиграли срочно помощь критический ноутбук информируем")
    assert classifier.classify(email) == "spam"