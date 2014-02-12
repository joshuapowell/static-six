CommonsCloudStatic
==================

A minimal static site generator to get you started building sites with the CommonsCloud's API



## Getting setup for the first time

Before you get started using the CommonsCloud Static Site Generator you should create a duplicate of the repository, not a fork. [See Github's instructions on duplicating a repository](https://help.github.com/articles/duplicating-a-repository)

Then after you've got the repository cloned to your machine you can change to your project directory and run

    bash setup.sh
    
Wait for the installation to walk through all of the steps outlined below, then you can start the server

    python start.py

## The Long Version of getting setup

To get started using the CommonsCloud Static Site Generator you'll need to ensure that a few things are installed on your machine.

1. We'll install a Virtual Enviornment so that the things we do, don't affect your system

    virtualenv venv
    
2. Once completed installing you can start the virtual enviornment

    source venv/bin/activate
    
3. Now that our virtual enviornment is started we can install our requirements

    pip install -r requirements.txt

4. Once our requirements are installed, we need to patch one of the packages to work according to our liking, so first we deactivate the Virtual Environment temporarily

    deactivate

    cd venv/lib/python2.7/site-packages/flask_flatpages/

    patch < ../../../../../patch/__init__.patch

5. Finally we can change back to the project root and restart our virtual enviornment 

    cd ../../../../..
    source venv/bin/activate
    
6. Start up the local server
    
    python start.py
