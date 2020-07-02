# PythonSFDemo
Using `simple-salesforce` library provided for Python, we can interact with a Salesforce Org.

## Install
- `$ git clone git@github.com:techb/Python-Salesforce-Examples.git`
- `$ cd Python-Salesforce-Examples`
- `$ pipenv shell`
- `$ pipenv install`
- `$ cp EXAMPLE_login.json login.json`
- Update `login.json` with your username, password, and token

## Run
- `$ python app.py`

## Pipenv
While working on this example, there was an update to simple-salesforce lib. Github has the current version and we need the format_soql method from it. **BUT** pip hasn't been updated with the new version as of yet July 2 2020.

So, we'll need to install it via it's repo on Github.
- `pipenv install -e git+https://github.com/simple-salesforce/simple-salesforce.git#egg=simple-salesforce`

If you are wondering where to get the `#egg=simple-salesforce` from checkout this [LINK](https://stackoverflow.com/questions/21638929/how-to-determine-the-name-of-an-egg-for-a-python-package-on-github). Basically we grab whatever the `name` is in the `setup.py` file.