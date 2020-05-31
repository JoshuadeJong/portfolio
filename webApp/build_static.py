from flask_frozen import Freezer
from webApp import app
import shutil
import os

freezer = Freezer(app)

if __name__ == '__main__':
    # Create the static pages
    freezer.freeze()

    # Copy home.html to index.html
    shutil.copy('webApp/build/home.html', 'webApp/build/index.html')

    # Clear manvanmaan.github.io of old files
    shutil.rmtree('../manvanmaan.github.io/static', True)
    for file in os.listdir('../manvanmaan.github.io'):
        file_type = file.split('.')[-1]

        if file_type == 'html':
            os.remove(os.path.join('../manvanmaan.github.io', file))

    # Move the files to the correct location for github pages
    for file in os.listdir('webApp/build/'):
        shutil.move(os.path.join('webApp/build', file), '../manvanmaan.github.io')

    # Delete build directory
    shutil.rmtree('webApp/build')
