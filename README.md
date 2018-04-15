# DuoCloud NAV 多云导航

掌控区块链

A flask start kit with [flask_restful](https://github.com/flask-restful/flask-restful) and mysql

#### Initial a virtualenv

```
$ pip install virtualenv
$ virtualenv -p python3 env
$ source env/bin/activate
```

#### Install dependence

```
$ git clone https://github.com/georgezouq/flask-start-kit.git
$ pip install -r requirements.txt
```

### Set database config

To use this project, you first need create a config file `config.py` in `common/`, with content:

```
db_config = {
    'mysql_user': 'root',
    'mysql_pwd': '',
    'mysql_host': '',
    'mysql_port': '3306',
    'mysql_db': ''
}

db_path = 'mysql+pymysql://' + db_config['mysql_user'] + ':' + db_config['mysql_pwd'] + '@' + db_config['mysql_host'] + ':' + db_config['mysql_port'] + '/' + db_config['mysql_db']

DEBUG = True
SECRET_KEY = "kkk-IKJNDFB"
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

Fill `db_config` with your configuration

#### Run main file

```
$ python main.py
```

Use your browser to: [http://localhost:5000/todos](http://localhost:5000/todos)

Congratulations! Enjoy your journey!

### Other Resources

By the way, this `vue.js` project [vue-admin](https://github.com/georgezouq/vue-admin) is build for this project's front end page.

- [Flask](http://flask.pocoo.org/)
- [Flask Restful](https://github.com/flask-restful/flask-restful)
