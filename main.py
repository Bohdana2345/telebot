# -*- coding: utf-8 -*-
import psycopg2
import telebot
from telebot import types
import random
from datetime import datetime
import aiohttp
import asyncio
import os

def connect_to_db():
   DATABASE_URL = os.getenv("DATABASE_URL")

   if not DATABASE_URL:
        raise ValueError("DATABASE_URL is not set")

   conn = psycopg2.connect(DATABASE_URL, sslmode="require") 
   return conn

mental1_health1_bot = telebot.TeleBot('6773157797:AAHk_A9WfRrpnHUyl2Ug0oZf-4mX5ByAQiU')


SOUNDS_API = {
    "rain": "https://mynoise.net/NoiseMachines/rainNoiseGenerator.php",
    "ocean": "https://mynoise.net/NoiseMachines/oceanNoiseGenerator.php",
    "forest": "https://mynoise.net/NoiseMachines/forestNoiseGenerator.php"
}

@mental1_health1_bot.message_handler(func=lambda message: message.text in ["Get nature sounds for relaxation", "Отримати фоновий звук для релаксації"])
def send_random_sound(message):
    # Вибір випадкового звуку зі списку
    random_sound = random.choice(list(SOUNDS_API.keys()))
    sound_url = SOUNDS_API[random_sound]
    
    mental1_health1_bot.send_message(
        message.chat.id, 
        f"🔊: ({sound_url})", 
        parse_mode="Markdown"
    )


translations = {
    "en": {
        "welcome_text": "Hey, {0.first_name}! I am a bot, created to help you with your mental health when needed. Please, select an option.",
        "menu_buttons": ["Get an inspirational quote", "Get psychological support", "Mood tracker", "Go to the website to communicate with a psychologist", "Get a good habit to work on today", "Change the language", "Get nature sounds for relaxation"],
        "website_prompt": "Click the button below to open the website:",
        "back_to_menu": "Back to Main Menu",
        "choose_emotion": "Choose emotion, please:",
        "register_prompt": "Please register to continue by setting a password:",
         "login_prompt": "Please log in by entering your password:",
           "login_success": "Login successful!",
        "register_success": "Registration successful!",
          "wrong_password_with_recovery": "Incorrect password. If you forgot your password, reply 'Yes' to recover it.",
        "wrong_password": "Incorrect password. Please try again.",
        "recovery_prompt": "Would you like to recover your password? Reply 'Yes' to proceed.",
        "recovery_success": "Your password has been reset. Your new temporary password is: {new_password}",
        "user_not_found": "User not found. Please register.",

    },
    "uk": {
        "welcome_text": "Привіт, {0.first_name}! Я бот, створений, щоб допомогти покращити ментальне здоров'я! Будь ласка, оберіть опцію.",
        "menu_buttons": ["Отримати надихаючу цитату", "Отримати психологічну підтримку", "Трекер настрою", "Перейти на сайт для спілкування з психологом", "Отримати корисну звичку, над якою варто попрацювати сьогодні", "Змінити мову", "Отримати фоновий звук для релаксації"],
        "website_prompt": "Натисніть кнопку нижче, щоб відкрити сайт:",
        "back_to_menu": "Повернутися до головного меню",
        "choose_emotion": "Оберіть емоцію, будь ласка:",
          "register_prompt": "Будь ласка, зареєструйтесь, встановивши пароль:",
        "already_registered": "Ви вже зареєстровані!",
        "login_prompt": "Будь ласка, увійдіть, ввівши свій пароль:",
         "login_success": "Вхід успішний!",
        "register_success": "Реєстрація успішна!",
        "wrong_password": "Неправильний пароль. Спробуйте ще раз.",
          "wrong_password_with_recovery": "Неправильний пароль. Якщо ви забули пароль, відповідайте 'Так', щоб відновити його.",
        "recovery_prompt": "Ви хочете відновити свій пароль? Відповідайте 'Так', щоб продовжити.",
        "recovery_success": "Ваш пароль скинуто. Ваш новий тимчасовий пароль: {new_password}",
        "user_not_found": "Користувача не знайдено. Будь ласка, зареєструйтеся."
        # Інші переклади...
    }
}

inspirational_quotes = [
    {
        "en": "The only way to do great work is to love what you do. - Steve Jobs",
        "uk": "Єдиний спосіб робити визначне — любити те, що ви робите. - Стів Джобс"
    },
    {
        "en": "Believe you can and you're halfway there. - Theodore Roosevelt",
        "uk": "Вірте, що можете, і ви вже на півдорозі. - Теодор Рузвельт"
    },
    {
        "en": "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "uk": "Майбутнє належить тим, хто вірить у красу своїх мрій. - Елеонора Рузвельт"
    },
    {
        "en": "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "uk": "Успіх — не остаточний, невдача — не фатальна: важлива мужність продовжувати. - Вінстон Черчилль"
    },
    {
        "en": "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "uk": "Ваш час обмежений, не витрачайте його проживаючи не своє життя. - Стів Джобс"
    },
    {
        "en": "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "uk": "Єдине обмеження нашого завтрашнього успіху — це наші сумніви сьогодні. - Франклін Д. Рузвельт"
    },
    {
        "en": "The journey of a thousand miles begins with one step. - Lao Tzu",
        "uk": "Подорож у тисячу миль починається з одного кроку. - Лао Цзи"
    },
    {
        "en": "In the middle of difficulty lies opportunity. - Albert Einstein",
        "uk": "Посеред труднощів лежить можливість. - Альберт Ейнштейн"
    },
    {
        "en": "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "uk": "Єдина людина, якою вам суджено стати, — це людина, якою ви вирішите бути. - Ральф Волдо Емерсон"
    },
    {
        "en": "Hard work beats talent when talent doesn't work hard. - Tim Notke",
        "uk": "Наполеглива праця перемагає талант, якщо талант не працює наполегливо. - Тім Нотке"
    },
    {
        "en": "The only way to achieve the impossible is to believe it is possible. - Charles Kingsleigh",
        "uk": "Єдиний спосіб досягти неможливого — повірити, що це можливо. - Чарльз Кінгслі"
    },
     {
        "en": "Success is stumbling from failure to failure with no loss of enthusiasm. - Winston Churchill",
        "uk": "Успіх — це cпотикатися від невдачі до невдачі без втрати ентузіазму. - Вінстон Черчилль"
    },
    {
        "en": "The most powerful relationship you will ever have is the relationship with yourself. - Steve Maraboli",
        "uk": "Найважливіші відносини, які у вас коли-небудь будуть, — це відносини з самим собою. - Стів Мараболі"
    },
    {
        "en": "Kindness is a language that the deaf can hear and the blind can see. - Mark Twain",
        "uk": "Доброта — це мова, яку чують глухі й бачать сліпі. - Марк Твен"
    },
    {
        "en": "To love oneself is the beginning of a lifelong romance. - Oscar Wilde",
        "uk": "Любити себе — це початок роману на все життя. - Оскар Уайльд"
    },
    {
        "en": "You yourself, as much as anybody in the entire universe, deserve your love and affection. - Buddha",
        "uk": "Ви самі, як і будь-хто у Всесвіті, заслуговуєте на свою любов і прихильність. - Будда"
    },
    {
        "en": "Kindness in words creates confidence. Kindness in thinking creates profoundness. Kindness in giving creates love. - Lao Tzu",
        "uk": "Доброта в словах створює впевненість. Доброта в думках створює глибину. Доброта у віддачі створює любов. - Лао Цзи"
    },
    {
        "en": "Love yourself first, and everything else falls into line. - Lucille Ball",
        "uk": "Спершу полюбіть себе, і все інше стане на свої місця. - Люсіль Болл"
    },
    {
        "en": "Your task is not to seek for love, but merely to seek and find all the barriers within yourself that you have built against it. - Rumi",
        "uk": "Ваше завдання — не шукати любов, а шукати й знаходити всі бар'єри в собі, які ви збудувал, щоб відгородитися від неї. - Румі"
    },
    {
        "en": "Remember always that you not only have the right to be an individual, you have an obligation to be one. - Eleanor Roosevelt",
        "uk": "Пам’ятайте завжди, що ви не лише маєте право бути особистістю, але й зобов’язані нею бути. - Елеонора Рузвельт"
    }
]

