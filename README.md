# pycon-uk-2019
Setup for Django REST Framework (DRF) workshop using virtualbox, vagrant, python, django, DRF, postgres

## Preparation of environment in advance 
Pre install these to follow the workshop in your own notebook. These tools should work almost identically on win, mac,
linux but my experience is primarily on win.
* postman for REST API testing (https://www.getpostman.com)
* git, preferably original git from git-scm: https://git-scm.com/downloads
* clone this repo: https://github.com/devangmehta123/pycon-uk-2019/
* latest version of virtualbox and vagrant
* latest version of professional pycharm from jetbrains. https://www.jetbrains.com/pycharm/. You can get a free trial
just for the purpose of this workshop. It is useful to have the full debugger support for Django to have a closer look.
* repo comes with pre-configured Vagrantfile. Just cd to project directory and do 'vagrant up' and whole system will be
  set up, including database server. It uses ubuntu bionic and could take some time to be up for the first time, but
  subsequent updates (reprovisions) and boot up should be quicker.

## Notes about virtualbox VM created by vagrant
* Vagrantfile configures it to use 4 CPU cores and 4GB memory. You can change that in Vagrantfile.
* Vagrantfile will create a host-only network on 192.168.33.10 in your notebook. We can use this IP through browser 
and other tools for testing.
* We will do a walk through of the Vagrantfile during the workshop just to have an approximate idea of how it works.

## Presenter's background
* Returned back to active development about 4 years ago.
* Wrote first line of python code in django/DRF to implement biz logic.
* Was more interested (at the time) in implementing biz logic in python in an established database schema and with lots
  of legacy biz logic implemented in wild PHP (no framework).
* Did not use django models (essentially, built-in ORM) initially due to very difficult database schema but beginning to
  use them now.
* Still learning advanced python features like generators, etc.
* No experience with postgresql, only mysql. But postgresql is more natural fit for DRF, hence we use it in this
  workshop.
* Learnt some parts of the framework through practically problem solving, but other specialists were responsible for
  framework and lower level issues. 
* THIS IS BIGGEST ADVANTAGE OF PYTHONIC APPROACH: It lets you be productive immediately without mastering too much
  detail about framework, setup, etc. You can be productive quickly which helps you build momentum and buy-in
  for your solution. 
* Django comes with a rich app eco system where there is a app for almost every plumbing issue that you might encounter
  for a web app. DRF is one of those apps; it lets you plumb a REST API around your biz logic.

## Django setup because DRF depends on Django
Vagrantfile above installs most dependencies. *You do not have to do the below explicitly because it is already done
and put into git by me.*
* A lot of below originates from these docs, https://docs.djangoproject.com/en/2.2/topics/install/ and 
  https://www.django-rest-framework.org/#installation. But we do not want to spend too much time on them,
  so I have compressed that process.
* ssh into VM (vagrant ssh), cd into /vagrant which is shared folder with host OS and git, then do 
  'django-admin startproject pycon' which will initialize project pycon. More details about what happens are here:
  https://docs.djangoproject.com/en/2.2/intro/tutorial01/, *but on ubuntu, just be careful about the python binary
  that you use. By default, python is version 2.x but we want to use 3.x. So, always use python3 and you will be 
  fine.*
* dev server is started like this: cd /vagrant/pycon (note that /vagrant/ is a shared folder between your VM and 
  your project in host OS) and then 'python3 manage.py runserver 0.0.0.0:8000'. More info about how this site works
  is here: https://docs.djangoproject.com/en/2.2/ref/contrib/admin/. We have to set the login/password manually here; 
  can't do it through Vagrantfile because the command will not take a password input: python3 manage.py createsuperuser 
* setting up debugger inside pycharm will help to see what is happening and the debugger typically runs the same
  dev server as above. Pycharm professional has a very useful feature for using remote interpreter inside vagrant VM
  (and more recently, inside docker containers). We will go through remote interpreter setup and debugger
  configuration during workshop.
* We can play around with the django shell like this, 'python3 manage.py shell' where the full django environment
  is available to you in a shell. That's very powerful, anything you can do in a web view, you can do here to see how it
  behaves.
     