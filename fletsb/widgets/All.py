from .widgets.title import Title
from .widgets.open_url import Open_Url
from .widgets.button import Button
from .widgets.label import Label
from .widgets.markdown import Markdown
from .widgets.paragraph import Paragraph
from .widgets.row import Row
from .widgets.column import Column
from .widgets.image import Image
from .widgets.padding import Padding
from .widgets.textfield import TextField
from .widgets.navigator import Navigator
from .widgets.dropdown import DropDown
from .widgets.filepicker import FilePicker

all_widgets = {
    "Title": {"icon": "TEXT_FIELDS_ROUNDED", "class": Title},
    "TextField": {"icon": "INPUT_ROUNDED", "class": TextField},
    "Open Url": {"icon": "INSERT_LINK_SHARP", "class": Open_Url},
    "Button": {"icon": "SMART_BUTTON_ROUNDED", "class": Button},
    "DropDown": {"icon": "LIST", "class": DropDown},
    "Label": {"icon": "MEDICAL_INFORMATION_OUTLINED", "class": Label},
    "Markdown": {"icon": "TEXT_SNIPPET_ROUNDED", "class": Markdown},
    "Paragraph": {"icon": "SHORT_TEXT_ROUNDED", "class": Paragraph},
    "Row": {"icon": "VIEW_COLUMN_OUTLINED", "class": Row},
    "Column" : {"icon":"TABLE_ROWS_SHARP", "class":Column},
    "Image": {"icon": "IMAGE_OUTLINED", "class": Image},
    "Padding": {"icon": "SPACE_BAR_ROUNDED", "class": Padding},
    "FilePicker": {"icon": "FOLDER", "class": FilePicker},
    "Navigator": {"icon": "NAVIGATE_NEXT", "class": Navigator}
}