good_habits = [
    {
        "en": "Express gratitude for three good things in your life every morning",
        "uk": "Щоранку висловлюйте вдячність за три хороші речі, які є у вашому житті"
    },
    {
        "en": "Eat a balanced and nutritious meal",
        "uk": "Їжте збалансовану та поживну їжу"
    },
    {
        "en": "Avoid screens at least 30 minutes before bedtime",
        "uk": "Уникайте гаджетів щонайменше за 30 хвилин до сну"
    },
    {
        "en": "Read one chapter from a self-improvement book every day",
        "uk": "Читайте один розділ книги щодня"
    },
    {
        "en": "Get at least 7-8 hours of sleep every night",
        "uk": "Спіть щонайменше 7-8 годин щоночі"
    },
    {
        "en": "Go to sleep before midnight and wake up before 8 a.m. every day",
        "uk": "Лягайте спати до півночі та прокидайтеся до 8 ранку щодня"
    },
    {
        "en": "Learn to say 'no'",
        "uk": "Навчіться говорити 'ні'"
    },
    {
        "en": "Engage in at least 15 minutes of physical exercise every day",
        "uk": "Займайтеся фізичними вправами щонайменше 15 хвилин щодня"
    },
    {
        "en": "Set aside at least 15 minutes per day for your hobby or creative activity",
        "uk": "Виділяйте щонайменше 15 хвилин на день для вашого хобі чи творчої діяльності"
    },
    {
        "en": "Maintain a clean and organized living space",
        "uk": "Підтримуйте чистоту та порядок навколо себе"
    },
    {
        "en": "Stay hydrated by drinking at least 1.5L of water throughout the day",
        "uk": "Підтримуйте водний баланс, випиваючи щонайменше 1,5 літри води на день"
    },
    {
        "en": "Cultivate a positive mindset by focusing on solutions",
        "uk": "Розвивайте позитивне мислення, зосереджуючись на рішеннях, а не проблемах"
    },
    {
        "en": "Limit time spent on social media to promote a healthy mind",
        "uk": "Обмежте використання соціальних мереж"
    },
    {
        "en": "Learn not to compare yourself with other people",
        "uk": "Навчіться не порівнювати себе з іншими людьми"
    },
    {
        "en": "Spend at least 2 hours walking in the fresh air every day",
        "uk": "Проводьте щонайменше 2 години на день, гуляючи на свіжому повітрі"
    },
    {
        "en": "Take a daily multivitamin supplement",
        "uk": "Щодня приймайте вітаміни"
    },
    {
        "en": "Learn not to procrastinate, tackle tasks and challenges promptly",
        "uk": "Навчіться не відкладати справи, вирішуйте завдання оперативно"
    },
    {
        "en": "Give at least three compliments to others every day",
        "uk": "Робіть щонайменше три компліменти іншим щодня"
    },
    {
        "en": "Make your bed every morning",
        "uk": "Застеляйте ліжко щоранку"
    },
    {
        "en": "Learn to eat without your phone",
        "uk": "Навчіться їсти без телефону"
    }
]

user_languages = {}

@mental1_health1_bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lang_btn1 = types.KeyboardButton("English")
    lang_btn2 = types.KeyboardButton("Українська")
    markup.add(lang_btn1, lang_btn2)
    mental1_health1_bot.send_message(
        message.chat.id,
        "Please choose your language / Будь ласка, оберіть мову:",
        reply_markup=markup
    )

@mental1_health1_bot.message_handler(func=lambda message: message.text in ["English", "Українська"])
def set_language(message):
    language = "en" if message.text == "English" else "uk"
    user_languages[message.chat.id] = language

    if is_user_registered(message.chat.id):
        ask_for_login(message)
    else:
        ask_for_registration(message)

