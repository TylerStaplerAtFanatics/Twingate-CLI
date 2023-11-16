# Python3 Command Line Interface for Twingate

A simple command line interface for Twingate in Python

## How to use it

1. Clone this repository
2. Install pandas for python (pip install pandas)
3. Authenticate (you can pass a Session Name or let it generate one at random):

```
python ./tgcli.py auth login -t "my Twingate Tenant Name" -a "my Twingate API token"
```

3. Check CLI Help to look at available Commands:

```
python ./tgcli.py -h
```

4. Check CLI Help to look at available subcommands for a given command:

```
python ./tgcli.py auth -h
```

5. Check CLI Help to look at available parameters for a given subcommand:
```
python ./tgcli.py auth login -h
```

## Things to know:

Before you can run any of the commands, you need to **authenticate**. The `auth login` command now prompts for the Twingate token and tenant name if they are not provided as command-line arguments:

```
python ./tgcli.py auth login
```

If you prefer to provide the Twingate token and tenant name directly, you can still use the following command:

```
python ./tgcli.py auth login --apikey "my Twingate API Token" --tenant "my Twingate Tenant Name"
```

The **authentication token** along with the **Tenant Name** in the authentication call are **stored locally** and **do not need to be passed as parameters beyond the first authentication call**.

The **Session Name** needs to be passed in all calls (it serves to retrieve the Tenant name and Authentication Token dynamically)

Apart from the initial authentication call, each call should contain **at least 1 option**: **-s** (**-s** is used to specify the **Session Name**.)

The output format can be set to CSV, DF (DataFrame) or JSON (Default) by using the -f option in addition to the -s option


## Commands & Subcommands Currently Available:

* Twingate CLI:

  * auth
    * login: create a session
    * logout: revoke a session
    * list: list existing sessions

  * device
    * list
    * show
    * updateTrust
    * archive
    * block
    * unblock

  * resource
    * list
    * show
    * create
    * delete
    * assignNetwork
    * visibility
    * address
    * alias

  * connector
    * list
    * show
    * create
    * rename
    * generateTokens
    * updateNotifications

  * group
    * list
    * show
    * addUsers
    * removeUsers
    * addResources
    * removeResources
    * create
    * delete
    * assignPolicy

  * user
    * list
    * show
    * role
    * create
    * delete
    * state

  * network
    * list
    * show
  
  * policy
    * list
    * show
    * addGroups
    * removeGroups
    * setGroups

  * service account
    * list
    * show
    * create
    * delete
    * addResources 
    * removeResources

  * key
    * show
    * create
    * revoke
    * delete
    * rename
    

## Poetry

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

### Installing Poetry

To get started with Poetry, install it via the official installer:

```
curl -sSL https://install.python-poetry.org | python3 -
```

### Using Poetry with this project

To install the dependencies for this project, navigate to the project's root directory and run:

```
poetry install
```

This will install all the dependencies listed in the `pyproject.toml` file.

To activate the virtual environment created by Poetry, you can run:

```
poetry shell
```

Now you can run the Twingate CLI within the virtual environment:

```
python tgcli.py <command>
```

For more information on Poetry and its commands, visit the [official documentation](https://python-poetry.org/docs/).

## Examples
```
# Authenticate
python ./tgcli.py auth login -t "my Twingate Tenant Name" -a "my Twingate API Token"
```

```
# List all devices (and display as Json (Default))
python ./tgcli.py -s RedPeacock device list
```

```
# List all devices (and display as DataFrame)
python ./tgcli.py -s RedPeacock -f DF device list
```

```
# List all devices (and display as CSV)
python ./tgcli.py -s RedPeacock -f CSV device list
```

```
# Update trust for a device (and set it to Trusted)
python ./tgcli.py -s RedPeacock device updateTrust -i "XXXabcNlOjE5MzI2OQ==" -t True
```

```
# Update trust for a list of devices (and set them to Untrusted)
python ./tgcli.py -s RedPeacock device updateTrust -l "XXXabcNlOjE5MzI2OQ==,YYYxyzFg4gT4SfC65K==" -t False
```
