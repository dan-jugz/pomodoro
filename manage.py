from app import create_app,db
from  flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

# Creating app instance
app = create_app('production')

migrate = Migrate(app,db)
manager=Manager(app)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)



if __name__ == '__main__':
    manager.run()