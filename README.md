# Data Visualization Tool

Django project to visualize financial securities data.

Getting Started
---------------

Development setup.

### Prerequisites

* Install Python 3.6
* Install [pip](https://pip.pypa.io/en/stable/installing/)
* Install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)

### Installing

Go to the main path of the project (where manage.py is located) and create a new virtual environment

```
mkvirtualenv <virtualenv_name> [-a <path_to_project>] [-r requirements.txt] [-p "python3.6"]
```

Enter in the virtual environment if you are not inside yet

```
workon <virtualenv_name>
```

Install external libraries if you haven't used [-r requirements.txt] in the previous step

```
pip install -r requirements.txt
```

Execute the project

```
python manage.py runserver --noreload 127.0.0.1:8002
```
