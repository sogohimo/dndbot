from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()

class CreateCharacter(StatesGroup):
    name = State()
    class_ = State()
    race = State()
    background = State()

@router.message(Command("createcharacter"))
async def create_character_command(message: types.Message, state: FSMContext):
    await message.reply("Введите имя вашего персонажа:")
    await state.set_state(CreateCharacter.name)

@router.message(CreateCharacter.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(CreateCharacter.class_)
    await message.reply("Выберите класс персонажа:")

@router.message(CreateCharacter.class_)
async def process_class(message: types.Message, state: FSMContext):
    await state.update_data(class_=message.text)
    await state.set_state(CreateCharacter.race)
    await message.reply("Введите расу и происхождение:")

@router.message(CreateCharacter.race)
async def process_race(message: types.Message, state: FSMContext):
    await state.update_data(race=message.text)
    await state.set_state(CreateCharacter.background)
    await message.reply("Опишите предысторию персонажа:")

@router.message(CreateCharacter.background)
async def process_background(message: types.Message, state: FSMContext):
    await state.update_data(background=message.text)
    data = await state.get_data()
    await message.reply(f"Персонаж создан!\nИмя: {data['name']}\nКласс: {data['class_']}\nРаса: {data['race']}\nПредыстория: {data['background']}")
    await state.set_state(None)  # Сбрасываем состояние, но сохраняем данные