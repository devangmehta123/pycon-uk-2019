# pycon-uk-2019
Setup for Django REST Framework (DRF) workshop using virtualbox, vagrant, python, django, DRF, postgres

## Pre install these to follow the workshop in your own notebook, it should work on win, mac, linux but my experience is primarily on win
* git, preferably original git from git-scm: https://git-scm.com/downloads
* clone this repo: https://github.com/devangmehta123/pycon-uk-2019/
* latest version of virtualbox and vagrant
* lastest version of the free community pycharm from jetbrains. https://www.jetbrains.com/pycharm/
* repo comes with pre-configured Vagrantfile. Just cd to project directory and do 'vagrant up' and whole system will be set up, including database server. It uses ubuntu bionic and could take
some time to be up for the first time, but subsquent updates (reprovisions) and boot up should be quicker.

## Notes about virtualbox VM created by vagrant
* Vagrantfile configures it to use 4 CPU cores and 4GB memory. You can change that in Vagrntfile.
* Vagrantfile will create a host-only network on 192.168.33.10 in your notebook. We can use this IP through browswer 
and other tools for testing.


