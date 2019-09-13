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
      cd /vagrant

      # Initialising django project and app as per tutorial here: https://docs.djangoproject.com/en/2.2/intro/tutorial01/
      # After initialising, copy an updated settings file, sample view and a sample URL mapping into the sample app 
      # named 'polls'. Each project has its own settings file
      # The result is all in git so we can comment this out now
      # sudo django-admin startproject pycon
      # cd pycon
      # sudo python3 manage.py startapp polls
      # sudo cp /vagrant/devang-contrib/polls/settings.py ./polls/
      # sudo cp /vagrant/devang-contrib/polls/views.py ./polls/
      # sudo cp /vagrant/devang-contrib/polls/urls.py ./polls/
      # sudo cp /vagrant/devang-contrib/pycon/urls.py ./pycon/

      # As per tuturial part 2, follow this up by changing the database to postgres, already changed in settings file
      # in pycon/pycon/settings.py in git so we won't do this here
      # But we will create a role named vagrant which will be the superuser and we will use this user for the workshop
      # And we will also create the database named vagrant to match this user's name
      # This is all we need to put in the settings.py file to connect for this dev database
      sudo -u postgres createuser --superuser vagrant
      sudo -u vagrant createdb vagrant
      sudo -u vagrant psql -c "ALTER USER vagrant PASSWORD 'vagrant'"

      # apply initial migrations for the apps admin, auth, contenttypes, sessions after database setup
      cd /vagrant/pycon
      sudo python3 manage.py migrate

      # If migrations are successful, you should be able to access the admin app after starting the debugger or 
      # doing using runserver like 'python3 manage.py runserver 0.0.0.0:8000' : http://192.168.33.10:8000/admin/
      # and our sample polls app is available here: http://192.168.33.10:8000/polls/
  SHELL
end
