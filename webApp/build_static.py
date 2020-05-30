from flask_frozen import Freezer
from webApp import app
import shutil

freezer = Freezer(app)

if __name__ == '__main__':
    # Create the static pages
    freezer.freeze()

    # Move the files to the correct location for github pages
    shutil.move('webApp/build', 'docs')



