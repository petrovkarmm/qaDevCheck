from aiogram import F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_dialog import DialogManager

from scr.dialogs.qa_menu_dialog_states import QaMenuStateGroup

from aiogram import Router

start_router = Router()



@start_router.message(F.text)
async def start_qa_menu_dialog_with_text(
        message: Message, state: FSMContext, dialog_manager: DialogManager
):
    await dialog_manager.start(
        QaMenuStateGroup.microservices_list
    )


@start_router.message(Command("start"))
async def start_qa_menu_dialog_with_command(
        message: Message, state: FSMContext, dialog_manager: DialogManager
):
    await dialog_manager.start(
        QaMenuStateGroup.microservices_list
    )
