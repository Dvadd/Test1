import os

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

reader = {
  'name': 'Давид',
  'surname': 'Завальнюк',
  'group': 'ІПЗс-23-2',
  'course': 1,
  'borrow': [],
  'statistic': []
}

books = [
  "Тигролови",
  "Кобзар",
  "Маруся Чурай",
  "Жовтий князь",
  "Кайдашева сім'я",
  "Дніпро в огні",
  "Пан Коцький",
  "Сто тисяч і мертвець",
  "Чорна рада",
  "Захар Беркут",
  "Андрій",
  "Тіні забутих предків",
  "Сад Гетсиманський",
  "Доля",
  "Метелики",
]

while True:
  print(f"Поточний читач: {reader['name']} {reader['surname']}\n")
  print(f"Група: {reader['group']}  Курс: {reader['course']}\n")
  print("Книги в бібліотеці:\n")
  print(', '.join(books))
  print()
  if (len(reader['borrow']) == 0):
    print("Заборгованих книг немає")
  else:
    print(f"\nЗаборговані книги: {', '.join(reader['borrow'])}")

  print()

  if (len(reader['statistic']) == 0):
    print("Прочитаних книг немає")
  else:
    print(f"\nПрочитані книги: {', '.join(reader['statistic'])}")

  user_input = input(
      "\nКоманди:\n0 - вхід/повернутися в головне меню\n1 - вивевсти карту читача\n2 - позичити книгу\n3 - віддати книгу\n\nВести: "
  )

  if user_input.strip() == "0":
    print("Вхід")
    break

  if user_input.strip() == "1":
    clear_screen()
    print("Ви вибрали: Вивести карту читача\n")
    print("\n-----------------------------------\n")
    print("КАРТА ЧИТАЧА\n\n")
    print(f"{reader['name']} {reader['surname']}\n")
    print(f"Група: {reader['group']}  Курс: {reader['course']}\n")
    print("\n-----------------------------------\n")
    continue

  if user_input.strip() == "2":
    clear_screen()
    print("Ви вибрали: Позичити книгу\n")
    print("Щоб позичити книгу введіть одну з наведених нижче назв: \n")
    for book in books:
      print(book)
    book_name = input("\nВведіть назву книги: ")

    if book_name.strip() == "0":
      clear_screen()
      continue

    if book_name in books:
      reader['borrow'].append(book_name)
      clear_screen()
      print(f"Книга \"{book_name}\" була додана до позичок\n")
    else:
      clear_screen()
      print(f"Книга \"{book_name}\" не знайдена\n")
    continue

  if user_input.strip() == "3":
    clear_screen()
    print("Ви вибрали: Віддати книгу\n")
    print("Позичені книги: \n")
    for book in reader['borrow']:
      print(book)

    if (len(reader['borrow']) == 0):
      clear_screen()
      print("У вас немає заборгованих книг\n")
      continue

    book_name = input("\nВведіть назву книги: ")
    if book_name in reader['borrow']:
      reader['borrow'].remove(book_name)
      if (book_name in reader['statistic']):
        clear_screen()
        print(f"Книга \"{book_name}\" була повернута\n")
        continue
      reader['statistic'].append(book_name)
      clear_screen()
      print(f"Книга \"{book_name}\" була повернута\n")
    else:
      clear_screen()
      print(f"Книга \"{book_name}\" не знайдена")
    continue
import os

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

reader = {
    'name': 'Vasia',
    "surname": 'Poplik',
    'group': 'ІПЗс-23-2',
    'course': 1,
    'borrow': [],
    'statistic': []
}

books = [
    "Тигролови",
    "Кобзар",
    "Маруся Чурай",
    "Жовтий князь",
    "Кайдашева сім'я",
    "Дніпро в огні",
    "Пан Коцький",
    "Сто тисяч і мертвець",
    "Чорна рада",
    "Захар Беркут",
    "Андрій",
    "Тіні забутих предків",
    "Сад Гетсиманський",
    "Доля",
    "Метелики",
]

while True:
  print(f"Поточний читач: {reader['name']} {reader['surname']}\n")
  print(f"Група: {reader['group']}  Курс: {reader['course']}\n")
  print("Книги в бібліотеці:\n")
  print(', '.join(books))
  print()
  if (len(reader['borrow']) == 0):
    print("Заборгованих книг немає")
  else:
    print(f"\nЗаборговані книги: {', '.join(reader['borrow'])}")

  print()

  if (len(reader['statistic']) == 0):
    print("Прочитаних книг немає")
  else:
    print(f"\nПрочитані книги: {', '.join(reader['statistic'])}")

  user_input = input(
      "\nКоманди:\n0 - вхід/повернутися в головне меню\n1 - вивевсти карту читача\n2 - позичити книгу\n3 - віддати книгу\n\nВести: "
  )

  if user_input.strip() == "0":
    print("Вхід")
    break

  if user_input.strip() == "1":
    clear_screen()
    print("Ви вибрали: Вивести карту читача\n")
    print("\n-----------------------------------\n")
    print("КАРТА ЧИТАЧА\n\n")
    print(f"{reader['name']} {reader['surname']}\n")
    print(f"Група: {reader['group']}  Курс: {reader['course']}\n")
    print("\n-----------------------------------\n")
    continue

  if user_input.strip() == "2":
    clear_screen()
    print("Ви вибрали: Позичити книгу\n")
    print("Щоб позичити книгу введіть одну з наведених нижче назв: \n")
    for book in books:
      print(book)
    book_name = input("\nВведіть назву книги: ")

    if book_name.strip() == "0":
      clear_screen()
      continue

    if book_name in books:
      reader['borrow'].append(book_name)
      clear_screen()
      print(f"Книга \"{book_name}\" була додана до позичок\n")
    else:
      clear_screen()
      print(f"Книга \"{book_name}\" не знайдена\n")
    continue

  if user_input.strip() == "3":
    clear_screen()
    print("Ви вибрали: Віддати книгу\n")
    print("Позичені книги: \n")
    for book in reader['borrow']:
      print(book)

    if (len(reader['borrow']) == 0):
      print("У вас нема книг")
      clear_screen()
      continue

    book_name = input("\nВведіть назву книги: ")
    if book_name in reader['borrow']:
      reader['borrow'].remove(book_name)
      if (book_name in reader['statistic']):
        clear_screen()
        print(f"Книга \"{book_name}\" була повернута\n")
        continue
      reader['statistic'].append(book_name)
      clear_screen()
      print(f"Книга \"{book_name}\" була повернута\n")
    else:
      clear_screen()
      print(f"Книга \"{book_name}\" не знайдена")
    continue
