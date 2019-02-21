import unittest
from flask_script import Manager,Server
from app import create_app,db
from flask_migrate import Migrate, MigrateCommand
from config import config_options
from app.models import User,Favorites,Review,Places

#Instances of app
app = create_app('development')
# app = create_app('testing')



manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
<<<<<<< HEAD
    return dict(app = app,db = db,User=User,Review=Review,Places=Places,Favorites=Favorites)
=======
    return dict(app = app,db = db,User=User,Places=Places,Favorites=Favorites,Review=Review)
>>>>>>> bca682c4ae666d195a54af2e49adb2c2d846f3f2


if __name__ == '__main__':
    manager.run()

