print("Ваш вірний лицар! Приєднуйтесь до мене, і разом ми розведемо жахливі таємниці Королівства Арконія.")
print("Наші першовідкривачі повідомляють, що бачили містичне озеро. Ви розумієте, що ваш король чекає на ваше повернення.")
print("\nПролог")
print("Ваш вірний лицар, Родріго, допомагає вам одягнутись для вашої нелегкої місії.")
print("\"Уявіть, ваша милість! Ось королівський меч та броню. Не соромтеся їх використовувати.\" - сказав Родріго, голосно розрядивши свої потужні м'язи.")
print("\"Ти мій найкращий друг, Родріго. І якщо ми маємо наважитися, нехай це буде разом.\" -відповів ви, відчуваючи хвилю відваги.")
print("Так ваша пригода в королівстві Арконія почалася.")
print("\nВ пустелі")
print("Ви нарешті дісталися краю містичного озера, але замість захоплюючої подорожі ви потрапляєте в непривабливу пустелю.")
print("Ви бачите дві можливості:")
print("1. Перейти через гори та знайти приховане озеро.")
print("2. Піти в пустелю, щоб знайти рятівну воду.")
def start_game():
    choice = input("Введіть номер вашого вибору: ")
    if choice == "1":
        mountain_path()
        da()
        zad()
        vad()
        vaddd()
    elif choice == "2":
        desert_path()

    else:
        print("Неправильне введення, спробуйте знову.")
        start_game()
def mountain_path():
    print("\nВи вирішили вирушити через гори.")
    print("Після довгої подорожі, ви знаходите одинокий будинок. Родріго розповідав, що в цьому будинку живе наймудріший чернець")
    print("1. Постукати до будинку.")
    print("2. Піти далі.")
    

def desert_path():
    print("\nВи вирішили відправитися в пустелю.")
    print("Після довгої та страшної подорожі, ви нарешті знаходите воду, і завдяки вашому героїзму, ви рятуєте свій королівський двір.")
    print("Кінець історії.")
1
def da():
    choice = input("Введіть номер вашого вибору: ")
    if choice == "1":
        sat()
    elif choice == "2":
        sad()
    else:
        print("Неправильне введення, спробуйте знову.")
        da()
def sat():
    print("\nВи вирішили постукати у двері.")
    print("д-з-зз-з * заскрипіли двері")
    print("Вітаю Господа, я знаю навіщо ви тут. Я можу вам допомогти, але й ви не повинні залишитися в боргу (натякнув дід). Мені нудно 2 золоті монети і шлях до озера буде ваш ")
    print("1. Погодитись")
    print("2. Відмовитись")
def sad():
    print("Хмм... На вашому місці, Я не був би так впевнений. Успіхів! (Злісно зачиняє двері) ")
    print("\nРодріго, я втомився. Я не можу більше йти (сказав наш герой). Родріго розумів, що дорого довжина має бути ще, але намагався максимально допомогти нашому товаришу")
    print("Через довгий час... Наші гером були максимально виснажені, але ДРУГ... ")
    print("Відкривається вид на озеро, чи це міраж?! Вони швидко почали рух до цього пейзажу, але звідки не візьмись з'являється поселення найближчого села і вони явно не раді нас бачити. ")
    print("1. Підійти до них")
    print("2. Втекти")
def zad():
    choice = input("Введіть номер вашого вибору: ")
    if choice == "1":
        dsz()
    elif choice == "2":
        zasd()
    else:
        print("Неправильне введення, спробуйте знову.")
        zad()
def dsz():
    print("Вітаю панове (сказав наш герой)!")
    print("Вітаю, як ви тут опинилися? Ми давно вже не зустрічали тут живих істот. Вам допомога потрібна? (сказав ватажок)")
    print("Ми шукаємо озеро. Ви можете нам допомогти?")
    print("Ми туди і прямуємо, ми готові взяти вас із собою")
    print("1. довіриться")
    print("2. Втекти")
def zasd():
    print("Фух! Ми тікали. Ми вже наближаємось , я це відчуваю сказав Родріго ")
def vad():
    choice = input("Введіть номер вашого вибору: ")
    if choice == "1":
        dszz()
    elif choice == "2":
        zasdd()
    else:
        print("Неправильне введення, спробуйте знову.")
        vad()
def dszz():
    print("Після однієї години важкої дороги Родріго не може йти з нами")
    print("Нам потрібно ухвалити важке рішення (сказав Родріго). Ти маєш піти сам")
    print("1. Дійти одному")
    print("2. Залишитися з ним")
def zasdd():
    print("Це важке рішення, але ми це зробили. Ми виконали це завдання!")
def vaddd():
    choice = input("Кінець історії: ")
    if choice == "Кінець історії":
        dszzs()
        zasddd() 
def dszzs():
    print("Кінець історії")
def zasddd():
    print("Кінець історії")
start_game()