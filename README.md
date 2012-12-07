Zenoss Dashboard
----------------

A (work in progress) clutter free dashboard for viewing events from Zenoss 3.x

### Getting started ###

Clone repo, create a virtualenv and install dependencies

    $ git clone git@github.com:morphizer/zendash.git zendash
    $ cd zendash
    $ virtualenv dashboard-env
    $ source ./dashboard-env/bin/activate
    $ pip install -r requirements.txt

### Using South for db migrations ###

Bit overkill as it's only storing a few config options, but:

* When creating a new app

        $ python manage.py startapp newapp
        $ python manage.py schemamigration newapp --initial
        $ python manage.py migrate newapp

* After making changes to the model

        $ python manage.py schemamigration dashboard --auto

* Run the migration

        $ python manage.py migrate dashboard
