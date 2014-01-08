CommonsCloudStatic
==================

A minimal static site generator to get you started building sites with the CommonsCloud's API



## Getting setup for the first time

Before you get started using the CommonsCloudStatic site generator you'll need to ensure that a few things are installed on your machine.

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