from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from utils.groq import groq_generate

router = Router()

class CreateGame(StatesGroup):
    plot = State()

@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.reply("Привет! Это бот для игры в D&D. Напиши /startdnd, чтобы начать игру.")

@router.message(Command("startdnd"))
async def start_dnd_command(message: types.Message, state: FSMContext):
    await message.reply("Введите сюжет игры (например, 'поиск древнего артефакта'):")
    await state.set_state(CreateGame.plot)

@router.message(CreateGame.plot)
async def process_plot(message: types.Message, state: FSMContext):
    await state.update_data(plot=message.text)

    # Генерация расширенного сюжета с помощью ИИ
    plot_prompt = f"Расширь сюжет для игры в D&D: {message.text}."
    expanded_plot = groq_generate(plot_prompt)

    await message.reply(
        f"Сюжет игры:\n{expanded_plot}\n\n"
        f"Теперь создайте персонажа с помощью /createcharacter."
    )
    await state.set_state(None)  # Сбрасываем состояние, но сохраняем данные