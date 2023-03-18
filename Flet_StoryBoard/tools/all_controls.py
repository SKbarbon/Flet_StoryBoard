import flet
from ..built_in_widgets.color_picker import colorPicker


def get_all_supported_controls ():
    return all_controls_supported


all_controls_supported = {
    "Text" : {
        "class" : flet.Text,
        "icon" : flet.icons.TEXT_FIELDS_ROUNDED,
        "properties" : {
            "value" : {"type":str, "default":"Hello, world!"},
            "italic" : {"type":bool, "default" : False},
            "selectable" : {"type":bool, "default":False},
            "visible" : {"type":bool, "default":True},
            "expand" : {"type":bool, "default":False},
            "size" : {"type":int, "default":18},
            "weight" : {"type":list, "default":"normal", "selections":["normal", "bold"]},
            "text_align" : {"type":list, "default":"LEFT", "selections":["left", "center", "right"]},
            "color" : {"type":colorPicker, "default":"white"},
            "bgcolor" : {"type":colorPicker, "default":None}
        },
    },
    "TextField" : {
        "class" : flet.TextField,
        "support_functions" : ["on_submit", "on_focus", "on_change"],
        "icon" : flet.icons.INPUT_ROUNDED,
        "properties" : {
            "value" : {"type":str, "default":""},
            "label" : {"type":str, "default":"Input"},
            "autofocus" : {"type":bool, "default":False},
            "expand" : {"type":bool, "default":False},
            "visible" : {"type":bool, "default":True},
            "multiline" : {"type":bool, "default":False},
            "password" : {"type":bool, "default":False},
            "text_size" : {"type":int, "default":15},
            "width" : {"type":int, "default":150},
            "height" : {"type":int, "default":35},
            "border_radius" : {"type":int, "default":8},
            "text_align" : {"type":list, "default":"LEFT", "selections":["LEFT", "RIGHT", "CENTER"]},
            "color" : {"type":colorPicker, "default":"black"},
            "bgcolor" : {"type":colorPicker, "default":"white"}
        }
    },
    "Icon" : {
        "class" : flet.Icon,
        "icon" : flet.icons.ICECREAM_OUTLINED,
        "properties" : {
            "name" : {"type":str, "default":"ICECREAM_OUTLINED"},
            "size" : {"type":int, "default":15},
            "width" : {"type":int, "default":25},
            "height" : {"type":int, "default":25},
            "color" : {"type":colorPicker, "default":"white"},
            "visible" : {"type":bool, "default":True}
        }
    },
    "Image" : {
        "class" : flet.Image,
        "icon" : flet.icons.IMAGE_ROUNDED,
        "properties" : {
            "src" : {"type":str, "default":""},
            "src_base64" : {"type":str, "default":"iVBORw0KGgoAAAANSUhEUgAAABkAAAAgCAYAAADnnNMGAAAACXBIWXMAAAORAAADkQFnq8zdAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAA6dJREFUSImllltoHFUYx3/fzOzm0lt23ZrQ1AQbtBehNpvQohgkBYVo410RwQctNE3Sh0IfiiBoIAjqi6TYrKnFy4O3oiiRavDJFi3mXomIBmOxNZe63ay52GR3Zj4f2sTEzmx3m//TYf7/c35zvgPnO6KqrESXqpq3muocAikv6m+/zytj3ejik1VN21G31YA9CgJ6xC+bMyQZPVCuarciPAMYC99V6Vw5pLbFSibHmlVoRVj9P3cmPBM8tSJI/M6mzabpfoAQ9fIF7WK4bd5vvuFnLGgy2vi0abg94A0AcJGvMq3hDxGRyar9r4F+iLAm0yIiRk8m37tctS1WsrIhhrI30+Srmg+J87OXUf3lWGS1q89dC6ltsSanxk4Aj2QBABii96300g87P/rtlrWr8l+vyDMfdlXSyyEikqxsiOUAQJCBhfHdXRfCq1LSsSlcWG+KBAGStvvrMkgiuv8lUc2mREukPwLUfHG+uTQv8Eown7VL3XlbBxYhf1c17hbVF3MDwA9bts280TnaU1YYqPby07aeFlUlHt27wSQ4CLo+F8AvoTCvHmyKF+ZbEb/M77P2LgvAwmrTHAHflN3KZxVbMC2jMFNOpgPnrMSOhvvFkMezXdwV4ePbtvHtxnJAMQ0j4JtVnO+eLb5oiSlt5HDbv7t1O90lpYCCCKbhfzW5kAIwUAazR0BlfII8Ow0I6uoVmI9MyAMwbMs8CExmDbk4zgu931MyO4OI4KrYflkRjOoTI+uM9d1vjotwKPu9QMk/sxzuO8POiVFcdZ1M2YBVsMEAKOqLvaPIe7mACuw0z/80SMH58SMplxlfiDhVi7dw2pltRhjKBQTQdrSja2KKTfE551NHuaZ0QVPvWYQUn31/Vm2nDvgjF4grVJx6suSvrvrSJ/6cSW2Oz9mf264uNrB806xZ1k/CZ49dUKgDEtlCROX2hfHpx8pGuuo3PpqYulw8fjndOp1yhgtNKRevJ1FyR2Ola+jXAjdnwTkZ6o896GdWdxDw7IxFg+0DpmXchTKSBWQnIuJn9u4j7dt+13UfHXEkXQOcuQ4kMhVtqsgUyPiQiPQfHw1NB2sRjmXKuTg1NwwBYLhtPtQX26eqTwGXPDOqvmcC4Hnwfrrad94GrVsOYTqUTkQY+iTlNe/6O1miSP/x0VB/+wMIDwHn/vtV1iQC4Xv95uUEWVCoL9Y5Z+gdovoyMHUFJHv88jmVy0vTuw7cZNv2YaA61Bfb7ZX5F8SaUv2xwZevAAAAAElFTkSuQmCC"},
            "tooltip" : {"type":str, "default":""},
            "width" : {"type":int, "default":150},
            "height" : {"type":int, "default":150},
            "visible" : {"type":bool, "default":True}
        }
    },
    "CircleAvatar" : {
        "class" : flet.CircleAvatar,
        "icon" : flet.icons.PERSON,
        "properties" : {
            "background_image_url" : {"type":str, "default":"https://picsum.photos/id/237/200/300"},
            "tooltip" : {"type":str, "default":""},
            "width" : {"type":int, "default":100},
            "height" : {"type":int, "default":100},
            "visible" : {"type":bool, "default":True}
        }
    },
    "TextButton" : {
        "class" : flet.TextButton,
        "icon" : flet.icons.SMART_BUTTON,
        "support_functions" : ["on_click", "on_hover", "on_long_press"],
        "properties" : {
            "text" : {"type":str, "default":"click me!"},
            "tooltip" : {"type":str, "default":""},
            "autofocus" : {"type":bool, "default":False},
            "visible" : {"type":bool, "default":True}
        }
    },
    "Container" : {
        "class" : flet.Container,
        "icon" : flet.icons.ADD_BOX_ROUNDED,
        "support_functions" : ["on_click", "on_hover", "on_long_press"],
        "support_content" : True,
        "properties" : {
            "ink" : {"type":bool, "default":False},
            "expand" : {"type":bool, "default":False},
            "visible" : {"type":bool, "default":True},
            "bgcolor" : {"type":colorPicker, "default":""},
            "width" : {"type":int, "default":150},
            "height" : {"type":int, "default":100},
            "border_radius" : {"type":int, "default":8}
        }
    },
    "Row" : {
        "class" : flet.Row,
        "icon" : flet.icons.TABLE_ROWS_ROUNDED,
        "support_controls" : True,
        "properties" : {
            "alignment" : {"type":list, "default":"START", "selections":["START", "center", "END"]},
            "scroll" : {"type":bool, "default":False},
            "auto_scroll" : {"type":bool, "default":False},
            "tight" : {"type":bool, "default":False},
            "height" : {"type":int, "default":50}
        }
    },
    "Column" : {
        "class" : flet.Column,
        "icon" : flet.icons.LINE_AXIS_OUTLINED,
        "support_controls" : True,
        "properties" : {
            "alignment" : {"type":list, "default":"START", "selections":["START", "center", "END"]},
            "scroll" : {"type":bool, "default":False},
            "auto_scroll" : {"type":bool, "default":False},
            "expand" : {"type":bool, "default":False},
            "tight" : {"type":bool, "default":False},
            "height" : {"type":int, "default":50},
            "width" : {"type":int, "default":100}
        }
    }
}