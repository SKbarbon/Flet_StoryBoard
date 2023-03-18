# Flet StoryBoard
Flet StoryBoard is a python library that have an easy to use tools for building graphical interfaces based on python `flet` library. Powerful interfaces with simple usability.
You can use these tools with only two main and simple functions!

## Goal 🏁
My goal is to allow programmers to focus on the back-end, and build the front-end using just a simple easy-to-use window without any front-end coding require.

## installation ⬇️
For install:
> `pip install Flet-StoryBoard`

for Upgrade:
> `pip install Flet-StoryBoard --upgrade`

if there was anything wrong, and its not upgrading properly, you should uninstall this package and reinstall it:
> `pip uninstall Flet_StoryBoard` To uninstall

## requirements ❗️
- `flet` python library -it will auto install it if you dont have it-.
- up than python3.7

## whats new on `Flet_StoryBoard` `0.2` 🎉
- Redesign the editor.
- We done a major update to the way you create a storyboard, just to make it even more simple to use.
- Major bug fixes and ui fix.
- Support Row & Collumn.
- Support Row-Collumn's sub-controls.
- Support full page building, instead of just a small widgets.
- Support editing the storyboard from the cmd/terminal.
- Big improvment to the preview engine. What you see while edit, its what you will see on the product case.
* if there is any another issues not fixed yet, please create an issue here: [issues page](https://github.com/SKbarbon/Flet_StoryBoard/issues)


## usage 🤝
There is two main cases you can use with Flet_Storyboard. Lets start with the edit case.
### edit case.
To edit an exist storyboard or to create a new one you can use the same cmd command:
* To create a new one:
```cmd
python3 -m Flet_StoryBoard.edit
```
* To edit an exist one:
```cmd
python3 -m Flet_StoryBoard.edit <Your StoryBoard file path>
```

### product case.
To view your storyboard as a `flet` page, you can write this command:
```python
from Flet_StoryBoard import load_flet_storyboard

fsb = load_flet_storyboard("My_File")
fsb.run()
```
Easy right 😇 ?

To link your functions with your buttons or whatever, you can add the functions like this:
```python
from Flet_StoryBoard import load_flet_storyboard

my_functions = {
    "MyFirstFunction" : MyFirstFunction
}

fsb = load_flet_storyboard("My_File", functions=my_functions)
fsb.run()
```
Then inside the editor you can type the function name inside the action field of a control.

## comming soon 🔜
- support more `flet` built-in controls.
- put a pre-templates UIs to make it even more simple and fast for developers to build their own GUIs.
- add custom non-built-in `flet` widgets. like `ColorPicker` and `AudioPlayer` widgets.
- support external-custom widgets from users/programmers.
- Learn/Help page on the editor to help them learing or with solving problems.