def is_user_registered(telegram_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE telegram_id = %s", (telegram_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return bool(user)

def ask_for_registration(message):
    lang = user_languages.get(message.chat.id, "en")
    register_prompt = translations[lang]["register_prompt"]
    msg = mental1_health1_bot.send_message(message.chat.id, register_prompt)
    mental1_health1_bot.register_next_step_handler(msg, process_registration)

def process_registration(message):
    telegram_id = message.chat.id
    password = message.text
    hashed_password = generate_password_hash(password)

    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (telegram_id, password)
        VALUES (%s, %s)
    """, (telegram_id, hashed_password))
    conn.commit()
    cursor.close()
    conn.close()

    lang = user_languages.get(message.chat.id, "en")
    success_text = translations[lang]["register_success"]
    mental1_health1_bot.send_message(telegram_id, success_text)
    send_main_menu(message)


def ask_for_login(message):
    lang = user_languages.get(message.chat.id, "en")
    login_prompt = translations[lang]["login_prompt"]
    msg = mental1_health1_bot.send_message(message.chat.id, login_prompt)
    mental1_health1_bot.register_next_step_handler(msg, process_login)


def process_login(message):
    telegram_id = message.chat.id
    input_password = message.text

    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE telegram_id = %s", (telegram_id,))
    result = cursor.fetchone()

    if result:
        stored_password = result[0]
        if check_password_hash(stored_password, input_password):
            lang = user_languages.get(message.chat.id, "en")
            success_text = translations[lang]["login_success"]
            mental1_health1_bot.send_message(telegram_id, success_text)
            send_main_menu(message)
        else:
            lang = user_languages.get(message.chat.id, "en")
            wrong_password_text = translations[lang]["wrong_password"]
            mental1_health1_bot.send_message(telegram_id, wrong_password_text)
            ask_for_login(message)
    else:
        lang = user_languages.get(message.chat.id, "en")
        mental1_health1_bot.send_message(telegram_id, "User not found. Please register.")
        ask_for_registration(message)

    cursor.close()
    conn.close()

def send_main_menu(message):
    lang = user_languages.get(message.chat.id, "en")
    text = translations[lang]["welcome_text"].format(message.from_user)
    buttons = translations[lang]["menu_buttons"]

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for btn_text in buttons:
        markup.add(types.KeyboardButton(btn_text))

    mental1_health1_bot.send_message(message.chat.id, text, reply_markup=markup)

    photo_path = "greeting.png"
    with open(photo_path, "rb") as photo:
        mental1_health1_bot.send_photo(message.chat.id, photo)

@mental1_health1_bot.message_handler(func=lambda message: message.text in ["Change the language", "Змінити мову"])
def change_language(message):
    start(message)


@mental1_health1_bot.message_handler(func=lambda message: message.text in ["Go to the website to communicate with a psychologist", "Перейти на сайт для спілкування з психологом"])
def open_website(message):
    # Вибір мови повідомлення
    if message.text == "Go to the website to communicate with a psychologist":
        prompt = "Click the button below to open the website:"
        button_text = "Open the website"  
    elif message.text == "Перейти на сайт для спілкування з психологом":
        prompt = "Натисніть на кнопку нижче, щоб перейти на сайт:"
        button_text = "Відкрити сайт" 
    else:
        prompt = "Click the button below to open the website:" 
        button_text = "Open the website"  

    url_button = types.InlineKeyboardButton(button_text, url='https://www.betterhelp.com/')
    keyboard = types.InlineKeyboardMarkup().add(url_button)

    mental1_health1_bot.send_message(message.chat.id, prompt, reply_markup=keyboard)


    

@mental1_health1_bot.message_handler(func=lambda message: message.text in ["Get an inspirational quote", "Отримати надихаючу цитату"])
def send_inspirational_quote(message):
    
    if message.text == "Get an inspirational quote":
        language = "en"
    elif message.text == "Отримати надихаючу цитату":
        language = "uk"
    
    random_quote = random.choice(inspirational_quotes)
    quote_to_send = random_quote[language] 
    

    mental1_health1_bot.send_message(message.chat.id, quote_to_send)

@mental1_health1_bot.message_handler(func=lambda message: message.text in ["Get psychological support", "Отримати психологічну підтримку"])
def psychological_support(message):
    
    if message.text == "Get psychological support":
        caption = "What are you feeling right now?"
        prompt = "Choose emotion, please:"
        buttons = [
            "Anger", "Envy", "Loneliness", "Laziness", 
            "Social anxiety", "Eating disorder phase", 
            "Offense", "Insecurity and self-hatred", "Back to Main Menu"
        ]
    elif message.text == "Отримати психологічну підтримку":
        caption = "Що ви зараз відчуваєте?"
        prompt = "Виберіть емоцію, будь ласка:"
        buttons = [
            "Гнів", "Заздрість", "Самотність", "Лінь", 
            "Соціальна тривожність", "Фаза розладу харчової поведінки", 
            "Образа", "Невпевненість", "Повернутися до головного меню"
        ]
    else:
        caption = "What are you feeling right now?" 
        prompt = "Choose emotion, please:" 
        buttons = [
            "Anger", "Envy", "Loneliness", "Laziness", 
            "Social anxiety", "Eating disorder phase", 
            "Offense", "Insecurity and self-hatred", "Back to Main Menu"
        ]


    with open("emot.png", "rb") as photo:
        mental1_health1_bot.send_photo(message.chat.id, photo, caption=caption)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for button_text in buttons:
        keyboard.add(types.KeyboardButton(button_text))


    mental1_health1_bot.send_message(message.chat.id, prompt, reply_markup=keyboard)

from werkzeug.security import generate_password_hash

@mental1_health1_bot.message_handler(func=lambda message: message.text in ["Register"])
def register_user(message):
    telegram_id = message.chat.id
    username = message.chat.username or "Unknown"
    first_name = message.chat.first_name or "Unknown"
    last_name = message.chat.last_name or "Unknown"


    msg = mental1_health1_bot.send_message(telegram_id, "Введіть пароль для реєстрації:")
    mental1_health1_bot.register_next_step_handler(msg, process_password, telegram_id, username, first_name, last_name)

def process_password(message, telegram_id, username, first_name, last_name):
    password = message.text

    hashed_password = generate_password_hash(password)

    conn = connect_to_db()
    cursor = conn.cursor()


    cursor.execute("SELECT id FROM users WHERE telegram_id = %s", (telegram_id,))
    user = cursor.fetchone()

    if user:
        mental1_health1_bot.send_message(telegram_id, "Ви вже зареєстровані!")
    else:
        cursor.execute("""
            INSERT INTO users (telegram_id, username, first_name, last_name, password)
            VALUES (%s, %s, %s, %s, %s)
        """, (telegram_id, username, first_name, last_name, hashed_password))
        conn.commit()
        mental1_health1_bot.send_message(telegram_id, "Реєстрація успішна!")

    cursor.close()
    conn.close()


from werkzeug.security import check_password_hash

@mental1_health1_bot.message_handler(func=lambda message: message.text in ["Login"])
def login_user(message):
    telegram_id = message.chat.id
    msg = mental1_health1_bot.send_message(telegram_id, "Введіть ваш пароль:")
    mental1_health1_bot.register_next_step_handler(msg, process_login_password, telegram_id)

def process_login_password(message, telegram_id):
    input_password = message.text

    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE telegram_id = %s", (telegram_id,))
    result = cursor.fetchone()

    if result:
        stored_password = result[0]
        if check_password_hash(stored_password, input_password):
            mental1_health1_bot.send_message(telegram_id, "Логін успішний!")
        else:
            mental1_health1_bot.send_message(telegram_id, "Невірний пароль!")
    else:
        mental1_health1_bot.send_message(telegram_id, "Користувача не знайдено! Спочатку зареєструйтесь.")

    cursor.close()
    conn.close()


@mental1_health1_bot.message_handler(func=lambda message: message.text in ["Anger", "Гнів"])
def handle_anger(message):
   
    if message.text == "Anger":
        anger_response = """Don't react harshly, remember that decisions made under the influence of anger will lead to regret later. Emotions prevent you from seeing the situation clearly, give yourself time to calm down and analyze it objectively. If you let someone or something make you angry, you acknowledge their power over you and let them control your mind, you choose to believe them and take their opinions personally. Don't spend energy on negative situations, embrace the fact that it is normal for people to make mistakes and not everyone will share your values. Forgive, breathe deeply, release your emotions by journaling, physical activity or whatever makes you feel better and focus on finding solutions.Be honest with yourself about what you fell, don't deny negative emotions, they are the indicators that help you to understand yourself better, but learn to develop emotional intelligence and control your reactions."""
    elif message.text == "Гнів":
        anger_response = """Не реагуйте різко, пам'ятайте, що рішення, прийняті під впливом гніву, змусять вас пошкодувати пізніше. Емоції заважають вам ясно бачити ситуацію, дайте собі час заспокоїтися і проаналізувати її об'єктивно. Якщо ви дозволяєте комусь чи чомусь розлютити вас, ви визнаєте їхню владу над собою і дозволяєте їм контролювати ваш стан, ви обираєте вірити їм і брати їхню поведінку на свій рахунок. Не витрачайте енергію на негативні ситуації, прийміть той факт, що людям властиво допускатися помилок і не всі будуть розділяти ваші цінності. Глибоко дихайте, дайте волю своїм емоціям через ведення щоденника, фізичну активність або будь-що, що допомагає вам почуватися краще, і зосередьтеся на пошуку рішення. Будьте чесні з собою щодо того, що ви відчуваєте, не відкидайте негативні емоції, вони є індикаторами, які допомагають вам краще зрозуміти себе, але навчіться розвивати емоційний інтелект і контролювати свої реакції."""
    else:
        anger_response = """Don't react harshly, remember that decisions made under the influence of anger will lead to regret later. Emotions prevent you from seeing the situation clearly, give yourself time to calm down and analyze it objectively. If you let someone or something make you angry, you acknowledge their power over you and let them control your mind, you choose to believe them and take their opinions personally. Don't spend energy on negative situations, embrace the fact that it is normal for people to make mistakes and not everyone will share your values. Forgive, breathe deeply, release your emotions by journaling, physical activity or whatever makes you feel better and focus on finding solutions.Be honest with yourself about what you fell, don't deny negative emotions, they are the indicators that help you to understand yourself better, but learn to develop emotional intelligence and control your reactions."""

    mental1_health1_bot.send_message(message.chat.id, anger_response)

@mental1_health1_bot.message_handler(func=lambda message: message.text in ["Envy", "Заздрість"])
def handle_envy(message):

    if message.text == "Envy":
        envy_response = """Envy is the indicator of what you desire the most in life. If you see someone possessing something and feel envy that's obviously what you would like to possess either and it is totally okay. There are two ways to ease this feeling - to put someone else down and wish them to fail or to level up yourself. Obviously, second variant is what we choose, it will positively influence your life and help you make real changes.  Convert your envy to feeling inspired by other person, learn from them,realize that if they've managed to get it, it is possible for you either, so work on it and see envy as guidance in some situations. Our universe is huge and everyone has their own space to success, what was meant for you will be yours. Also it is important to realize that every person is unique, so someone could get what you want easier or faster, but that doesn't mean you can't have it either - you can and you will in your unique way and perfect timing. Don't compare yourself with other people, only with the person you were yesterday and be grateful for your own blessings."""
    elif message.text == "Заздрість":
        envy_response = """Заздрість — це індикатор того, що ви найбільше бажаєте в житті. Якщо ви бачите, що хтось володіє чимось, і відчуваєте заздрість, це очевидно те, чого ви хочете досягти, і це абсолютно нормально. Існує два способи полегшити це відчуття — принижувати когось і бажати, щоб вони зазнали невдачі або вдосконалити себе. Очевидно, ми вибираємо другий варіант, це позитивно вплине на ваше життя і допоможе зробити реальні зміни. Перетворіть свою заздрість на натхнення, навчайтеся в інших людей, усвідомте, що якщо їм вдалося це досягти, значить, це можливо і для вас, тому працюйте над цим і сприймайте заздрість як орієнтир у деяких ситуаціях. Наш всесвіт величезний, і у кожного є своє місце для успіху, те, що призначено для вас, буде вашим. Також важливо усвідомити, що кожна людина унікальна, тому хтось може отримати те, що ви хочете, легше чи швидше, але це не означає, що ви не можете цього досягти — ви можете і досягнете цього у свій унікальний спосіб та в ідеальний час. Не порівнюйте себе з іншими людьми, порівнюйте себе тільки з тим, ким ви були вчора, і будьте вдячні за блага, які є у вашому житті."""
    else:
        envy_response = """Envy is the indicator of what you desire the most in life. If you see someone possessing something and feel envy that's obviously what you would like to possess either and it is totally okay. There are two ways to ease this feeling - to put someone else down and wish them to fail or to level up yourself. Obviously, second variant is what we choose, it will positively influence your life and help you make real changes.  Convert your envy to feeling inspired by other person, learn from them,realize that if they've managed to get it, it is possible for you either, so work on it and see envy as guidance in some situations. Our universe is huge and everyone has their own space to success, what was meant for you will be yours. Also it is important to realize that every person is unique, so someone could get what you want easier or faster, but that doesn't mean you can't have it either - you can and you will in your unique way and perfect timing. Don't compare yourself with other people, only with the person you were yesterday and be grateful for your own blessings."""

    mental1_health1_bot.send_message(message.chat.id, envy_response)

   
@mental1_health1_bot.message_handler(func=lambda message: message.text in ["Loneliness", "Самотність"])
def handle_loneliness(message):
    
    if message.text == "Loneliness":
        loneliness_response = """Dealing with loneliness can be challenging, but there are several strategies and activities that may help alleviate feelings of isolation. Sometimes we find ourselves in situations were for whatever reason we lost connections with other people - maybe we choose different pathes, maybe we lost interest, maybe we had a serious fight. Your task now is to realize that in order to change your situation you need to take action. First, analyze your social needs, what you can give to other people and what you want to have in exchange. Try to connect with your loved ones, take the initiative and ask them out more, explain your needs and feelings. If you want to have a new social circle, don't be a homebody, open your mind to new acquaintance. Attend social events, participate in various clubs and classes that align with your interests. You can start just with walkings in the nearest park - the most important thing is to be around other people. Be nice and sociable and you will definitely feel better. If you have some problems that prevent you from being outgoing - like fear of rejection or insecurity, work on it first. Don't overcare about failed social experiences, don't overthink about what other people will think about you, don't fill your mind with negative expectations,  just enjoy the moment and be yourself. It is better to try and fail than not to try at all and regret, don't forget that other people have similar fears, insecurities and needs, so be active and take initiative. Also work on your personality - take care of your appearence and mind, know who you are and it will help you to feel more confident while interacting with other peole. Consider getting a pet if your living situation allows. Pets can provide companionship and a sense of purpose. Also don't use other people to fill the gap inside your soul, remeber that you should cover your basic needs(like need of love, safety, validation etc) yourself to prevent depending on others. Be okay with spending time on your own company and build strong relationship with yourself, then your relationship with other people will follow."""
    elif message.text == "Самотність":
        loneliness_response = """Боротися з відчуттям самотності непросто, але існує кілька стратегій, які можуть допомогти зменшити відчуття ізольованості. Іноді ми опиняємося в ситуаціях, коли з різних причин втрачаємо почуття зв'язку з іншими людьми — можливо, ми вибрали різні шляхи, можливо, втратили інтерес одне до одного, можливо, серйозно посварилися. Ваше завдання зараз — зрозуміти, що для зміни ситуації потрібно діяти. По-перше, проаналізуйте свої соціальні потреби, що ви можете дати іншим людям і що хочете отримати взамін. Спробуйте налагодити зв'язки з близькими, проявіть ініціативу, запрошуйте їх проводити час разом частіше, поясніть свої потреби та почуття. Якщо ви хочете мати нове коло спілкування, не будьте домосідом, налаштуйтеся на нові знайомства. Ходіть на соціальні заходи, відвідуйте гуртки, які відповідають вашим інтересам. Почати можна просто з прогулянок у найближчому парку — найголовніше, бути серед інших людей. Будьте доброзичливими та товариськими, і ви точно відчуєте себе краще. Якщо у вас є проблеми, які заважають бути відкритими, такі як страх відмови чи невпевненість, спершу попрацюйте над ними. Не переживайте через невдалі досвіди соціальної взаємодії, не надто зосереджуйтеся на тому, що подумають інші, не наповнюйте свій розум негативними очікуваннями, просто насолоджуйтесь моментом і будьте собою. Краще спробувати і зазнати невдачі, ніж навіть не спробувати і шкодувати про це — не забувайте, що інші люди мають подібні страхи, невпевненість і потреби, тому будьте активними і проявляйте ініціативу. Також працюйте над своєю особистістю — піклуйтесь про свою зовнішність і свідомість, знайте, хто ви, і це допоможе вам бути більш впевненим при взаємодії з іншими людьми. Розгляньте рішення завести домашнього улюбленця, якщо ваші умови дозволяють. Також не використовуйте інших людей, щоб заповнити порожнечу всередині, пам'ятайте, що ви повинні задовольняти свої основні потреби (такі як потреба в любові, безпеці, визнанні тощо) самостійно, щоб не залежати від інишх. Проводьте певну кількість часу на самоті, будуйте міцні відносини з собою, і тоді ваші відносини з іншими людьми теж налагодяться."""
    else:
        loneliness_response = """Dealing with loneliness can be challenging, but there are several strategies and activities that may help alleviate feelings of isolation. Sometimes we find ourselves in situations were for whatever reason we lost connections with other people - maybe we choose different pathes, maybe we lost interest, maybe we had a serious fight. Your task now is to realize that in order to change your situation you need to take action. First, analyze your social needs, what you can give to other people and what you want to have in exchange. Try to connect with your loved ones, take the initiative and ask them out more, explain your needs and feelings. If you want to have a new social circle, don't be a homebody, open your mind to new acquaintance. Attend social events, participate in various clubs and classes that align with your interests. You can start just with walkings in the nearest park - the most important thing is to be around other people. Be nice and sociable and you will definitely feel better. If you have some problems that prevent you from being outgoing - like fear of rejection or insecurity, work on it first. Don't overcare about failed social experiences, don't overthink about what other people will think about you, don't fill your mind with negative expectations,  just enjoy the moment and be yourself. It is better to try and fail than not to try at all and regret, don't forget that other people have similar fears, insecurities and needs, so be active and take initiative. Also work on your personality - take care of your appearence and mind, know who you are and it will help you to feel more confident while interacting with other peole. Consider getting a pet if your living situation allows. Pets can provide companionship and a sense of purpose. Also don't use other people to fill the gap inside your soul, remeber that you should cover your basic needs(like need of love, safety, validation etc) yourself to prevent depending on others. Be okay with spending time on your own company and build strong relationship with yourself, then your relationship with other people will follow."""

    mental1_health1_bot.send_message(message.chat.id, loneliness_response)

@mental1_health1_bot.message_handler(func=lambda message: message.text in ["Laziness", "Лінь"])
def handle_laziness(message):
   
    if message.text == "Laziness":
        laziness_response = """Realize that your goals won't be achieved without your actions, realize that everything has consequences - if you choose to be lazy today you will end up being broke tomorrow, being the person that chooses pain of regret over the pain of discipline, person that struggles thinking what they could've had if they chose to use their potential fully and fought their weakness. If you choose what you want now over you want the most - you choose to be a failure. Know the difference between  being lazy and having a burnout though. If you are really tired, take a day off and give yourself a time to rennovate your recourses,always be honest with yourself about it. If you struggle with discipline, cutt off all discractors and give yourself just 10 minutes to be involved in what you should do, to start is always the hardest and the most probable wou will continue after you've done that. Plan your schedule, limit your screen time, develop small habits like making your bed in the morning and engage in sports - it will make your mind more disciplined and help you to overcome laziness easier. Set realistic goals for yourself and give youself rewards for performing well, always start with easier tasks, but do the hardest when you are the most productive, divide great job into smaller parts. Do job with companion - it will increase your responsibility and provide more encouragement.  Remember, that if you are too lazy to take care of yourself and do what will be good for you, you don't love yourself. Love is always an action, so do this action for yourself. Remember that overcoming laziness is a gradual process, and it's okay to face setbacks. Be patient with yourself and consistently apply these strategies to build positive habits and increase productivity over time."""
    elif message.text == "Лінь":
        laziness_response = """Зрозумійте, що ваші цілі не будуть реалізовані без ваших дій, зрозумійте, що все має свої наслідки — якщо ви обираєте бути лінивим сьогодні, то завтра будете розчаровані, будете тією людиною, яка обирає біль жалю про втрачені можливості замість болю дисципліни, людиною, яка страждає, думаючи про те, що вона могла б досягти, якби повністю реалізовувала свій потенціал і боролася зі своїми слабкостями. Якщо ви обираєте секундні імпульси замість того, що вам потрібно в довгостроковій перспективі — ви обираєте бути невдахою. Проте зрозумійте різницю між лінню та вигоранням. Якщо ви справді втомилися, візьміть день відпочинку і дайте собі час для відновлення ресурсів, завжди будьте чесні з собою. Якщо вам важко з дисципліною, позбудьтеся всіх відволіканючих чинників і дайте собі хоча б 10 хвилин, щоб зайнятися тим, що потрібно зробити. Почати завжди найскладніше, але, ймовірно, ви продовжите після того, як це зробите. Плануйте свій графік, обмежте час в гаджетах, розвивайте дрібні звички, як-от застилання ліжка вранці та заняття спортом — це допоможе дисциплінувати ваш розум і полегшить подолання ліні. Встановлюйте реалістичні цілі для себе і винагороджуйте себе за добре виконану роботу, завжди починайте з легших завдань, а найскладніші робіть, коли ви найпродуктивніші, розділяйте великі завдання на менші частини. Виконуйте роботу з партнером — це збільшить ваше почуття відповідальності і дасть додаткову мотивацію. Пам'ятайте, що якщо ви занадто ліниві, щоб подбати про себе і зробити те, що буде корисно для вас, то ви не любите себе. Любов — це завжди дія, тому зробіть цю дію для себе. Пам'ятайте, що подолання ліні — це поступовий процес, і це нормально стикатися з невдачами і пробувати знову. Будьте терплячими до себе і регулярно застосовуйте ці стратегії для формування позитивних звичок та підвищення продуктивності."""
    else:
        laziness_response = """Realize that your goals won't be achieved without your actions, realize that everything has consequences - if you choose to be lazy today you will end up being broke tomorrow, being the person that chooses pain of regret over the pain of discipline, person that struggles thinking what they could've had if they chose to use their potential fully and fought their weakness. If you choose what you want now over you want the most - you choose to be a failure. Know the difference between  being lazy and having a burnout though. If you are really tired, take a day off and give yourself a time to rennovate your recourses,always be honest with yourself about it. If you struggle with discipline, cutt off all discractors and give yourself just 10 minutes to be involved in what you should do, to start is always the hardest and the most probable wou will continue after you've done that. Plan your schedule, limit your screen time, develop small habits like making your bed in the morning and engage in sports - it will make your mind more disciplined and help you to overcome laziness easier. Set realistic goals for yourself and give youself rewards for performing well, always start with easier tasks, but do the hardest when you are the most productive, divide great job into smaller parts. Do job with companion - it will increase your responsibility and provide more encouragement.  Remember, that if you are too lazy to take care of yourself and do what will be good for you, you don't love yourself. Love is always an action, so do this action for yourself. Remember that overcoming laziness is a gradual process, and it's okay to face setbacks. Be patient with yourself and consistently apply these strategies to build positive habits and increase productivity over time."""
    
    mental1_health1_bot.send_message(message.chat.id, laziness_response)
 

@mental1_health1_bot.message_handler(func=lambda message: message.text in ["Social anxiety", "Соціальна тривожність"])
def handle_saxiety(message):
   
    if message.text == "Social anxiety":
        sanxiety_response = """To overcome social anxiety, stop putting other people on pedestal. Fear of embarrassment seems to be something horrible,  failing or seeing disapproval in someone's eyes seems to be the end of our lives, but it is only a silly illusion. Realize that other people are not better than you, we all are unique, have our own strengths and weaknesses, but are equal on the whole. So other people do not hold the power to determine who you are or judge you. This right belongs to you, you should determine your value on your own, build strong self-esteem and peaceful place in your mind. Let yourself to fail and be imperfect, enjoy your life without caring what someone thinks about you or what will hapen if some of  your social experiences won't work out. Every failed social interaction still brings you an useful experience. Remember that everyone has their own lives and problems and other people don't focus on you as much as you think, in most cases they don't care. Still, someone may not like you and it is tottaly fine - you don't like everyone either. Still someome may talk poorly about you - and it is only about them, they obviously don't have anything wiser to say and are unsattisfied because you do what they are afraid even to try. Let them be mean, be proud you are so important for  someone that they are obsessed with you enough to hate you. If your relationship with someone turns out to be a failure - it is okay, this what happens sometimes, make conclusions, move on and stop caring. Realize that there is no reason for social anxiety - nothing fatal can happen to you during social interections, other people are just like you, they have same fears and insecurities. Just enjoy communication, be yourself, be okay either it works out or not - there are no bad endings, it is either a good one or an experience. If someone makes fun of you - realize that it is projection of their own insecuruties, be ready to defend your peace and not let someone's opinion to ruin your self-perception. Be polite, nice and confident, think not about who will like you, think about if you like what you do. Leave your comfort zone, remember, that it is better to try and fail than even not to try and don't waste your energy on unimportant things."""

    elif message.text == "Соціальна тривожність":
        sanxiety_response = """Щоб подолати соціальну тривожність, перестаньте ставити інших людей на п’єдестал. Страх осоромитися здається чимось жахливим, поразка або осуд з боку інших здається кінцем світу, але це лише дурна ілюзія. Зрозумійте, що інші люди не кращі за вас, ми всі унікальні, маємо свої сильні і слабкі сторони, але в цілому ми рівні. Тому інші люди не мають права визначати, хто ви є або судити вас. Це право належить вам, ви повинні визначати свою цінність самостійно, будувати сильну самооцінку та стійкість. Дозвольте собі бути недосконалим, насолоджуйтеся життям, не переживаючи, що інші думають про вас або що станеться, якщо якийсь ваш досвід соціальної взаємодії закінчиться не так, як там хотілося б. Кожен невдалий соціальний контакт все одно приносить корисний досвід. Пам’ятайте, що у кожного є своє життя та свої проблеми, і інші люди не зосереджуються на вас так, як вам здається, у більшості випадків їм все одно. Комусь ви можете не подобатися — і це абсолютно нормально. Хтось може поводитися грубо — і це не ваша відповідальність, а проєкція їхній власних незадоволеностей. Якщо ваші стосунки з кимось не склалися, це нормально, так буває, зробіть висновки, рухайтеся далі і припиніть переживати про це. Зрозумійте, що немає жодної причини для соціальної тривожності — нічого фатального не може трапитися під час соціальних взаємодій, інші люди такі самі, як і ви, у них ті ж страхи та невпевненість. Просто насолоджуйтеся спілкуванням, будьте собою, не переживайте — в цьому аспекті немає поганих результатів, є лише хороші або досвід. Будьте готові захищати себе і не дозволяти чужій думці руйнувати вашу самооцінку. Будьте ввічливими та впевненими, думайте не про те, кому ви сподобалися, а про те, чи подобається вам те, що ви робите. Виходьте зі своєї зони комфорту, пам’ятайте, що краще спробувати і зазнати невдачі, ніж навіть не спробувати. Не витрачайте свою енергію на непотрібні речі."""
    else:
        sanxiety_response = """To overcome social anxiety, stop putting other people on pedestal. Fear of embarrassment seems to be something horrible,  failing or seeing disapproval in someone's eyes seems to be the end of our lives, but it is only a silly illusion. Realize that other people are not better than you, we all are unique, have our own strengths and weaknesses, but are equal on the whole. So other people do not hold the power to determine who you are or judge you. This right belongs to you, you should determine your value on your own, build strong self-esteem and peaceful place in your mind. Let yourself to fail and be imperfect, enjoy your life without caring what someone thinks about you or what will hapen if some of  your social experiences won't work out. Every failed social interaction still brings you an useful experience. Remember that everyone has their own lives and problems and other people don't focus on you as much as you think, in most cases they don't care. Still, someone may not like you and it is tottaly fine - you don't like everyone either. Still someome may talk poorly about you - and it is only about them, they obviously don't have anything wiser to say and are unsattisfied because you do what they are afraid even to try. Let them be mean, be proud you are so important for  someone that they are obsessed with you enough to hate you. If your relationship with someone turns out to be a failure - it is okay, this what happens sometimes, make conclusions, move on and stop caring. Realize that there is no reason for social anxiety - nothing fatal can happen to you during social interections, other people are just like you, they have same fears and insecurities. Just enjoy communication, be yourself, be okay either it works out or not - there are no bad endings, it is either a good one or an experience. If someone makes fun of you - realize that it is projection of their own insecuruties, be ready to defend your peace and not let someone's opinion to ruin your self-perception. Be polite, nice and confident, think not about who will like you, think about if you like what you do. Leave your comfort zone, remember, that it is better to try and fail than even not to try and don't waste your energy on unimportant things."""

    mental1_health1_bot.send_message(message.chat.id, sanxiety_response)

@mental1_health1_bot.message_handler(func=lambda message: message.text == "Eating disorder phase" or message.text == "Фаза розладу харчової поведінки")
def handle_ed(message):
    responses = {
        "Eating disorder phase": """Dealing with an eating disorder is a complex process that takes a lot of stamina. The first thing is to realize that it is not a problem, it is an aftermath. So your task is to find a reason that causes you to overeat or starve yourself - something that disturbs you and to solve it initially. You use food only to distract yourself from your true problem and receive temporary relief. An example of such problem can be anxiety, unhealed trauma, loneliness, boredom, low self-esteem etc. Learn what (or who) triggers your eating disorder and focus on the root of your problem. Then embrace self-love and care, don't try to punish yourself, focus not on your body measurements, but on your health first of all. Be patient, take little steps when you are trying to gain or lose weight, realize that sometimes when you are dealing with a lot of stress, your eating disorder comes back even though you've been successfully overcoming it recently, don't give up and be good to yourself. Don't put your entire focus on your food, people who struggle with eating disorders tend to be obsessed with their meals and think about that 24/7 as well as dramatize everything linked with this topic (like they are convinced that 1 ice-cream will make them very fat etc). Don't prevent yourself from going out, dating, buying that one piece of clothes you want to wear etc because you are not "skinny enough" or on the contrary "too skinny", don't let your eating disorder put your life on hold. Be objective and try to be in your best shape, but in any stage of your life, you should support and love your body. Fill your life with events, people, interesting experiences and hobbies so your mind has other things to care about. Don't put your entire value in your weight, realize that you are not only that, you are also what you think, you are your values, your hobbies etc. Try to find a golden mean - it is cool to be fit, but above everything you should be healthy and create for yourself a healthy lifestyle you will be able to lead. Listen to your body needs, walk in fresh air, eat enough nutrients, stay hydrated, do sports and don't forget to keep balance. Don't set very strict constraints for yourself, don't divide food into bad and good, embrace the 80/20 principle, trying to eat healthy most of the time, but letting yourself eat your favorite sweets or fast food sometimes. Don't starve or overfeed yourself during the day. Develop healthy eating habits, like eating without your phone or chewing slowly, it will help you to deal with your problem. Also, try to find support in your loved ones or talk with a specialist, it can be extremely helpful as well.""",
        
        "Фаза розладу харчової поведінки": """Подолання розладу харчової поведінки - це складний процес, який вимагає великої витривалості. Перше, що треба зрозуміти, це те, що це не проблема, а наслідок. Тому ваше завдання - знайти причину, через яку ви переїдаєте або голодуєте, щось, що вас турбує, і вирішити це спочатку. Ви використовуєте їжу лише для того, щоб відволіктися від справжньої проблеми і отримати тимчасове полегшення. Прикладом такої проблеми може бути тривога, незагоєні дитячі травми, самотність, нудьга, низька самооцінка тощо. Дізнайтеся, що (або хто) тригерить ваш розлад харчової поведінки, і зосередьтесь на корені вашої проблеми. Ставтеся до себе з любов’ю і турботою, не намагайтеся карати себе, зосереджуйтесь не на своїй вазі чи параметрах, а на здоров’ї в першу чергу. Будьте терплячими, робіть маленькі кроки, коли намагаєтеся набрати або скинути вагу, зрозумійте, що інколи, коли ви стикаєтесь із великою кількістю стресу, ваш розлад харчової поведінки може повернутися, навіть якщо нещодавно вам вдалося вийти в ремісію, не здавайтеся і будьте добрі до себе. Не ставте весь свій фокус на їжу, люди, які борються з розладами харчової поведінки, схильні бути одержимими їжею і думати про це 24/7, а також драматизувати все, що з цим пов'язано (наприклад, вони впевнені, що один шматочок торта зробить їх дуже товстими і т.д.). Не забороняйте собі виходити на вулицю, ходити на побачення, купувати гарний одяг, який хочете носити, і т.д., тому що ви  "недостатньо худі" або, навпаки, "занадто худі", не дозволяйте вашому розладу харчової поведінки поставити ваше життя на паузу. Будьте об’єктивними і намагайтеся бути у найкращій формі, але на будь-якому етапі вашого життя ви повинні підтримувати і любити своє тіло. Наповнюйте своє життя подіями, людьми, цікавими враженнями і хобі, щоб ваш розум мав іншу їжу для роздумів. Не зосереджуйте всю свою цінність у тому, скільки ви важите, зрозумійте, що ви - це не тільки ваше тіло, ви також є тим, що ви думаєте, вашими цінностями, вашими інтресами, рисами характеру, вміннями тощо. Спробуйте знайти золоту середину - бути у хорошій формі - це круто, але понад усе ви повинні бути здоровими і створити для себе здоровий спосіб життя, який ви зможете підтримувати. Прислухайтеся до потреб вашого тіла, гуляйте на свіжому повітрі, їжте достатньо поживних речовин, пийте воду, займайтеся спортом і не забувайте зберігати баланс. Не встановлюйте дуже суворих обмежень, не діліть їжу на погану і хорошу, дотримуйтеся принципу 80/20, намагаючись їсти здорову їжу більшість часу, але дозволяючи собі інколи їсти улюблені солодощі або фаст-фуд. Не голодуйте і не переїдайте протягом дня. Розвивайте здорові звички в їжі, такі як їсти без телефону або повільно пережовувати їжу, це допоможе вам впоратися з вашою проблемою. Також спробуйте знайти підтримку у своїх близьких або поговоріть зі спеціалістом, це може бути надзвичайно корисно."""
    }

    mental1_health1_bot.send_message(message.chat.id, responses.get(message.text, "Sorry, I don't have a response for that."))

       

@mental1_health1_bot.message_handler(func=lambda message: message.text == "Offense" or message.text == "Образа")
def handle_offense(message):
    responses = {
        "Offense": """If you feel offense, number one point is to let yourself calm down and don't act out of emotions. Recognize your feelings, trust yourself, let yourself feel what you feel and deal with it rationally. Then talk with a person that has insulted you - be honest, but don't be rude. Realize that all people were brought up in different environments so what is offensive for you can be totally okay for someone else, that's why you should use communication to talk about your needs and feelings. Explain the situation without aggressive accusations and dramas, discuss a way to make you feel okay and solve this problem. If that person really appreciates you, they will take into account your opinion and will act understanding. They will apologize and not do that again. If in response an individual derides you and offers only justification, then think twice before communicating with this person who doesn't care about your feelings. Whether you managed to find a common ground and make peace with this person or decided to end communication, forgive them and move on for your own sake. Sometimes we might be offended by people without having the opportunity to talk with them about it or we find some offense too serious and don't want to deal with our insulter at all anymore, so all that is left anyways is to let it go. Don't waste your energy on negativity, the best revenge is just to focus on your life, work on your healing and level up.""",
        
        "Образа": """Якщо ви відчуваєте образу, перше, що треба зробити - це дати собі час заспокоїтися і не діяти під впливом емоцій. Визнайте свої почуття, дозвольте собі відчувати те, що ви відчуваєте, і порайтеся з цим раціонально. Поговоріть з людиною, яка вас образила - будьте чесними, але не грубими. Зрозумійте, що всі люди виросли в різних середовищах, і те, що є образливим для вас, може бути абсолютно нормальним для іншої людини і вона могла образити вас ненавмисно, тому ви повинні використовувати екологічну комунікацію, щоб говорити про свої потреби і почуття. Поясніть ситуацію без агресивних звинувачень і драм, обговоріть спосіб зробити так, щоб вам було комфортно, і вирішити цю проблему. Якщо ця людина дійсно цінує вас, вона врахує вашу думку і проявить розуміння. Вона вибачиться і візьме до уваги ваші почуття. Якщо вислухавши вас людина не намагається вас зрозуміти, принижує, висміює, виправдовується, подумайте двічі, перш ніж спілкуватися з тим, кого не хвилюють ваші почуття. Незалежно від того, чи вам вдалося знайти спільну мову і помиритися з цією людиною, чи ви вирішили припинити спілкування, вибачте їй і рухайтеся далі заради себе. Іноді ми можемо ображатися на людей, не маючи можливості поговорити з ними про це, або вважаємо образу надто серйозною і не хочемо більше спілкуватися з цією людиною, тому все, що залишається - просто відпустити це. Не витрачайте свою енергію на негатив, найкраще - зосередитися на своєму житті, працювати над своїм зціленням і вдосконалюватися."""
    }
    
    mental1_health1_bot.send_message(message.chat.id, responses.get(message.text, "Sorry, I don't have a response for that."))

@mental1_health1_bot.message_handler(func=lambda message: message.text == "Insecurity and self-hatred" or message.text == "Невпевненість")
def handle_insecurity(message):
    responses = {
        "Insecurity and self-hatred": """Dealing with insecurity and self-hatred is a personal and often ongoing process that involves self-reflection, self-compassion, and personal growth. Analyze the source of your insecurity, maybe you don't like your appearance, maybe you don't like your character, and being in this role model causes your unconfidence. Remember that life is not just about finding yourself, it is about creating yourself, so write down how would the best, the most confident version of you look like, how would they behave, who would be their friends, and any other detail you can see. Work on turning yourself into this person. You should be honest with yourself, and if something makes you feel insecure, you can always work on changing it. Another thing is you should work on replacing self-hatred with unconditional self-love. Be good to yourself, realize that even if you are not the best version of yourself now, you need your care, love, and compassion to heal, not your hatred. Treat yourself the way you would treat your loved one if they were in a difficult life situation, remember that inside of you there is always your inner child that needs you to be the loving adult for them. No matter how beautiful, rich, or wise you are, if you don't truly love yourself, no outer attributes will help you with that, truly self-love lies in giving yourself support and care unconditionally, letting yourself be imperfect sometimes. Embrace your uniqueness and work on YOUR personal growth and on what will make YOU happy. It must be your journey of growing into your truly and best self, without social stereotypes and other people's visions of you. Also, ask yourself if you don't tend to seek validation from other people and overcare what someone might think about you. Remember, that true confidence lies in your self-perception. If you know who you are and you like what you are, you will be enough with your own approval. Other people's approval is something too shaky to rely on, in different situations you may receive it or not, but it shouldn't determine your value in your eyes. Be okay with the fact that not everyone will like you, the beauty is in the eyes of the beholder, care only how you feel about yourself. Also, don't forget that confidence is always an action. You can't be confident if you don't work on anything challenging in life, there is nothing to be confident about then. Engage in sports and social activities, realization that you challenge yourself and constantly evolve will make you feel much more confident about yourself. If insecurity has become your habit, just fake confidence. Confidence is about your energy, so pretend to be like that till you actually embrace this emotion. Keep eye contact, keep good posture, speak clearly even if you don't feel like it, and you will become mesmerizing.""",
        
        "Невпевненість": """Робота з невпевненістю і ненавистю до себе - це часто тривалий процес, який вимагає багато саморефлексії та роботи над собою. Проаналізуйте джерело вашої невпевненості, можливо, вам не подобається ваша зовнішність, можливо, вам не подобається ваш характер, і перебування в цьому образі викликає у вас невпевненість. Пам'ятайте, що життя - це не просто пошук себе, це створення себе, тому запишіть, якою була б найкраща версія вас, як би вона поводилися, як виглядала, чим займалася, ким би були її друзі і будь-які інші деталі, які ви можете побачити. Працюйте над тим, щоб стати цією людиною. Ви повинні бути чесними з собою, і якщо щось викликає у вас невпевненість, ви завжди можете змінити це. Інше, над чим потрібно працювати, - це замінити самоненависть на безумовну любов до себе. Будьте добрими до себе, зрозумійте, що навіть якщо ви не є найкращою версією себе зараз, вам потрібні турбота, любов і співчуття, а не ненависть. Ставтесь до себе так, як би ви ставились до вашого близького, якби він потрапив у складну життєву ситуацію, пам'ятайте, що всередині вас завжди є ваша внутрішня дитина, яка потребує вас як люблячого дорослого. Незалежно від того, яким красивим, багатим чи розумним ви є, якщо ви насправді не любите себе, жодні зовнішні атрибути не допоможуть вам у цьому, справжня любов до себе полягає в наданні собі підтримки та турботи без умов, дозволяючи собі іноді бути недосконалим. Прийміть свої особливості, працюйте над собою і над тим, що зробить ВАС щасливими. Це повинен бути ваш шлях у становленні вашим справжнім і найкращим «я», без соціальних стереотипів і чужих уявлень про вас. Також запитайте себе, чи не схильні ви шукати визнання в інших людях і надмірно перейматися тим, що хтось думає про вас. Пам'ятайте, справжня впевненість полягає у вашому самосприйнятті. Якщо ви знаєте, хто ви є, і вам подобається, ким ви є, вам буде достатньо вашого власного схвалення. Схвалення інших людей - це надто нестабільна основа, у різних ситуаціях ви можете отримати його чи ні, але воно не повинно визначати вашу цінність у власних очах. Будьте готові до того, що ви не всім сподобаєтесь, краса субєктивна, турбуйтесь лише про те, як ви відчуваєте себе. Також не забувайте, що впевненість - це завжди дія. Ви не можете бути впевненими, якщо не працюєте над чимось у своєму житті. Займайтесь спортом і улюбеною справою, усвідомлення того, що ви кидаєте собі виклик і постійно розвиваєтесь, зробить вас набагато впевненішими в собі."""
    }

    mental1_health1_bot.send_message(message.chat.id, responses.get(message.text, "Sorry, I don't have a response for that."))


@mental1_health1_bot.message_handler(func=lambda message: message.text in ["Back to Main Menu", "Повернутися до головного меню"])
def back_to_main_menu(message):
    start(message)


@mental1_health1_bot.message_handler(func=lambda message: message.text in ["Get a good habit to work on today", "Отримати корисну звичку, над якою варто попрацювати сьогодні"])
def send_good_habit(message):
    if message.text == "Get a good habit to work on today":
        language = "en"
    elif message.text == "Отримати корисну звичку, над якою варто попрацювати сьогодні":
        language = "uk"
    else:
        language = "en"

    random_habit = random.choice(good_habits)
    habit_to_send = random_habit.get(language, "Sorry, the habit is not available in your language.") 

    mental1_health1_bot.send_message(message.chat.id, habit_to_send)


@mental1_health1_bot.message_handler(func=lambda message: message.text in ["Mood tracker", "Трекер настрою"])
def mood_tracker_menu(message):
    if message.text == "Трекер настрою":
        user_language = "uk" 
    else:
        user_language = "en"  


    user_states[message.chat.id] = {"language": user_language}

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if user_language == 'uk':

        btn1 = types.KeyboardButton("😃 Щасливо")
        btn2 = types.KeyboardButton("😐 Нейтрально")
        btn3 = types.KeyboardButton("😢 Сумно")
        btn4 = types.KeyboardButton("😡 Роздратовано")
        btn5 = types.KeyboardButton("Історія записів")
        btn6 = types.KeyboardButton("Повернутися до головного меню")
        btn7 = types.KeyboardButton("Редагувати запис")
        btn8 = types.KeyboardButton("Видалити запис")
        text = "Як ви себе сьогодні почуваєте? Оберіть емоцію, яка відповідає вашому настрою."
    
    else:

        btn1 = types.KeyboardButton("😃 Happy")
        btn2 = types.KeyboardButton("😐 Neutral")
        btn3 = types.KeyboardButton("😢 Sad")
        btn4 = types.KeyboardButton("😡 Angry")
        btn5 = types.KeyboardButton("Mood History")
        btn6 = types.KeyboardButton("Back to Main Menu")
        btn7 = types.KeyboardButton("Edit Mood record")
        btn8 = types.KeyboardButton("Delete Mood record")
        text = "How are you feeling today? Choose an emoji that represents your mood."

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)

    mental1_health1_bot.send_message(message.chat.id, text, reply_markup=markup)

