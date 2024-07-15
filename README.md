
<p align="center">
  <img src="https://raw.githubusercontent.com/eivl/amdreader/6f27ff68b130ea43303a7a8a90cc07776e446cd8/amd-logo.png"  width="600" align="center"/>
</p>


# AMD Reader


AMD reader is a Markdown viewer / browser for your terminal, built with [Textual](https://github.com/Textualize/textual).
It is a hard fork from Textualize and all credits goes to their work. This derived work adds custom features and improvements.
amd can open `*.md` files locally or via a URL.
There is a familiar browser-like navigation stack, history, bookmarks, and table of contents.


## Compatibility

amd runs on Linux, macOS, and Windows. amd requires Python **3.8** or above.


## Installing

The easiest way to install amd is with [pipx](https://pypa.github.io/pipx/) (particularly if you aren't a Python developer).

```
pipx install amdreader
```

You can also install amd with `pip`:

```
pip install amdreader
```

Whichever method you use, you should have a `amd` command on your path.

## Running

Enter `amd` at the prompt to run the app, optionally followed by a path to a Markdown file:

```
amd README.md
```

You can navigate with the mouse or the keyboard.
Use <kbd>tab</kbd> and <kbd>shift</kbd>+<kbd>tab</kbd> to navigate between the various controls on screen.

## Features

You can load README files direct from GitHub repositories with the `gh` command.
Use the following syntax:

```
amd gh textualize/textual
```

This also works with the address bar in the app.
See the help (<kbd>F1</kbd>) in the app for details.
