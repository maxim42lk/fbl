 a.send_message(message.from_user.id, 'Цифрами, пожалуйста');
 
 a.send_message(message.from_uimport telebot
#логгируем токен и используем библиотеку через нашу переменную, например а
a = telebot.TeleBot("1534882898:AAGGdE4SsWJsDa2fvjldmTczlpxEZFsxiSs")
#делается своего рода флажок для использования в дальнейшем
keyboard_test = telebot.types.ReplyKeyboardMarkup(True)
#Прописываем кнопки в строчку
keyboard_test.row("Привет", "Пока","Словарь для программиста","Кибербезопасность","Для IT и бизнеса","закрыть")
 
#простыми словами, если бот перехватил команду /start, то начинает запускать функцию, которая следует после декоратора (@) в этой же функции мы можем как-по своему обработать ответ бота на сообщение пользователя
@a.message_handler(commands=['start'])
def startWork(message):
 #в этом пример tid = айди сообщения, параметр, который следует использовать в сигнатуре функции send_message, если надо отправить под именем бота сообщение пользователю
 tid = message.chat.id
 #отправка пользователю сообщение, два параметра = айди, текст и параметр reply_markup для установки клавиатуры на этом этапе
 a.send_message(tid, "start work!", reply_markup = keyboard_test)
#простыми словами, если бот перехватил команду любой текст, который отправил пользователь боту, то начинает запускать функцию, которая следует после декоратора (@) в этой же функции мы можем как-по своему обработать ответ бота на сообщение пользователя
name = '';
surname = '';
age = 0;
@a.message_handler(content_types=['text'])
def sendYourMessage(message):
 mid = message.chat.id
 #если пользователь написал Привет, то бот ответ в соответвии с тем, что ему предписано
 if message.text == "Привет":
   a.send_message(mid, "Привет:)")
 elif message.text == "Кибербезопасность":
   a.send_message(mid, "DARKReading.com — известный сайт, который полностью посвящен особенной теме — кибербезопасности")
 elif message.text == "Для IT и бизнеса":
  a.send_message(mid, "CIO.com — отличный американский ресурс с обилием контента на многие темы как для IT-специалистов, так и для руководящего звена IT-компаний")
 elif message.text == "Словарь для программиста":
   a.send_message(mid, "multitran.ru — отличный словарь с кучей значений на каждое слово, есть категории применения слов и подробные пояснения;")
 elif message.text =="закрыть":
  a.send_message(mid, "ок",reply_markup=telebot.types.ReplyKeyboardRemove())
 elif message.text =="Пока":
  a.send_message(mid, "Пока:(")
 else:
 #если пользователь написал сообщение, которое у бота никак выше не обрабатывается
   a.send_message(mid, "Не понимаю тебя что ты хочешь")
 
 if message.text == '/reg':
 
   a.send_message(message.from_user.id, "Как тебя зовут?");
 
   a.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
 
 
def get_name(message): #получаем фамилию
 
 global name;
 
 name = message.text;
 
 a.send_message(message.from_user.id, 'Какая у тебя фамилия?');
 
 a.register_next_step_handler(message, get_surname);
 
def get_surname(message):
 
 global surname;
 
 surname = message.text;
 
 a.send_message(message.from_user.id, 'Сколько тебе лет?');
 
 a.register_next_step_handler(message, get_age);
 
def get_age(message):
 
 global age;
 
 while age == 0: #проверяем что возраст изменился
 
   try:
 
     age = int(message.text) #проверяем, что возраст введен корректно
 
   except Exception:
 
ser.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')
 #polling нужен для того, чтобы бот не переставал перехватывать сообщения, работал в режиме ожидания от пользователя действий
@a.message_handler(content_types=['voice'])
def sendYourMessage(message):
if message.content_type=='voice':
 a.send_message(message.chat.id, "Не говори со мной")
 
a.polling()
