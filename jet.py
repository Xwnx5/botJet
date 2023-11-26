from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram import executor
import json
import os

bot = Bot(token='') #Вставьте сюда токен своего бота
dp = Dispatcher(bot, storage=MemoryStorage())

class FSMAdmin(StatesGroup):
    firstState = State()
    secondState = State()


class FSMAdmin_2(StatesGroup):
    firstState2 = State()
    secondState2 = State()


class FSMAdmin_3(StatesGroup):
    firstState3 = State()
    secondState3 = State()


class FSMAdmin_4(StatesGroup):
    firstState4 = State()
    secondState4 = State()


@dp.message_handler(commands='start')
async def echo(message: types.Message):
    await message.answer('Привет!👋 Это бот Стратегий!!!', parse_mode='HTML')   
    keyboardmain = types.InlineKeyboardMarkup(row_width=1)
    first_button = types.InlineKeyboardButton(text="🏆СМОТРЕТЬ СТРАТЕГИИ🏆", callback_data="first")
    dev_button = types.InlineKeyboardButton(text="🧠О разработке стратегий🧠", callback_data="dev_strat")
    keyboardmain.add(first_button, dev_button)
    await message.answer('<b>Кто мы?</b>👥\n\nМы - команда программистов, которые устали работать на других и тратить свой потенциал в достижение чужих целей\n\n===============================\n\n<b>Что мы делаем?</b>💻\n\nМы взламываем различные приложения, игры, системы защиты сайтов и используем их в своих целях, например перепродажа по более низким ценам или как в случае с этим ботом, для продажи стратегий, которые мы разработали в ходе анализа кода сайта 1win\n\n===============================\n\n<b>Что мы предлагаем?</b>💰\n\nМы предлагаем вам приобрести математически выверенные стратегии! Никаких сигналов или интуиций! Чистая математика! Существуют разные стратегии, бывают более прибыльные, но медленные, а бывают быстрее но с меньшим заработком, либо стратегии с высоким заработком и быстрые, но с большим риском. Какую стратегию использовать решать вам! Конечно стопроцентного результата не может обещать никто, так как алгоритм сайта меняется, но стратегии со временем дополняются и обновляются!', parse_mode='HTML', reply_markup= keyboardmain)

