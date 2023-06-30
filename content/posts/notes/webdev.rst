==========================================
building this website — a series of firsts
==========================================

:date: 2023-06-30 04:58
:tags: css, html, github
:category: webdev
:slug: building-this-website
:summary: web-building with pelican, css, and html
:lang: en
.. |gh| replace:: GitHub
.. |cr| unicode:: 0xA9 .. copyright sign

This is my first webdev project. 

birthing this love child
========================

After galavanting across webrings, bookmarked websites, and premade jekyll themes, I decided to prioritise the following in regards to the creation of this website:

1. incredibly minimal, but not devoid of life.
2. create from scratch.
3. easy content building & publishing.

In part due to my disatisfaciton with existing templates, I took inspiration from basic "no-theme" themes and the classic terminal-like feel, hence the backslashes, monospace font, and some format- and favicon-dependent "personal-branding". 

But before I was able to address such goals, I was met with a number of challenges:

* beyond foetal with anything webdev (how websites work, css & html syntax, etc..)
* a learning curve = a need for time-efficiency

My journey kickstarted with the purchase of a domain name which I then linked to a |gh| Pages repo to set up my first foundational html and css files. Learning approrpiate syntax consisted of simultaneously relying on documentation guidlines and ``view page source`` or ``inspect`` browser tools to pinpoint features that intrigued me and practice tweak existing code to get a feel of what I wanted to add to my tabula rasa. These tools came in handy later down the road, on my own website, when testing different formats to achieve my desired layout or identifying any errors in css selections. 

setting up my workflow
======================

Half my time was spent understanding the workings of web-hosting and setting up a static site generator with some personal customisations. I chose to install ``Pelican``, despite the popularity of Jekyll (which |gh| Actions also uses by default). I fancied the idea of fast rebuild times and easily accessible web-hosting, being able to easily implement my original html and css attempts, and having the freedom to publish articles in other languages. 

Thankfully, such features were readily available with Pelican. Upon stripping default files and scripts from its working pathway, I better understood the dependencies and configuration settings required to ensure the compatibility of my original files with engine. I learned of the ease and elegance of Pelican in executing test runs of my scripts from terminal, after tediously git committing small changes via |gh| Pages and developing an addiction to the slow emergence of green ticks when repeatedly abusing |gh| Actions. reat blog-style content in a high-level file format such as ``ReStructuredText``. 



If you're also picking up ``html`` and ``css`` for the first time, setting up an open source static site generator like Pelican in your terminal will help you create a development server in your local browser to swiftly see immediate changes within seconds. This immensely accelerated my on-the-go learning.



I'm currently working on automatically deploying my Pelican-based webdev project to |gh| Pages with |gh| Actions.

.. contents:: Table of Contents
   :depth: 2
   :backlinks: "entry"
   





