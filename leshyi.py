import datetime
import time
import logging

tasks = [] # Очередь

chas = datetime.datetime.now()
kros = chas.strftime("%D:%H:%M:%S")
boss = 'Worker_Village_Spy'

# Настройка логирования (для отладки, если что-то пойдёт не так)
logging.basicConfig(filename='my_app.log', level=logging.ERROR, 
          format='%(asctime)s - %(levelname)s - %(message)s')

def process_tasks():
  with open('sistem31.txt', 'a') as f:
    f.write(boss + '\n')

while True:
  try:
    task = input()
    if task == "косяков":
      break
    tasks.append(task)
    with open('sistem31.txt', 'a') as f:
      f.write(kros + '_' + task + '\n')
  except EOFError:
    break
  
def main():
  while True:
    try:
      process_tasks()
      time.sleep(60) # Проверяем задачи каждые 60 секунд
    except Exception as e:
      logging.exception(f"Критическая ошибка: {e}")
      break # Прекращаем работу при критических ошибках

if __name__ == "__main__":
  main()