@dp.callback_query_handler(lambda call:True)
async def callback_inline(call):

    if call.data == "dev_strat":
        keyboardmain = types.InlineKeyboardMarkup(row_width=1)
        back_to_menu = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboardmain.add(back_to_menu)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='<b>Как мы разрабатываем стратегии?</b>🤔\n\n<b>Наш алгоритм разработки выглядит следующим образом:</b>👇👇👇👇👇 \n\n1️⃣ Включается ранее написанная программа, которая берёт данные с сайта 1win, если конкретнее, то программа собирает выпавшие иксы в большой файл данных(массив)\n\n2️⃣ Спустя определённое количество времени(в среднем месяц для более точных рузальтатов), программа начинает анализировать полученные данные на предмет закономерностей и повторяющихся коэффицентов, и выносит все полученные результаты в новый файл\n\n3️⃣ Наши люди вручную перебирают данные и проверяют полученные стратегии, отбирают лучшие и сохраняют\n\n4️⃣ Продажа стратегий на разных ресурсах\n\n<b>Наиболее прибыльные стратегии продаются в единичных экземплярах за большие суммы денег, а остальное идёт в массовый сбыт</b>', parse_mode='HTML', reply_markup= keyboardmain)

    if call.data == "menu":
        keyboardmain = types.InlineKeyboardMarkup(row_width=1)
        first_button = types.InlineKeyboardButton(text="🏆СМОТРЕТЬ СТРАТЕГИИ🏆", callback_data="first")
        dev_button = types.InlineKeyboardButton(text="🧠О разработке стратегий🧠", callback_data="dev_strat")
        
        keyboardmain.add(first_button, dev_button)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='<b>Кто мы?</b>👥\n\nМы - команда программистов, которые устали работать на других и тратить свой потенциал в достижение чужих целей\n\n===============================\n\n<b>Что мы делаем?</b>💻\n\nМы взламываем различные приложения, игры, системы защиты сайтов и используем их в своих целях, например перепродажа по более низким ценам или как в случае с этим ботом, для продажи стратегий, которые мы разработали в ходе анализа кода сайта 1win\n\n===============================\n\n<b>Что мы предлагаем?</b>💰\n\nМы предлагаем вам приобрести математически выверенные стратегии! Никаких сигналов или интуиций! Чистая математика! Существуют разные стратегии, бывают более прибыльные, но медленные, а бывают быстрее но с меньшим заработком, либо стратегии с высоким заработком и быстрые, но с большим риском. Какую стратегию использовать решать вам! Конечно стопроцентного результата не может обещать никто, так как алгоритм сайта меняется, но стратегии со временем дополняются и обновляются!', parse_mode='HTML', reply_markup= keyboardmain)

    if call.data == "first":
        keyboard = types.InlineKeyboardMarkup(row_width=1)

        a = '🤠Стратегия ДЕВЯТКА🤠\n🔥ХИТ🔥'

        but1 = types.InlineKeyboardButton(text="🤓Стратегия НАЧАЛЬНАЯ(ВЕЧНАЯ)🤓", callback_data="1")
        but2 = types.InlineKeyboardButton(text=a, callback_data="2")
        but7 = types.InlineKeyboardButton(text="😎Стратегия МАЖОР😎", callback_data="7")
        
        butDiamondOge = types.InlineKeyboardButton(text="✅💎ВСЁ💎✅", callback_data="diamondOge")
        back_to_menu = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard.add(but1, but2, but7, butDiamondOge ,back_to_menu)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='<b>Кто мы?</b>👥\n\nМы - команда программистов, которые устали работать на других и тратить свой потенциал в достижение чужих целей\n\n===============================\n\n<b>Что мы делаем?</b>💻\n\nМы взламываем различные приложения, игры, системы защиты сайтов и используем их в своих целях, например перепродажа по более низким ценам или как в случае с этим ботом, для продажи стратегий, которые мы разработали в ходе анализа кода сайта 1win\n\n===============================\n\n<b>Что мы предлагаем?</b>💰\n\nМы предлагаем вам приобрести математически выверенные стратегии! Никаких сигналов или интуиций! Чистая математика! Существуют разные стратегии, бывают более прибыльные, но медленные, а бывают быстрее но с меньшим заработком, либо стратегии с высоким заработком и быстрые, но с большим риском. Какую стратегию использовать решать вам! Конечно стопроцентного результата не может обещать никто, так как алгоритм сайта меняется, но стратегии со временем дополняются и обновляются!', parse_mode='HTML', reply_markup=keyboard)
         
    
    elif call.data == "1":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🤓Стратегия НАЧАЛЬНАЯ🤓\n\n<b>Стоимость:</b> 490 рублей🇷🇺\n\n<b>Описание:</b> Одна из самых распространённых стратегий, но рабочая и доработанная. \n\n<b>Рекомендуемый начальный баланс от 1000р.</b>\n\n<b>Гарантированный заработок с баланса 1000 рублей : 500 - 800 рублей в час.</b>\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ СТРАТЕГИЮ В ТЕЧЕНИИ СУТОК‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)

    elif call.data == "2":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🤠Стратегия ДЕВЯТКА🤠\n\n<b>Стоимость:</b> 990 рублей🇷🇺\n\n<b>Описание:</b> Отличная стратегия с 96% заходом. \n\n<b>Доход зависит от вашего баланса!</b>\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ СТРАТЕГИЮ В ТЕЧЕНИИ СУТОК‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)
    
    elif call.data == "7":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>😎Стратегия МАЖОР😎\n\n<b>Стоимость:</b> 2490 рублей🇷🇺\n\n<b>Описание:</b> Стратегия с бешеным доходом!🔥 \n\n<b>Доход также зависит от вашего баланса! В среднем получалось сделать 50% от баланса буквально за 15 минут!</b>\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ СТРАТЕГИЮ В ТЕЧЕНИИ СУТОК‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)
    
    elif call.data == "diamondOge":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>✅💎ВСЁ💎✅\n\n<b>Стоимость:</b> 3249 рублей🇷🇺\n\n<b>Описание:</b> Все стратегии, представленные в нашем боте! Чтобы попробовать все и выбрать ту, которая больше всего понравится!\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ СТРАТЕГИИ В ТЕЧЕНИИ СУТОК‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)

 

    elif call.data == "payment_oge":
        keyboard_pay = types.InlineKeyboardMarkup(row_width=1)
        but_oge_pay_ok = types.InlineKeyboardButton(text="Я оплатил👍", callback_data="payment_oge_ok")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_pay.add(but_oge_pay_ok, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= f'<b>Отправьте сумму с комментарием:</b>\n "{call.message.chat.id}" и название тарифа <b>БЕЗ ЭМОДЗИ</b>\n\n🟣<b>ЮMoney: 4100118152600671</b>🟣\n🟢<b>СберБанк\Тинькоф: <s>СЕЙЧАС НЕДОСТУПНО</s></b>🟢\n🔵<b>FKWallet: F112328624</b>🔵\n\n ‼️<b>ЕСЛИ СУММА НЕТОЧНАЯ, ТО ОПЛАТА НЕ БУДЕТ ПРОВЕДЕНА И ВЫ ПОТЕРЯЕТЕ СВОИ ДЕНЬГИ</b>‼️' ,parse_mode='HTML', reply_markup=keyboard_pay)

    elif call.data == "payment_oge_ok":
        keyboard_pay = types.InlineKeyboardMarkup(row_width=1)
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_pay.add(back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= '<b>Спасибо!❤️‍🔥</b>\nОжидайте пока транзакция подтвердится✅\nБот скоро пришлёт вам сообщение с подтверждением!' ,parse_mode='HTML', reply_markup=keyboard_pay)