@mental1_health1_bot.message_handler(func=lambda message: message.text in ["logout"])

def logout(message):
    telegram_id = message.chat.id
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE telegram_id = %s", (telegram_id,))
    conn.commit()
    cursor.close()
    conn.close()

    if telegram_id in user_languages:
        del user_languages[telegram_id]

    mental1_health1_bot.send_message(
        message.chat.id,
        "You have been logged out. Please register again by entering a new password."
    )
    ask_for_registration(message)


from datetime import datetime

@mental1_health1_bot.message_handler(func=lambda message: message.text in ["😃 Щасливо", "😐 Нейтрально", "😢 Сумно", "😡 Роздратовано", "😃 Happy", "😐 Neutral", "😢 Sad", "😡 Angry"])
def record_mood(message):
    print(f"Received message: {message.text}")

    mood_map = {
        "😃 Щасливо": ("Happy", "Щасливо", "uk"),
        "😐 Нейтрально": ("Neutral", "Нейтрально", "uk"),
        "😢 Сумно": ("Sad", "Сумно", "uk"),
        "😡 Роздратовано": ("Angry", "Роздратовано", "uk"),
        "😃 Happy": ("Happy", "Happy", "en"),
        "😐 Neutral": ("Neutral", "Neutral", "en"),
        "😢 Sad": ("Sad", "Sad", "en"),
        "😡 Angry": ("Angry", "Angry", "en")
    }

    user_mood = message.text
    user_id = message.chat.id 

    if user_mood not in mood_map:
        mental1_health1_bot.send_message(message.chat.id, "Invalid mood selection!")
        return

    user_mood_db, user_mood_display, user_language = mood_map[user_mood]

    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id FROM users WHERE telegram_id = %s", (user_id,))
        user = cursor.fetchone()

        if not user:

            mental1_health1_bot.send_message(
                message.chat.id,
                "You are not registered. Please register first." if user_language == 'en' else "Вас не зареєстровано. Спершу зареєструйтесь."
            )
            return

        db_user_id = user[0]  

        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("""
            INSERT INTO moods (user_id, mood, timestamp)
            VALUES (%s, %s, %s)
        """, (db_user_id, user_mood_db, current_datetime))

        conn.commit()

        confirmation_message = (
            f"Ваш настрій ({user_mood_display}) було записано {current_datetime}."
            if user_language == 'uk'
            else f"Your mood ({user_mood_display}) has been recorded for {current_datetime}."
        )
        mental1_health1_bot.send_message(message.chat.id, confirmation_message)

    except Exception as e:
        print(f"Error: {e}")
        mental1_health1_bot.send_message(
            message.chat.id,
            "An error occurred. Please try again later." if user_language == 'en' else "Сталася помилка. Будь ласка, спробуйте ще раз пізніше."
        )
    finally:
        cursor.close()
        conn.close()


