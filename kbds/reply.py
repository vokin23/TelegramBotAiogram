from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Начать рабочий день'),
            KeyboardButton(text='Мой график'),
        ],
        [
            KeyboardButton(text='Статистика'),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите одно из полей в клавиатуре!'
)

del_kbd = ReplyKeyboardRemove()


# start_kb_main = ReplyKeyboardBuilder()
# start_kb_main.add(
#     KeyboardButton(text='Начать рабочий день'),
#     KeyboardButton(text='Мой график'),
#     KeyboardButton(text='Статистика')
# )
# start_kb_main.adjust(2, 1)


# start_kb3 = ReplyKeyboardBuilder()
# start_kb3.attach(start_kb2)
# start_kb3.add(KeyboardButton(text='Добавляем в start_kb2 новую кнопку!'))
# start_kb3.adjust(2, 2)
