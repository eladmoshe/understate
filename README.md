understate
==========
[![Build Status](https://travis-ci.org/L3V3L9/understate.png)](https://travis-ci.org/L3V3L9/understate)

Make stunning terminal presentations using markdown and some ncurses magic.

Understate presents regular markdown file as beautifully designed presentation that runs in your terminal window.

Highlights:

* Terminal application, no GUI whatsoever
* Uses standard markdown language syntax, no learning curve
* Syntax highlighting for almost any programming language
* Lightweight and cross platform
* Much faster than Power Point
* Cool animations (will be implemented in version 0.3)

Install
-------

The easiest way is to use pip (or pip2 if your default is python3):
   
    $ pip install understate 

Otherwise, just use:

    $ sudo make install

Usage
-----
   
    $ understate filename.md


Compatibility
-------------

Understate requires python 2.7 and was tested in the following terminals:

* iTerm
* Mac Terminal
* rxvt


Roadmap
-------

- [X] version 0.1 - Basic project structure
- [X] version 0.2 - Limited Markdown Support, Curses Renderer, Forward Navigation
- [ ] version 0.3 - Config File, More Markdown Elements, Simple Transition Effect
- [ ] version 0.4 - Slide Navigation, Status Bar, PIP integration
- [ ] version 0.5 - More Transition Options and Effects 
