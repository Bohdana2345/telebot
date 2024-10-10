import telebot
from telebot import types
import random
from datetime import datetime

mental1_health1_bot = telebot.TeleBot('6773157797:AAHk_A9WfRrpnHUyl2Ug0oZf-4mX5ByAQiU')

inspirational_quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "The journey of a thousand miles begins with one step. - Lao Tzu",
    "In the middle of difficulty lies opportunity. - Albert Einstein",
    "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
    "Hard work beats talent when talent doesn't work hard. - Tim Notke",
    "The only way to achieve the impossible is to believe it is possible. - Charles Kingsleigh", 
    "Success is stumbling from failure to failure with no loss of enthusiasm. - Winston Churchill",
    "The most powerful relationship you will ever have is the relationship with yourself. - Steve Maraboli",
    "Kindness is a language that the deaf can hear and the blind can see. - Mark Twain",
    "To love oneself is the beginning of a lifelong romance. - Oscar Wilde",
    "You yourself, as much as anybody in the entire universe, deserve your love and affection. - Buddha",
    "Kindness in words creates confidence. Kindness in thinking creates profoundness. Kindness in giving creates love. - Lao Tzu",
    "Love yourself first, and everything else falls into line. - Lucille Ball",
    "Your task is not to seek for love, but merely to seek and find all the barriers within yourself that you have built against it. - Rumi",
    "Remember always that you not only have the right to be an individual, you have an obligation to be one. - Eleanor Roosevelt"
    
]

good_habits=[
    "Express gratitude for three good things in your life every morning",
    "Eat a balanced and nutritious meal",
    "Avoid screens at least 30 minutes before bedtime",
    "Read one chapter from a self-improvement book every day",
    "Get at least 7-8 hours of sleep every night",
    "Go to sleep before midnight and wake up before 8 a.m. every day",
    "Learn to say 'no'",
    "Engage in at least 15 minutes of physical exercise every day",
    "Set aside at least 15 minutes per day for your hobby or creative activity",
    "Maintain a clean and organized living space",
    "Stay hydrated by drinking at least 2L of water throughout the day",
    "Cultivate a positive mindset by focusing on solutions",
    "Limit time spent on social media to promote a healthy mind",
    "Learn not to compare yourself with other people",
    "Spend at least 2 hours walking in the fresh air every day",
    "Take a daily multivitamin supplement",
    "Learn not to procrastinate, tackle tasks and challenges promptly",
    "Give at least three compliments to others every day",
    "Make your bed every morning", 
    "Learn to eat without your phone"

]
# відслідковувач команди start
@mental1_health1_bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Get an inspirational quote")
    btn2 = types.KeyboardButton("Get psychological support")
    btn3 = types.KeyboardButton("Mood tracker")
    btn4 = types.KeyboardButton("Go to the website to communicate with a psychologist")
    btn5 = types.KeyboardButton("Get a good habit to work on today")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    text = "Hey, {0.first_name}! I am a bot, created to help you with your mental health when needed. Please, select an option.".format(message.from_user)
    mental1_health1_bot.send_message(message.chat.id, text, reply_markup=markup)
    with open("greeting.png", "rb") as photo:
        mental1_health1_bot.send_photo(message.chat.id, photo)

@mental1_health1_bot.message_handler(func=lambda message: message.text == "Go to the website to communicate with a psychologist")
def open_website(message):
    url_button = types.InlineKeyboardButton("Open the website", url='https://www.betterhelp.com/')
    keyboard = types.InlineKeyboardMarkup().add(url_button)
    mental1_health1_bot.send_message(message.chat.id, "Click the button below to open the website:", reply_markup=keyboard)
    
@mental1_health1_bot.message_handler(func=lambda message: message.text == "Get an inspirational quote")
def send_inspirational_quote(message):
    # Select a random quote from the list
    random_quote = random.choice(inspirational_quotes)
    mental1_health1_bot.send_message(message.chat.id, random_quote)

