# CloneLab
A python script to recursively clone project groups and subgroups on GitLab

## Usage:
To clone  repositories accessible to a logged in user:
```bash
python clone.py -t <your private token> <namespace search string>
```

To clone public repositories:
```bash
python clone.py <namespace search string>
```
If multiple groups matching the search string are found, cloneLab will list all possible options and wait for the user to enter the option to select the required repository.



