from aiogram import Router

from scr.dialogs.qa_menu_dialog import qa_menu_dialog

qa_menu_dialog_router = Router()

qa_menu_dialog_router.include_router(qa_menu_dialog)
