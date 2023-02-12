from flet import *
from ..widgets.color_picker import ColorPicker
import flet



BuiltIn_Widgets = {
    "Text" : {
        "class" : flet.Text,
        "icon" : "TEXT_FIELDS_ROUNDED",
        "properties" : {
            "value" : str,
            "color" : ColorPicker,
            "bgcolor" : ColorPicker,
            "size" : int,
            "visible" : bool,
            "disabled" : bool,
            "expand" : bool
        },
        "multi_select-prop" : {
            "text_align" : ["LEFT", "RIGHT", "CENTER", "JUSTIFY", "START", "END"]
        }
    },
    "TextButton" : {
        "class" : flet.TextButton,
        "icon" : "RECTANGLE_OUTLINED",
        "on_click_support" : "on_click",
        "properties" : {
            "text" : str,
            "icon" : str,
            "icon_color" : ColorPicker,
            "tooltip" : str,
            "visible" : bool,
            "disabled" : bool,
            "expand" : bool
        }
    },
    "Icon" : {
        "class" : flet.Icon,
        "icon" : "EMOJI_FLAGS_OUTLINED",
        "properties" : {
            "name" : str,
            "color" : ColorPicker,
            "size" : int,
            "tooltip" : str
        }
    },
    "ProgressRing" : {
        "class" : flet.ProgressRing,
        "icon" : "DOWNLOADING_OUTLINED",
        "properties" : {
            "tooltip" : str,
            "value" : int,
            "stroke_width" : int,
            "color" : ColorPicker,
            "bgcolor" : ColorPicker
        }
    },
    "Checkbox" : {
        "class" : flet.Checkbox,
        "icon" : "CHECK_BOX_OUTLINED",
        "on_click_support" : "on_change",
        "properties" : {
            "label" : str,
            "tristate" : bool,
            "value" : bool,
            "check_color" : ColorPicker
        }
    },
    "Slider" : {
        "class" : flet.Slider,
        "icon" : "CABLE_OUTLINED",
        "on_click_support" : "on_change",
        "properties" : {
            "label" : str,
            "value" : int,
            "max" : int,
            "min" : int,
            "divisions" : int,
            "active_color" : ColorPicker,
            "thumb_color" : ColorPicker,
            "autofocus" : bool,
            "divisions" : bool
        }
    },
    "Switch" : {
        "class" : flet.Switch,
        "icon" : "CHECK_CIRCLE_OUTLINE",
        "on_click_support" : "on_change",
        "properties" : {
            "label" : str,
            "value" : int,
            "autofocus" : bool,
            "active_color" : ColorPicker,
            "active_track_color" : ColorPicker,
            "inactive_track_color" : ColorPicker,
            "thumb_color" : ColorPicker,
            "track_color" : ColorPicker
        }
    },
    "TextField" : {
        "class" : flet.TextField,
        "icon" : "INPUT_OUTLINED",
        "on_click_support" : "on_submit",
        "properties" : {
            "value" : str,
            "label" : str,
            "can_reveal_password" : bool,
            "filled" : bool,
            "bgcolor" : ColorPicker,
            "color" : ColorPicker,
            "width" : int,
            "height" : int
        }
    }
}