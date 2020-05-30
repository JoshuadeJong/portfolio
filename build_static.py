from flask_frozen import Freezer
from webApp import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.run()