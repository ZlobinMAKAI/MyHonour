from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from asyncio import sleep

from loader import dp
from utils.sql_commands import register_user
import handlers.users.makups as nav
from handlers.admin.makups import mainMenu as adminMainMenu
from data.config import ADMINS_ID
from states.user import Read
from utils.sql_commands import add_coin_user, get_user


@dp.message_handler(CommandStart(), state='*')
async def start_bot(message: types.Message, state: FSMContext):
    register_user(message.from_user.id)

    if message.from_user.id in ADMINS_ID:
        await message.answer(
            'Привет, Владелец!', reply_markup=adminMainMenu
        )
        return

    await message.answer(
        'Привет, ты успешно авторизован!', reply_markup=nav.mainMenu
    )


@dp.message_handler(commands=['includeKey'], state='*')
async def readKey(message: types.Message):
    await message.answer("Введите ключ")
    await Read.reading.set()


# IM DOING IT
@dp.message_handler(state=Read.reading, content_types=types.ContentType.TEXT)
async def readKey_on(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=False)
    if types.ContentType.TEXT == message.content_type:
        file = open('qr_code/key.txt', 'r')

        await sleep(1)

        if file.read().strip() == message.text.strip():
            add_coin_user(message.from_user.id, 5)
            await message.answer("Спасибо что сегодня пришли!")
        else:
            await message.answer("Увы... Ключ не тот")

        file.close()

    else:
        await message.answer(
            '<b>❗️ Данный формат контента не поддерживается!</b>'
        )


@dp.message_handler(commands=['menu'])
async def command_menu(message: types.Message):
    await message.answer('Главное Меню', reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == '⬅️ Главное меню':
        await message.answer('⬅️ Главное меню', reply_markup=nav.mainMenu)

    elif message.text == '📈 Посмотреть рейтинг':
        await message.answer(f'Ваш баллы за посещение лекций {get_user(message.from_user.id).coins}')

    elif message.text == '♦️ Ввести код':
        await readKey(message)

    elif message.text == '✉ Наши соцсети':
        await message.answer('✉ Наши соцсети', reply_markup=nav.tests2Menu)

    elif message.text == '📨 Телеграмм':
        await message.answer('Телеграмм - https://t.me/stackers_team')

    elif message.text == '👥 Вконтакте':
        await message.answer('Вконтакте - https://vk.com/stackers.team')

    elif message.text == '📸 Инстаграмм':
        await message.answer('Инстаграмм - https://www.instagram.com/stackers.team/')

    elif message.text == '📝 Посмотреть активные тесты':
        await message.answer('📝 Активные тесты', reply_markup=nav.testsMenu)

    elif message.text == '🎄 Новогодний хакатон':
        await message.answer('🎄 Новогодний хакатон - какой-то тест №1')

    elif message.text == '🍲 Beautiful Soup':
        await message.answer('🍲 Beautiful Soup - какой-то тест №2')

    else:
        await message.reply('Неизвестная команда')
