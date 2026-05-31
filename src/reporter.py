import json
import logging
import os
from datetime import datetime
from typing import List, Dict


def setup_logger(path: str) -> logging.Logger:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    l = logging.getLogger("email_classifier")
    l.setLevel(logging.DEBUG)
    if l.handlers:
        l.handlers.clear()
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    fh = logging.FileHandler(path, encoding="utf-8")
    fh.setFormatter(fmt)
    fh.setLevel(logging.DEBUG)
    l.addHandler(fh)
    return l


class Reporter:
    def __init__(self, path: str, l: logging.Logger):
        self.path = path
        self.l = l
        self.ans: List[Dict] = []
        self.start = datetime.now()

    def record(self, name: str, c: str, error: str = None):
        self.ans.append({"name": name, "category": c, "error": error})
        if error:
            self.l.warning(f"{name} -> {c} [{error}]")
        else:
            self.l.info(f"{name} -> {c}")

    def save(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        total = len(self.ans)
        cnt = {}
        errors = [r for r in self.ans if r["error"]]
        for r in self.ans:
            cnt[r["category"]] = cnt.get(r["category"], 0) + 1
        duration = (datetime.now() - self.start).total_seconds()
        stats = {
            "время": self.start.isoformat(),
            "продолжительность": round(duration, 2),
            "проверенно писем": total,
            "по категориям": cnt,
            "количество ошибок": len(errors),
            "ошибки": errors,
        }
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
        self.l.info(f"Выполнено. Всего: {total}, Ошибок: {len(errors)}, Продолжительность: {duration:.1f}s")
        self.l.info(f"Статистика сохранена -> {self.path}")
        return stats
