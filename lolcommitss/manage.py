# coding: utf-8
import os

from flask.ext.script import Manager
from lolcommitss.app import app

from flask.ext.migrate import Migrate, MigrateCommand


manager = Manager(app)
root_directory = os.path.abspath(os.path.dirname(__file__))



# trick for using db maagement command from amywhere
migration_directory=os.path.join(root_directory, 'migrations')
migrate = Migrate(app, app.db, directory=migration_directory)
manager.add_command('db', MigrateCommand)

def main():
    manager.run()

if __name__ == "__main__":
    main()

