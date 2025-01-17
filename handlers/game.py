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
    quest = groq_generate(f"Создай начальный квест для группы. Сюжет: {plot}.")
    await message.reply(f"Ваш первый квест:\n{quest}")

@router.message(Command("action"))
async def handle_action(message: types.Message):
    # Обработка действий игроков
    action = message.text
    response = groq_generate(f"Опиши, что происходит, когда игрок делает следующее: {action}.")
    await message.reply(response)