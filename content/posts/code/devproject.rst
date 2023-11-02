####################
my dashboard project
####################

:date: 2023-10-10 20:00
:tags: software, compsci
:slug: my-dashboard-project
:summary: dashboard project to practice my programming skills and understanding of compsci
:lang: en
:status: hidden


.. |ex| replace:: example:

.. contents:: Table of Contents
    :depth: 2
    :backlinks: entry


Custom Dashboard Application
----------------------------

Aim = To create a desktop application that opens a dashboard with a spotify controller, audiovisualiser, email pane/articles pane, and a terminal pane. 

I always open the same applications every day, so may be worth having it all in one place, one window. It does sound very much like a window manager or a linux ricing set-up but I wanted to code something from scratch.

The frameworks I considered for desktop application development were either purely Python focused or Javascript-based. I decided to take this opportunity to learn ``Electron`` and Javascript, as I am interested in Typescript. 

Setting up Electron in my terminal
----------------------------------

I basically followed the Electron quickstart documentation, but didn't use Fiddle. At the top level, I have my ``main.js`` file which contains the commands for the Browser window, 
