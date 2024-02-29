# Flet StoryBoard
Flet StoryBoard is a python library that have an easy to use tools for building graphical interfaces based on python `flet` library. Powerful interfaces with simple usability. Build the UI with ease of `fletsb`, then connect it with your back-end!

## Goal 🏁
My goal is to allow programmers to focus on the back-end, and build the front-end using just a simple easy-to-use window without any front-end coding require.

## installation ⬇️
- Python > 3.7

You can try Flet_StoryBoard on web!, just click here: [fletsb on web](https://skbarbon.github.io/wfletsb/)

For install:
> `pip install Flet_StoryBoard`

for Upgrade:
> `pip install Flet_StoryBoard --upgrade`

## Little Peek

<img width="1332" alt="Showcase" src="Readme_files/showcase.png">

## What's new on `Flet_StoryBoard` `1.1` 🎉
- New UI revamp.
- Added support for dropdown widget.
- Updated the architecture of the library.
* Please read the docs to know more about library usage. [docs page](https://github.com/SKbarbon/Flet_StoryBoard/wiki)
* if there is any another issues not fixed yet, please create an issue here: [issues page](https://github.com/SKbarbon/Flet_StoryBoard/issues)


## usage & examples 🤝
You can use the editor just from the web!, click here to start:
[fletsb on web](https://x-0d.github.io/wfletsb/) (*Old)

There is a very simple docs here about library usage.
[docs page](https://github.com/SKbarbon/Flet_StoryBoard/wiki)

### create/edit your own StoryBoard
```cmd
python3 -m fletsb.edit myUI.fletsb
```
It will edit the existing one or create a new one if not.

### load a StoryBoard
To load your StoryBoard on your app, you can do this example code:

```python
from fletsb import LoadStoryBoard, StoryBoard

def main (storyBoard:StoryBoard):
    pass

LoadStoryBoard(target_function=main, storyboard_file_path="myUI.fletsb")
```

To know more about the `StoryBoard` class, follow the [docs page](https://github.com/SKbarbon/Flet_StoryBoard/wiki) .