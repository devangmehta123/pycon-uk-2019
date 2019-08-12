# pycon-uk-2019
Setup for Django REST Framework (DRF) workshop using virtualbox, vagrant, python, django, DRF, postgres

## Pre install these to follow the workshop in your own notebook, it should work on win, mac, linux but my experience is primarily on win
* git, preferably original git from git-scm: https://git-scm.com/downloads
* clone this repo: https://github.com/devangmehta123/pycon-uk-2019/
* latest version of virtualbox and vagrant
* lastest version of the free community pycharm from jetbrains. https://www.jetbrains.com/pycharm/
* repo comes with pre-configured Vagrantfile. Just cd to project directory and do 'vagrant up' and whole system will be
 set up, including database server. It uses ubuntu bionic and could take
some time to be up for the first time, but subsquent updates (reprovisions) and boot up should be quicker.

## Notes about virtualbox VM created by vagrant
* Vagrantfile configures it to use 4 CPU cores and 4GB memory. You can change that in Vagrantfile.
* Vagrantfile will create a host-only network on 192.168.33.10 in your notebook. We can use this IP through browser 
and other tools for testing.

## Presenter's background
* Returned back to active development about 3 years ago.
* Wrote first line of python code in Django/DRF to implement biz logic.
* More interested in implementing biz logic in python in an established database schema and with lots of legacy biz
logic implemented in wild PHP (no framework).
* Learnt some parts of the framework through practically problem solving, but other specialists were responsible for
setting up framework, etc. 
* THIS IS BIGGEST ADVANTAGE OF PYTHONIC APPROACH: It lets you be productive immediately without mastering too much
detail about framework, setup, etc. *You only need to know what is practical and useful.*

## Django setup because DRF depends on Django
* Vagrantfile above installs most dependencies but Django project has to be initialized
    * ssh into VM (vagrant ssh), cd into /vagrant which is shared folder with host OS and git, then do 
    'django-admin startproject pycon' which will initialize project pycon. More details about what happens are here:
    https://docs.djangoproject.com/en/2.2/intro/tutorial01/, *but on ubuntu, just be careful about which python you
    use. By default, python is version 2.x but we want to use 3.x. So, always use python3 and you will be fine.*
    * dev server is started like this: cd /vagrant/pycon; python3 manage.py runserver
     