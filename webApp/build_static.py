from flask_frozen import Freezer
from webApp import app
import shutil

freezer = Freezer(app)

if __name__ == '__main__':
    # Create the static pages
    freezer.freeze()

    # Clear the docs directory
    shutil.rmtree('docs', True)

    # Move the files to the correct location for github pages
    shutil.move('webApp/build', 'docs')

    # Move css, fonts, images, js out of the static directory
    shutil.move('docs/static/css', 'docs/css')
    shutil.move('docs/static/fonts', 'docs/fonts')
    shutil.move('docs/static/images', 'docs/images')
    shutil.move('docs/static/js', 'docs/js')
    
    # Remove static directory
    shutil.rmtree('docs/static', True)