@mental1_health1_bot.message_handler(func=lambda message: message.text == "Get psychological support")
def psychological_support(message):
    # Send a photo with a caption
    with open("emot.png", "rb") as photo:
        mental1_health1_bot.send_photo(message.chat.id, photo, caption="What are you feeling right now?")

    # Create a custom keyboard with buttons
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "Anger", "Envy", "Loneliness", "Laziness", 
        "Social anxiety", "Eating disorder phase", 
        "Offense", "Insecurity and self-hatred", "Back to Main Menu"
       
    ]

    for button_text in buttons:
        keyboard.add(types.KeyboardButton(button_text))

    mental1_health1_bot.send_message(message.chat.id, "Choose emotion, please:", reply_markup=keyboard)

@mental1_health1_bot.message_handler(func=lambda message: message.text == "Back to Main Menu")
def back_to_main_menu(message):
    # Return to the main menu
    start(message)

@mental1_health1_bot.message_handler(func=lambda message: message.text == "Get a good habit to work on today")
def send_good_habit(message):
    # Select a random habit from the list
    random_habit = random.choice(good_habits)
    mental1_health1_bot.send_message(message.chat.id, random_habit)

@mental1_health1_bot.message_handler(func=lambda message: message.text == "Anger")
def handle_anger(message):
    anger_response = """Don't react harshly, remember that decisions made under the influence of anger will lead to regret later. Emotions prevent you from seeing the situation clearly, give yourself time to calm down and analyze it objectively. If you let someone or something make you angry, you acknowledge their power over you and let them control your mind, you choose to believe them and take their opinions personally. Don't spend energy on negative situations, embrace the fact that it is normal for people to make mistakes and not everyone will share your values. Forgive, breathe deeply, release your emotions by journaling, physical activity or whatever makes you feel better and focus on finding solutions.Be honest with yourself about what you fell, don't deny negative emotions, they are the indicators that help you to understand yourself better, but learn to develop emotional intelligence and control your reactions."""
    mental1_health1_bot.send_message(message.chat.id, anger_response)

@mental1_health1_bot.message_handler(func=lambda message: message.text == "Envy")
def handle_envy(message):
    envy_response = """Envy is the indicator of what you desire the most in life. If you see someone possessing something and feel envy that's obviously what you would like to possess either and it is totally okay. There are two ways to ease this feeling - to put someone else down and wish them to fail or to level up yourself. Obviously, second variant is what we choose, it will positively influence your life and help you make real changes.  Convert your envy to feeling inspired by other person, learn from them,realize that if they've managed to get it, it is possible for you either, so work on it and see envy as guidance in some situations. Our universe is huge and everyone has their own space to success, what was meant for you will be yours. Also it is important to realize that every person is unique, so someone could get what you want easier or faster, but that doesn't mean you can't have it either - you can and you will in your unique way and perfect timing. Don't compare yourself with other people, only with the person you were yesterday and be grateful for your own blessings."""
    mental1_health1_bot.send_message(message.chat.id, envy_response)
   
@mental1_health1_bot.message_handler(func=lambda message: message.text == "Loneliness")
def handle_loneliness(message):
    loneliness_response = """Dealing with loneliness can be challenging, but there are several strategies and activities that may help alleviate feelings of isolation. Sometimes we find ourselves in situations were for whatever reason we lost connections with other people - maybe we choose different pathes, maybe we lost interest, maybe we had a serious fight. Your task now is to realize that in order to change your situation you need to take action. First, analyze your social needs, what you can give to other people and what you want to have in exchange. Try to connect with your loved ones, take the initiative and ask them out more, explain your needs and feelings. If you want to have a new social circle, don't be a homebody, open your mind to new acquaintance. Attend social events, participate in various clubs and classes that align with your interests. You can start just with walkings in the nearest park - the most important thing is to be around other people. Be nice and sociable and you will definitely feel better. If you have some problems that prevent you from being outgoing - like fear of rejection or insecurity, work on it first. Don't overcare about failed social experiences, don't overthink about what other people will think about you, don't fill your mind with negative expectations,  just enjoy the moment and be yourself. It is better to try and fail than not to try at all and regret, don't forget that other people have similar fears, insecurities and needs, so be active and take initiative. Also work on your personality - take care of your appearence and mind, know who you are and it will help you to feel more confident while interacting with other peole. Consider getting a pet if your living situation allows. Pets can provide companionship and a sense of purpose. Also don't use other people to fill the gap inside your soul, remeber that you should cover your basic needs(like need of love, safety, validation etc) yourself to prevent depending on others. Be okay with spending time on your own company and build strong relationship with yourself, then your relationship with other people will follow."""
    mental1_health1_bot.send_message(message.chat.id, loneliness_response)

