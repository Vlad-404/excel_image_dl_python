# Download images from image links from an Excel spreadsheet

A mouthfull of a title. Simple explanation: A script that downloads images that are stored as links in an Excel spreadsheet.

Presumptions (until app is upgraded):
- all of your images are stored as a url link(example: [image](https://www.shutterstock.com/shutterstock/photos/2051190098/display_1500/stock-photo-scenic-view-of-sandy-desert-under-starry-sky-in-night-2051190098.jpg))
- all of your images are in one and the same column (see column variable in `get_urls.py`)
- only the first sheet is used

As the app is reading hyperlink values, they need to be **stored as url links** not as plain text or images themselves.

Pre-requisites:
- Python 3.10 or newer installed ([Install Python](https://www.python.org/downloads/))
- Pip - for installing packages
- Code editor (Like [VSCode](https://code.visualstudio.com/download) or any other to edit the code)

Using the app:
1. First clone this repo or make a fork.
2. Create venv (optional):

    `python3 -m venv excel_venv`

      You can replace excel_venv with your own name, but don't forget to change the name in .gitignore file! Replace `python3` with `python` depending on your OS:

    `python -m venv excel_venv`

   2a. Activate venv:

    `source excel_venv/bin/activate`

    Depending on your OS, if venv isn't activated, look for `activate` file and use that path. On Windows it's usually in `/scripts/activate`

3. Run:

    `pip install requirements.txt`

    This will install all of the required packages. Depending on your OS, you might want to add `-r` handle:

    `pip install -r requirements.txt`

4. Run any of the `.py` scripts.

If you install any additional packages, don't forget to `pip freeze > requirements.txt`.

At the moment, scripts only works with a sheet that is in the root folder of this app. Other paths can be used, but then the paths in `get_urls.py` also need to be changed.

The app will get upgraded and the goal is to make it have it's own UI. The main goal is for any user without any coding knowledge to be able to use it through said UI.
