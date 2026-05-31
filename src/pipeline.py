import os
from src.email_reader import EmailReader
from src.classifier import Classifier, dict
from src.file_manager import FileManager
from src.reporter import Reporter, setup_logger


class Pipeline:
    def __init__(self, inbox: str, dest: str, log: str, report: str):
        self.inbox = inbox
        self.dest = dest
        self.log = setup_logger(log)
        self.reader = EmailReader()
        self.classifier = Classifier()
        self.file_manager = FileManager(self.dest)
        self.reporter = Reporter(report, self.log)

    def run(self):
        self.log.info(f"Pipeline запустился. Письма к сортировке={self.inbox}")
        if not os.path.isdir(self.inbox):
            self.log.error(f"Письма не найдены: {self.inbox}")
            raise FileNotFoundError(self.inbox)
        self.file_manager.create(list(dict.keys()))
        files = []
        for f in os.listdir(self.inbox):
            if os.path.isfile(os.path.join(self.inbox, f)):
                files.append(f)
        self.log.info(f"Найдено {len(files)} файлов")
        for fname in files:
            path = os.path.join(self.inbox, fname)
            email = self.reader.read(path)
            c = self.classifier.classify(email)
            try:
                self.file_manager.move(path, c)
                self.reporter.record(fname, c, email.error)
            except Exception as e:
                self.log.error(f"Ошибка при копировании {fname}: {e}")
                self.reporter.record(fname, "unclassified", str(e))
        return self.reporter.save()