# СТРАТЕГИЯ НАЧАЛЬНАЯ - БАЗА ДАННЫХ
@dp.message_handler(commands='330334001360')
async def echo_admin(message: types.Message):
    await message.answer('Выполнен вход в режим администратора для стратегии НАЧАЛЬНАЯ, чтобы выйти пропишите команду /start\n\n')
    await message.answer('Впишите id покупалетя\n\n')
    await FSMAdmin.firstState.set()

@dp.message_handler(state = FSMAdmin.firstState)
async def enterId(message: types.Message, state: FSMContext):
    
    with open("Jet1.json", 'r') as json_file_r:
       mamont_id = json.load(json_file_r)

    try:
        a = int(message.text)
        mamont_id['ids'].append(a)
        await message.answer('ПОКУПАТЕЛЬ ДОБАВЛЕН')
        with open("Jet1.json", 'w') as json_file:
            json.dump(mamont_id, json_file, indent=2)
        await state.finish()
    except:
        await message.answer('Впишите только id мамонта')

@dp.message_handler(commands='361370001380')
async def new_post_fun (message: types.Message):

    if message.from_user.id == {}: #Сюда нужно вставить id администратора

        text = message.text[14:]

        with open("Jet1.json", 'r') as json_file_r:
            mamont_id = json.load(json_file_r)
        for i in mamont_id['ids']:
            try:
                await bot.send_message(chat_id=i, text=text, parse_mode='HTML')
            except:
                continue
   
@dp.message_handler(commands='jsonbase370376')
async def json_base (message: types.Message):

    with open("Jet1.json", 'r') as json_file_r:
        mamont_id = json.load(json_file_r)

    await message.answer('Json-база (начальная) сейчас:' + str(mamont_id))



# СТРАТЕГИЯ ДЕВЯТКА - БАЗА ДАННЫХ
@dp.message_handler(commands='3303340013602')
async def echo_admin(message: types.Message):
    await message.answer('Выполнен вход в режим администратора для стратегии ДЕВЯТКА, чтобы выйти пропишите команду /start\n\n')
    await message.answer('Впишите id покупателя\n\n')
    await FSMAdmin_2.firstState2.set()

@dp.message_handler(state = FSMAdmin_2.firstState2)
async def enterId(message: types.Message, state: FSMContext):
    
    with open("Jet2.json", 'r') as json_file_r:
       mamont_id2 = json.load(json_file_r)

    try:
        a = int(message.text)
        mamont_id2['ids'].append(a)
        await message.answer('ПОКУПАТЕЛЬ ДОБАВЛЕН')
        with open("Jet2.json", 'w') as json_file:
            json.dump(mamont_id2, json_file, indent=2)
        await state.finish()
    except:
        await message.answer('Впишите только id покупателя')