@mental1_health1_bot.message_handler(func=lambda message: message.text == "Laziness")
def handle_laziness(message):
    laziness_response = """Realize that your goals won't be achieved without your actions, realize that everything has consequences - if you choose to be lazy today you will end up being broke tomorrow, being the person that chooses pain of regret over the pain of discipline, person that struggles thinking what they could've had if they chose to use their potential fully and fought their weakness. If you choose what you want now over you want the most - you choose to be a failure. Know the difference between  being lazy and having a burnout though. If you are really tired, take a day off and give yourself a time to rennovate your recources,always be honest with yourself about it. If you struggle with discipline, cutt off all discractors and give yourself just 10 minutes to be involved in what you should do, to start is always the hardest and the most probable wou will continue after you've done that. Plan your schedule, limit your screen time, develop small habits like making your bed in the morning and engage in sports - it will make your mind more disciplined and help you to overcome laziness easier. Set realistic goals for yourself and give youself rewards for performing well, always start with easier tasks, but do the hardest when you are the most productive, divide great job into smaller parts. Do job with companion - it will increase your responsibility and provide more encouragement.  Remember, that if you are too lazy to take care of yourself and do what will be good for you, you don't love yourself. Love is always an action, so do this action for yourself. Remember that overcoming laziness is a gradual process, and it's okay to face setbacks. Be patient with yourself and consistently apply these strategies to build positive habits and increase productivity over time. """
    mental1_health1_bot.send_message(message.chat.id, laziness_response)

@mental1_health1_bot.message_handler(func=lambda message: message.text == "Social anxiety")
def handle_saxiety(message):
    sanxiety_response = """To overcome social anxiety, stop putting other people on pedestal. Fear of embarrassment seems to be something horrible,  failing or seeing disapproval in someone's eyes seems to be the end of our lives, but it is only a silly illusion. Realize that other people are not better than you, we all are unique, have our own strengths and weaknesses, but are equal on the whole. So other people do not hold the power to determine who you are or judge you. This right belongs to you, you should determine your value on your own, build strong self-esteem and peaceful place in your mind. Let yourself to fail and be imperfect, enjoy your life without caring what someone thinks about you or what will hapen if some of  your social experiences won't work out. Every failed social interaction still brings you an useful experience. Remember that everyone has their own lives and problems and other people don't focus on you as much as you think, in most cases they don't care. Still, someone may not like you and it is tottaly fine - you don't like everyone either. Still someome may talk poorly about you - and it is only about them, they obviously don't have anything wiser to say and are unsattisfied because you do what they are afraid even to try. Let them be mean, be proud you are so important for  someone that they are obsessed with you enough to hate you. If your relationship with someone turns out to be a failure - it is okay, this what happens sometimes, make conclusions, move on and stop caring. Realize that there is no reason for social anxiety - nothing fatal can happen to you during social interections, other people are just like you, they have same fears and insecurities. Just enjoy communication, be yourself, be okay either it works out or not - there are no bad endings, it is either a good one or an experience. If someone makes fun of you - realize that it is projection of their own insecuruties, be ready to defend your peace and not let someone's opinion to ruin your self-perception. Be polite, nice and confident, think not about who will like you, think about if you like what you do. Leave your comfort zone, remember, that it is better to try and fail than even not to try and don't waste your energy on unimportant things."""
    mental1_health1_bot.send_message(message.chat.id, sanxiety_response)   


