from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Format

from scr.dialogs.qa_menu_dialog_states import QaMenuStateGroup

microservices_list = Window(
    Format(
        text="Test"
    ),
    Button(
        id="refresh", text=Format("Обновить"), on_click=None
    ),
    state=QaMenuStateGroup.microservices_list
)

qa_menu_dialog = Dialog(
    microservices_list
)
