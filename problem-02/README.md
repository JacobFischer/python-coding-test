# Problem 2 - Answer

This is a python answer, that takes all arguments via CLI, and then preforms
the needed API call, and dumps the result to stdout.

## Requirements

Obviously, Python 3 (v 3.5.2) will be required.

In addition, this does require a pip3 package, [`requests`][1]. However I've wrapped this up
in a `requirements.txt` file, so just run:

```
pip3 install -r requirements.txt
```

## Usage

```
python3 main.py -h
usage: main.py [-h] action [todo_id]

Runs the problem 3 solver against some input file

positional arguments:
  action      The type of action to perform, must be get, create, or delete.
  todo_id     The id of the todo to delete (or override for get).

optional arguments:
  -h, --help  show this help message and exit

```

## Examples

### Get the 200 most recent TODOs

```
python3 main.py get
Getting TODO records
Success!
Got response: [{'completed': False, 'id': 1, 'userId': 1, 'title': 'delectus aut autem'}, {'completed': False, 'id': 2, 'userId': 1, /** truncated because 200 records is a lot */ }]
```

### Create a TODO

```
python3 main.py create
Creating "foobar" TODO record
Success!
Got response: {'title': 'foobar', 'userId': 1, 'id': 201}
```

### Delete a TODO given an ID

```
Deleting TODO with id 1
Success!
Got response: {}
```

As always, if you have any questions, feel free to ask.

[1]: http://docs.python-requests.org/en/master/
