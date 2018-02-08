db_config = {
    'mysql_user': 'root',
    'mysql_pwd': 'TFMysql02',
    'mysql_host': '127.0.0.1',
    'mysql_port': '3306',
    'mysql_db': 'flask_boilerplate'
}

db_path = 'mysql+pymysql://' + db_config['mysql_user'] + ':' + db_config['mysql_pwd'] + '@' + db_config['mysql_host'] + ':' + db_config['mysql_port'] + '/' + db_config['mysql_db']

DEBUG = True
SECRET_KEY = "payment-platform-IKJNDFB"
SQLALCHEMY_TRACK_MODIFICATIONS = False