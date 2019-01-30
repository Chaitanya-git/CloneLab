# CloneLab
A python utility to recursively clone project groups and subgroups on GitLab

## Installation using pip
To build and install clonelab using pip, do the following:

First, make sure you have the latest version of ```setuptools``` and ```wheel``` installed.
```bash
python3 -m pip install --user --upgrade setuptools wheel
```
Then, build clonelab into a wheel package.
```bash
python3 setup.py sdist bdist_wheel
```
This puts the built wheel package in the ```dist``` folder.
Finally, install the wheel package using pip
```bash
pip3 install --user dist/clonelab-0.0.1-py3-none-any.whl
```
This should install the clonelab script in the ```.local/bin``` folder inside of your home folder. To be able to run clonelab from other directories, append ```~/.local/bin``` to your ```$PATH``` variable.

## Usage:
To clone  repositories accessible to a logged in user:
```bash
clonelab -t <your private token> <namespace search string> [optional parameters for git]
```

To clone public repositories:
```bash
clonelab <namespace search string> [optional parameters for git]
```
If multiple groups matching the search string are found, cloneLab will list all possible options and wait for the user to enter the option to select the required repository.

Any flag or argument not recognized by clonelab will be passed along to git when clonelab either clones repos or pulls updates inside the git repos. Currently options unique to either ```git clone``` or ```git pull``` are not supported when updating partially cloned subgroups.

If you do not wish to build and install a pip package, simply run the ```clonelab``` file inside the scripts folder with a python interpreter of your choice.
