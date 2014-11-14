rvagaming-flask
===============

A work-in-progress from-scratch rewrite of github.com/mosbasik/rvagaming using the Flask Python web framework.

# To use this project:

* Make sure you have at least Python 2.7 installed

* Make sure you have the Python module `virtualenv` installed (You will need to download and install this for any version of Python older than 3.4).

  * You might be able to get it using a package from your distribution.  For instance, on Ubuntu:

  ```
  sudo apt-get install python-virtualenv
  ```

  * Otherwise, the easiest way is to install `pip` and use that to get `virtualenv`:

  ```
  pip install virtualenv
  ```

* Navigate to the directory you want the app to be in and copy/clone/whatever the `rvagaming-flask` repository into it

* Within `rvagaming-flask/` create a virtual Python environment:

  * In versions of Python older than 3.4, use

  ```
  python virtualenv.py flask
  ```

  * in versions of Python 3.4 or newer, use (untested):

  ```
  python -m venv flask
  ```

* You now have a contained Python environment in `rvagaming-flask/flask/`, and it can be called using `rvagaming-flask/flask/bin/python`

* Now we install the necessary modules in this environment:

```
flask/bin/pip install flask
flask/bin/pip install flask-login
flask/bin/pip install flask-openid
flask/bin/pip install flask-mail
flask/bin/pip install flask-sqlalchemy
flask/bin/pip install sqlalchemy-migrate
flask/bin/pip install flask-whooshalchemy
flask/bin/pip install flask-wtf
flask/bin/pip install flask-babel
flask/bin/pip install guess_language
flask/bin/pip install flipflop
flask/bin/pip install coverage
```

* You should now be able to run the application by executing `run.py`

  * If you make `run.py` executable with

  ```
  chmod a+x run.py
  ```

  You can execute it with

  ```
  ./run.py
  ```

  * Otherwise, you can execute it with

  ```
  flask/bin/python run.py
  ```
