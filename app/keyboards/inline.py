from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_author_keyboard(owner_id):
    buttons = [
        [InlineKeyboardButton(text="Автор", url=f"tg://user?id={owner_id}")],
    ]
    keyboard = InlineKeyboardBuilder(markup=buttons)
    return keyboard.as_markup()


def wallet_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text="➡️ Перевести", callback_data="pay"),
            InlineKeyboardButton(text="➕ Получить", url="https://t.me/vsecoder"),
        ],
        [InlineKeyboardButton(text="🔄 Обновить", callback_data="refresh")],
    ]
    keyboard = InlineKeyboardBuilder(markup=buttons)
    return keyboard.as_markup()
