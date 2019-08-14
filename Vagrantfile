# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-18.04"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.provider "virtualbox" do |v|
        v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
        v.memory = 4096
        v.cpus = 4
  end
  config.vm.provision "shell", inline: <<-SHELL
      echo I am provisioning...
      date > /etc/vagrant_provisioned_at
      sudo apt-get -y update
      sudo apt-get -y install python3 python3-pip postgresql-10 libpq-dev
      sudo pip3 install psycopg2 django markdown django-filter djangorestframework

      # Initialising django project and app as per tutorial here: https://docs.djangoproject.com/en/2.2/intro/tutorial01/
      # After initialising, copy a sample view and a sample URL mapping into the sample app named 'polls'
      # The result is all in git so we can comment this out now
      cd /vagrant
      # sudo django-admin startproject pycon
      # cd pycon
      # sudo python3 manage.py startapp polls
      # sudo cp /vagrant/contrib/polls/views.py ./polls/
      # sudo cp /vagrant/contrib/polls/urls.py ./polls/
      # sudo cp /vagrant/contrib/pycon/urls.py ./pycon/


  SHELL
end