@mental1_health1_bot.message_handler(func=lambda message: message.text in ["Mood History", "Історія записів"])
def mood_history(message):
    try:

        conn = connect_to_db()
        cursor = conn.cursor()


        cursor.execute("SELECT id FROM users WHERE telegram_id = %s", (message.chat.id,))
        user = cursor.fetchone()

        if not user:
          
            user_language = 'uk' if message.text == "Історія записів" else 'en'
            no_user_message = (
                "Вас не зареєстровано. Спершу зареєструйтесь."
                if user_language == 'uk' else
                "You are not registered. Please register first."
            )
            mental1_health1_bot.send_message(message.chat.id, no_user_message)
            return

        db_user_id = user[0]  

        cursor.execute("""
            SELECT id, mood, timestamp FROM moods
            WHERE user_id = %s
            ORDER BY timestamp DESC
        """, (db_user_id,))

        mood_history_content = cursor.fetchall()

        user_language = 'uk' if message.text == "Історія записів" else 'en'

        if mood_history_content:
            history_message = (
                "Ваша історія записів:\n"
                if user_language == 'uk' else
                "Your mood history:\n"
            )

            for record_id, mood, timestamp in mood_history_content:
              
                formatted_date = timestamp.strftime('%d-%m-%Y %H:%M')

                mood_display = {
                    "Happy": "😃 Щасливо" if user_language == 'uk' else "😃 Happy",
                    "Neutral": "😐 Нейтрально" if user_language == 'uk' else "😐 Neutral",
                    "Sad": "😢 Сумно" if user_language == 'uk' else "😢 Sad",
                    "Angry": "😡 Роздратовано" if user_language == 'uk' else "😡 Angry"
                }.get(mood, mood)

                history_message += f"ID: {record_id} | {formatted_date} - {mood_display}\n"

            mental1_health1_bot.send_message(message.chat.id, history_message)
        else:
            empty_message = (
                "Ваша історія записів порожня."
                if user_language == 'uk' else
                "Your mood history is empty."
            )
            mental1_health1_bot.send_message(message.chat.id, empty_message)


        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error fetching mood history: {e}")
        user_language = 'uk' if message.text == "Історія записів" else 'en'
        error_message = (
            "Сталася помилка при завантаженні історії записів."
            if user_language == 'uk' else
            "An error occurred while fetching your mood history."
        )
        mental1_health1_bot.send_message(message.chat.id, error_message)

