from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('⬅️ Главное меню')

# Main Menu
btnTest = KeyboardButton('📝 Посмотреть активные тесты')
btnTop = KeyboardButton('📈 Посмотреть рейтинг')
btnCode = KeyboardButton('♦️ Ввести код')
btnInfo = KeyboardButton('✉ Наши соцсети')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTest, btnTop, btnCode, btnInfo)

# Tests
btnFirst = KeyboardButton('🎄 Новогодний хакатон')
btnSecond = KeyboardButton('🍲 Beautiful Soup')
testsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFirst, btnSecond, btnMain)

# Tests 2
btnTg = KeyboardButton('📨 Телеграмм')
btnVk = KeyboardButton('👥 Вконтакте')
btnInst = KeyboardButton('📸 Инстаграмм')
tests2Menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTg, btnVk, btnInst, btnMain)
