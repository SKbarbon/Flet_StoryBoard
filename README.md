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
- `git` -for the installation-. [git install site](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
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
To edit an exist storyboard or to create a new one then edit it, you can use:
```python
from Flet_StoryBoard import edit_flet_storyboard

edit_flet_storyboard("MyStoryBoard")
# This will open a window that will allow you to build your own widget.
# To save the changes click -save- button or cmd+s/ctrl+s to save.
```
On the test or production case you can load the widget that you built on multiple ways, but with just one function to call. here is the explanation:
```python
from Flet_StoryBoard import load_flet_storyboard

def Home(page:flet.Page):
    MyWidget = load_flet_storyboard("my_ui") # returns -> flet.Container
    page.add(MyWidget)

flet.app(target=Home)
# This will add the the widget you built as a Container, then you will be able to edit it as a normal flet control.
```
If you want to use the another short way, you do this:
```python
from Flet_StoryBoard import load_flet_storyboard

def Home(page:flet.Page):
    load_flet_storyboard("my_ui", page)

flet.app(target=Home)
# This will load the widget on the page as a Container.
#* Note: This way will center the contaner on the page by default.
```
To add your functions to work with `on_click`, `on_submit` and other like it, you can do:
On building/editing case:
```python
from Flet_StoryBoard import edit_flet_storyboard

my_functions = {
    "function1" : print,
    "function2" : print
}

edit_flet_storyboard("my_ui", functions=my_functions)
```
On production case:
```python
from Flet_StoryBoard import load_flet_storyboard

my_functions = {
    "function1" : print,
    "function2" : print
}

def Home(page:flet.Page):
    load_flet_storyboard("my_ui", page, functions=my_functions)

flet.app(target=Home)
```

## comming soon 🔜
- support all controls that accept sub-controls/childs like `content` on `Container`, `controls` on `Row` and `Column`.
- add custom non-built-in `flet` widgets. like `ColorPicker` and `AudioPlayer` widgets.
- support external-custom widgets from users/programmers.
