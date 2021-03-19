pgbackup
========
CLI for export a system's user information into formats that can be used.

## Usage
The command will be able to export user names, IDs, home directories, and shells as either JSON or CSV.

By default, the command will display the information as JSON to Stdout:

```
$ hr --path=path/to/users.json
```
but the ``` --format```  flag will allow a person to specify csv as an alternative export type:

```
$ hr --format=csv --path=path/to/users.csv
```

To install the package after you've cloned the repository, you'll want to run the following command from within the project directory:

```
$ pip install --user -e .
```

## Preparing for Development

Follow these steps to start developing with this project:

1. Ensure `pip` and `pipenv` are installed
2. Clone repository: `git clone git@github.com:example/hr-project-cli`
3. `cd` into the repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`