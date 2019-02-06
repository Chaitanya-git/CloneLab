# CloneLab
A python utility to recursively clone project groups and subgroups on GitLab

## Installation using pip
To build and install clonelab using pip, do the following:

First, make sure you have cloned the repository and cd into it

Now make sure you have the latest version of ```setuptools``` and ```wheel``` installed.
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
pip3 install --user dist/clonelab-0.0.3-py3-none-any.whl
```
This should install the clonelab script in the ```.local/bin``` folder inside of your home folder. To be able to run clonelab from other directories, append ```~/.local/bin``` to your ```$PATH``` variable.
To do so, run:
```bash
export PATH=$PATH:~/.local/bin
```
Add this line at the end of your ```.bashrc``` or ```.zshrc``` to avoid having to export ```PATH``` every time you open a new shell.
## Usage:
To clone  repositories accessible to a logged in user:
```bash
clonelab -t <your private token> <namespace search string> [optional parameters for git]
```
You can create a private access token for your account from your gitlab account settings. Make sure you create an access token for clonelab with full API access enabled.

To clone public repositories:
```bash
clonelab <namespace search string> [optional parameters for git]
```
The namespace search string consists of either just the name of the group you want to clone or space separated group and subgroup names if you want to narrow down the search.
For instance, if your group structure were as follows: 
```
MainGroupA
    - SubgroupA
    - SubgroupB
    - SubgroupC
MainGroupB
    - SubgroupA
    - SubgroupD
```
Then, valid namespace search strings for ```SubgroupA``` would be either "SubgroupA" or "MainGroupA SubgroupA" or "MainGroupA/SubgroupA".
If multiple groups matching the search string are found, clonelab will list all possible options and wait for the user to enter the option to select the required repository/group.

The following arguments are supported by clonelab:

| Short Options | Long Options | Description |
| ------------- | ------------ | ----------- |
| -t | --token | Provide a private access token to allow access to private repositories |
| -d | --dir | Specify a working directory to clone the group into |
| -h | --help | Display a help message |

*Note:* Long options that require arguments are used with an '=' sign.
eg: --dir=/home/user/repo

Any flag or argument not recognized by clonelab will be passed along to git when clonelab either clones repos or pulls updates inside the git repos. Currently options unique to either ```git clone``` or ```git pull``` are not supported when updating partially cloned subgroups.

If you do not wish to build and install a pip package, simply run the ```clonelab``` file inside the scripts folder with a python interpreter of your choice.
