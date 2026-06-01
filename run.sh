set -e
mkdir -p "./logs" "./mailbox"
if [ ! -d "./inbox" ]; then
  echo "Ошибка: папка inbox не найдена"
  exit 1
fi
echo "Установка необходимых модулей и библиотек из файла с зависимостями:"
pip install -r requirements.txt
echo "Установлено"
cnt=$(ls "./inbox" | wc -l)
echo "Найдено файлов в inbox: $cnt"
echo "Запуск сортировщика"
python3 main.py | tee -a "./logs/processing.log"
fl=$?
if [ $fl -eq 0 ]; then
  echo "Обработка завершена успешно. Статистика:"
  cat "./logs/stats.json"
else
  echo "Ошибка во время выполнения (код $fl)"
  exit $fl
fi