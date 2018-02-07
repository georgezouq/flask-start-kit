from app import create_app
import common.db as db

if __name__ == '__main__':
    db.init_tables()
    create_app().run(debug=True)

