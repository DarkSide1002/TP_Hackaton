import os
from dataclasses import dataclass

@dataclass
class Email:
    name: str = ""
    text: str = ""
    isu: bool = False
    error: str = ""


class EmailReader:
    extensions = {".txt", ".eml", ".json", ".html", ".htm", ".md"}

    def read(self, path: str) -> Email:
        name = os.path.basename(path)
        ext = os.path.splitext(path)[1].lower()
        if not os.path.exists(path):
            return Email(name=name, isu=True, error="Файл не найден")
        if os.path.getsize(path) == 0:
            return Email(name=name, isu=True, error="Пустой файл")
        if ext not in self.extensions:
            return Email(name=name, isu=True, error=f"Неподдерживающийся формат:{ext}")
        try:
            raw = self.read2(path)
        except Exception as e:
            return Email(name=name, isu=True, error=f"Ошибка чтения:{e}")
        return Email(name=name, text=raw)

    @staticmethod
    def read2(path: str) -> str:
        for c in ("utf-8", "utf-16", "cp1251", "latin-1"):
            try:
                with open(path, "r", encoding=c) as f:
                    return f.read()
            except UnicodeDecodeError:
                continue
        raise Exception("Ни одна кодировка не подошла")
