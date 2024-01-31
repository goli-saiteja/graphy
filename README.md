
![enter image description here](https://lh3.googleusercontent.com/pw/ABLVV878HLpP2gvJyLXTp8UPM9oXgyDq8lIwhytZ11tJj52koPqXXu7aJRw4NKmWnnMAMdEhnlW08VmuLDzwGsJfnXC0QgSzvFNVlkClvTte2DtOlKVob0_UFCfXsmJfLaZgGx50ORAqKXQ8m6nWyrZuHm4j=w3550-h1918-s-no-gm)
# Application setup


## Initial Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/goli-saiteja/graphy.git
$ cd graphy
```
## Backend Setup


Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env_name
$ source env_name/bin/activate
```

Then install the dependencies:

```sh
(env)$ cd graphy/backend
(env)$ pip install -r requirements.txt
```


Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd graphy/backend
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py loaddata fixtures/metrics_fixture.json
(env)$ python manage.py loaddata fixtures/departments_fixture.json
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:3022/api/departments/`.


## Frontend Setup

Install the dependencies:

```sh
(env)$ cd graphy/client
(env)$ npm i
```

Once `npm` has finished downloading the dependencies:
```sh
(env)$ npm run start
```
And navigate to `http://localhost:3020/`.