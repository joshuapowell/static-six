# StaticVI (Static Six)

A flexible, Python based static site generator to assist in your site building
and application prototyping projects.

## Getting setup for the first time

Before you get started using StaticVI you should create a duplicate of the
repository, not a fork. [See Github's instructions on duplicating a repository](https://help.github.com/articles/duplicating-a-repository)

### Installing a Virtual Environment

To get started using StaticVI you'll need to ensure that a few things are
installed on your machine.

1. We'll install a Virtual Environment so that the things we do, don't affect
your system.
```
    virtualenv venv
```
2. Once completed installing you can start the virtual environment.
```
    source venv/bin/activate
```
3. Now that our virtual environment is started we can install our requirements.
```
    pip install -r requirements.txt
```
4. Start up the local server
```
    python runserver.py --environment="development"
```
5. Or Build the static site
```
    python runserver.py --environment="build"
```
