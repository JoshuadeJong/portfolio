from flask_frozen import Freezer
from webApp import app
import shutil
import os
import glob

freezer = Freezer(app)

@freezer.register_generator
def error_handlers():
    yield "/403.html"
    yield "/404.html"
    yield "/500.html"
    yield "/501.html"

if __name__ == '__main__':
    # Create the static pages
    freezer.freeze()

    # Copy home.html to index.html
    shutil.copy('webApp/build/home.html', 'webApp/build/index.html')

    # Find *.github.io directory
    directory = glob.glob('../*.github.io')[0]

    # Clear *.github.io of old files
    shutil.rmtree(directory + '//static', True)
    for file in os.listdir(directory):
        file_type = file.split('.')[-1]

        if file_type == 'html':
            os.remove(os.path.join(directory, file))

    # Move the files to the correct location for github pages
    for file in os.listdir('webApp/build/'):
        shutil.move(os.path.join('webApp/build', file), directory)

    # Delete build directory
    shutil.rmtree('webApp/build')
