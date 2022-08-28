# python3 -m venv tutorial-env
# tutorial-env\Scripts\activate.bat --> windows
# source tutorial-env/bin/activate --> mac or unix
# You can also install a specific version of a package by giving the package name followed by == and the version number:
# pip install requests==2.6.0
# pip uninstall followed by one or more package names will remove the packages from the virtual environment.

# pip show will display information about a particular package:
# pip show requests
#  pip freeze > requirements.txt

# The requirements.txt can then be committed to version control and shipped as part of an application. Users can then install all the necessary packages with install -r:
# pip install -r requirements.txt