@mental1_health1_bot.message_handler(func=lambda message: message.text == "Eating disorder phase")
def handle_ed(message):
    ed_response = """Dealing with an eating disorder is a complex process that takes a lot of stamina. The first thing is to realize that it is not a problem, it is an aftermath. So your task is to find a reason that causes you to overeat or starve yourself - something that disturbs you and to solve it innitialy. You use food only to distract yourself from your true problem and receive temporary relief. An example of such problem can be anxiety, unhealed trauma, loneliness, boredom, low self-esteem etc. Learn what(or who) triggers your eating disorder and focus on the root of your problem. Then embrace self-love and care, don't try to punish yourself, focus not on your body measeruments, but on your health first of all. Be patient, take little steps when you are trying to gain or loose weight, realize that sometimes when you are dealing with a lot of stress your eating disorder comes back even though you've been succesfully overcoming it recently, don't give up and be good to yourself. Don't put your entire focus on  your food, people who struggle with eating disorder tend to be obsessed with their meals and think about that 24/7 as well as dramatize everything linked with this topic( like they are convicted that 1 ice-cream will make them very fat etc). Don't prevent yourself from going out, dating, buying that one piece of clothes you want to wear etc because you are not "skiny enough" or on the contrary "too skinny",  don't let your eating disorder  put your life on hold. Be objective and try to be in your best shape, but in any stage of your life you should support and love your body.  Fill your life with events, people, interesting experiences and hobbies so your mind had another things to care about.  Don't put your entire value in your weight,  realize that you are not only that, you are also what you think, you are your values, your hobbies etc. Try to find a golden mean - it is cool to be fit, but above everything you should be healthy and create for yourself healthy lifestyle you will be able to lead. Listen to your body needs, walk on fresh air, eat enough nutriments, stay hydrated, do sport and don't forget to keep balance. Don't set very strict constraints for youself, don't divide food into bad and good, embrace 80/20 principle, trying to eat healthy most of the time, but letting yourself to eat your favorite sweets or fast-food sometimes. Don't starve or overfeed yourself during the day. Develop healthy eating habits, like eating without your phone or chewing slowly, it will help you to deal with your problem. Also try to find support in your loved ones or talk with specialist, it can be extremely helpful as well."""
    mental1_health1_bot.send_message(message.chat.id, ed_response)        

@mental1_health1_bot.message_handler(func=lambda message: message.text == "Offense")
def handle_offense(message):
    offense_response = """If you feel offense, number one point is to let yourself calm down and don't act out of emotions. Recognize your feelings,trust yourself, let yourself feel what you feel and deal with it rationally. Then talk with a person that have insulted you - be honest, but don't be rude. Realize that all people were brought up in  different environments so what is offensive for you can be tottaly okay for someone else, that's why you should use communication to talk about your needs and feelings. Explain situation without aggressive accusations and dramas, discuss a way to make you feel okay and solve this problem. If that person really appreciates you, they will take into account your opinion and will act understanding. They will appologize and not do that again. If in response individual derides you and offers only justification, then think twice before communicating with this person who doesn't care about your feelings. Whether you managed fo find a common ground and make peace with this person or decided to end communication, forgive them and move on for your own sake. Sometimes we might be offended by people without having opportunity to talk with them about it or we find some offense too serious and don't want to deal with our insulter at all anymore, so all that is left anyways is to let it go. Don't waste your energy on negativity, the best revenge is just to focus on your life, work on your healing and level up."""
    mental1_health1_bot.send_message(message.chat.id, offense_response)   