@dp.message_handler(commands='3613700013802')
async def new_post_fun (message: types.Message):

    if message.from_user.id == {}: #сюда нужно вставить id админа

        text = message.text[14:]

        with open("Jet2.json", 'r') as json_file_r:
            mamont_id2 = json.load(json_file_r)
        for i in mamont_id2['ids']:
            try:
                await bot.send_message(chat_id=i, text=text, parse_mode='HTML')
            except:
                continue
   
@dp.message_handler(commands='jsonbase3703762')
async def json_base (message: types.Message):

    with open("Jet2.json", 'r') as json_file_r:
        mamont_id2 = json.load(json_file_r)

    await message.answer('Json-база(девятка) сейчас:' + str(mamont_id2))

# СТРАТЕГИЯ МАЖОР - БАЗА ДАННЫХ
@dp.message_handler(commands='3303340013603')
async def echo_admin(message: types.Message):
    await message.answer('Выполнен вход в режим администратора для стратегии МАЖОР, чтобы выйти пропишите команду /start\n\n')
    await message.answer('Впишите id покупателя\n\n')
    await FSMAdmin_3.firstState3.set()

@dp.message_handler(state = FSMAdmin_3.firstState3)
async def enterId(message: types.Message, state: FSMContext):
    
    with open("Jet3.json", 'r') as json_file_r:
       mamont_id3 = json.load(json_file_r)

    try:
        a = int(message.text)
        mamont_id3['ids'].append(a)
        await message.answer('ПОКУПАТЕЛЬ ДОБАВЛЕН')
        with open("Jet3.json", 'w') as json_file:
            json.dump(mamont_id3, json_file, indent=2)
        await state.finish()
    except:
        await message.answer('Впишите только id покупателя')

@dp.message_handler(commands='3613700013803')
async def new_post_fun (message: types.Message):

    if message.from_user.id == {}: #Сюда нужно вставить id админа

        text = message.text[14:]

        with open("Jet3.json", 'r') as json_file_r:
            mamont_id3 = json.load(json_file_r)
        for i in mamont_id3['ids']:
            try:
                await bot.send_message(chat_id=i, text=text, parse_mode='HTML')
            except:
                continue
   
@dp.message_handler(commands='jsonbase3703763')
async def json_base (message: types.Message):

    with open("mamontsJet3.json", 'r') as json_file_r:
        mamont_id3 = json.load(json_file_r)

    await message.answer('Json-база (мажор) сейчас:' + str(mamont_id3))

# СТРАТЕГИЯ ВСЁ - БАЗА ДАННЫХ
@dp.message_handler(commands='3303340013604')
async def echo_admin(message: types.Message):
    await message.answer('Выполнен вход в режим администратора для стратегии ВСЁ, чтобы выйти пропишите команду /start\n\n')
    await message.answer('Впишите id покупателя\n\n')
    await FSMAdmin_4.firstState4.set()

@dp.message_handler(state = FSMAdmin_4.firstState4)
async def enterId(message: types.Message, state: FSMContext):
    
    with open("Jet4.json", 'r') as json_file_r:
       mamont_id4 = json.load(json_file_r)

    try:
        a = int(message.text)
        mamont_id4['ids'].append(a)
        await message.answer('ПОКУПАТЕЛЬ ДОБАВЛЕН')
        with open("Jet4.json", 'w') as json_file:
            json.dump(mamont_id4, json_file, indent=2)
        await state.finish()
    except:
        await message.answer('Впишите только id покупателя')

@dp.message_handler(commands='3613700013804')
async def new_post_fun (message: types.Message):

    if message.from_user.id == {}: #Сюда нужно встваить id админа

        text = message.text[14:]

        with open("Jet4.json", 'r') as json_file_r:
            mamont_id4 = json.load(json_file_r)
        for i in mamont_id4['ids']:
            try:
                await bot.send_message(chat_id=i, text=text, parse_mode='HTML')
            except:
                continue
   
@dp.message_handler(commands='jsonbase3703764')
async def json_base (message: types.Message):

    with open("Jet4.json", 'r') as json_file_r:
        mamont_id4 = json.load(json_file_r)

    await message.answer('Json-база (всё) сейчас:' + str(mamont_id4))

executor.start_polling(dp, skip_updates=True)