user_states = {}

@mental1_health1_bot.message_handler(func=lambda message: message.text in ["Редагувати запис", "Edit Mood record"])
def request_edit_mood(message):
    user_language = "uk" if message.text == "Редагувати запис" else "en"
    user_states[message.chat.id] = {"state": "waiting_for_edit_id", "language": user_language}
    
    if user_language == "uk":
        mental1_health1_bot.send_message(
            message.chat.id,
            "Будь ласка, надішліть мені ID запису, який ви хочете редагувати."
        )
    else:
        mental1_health1_bot.send_message(
            message.chat.id,
            "Please send me the ID of the mood record you want to edit."
        )

@mental1_health1_bot.message_handler(func=lambda message: user_states.get(message.chat.id, {}).get("state") == "waiting_for_edit_id")
def process_edit_id(message):
    user_language = user_states[message.chat.id].get("language", "en")
    user_states[message.chat.id] = {"state": "waiting_for_new_mood", "edit_id": message.text, "language": user_language}
    
    if user_language == "uk":
        mental1_health1_bot.send_message(
            message.chat.id,
            "Тепер надішліть нове значення для цього запису."
        )
    else:
        mental1_health1_bot.send_message(
            message.chat.id,
            "Now send me the new mood for the record."
        )

@mental1_health1_bot.message_handler(func=lambda message: user_states.get(message.chat.id, {}).get("state") == "waiting_for_new_mood")
def process_new_mood(message):
    user_data = user_states[message.chat.id]
    edit_id = user_data["edit_id"]
    new_mood = message.text
    user_language = user_data["language"]


    valid_moods_en = ["Happy", "Neutral", "Sad", "Angry"]
    valid_moods_uk = ["Щасливо", "Нейтрально", "Сумно", "Роздратовано"]

    try:
        if new_mood not in valid_moods_en and new_mood not in valid_moods_uk:
            if user_language == "uk":
                mental1_health1_bot.send_message(message.chat.id, "Будь ласка, натисніть Редагувати запис знову і введіть коректний настрій з наступного списку: Щасливо, Нейтрально, Сумно, Роздратовано.")
            else:
                mental1_health1_bot.send_message(message.chat.id, "Please press Edit Mood record again and enter a valid mood from the list: Happy, Neutral, Sad, Angry.")
            return

        if user_language == 'uk':
            if new_mood == "Щасливо":
                new_mood_db = "Happy"
            elif new_mood == "Нейтрально":
                new_mood_db = "Neutral"
            elif new_mood == "Сумно":
                new_mood_db = "Sad"
            elif new_mood == "Роздратовано":
                new_mood_db = "Angry"
        else:
            new_mood_db = new_mood  

        conn = connect_to_db()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE moods
            SET mood = %s
            WHERE id = %s AND user_id = (
                SELECT id FROM users WHERE telegram_id = %s
            )
        """, (new_mood_db, edit_id, message.chat.id))

        conn.commit()

        if cursor.rowcount > 0:
            if user_language == 'uk':
                mental1_health1_bot.send_message(
                    message.chat.id, f"Ваш запис з ID {edit_id} було оновлено на '{new_mood}'."
                )
            else:
                mental1_health1_bot.send_message(
                    message.chat.id, f"Your mood record with ID {edit_id} has been updated to '{new_mood}'."
                )
        else:
            if user_language == 'uk':
                mental1_health1_bot.send_message(
                    message.chat.id, f"Запис з ID {edit_id} не знайдено."
                )
            else:
                mental1_health1_bot.send_message(
                    message.chat.id, f"No record found with ID {edit_id} for editing."
                )

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error editing mood: {e}")
        if user_language == 'uk':
            mental1_health1_bot.send_message(message.chat.id, "Сталася помилка при редагуванні запису.")
        else:
            mental1_health1_bot.send_message(message.chat.id, "An error occurred while editing the mood record.")
    finally:

        user_states.pop(message.chat.id, None)


@mental1_health1_bot.message_handler(func=lambda message: message.text in ["Delete Mood record", "Видалити запис"])
def initiate_delete_mood(message):
    user_language = "uk" if message.text == "Видалити запис" else "en"
    user_states[message.chat.id] = {"state": "waiting_for_delete_id", "language": user_language}

    if user_language == "uk":
        mental1_health1_bot.send_message(
            message.chat.id,
            "Будь ласка, надішліть мені ID запису, який ви хочете видалити."
        )
    else:
        mental1_health1_bot.send_message(
            message.chat.id,
            "Please send me the ID of the mood record you want to delete."
        )

@mental1_health1_bot.message_handler(func=lambda message: user_states.get(message.chat.id, {}).get("state") == "waiting_for_delete_id")
def delete_mood_record(message):
    mood_id = message.text.strip()
    user_language = user_states[message.chat.id].get("language", "en")

    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM moods
            WHERE id = %s AND user_id = (
                SELECT id FROM users WHERE telegram_id = %s
            )
        """, (mood_id, message.chat.id))
        conn.commit()

        if cursor.rowcount > 0:
            if user_language == "uk":
                mental1_health1_bot.send_message(
                    message.chat.id, f"Запис з ID {mood_id} успішно видалено."
                )
            else:
                mental1_health1_bot.send_message(
                    message.chat.id, f"The mood record with ID {mood_id} has been successfully deleted."
                )
        else:
            if user_language == "uk":
                mental1_health1_bot.send_message(
                    message.chat.id, f"Запис з ID {mood_id} не знайдено."
                )
            else:
                mental1_health1_bot.send_message(
                    message.chat.id, f"No record found with ID {mood_id} to delete."
                )

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error deleting mood: {e}")
        if user_language == "uk":
            mental1_health1_bot.send_message(message.chat.id, "Сталася помилка при видаленні запису.")
        else:
            mental1_health1_bot.send_message(message.chat.id, "An error occurred while deleting the mood record.")

    user_states.pop(message.chat.id, None)


@mental1_health1_bot.message_handler(func=lambda message: user_states.get(message.chat.id, {}).get("state") != "waiting_for_new_mood", content_types=['text'])
def empty(message):

    user_language = user_states.get(message.chat.id, {}).get("language", "en")

    response_message = (
        "Вибачте, ця команда мені невідома."
        if user_language == "uk" else
        "Sorry, this command is unknown for me."
    )

    mental1_health1_bot.send_message(message.chat.id, text=response_message)

mental1_health1_bot.polling(none_stop=True, timeout=20)