@mental1_health1_bot.message_handler(func=lambda message: message.text == "Insecurity and self-hatred")
def handle_insecuruty(message):
    insecuruty_response = """Dealing with insecurity and self-hatred is a personal and often ongoing process that involves self-reflection, self-compassion, and personal growth. Analyze the source of your insecurity, maybe you don't like your appearance, maybe you don't like your character and  being in this role model causes your unconfidence. Remember then life is not just about finding yourself, it is about creating yourself, so write down how would the best, the most confident version of you look like, how would they behave, who would be their friends and any other detail you can see. Work on turning yourself into this person. You should be honest with yourself and if something makes you feel insecure you can always work on changing it. Another thing is you should work on replacing self-hatrage with unconditional self-love. Be good to yourself, realize that even if you are not the best version of yourself now, you need your care, love and compassion to heal, not your hatrage. Treat yourself the way you would treat your loved one if they were in difficult life situation, remember that inside of you there is always your inner child that needs you to be the loving adult for them. No matter how beatiful, rich or wise you are, if you don't truly love yourself, no outer attributes will help you with that, truly self-love lies in giving yourself support and care unconditially, letting yourself to be imperfect sometimes. Embrace your uniqueness and work on YOUR personal growth and on what will make YOU happy. It must be your journey of growing into your truly and best self, without social stereotypes and other people's visions of you. Also ask yourself if you don't tend to seek validation from other people and overcare  what someone might think about you. Remeber, that truly confidence lies in your self-perception. If you know who you are and you like what you are, you will be enough with your own approval. Other  people's approval is something too shaky to rely on, in different situations you may receive it or not, but it shouldn't determine your value in your eyes. Be okay with the fact that not everyone will like you, the beauty is in the eyes of the beholder, care only how you feel about yourself. Also don't forger that confidence is always an action. You can't be confident if you don't work on anything challenging in life, there is nothing to be confident about then. Enage in sports and social activities, realization that you challenge yourself and constanly evolve will make you feel much more confident about yourself. If insecurity has become your habit, just fake confidence. Confidence is about your energy, so pretend to be like that till you actually embrace this emotion. Keep eye contact, keep good posture, speak clearly even if you don't feel like it and you will become meshmerazing."""
    mental1_health1_bot.send_message(message.chat.id, insecuruty_response)  

@mental1_health1_bot.message_handler(func=lambda message: message.text == "Mood tracker")
def mood_tracker_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("😃 Happy")
    btn2 = types.KeyboardButton("😐 Neutral")
    btn3 = types.KeyboardButton("😢 Sad")
    btn4 = types.KeyboardButton("😡 Angry")
    btn5 = types.KeyboardButton("Mood History")
    btn6 = types.KeyboardButton("Back to Main Menu")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

    text = "How are you feeling today? Choose an emoji that represents your mood."
    mental1_health1_bot.send_message(message.chat.id, text, reply_markup=markup)

# Обробник кнопки "Mood History"
@mental1_health1_bot.message_handler(func=lambda message: message.text == "Mood History")
def mood_history(message):
    try:
        # Зчитування вмісту файлу з історією настроїв
        with open("mood_tracker.txt", "r", encoding="utf-8") as file:
            mood_history_content = file.read()

        # Відправлення історії настроїв користувачеві
        if mood_history_content:
            mental1_health1_bot.send_message(message.chat.id, "Your mood history:\n" + mood_history_content)
        else:
            mental1_health1_bot.send_message(message.chat.id, "Your mood history is empty.")
    except Exception as e:
        print(f"Error reading mood history: {e}")
        mental1_health1_bot.send_message(message.chat.id, "An error occurred while reading your mood history.")

# ...

# Обробник вибору настрою користувачем
@mental1_health1_bot.message_handler(func=lambda message: message.text in ["😃 Happy", "😐 Neutral", "😢 Sad", "😡 Angry"])
def record_mood(message):
    # Отримання вибору настрою користувача
    user_mood = message.text

    # Отримання поточної дати та часу
    current_datetime = datetime.now()

    # Збереження настрою та мітки часу в файл чи базу даних (цю частину можна налаштувати під свої потреби)
    with open("mood_tracker.txt", "a", encoding="utf-8") as file:
        file.write(f"{current_datetime}: {user_mood}\n")

    # Відправлення підтвердження користувачеві
    confirmation_message = f"Your mood ({user_mood}) has been recorded for {current_datetime}."
    mental1_health1_bot.send_message(message.chat.id, confirmation_message)

@mental1_health1_bot.message_handler(content_types=['text'])
def empty(message):
    mental1_health1_bot.send_message(message.chat.id, text='Sorry, this command is unknown for me.')

mental1_health1_bot.polling()
