import os
import app as application

app = application.create_app(os.getenv('FLASK_CONFIG') or 'default')

application.db.drop_all()
application.db.create_all()

if __name__ == '__main__':
    application.manager.run()
