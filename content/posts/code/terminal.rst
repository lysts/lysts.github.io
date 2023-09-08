===========================================
my current set-up, for a reductive workflow
===========================================

:date: 2023-07-11 18:06
:tags: compsci, terminal, vim, ranger
:category: compsci, workflow
:slugs: terminal-centric-setup
:summary: tools revolving around terminal for reductive workflow
:lang: en
:status: published

.. |ex| replace:: example:

.. contents:: Table of Contents
    :depth: 2
    :backlinks: entry

Tools I use and how I've configured them to provide simplicity to my reductive
workflow.

iTerm2, my CLI (command-line interface)
---------------------------------------
**CLIs** allow users to give text-based inputs (command lines) to interact with a computer's
operating system and perform operations or automate processes.

With a simple command such as ``mkdir (filename)``, you're able to create
files (|ex| ``mkdir``), rather than clicking through folders
with your cursor with a **GUI** (graphical user interface).

As a macOS user, I constantly search for tools that can bring me more
customisability (Apple is famous for being stubbornly unsupportive that kind of self-autonomy).

Inevitably, I tried the pre-installed ``Mac Terminal``. To no surprise, the lackness of 
helpful features became a hindrance — there was just zero flow. I had to utilise ``tmux``, 
an open-source terminal multiplexer that allows you to acces multiple sessions in a single window. 

I then stumbled across ``iTerm2``, a terminal emulator for macOS, and *oh boy*!
* It is highly customisable, beyond themes and formatting. I personally enjoy 
the *Zenbones Dark* theme:)
* Robust support for a multitude of third-party plugins and extensions, which I will detail later.
* Even without plugins, it allows you to divide the windows horizontally or
vertically with ``^+cmd+D`` and ``cmd+D``, and can toggle any pane to full screen and
back with ``^+cmd+enter``. To move between panes, ``alt+cmd`` and arrowkeys.
Moving between tabs require ``cmd`` and 1, 2, or 9. Similarly, moving through
windows require ``atl+cmd`` and the same numbers. 
* As such, there are a multitude of useful key bindings such as ``cmd+F`` like
on browser! They are easily accessed via *Preferences > Keys > Key Bindings*.

I use ``zsh`` (Z shell) and ``Bash`` (Bourne Again Shell) as my command-line shells.
I, however, avoid ``Oh My Zsh``, a popular framework used with ``zsh`` for a number of reasons:
1. my philosophy is to figure out what I need and to use it
well vs installing things that I need to understand when I may or may not use it
2. it takes up a LOT of space.
Which brings me to the next section, where I detail how I manage my additional software, plugins, and text-editors...

More Key Software
*****************

.. _vim:

vim (Vi IMproved), my text-editor
---------------------------------

``Vim`` is a lifesaving screen-based text editor program — free and open-source as
usual. Built-in tutorial, ``vimtutor`` helps you pick up all the key bindings
and shortcuts that allow you to edit code at lightning speed. It goes beyond
editing, it also allows navigation between different files, and ``:help`` is
always available for when you forget. See vim modes for more usage deets!

For example, to copy/paste in different instances of vim, ``"+y`` yanks to the
system clipboard rather than the vim clipboard, which is done simply by ``y``.

There is a native third-party package loading system that has been implemented
with vim, which I prefer rather than using ``Pathogen`` and ``vundle`` or other popular Vim 
plugin managers. Packages are recognised under ``~/.vim/pack`` and can be downloaded separately 
and unpacked in its own directory, making package/plugin additions, removals, and updates easy. 

Plugins under ``~/.vim/pack/*/start/{name}`` are autoloaded on startup, and
``~/.vim/pack/*/opt/{name}`` are loaded manuanlly with ``:packadd {name}``. I
use the ``start`` folder only, and separate my plugins into **ftplugin** for plugins specific 
to programming languages and **plugin** for ``.vimrc`` configuration.

.. _ranger:

ranger, my file navigator
-------------------------

Sometimes, you miss being able to see all of your files at a glance, and the
hierarchy they reside in. This is where ``Ranger`` comes in, a terminal-based
file manager application that allows users to browse and navigate with a dual-pane layout for 
file management, with a directory tree view, allowing file previews, operations (copy, move, delete).

extra tip!
----------

type ``tree`` and see what you get;)
