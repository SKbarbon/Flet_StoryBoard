# Flet StoryBoard
Flet StoryBoard is a python library that have an easy to use tools for building graphical interfaces based on python `flet` library. Powerful interfaces with simple usability.
You can use these tools with only two main and simple functions!

## Goal 🏁
My goal is to allow programmers to focus on the back-end, and build the front-end using just a simple easy-to-use window without any front-end coding require.

## installation ⬇️
For install:
> `pip install git+https://github.com/SKbarbon/Flet_StoryBoard.git`

for Upgrade:
> `pip install git+https://github.com/SKbarbon/Flet_StoryBoard.git --upgrade`

if there was anything wrong, and its not upgrading properly, you should uninstall this package and reinstall it:
> `pip uninstall Flet_StoryBoard` To uninstall

## requirements ❗️
- `flet` python library.
- up than python3.7

## whats new on `Flet_StoryBoard` `0.1` 🎉
- support most of built-in `flet` widgets.
- support buttons `on_click`.
- bug fixes and ui fix.
* if there is any another issues not fixed yet, please create an issue here: [issues page](https://github.com/SKbarbon/Flet_StoryBoard/issues)


## usage 🤝
There is just two main easy-to-use functions that you can use to build your-own `flet` widgets.
### How is it work ?
`Flet StoryBoard` creates a file with `.fletsb` format that save all your front-end informations. On the building case you can edit this file using only one function and save all its changes. And on the production case you can load this widget using another easy function and it will return the widget as a `flet` `Container`.
### usage example
To edit an exist storyboard or to create a new then edit, you can use:
```python
from Flet_StoryBoard import edit_flet_storyboard

edit_flet_storyboard("MyStoryBoard")
# This will open a window that will allow you to build your own widget.
# To save the changes click -save- button or cmd+s/ctrl+s to save.
```


## comming soon 🔜
- support all controls that accept sub-controls/childs like `content` on `Container`, `controls` on `Row` and `Column`.
- add custom non-built-in `flet` widgets. like `ColorPicker` and `AudioPlayer` widgets.
- support external-custom widgets from users/programmers.
