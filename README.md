# TP_Hackaton

email-classifier/
├── README.md
├── .gitignore
│
├── data/
│   ├── inbox/               # исходные входящие письма (~100 файлx x   ов)
│   │   ├── email_001.eml
│   │   ├── email_002.txt
│   │   ├── email_003.json
│   │   └── ...
│   └── mailbox/             # результат — классифицированные папки
│       ├── inbox/           # нераспознанные / требуют внимания
│       ├── critical/        # критичgiеские инциденты
│       ├── spam/            # спам
│       ├── requests/        # обычные запросы в поддержку
│       ├── info/            # информационные письма
│       └── unclassified/    # не попало ни в одну категорию
│
├── src/
│   ├── __init__.py
│   ├── email_reader.py      # чтение и парсинг файлов
│   ├── classifier.py        # логика классификации
│   ├── file_manager.py      # перемещение файлов по папкам
│   ├── reporter.py          # формирование лога и статистики
│   └── pipeline.py          # главный оркестратор (main-класс)
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # фикстуры pytest
│   ├── test_reader.py       # тесты чтения писем
│   ├── test_classifier.py   # тесты классификации
│   ├── test_file_manager.py # тесты перемещения файлов
│   └── test_edge_cases.py   # граничные случаи
│
├── logs/
│   └── processing.log       # генерируется при запуске
│
├── reports/
│   └── stats.json           # JSON-статистика последнего запуска
│
├── main.py                  # точка входа Python
└── run.sh                   # bash-скрипт запуска