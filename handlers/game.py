from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from utils.groq import groq_generate

router = Router()

@router.message(Command("startgame"))
async def start_game_command(message: types.Message, state: FSMContext):
    data = await state.get_data()
    plot = data.get("plot", "без сюжета")
    await message.reply(f"Игра началась! Сюжет: {plot}. Больше никто не может присоединиться.")

    # Генерация начального квеста
    quest_prompt = f"Создай начальный квест для группы. Сюжет: {plot}."
    quest = groq_generate(quest_prompt)
    await message.reply(f"Ваш первый квест:\n{quest}")

@router.message(Command("action"))
async def handle_action(message: types.Message, state: FSMContext):
    # Получаем текущий сюжет из состояния
    data = await state.get_data()
    plot = data.get("plot", "без сюжета")

    # Генерация ответа на действие игрока
    action = message.text
    response_prompt = f"Опиши, что происходит, когда игрок делает следующее: {action}. Сюжет: {plot}."
    response = groq_generate(response_prompt)
    await message.reply(response)

# Обработчик для текстовых сообщений (например, "Да! Поехали")
@router.message()
async def handle_text(message: types.Message, state: FSMContext):
    # Получаем текущий сюжет из состояния
    data = await state.get_data()
    plot = data.get("plot", "без сюжета")

    # Генерация ответа на текст пользователя
    user_text = message.text
    response_prompt = f"Опиши, что происходит, когда игрок говорит: {user_text}. Сюжет: {plot}."
    response = groq_generate(response_prompt)
    await message.reply(response)