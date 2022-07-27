# Django Haystack + Elasticsearch + Autocomplete + Faceting Tutorial

Code accompanying Django Haystack + Elasticsearch + Autocomplete + Faceting Demo

![Django Haystack + Elasticsearch + Autocomplete + Faceting Tutorial](/searchdemo.png?raw=true "")




### Installation

1) Download and Unzip the files

2) Install Elasticsearch and start the server. 

3) create a virtualenv
    
    virtualenv venv

4) Install dependencies
    
    pip install -r requirements.txt

5) Run following Django commands:

    python manage.py makemigrations
    python manage.py migrate
    python manage.py rebuild_index
    python manage.py runserver

6) Visit home page 127.0.0.1:8000  and try out some searches.
