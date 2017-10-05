#!/usr/bin/python3

"""
See the README.md for instructions on how to run this file, and problem-02.md
for instructions on the problem this code solves :D
"""

import sys
import argparse
import requests  # NOTE: this is a pip package, please install it!

BASE_URL = 'http://jsonplaceholder.typicode.com/'
GET = 'get'
CREATE = 'create'
DELETE = 'delete'
ACTIONS = [GET, CREATE, DELETE]

# make the lists into the pretty string "get", "create", or "delete"
# by combing with with commands, and add the 'or ' part to the last item
# This is probably pretty silly for such a small program :P
pretty_actions = ', '.join(ACTIONS[:-1] + ['or ' + ACTIONS[-1]])

parser = argparse.ArgumentParser(
    description='Runs the problem 3 solver against some input file'
)

parser.add_argument(
    'action',
    action='store',
    type=str,
    help='The type of action to perform, must be {}.'.format(pretty_actions)
)

parser.add_argument(
    'todo_id',
    action='store',
    type=int,
    default=-1,
    help='The id of the todo to delete (or override for get).',
    nargs='?'
)

args = parser.parse_args()

if args.action not in ACTIONS:
    parser.error('{} is not a valid action. Must be {}'.format(
        args.action,
        pretty_actions
    ))

if args.action == DELETE and args.todo_id == -1:
    parser.error('"delete" action must be given a valid id to delete TODOs on')

# argparse will ensure that the CLI options are valid, and the above checks
# will throw parser errors for our custom logic argparse can't do directly

# if we get to here, then we can assume our args are validated

response = None
if args.action == GET:
    print('Getting TODO records')
    # adding a feature here, if they send a TODO id, just get that id and
    # not the whole 200
    suffix = '/{}'.format(args.todo_id)
    if args.todo_id == -1:
        suffix = ''
    response = requests.get(BASE_URL + 'todos' + suffix)

    # NOTE:
    # Normally I'd expect some sort of pagination as part of the API, however
    # the jsonplaceholder API always claims to return 200 TODO records for this
    # endpoint.
    # I did find a GitHub issue:
    #   https://github.com/typicode/jsonplaceholder/issues/29
    # that covers this topic, so it does NOT appear to be an officially
    # supported parameter, so the above code will always assume it gets exactly
    # 200 TODOs sent back

elif args.action == CREATE:
    print('Creating "foobar" TODO record')
    response = requests.post(BASE_URL + 'todos', {
        'title': 'foobar',
        'userId': 1
    })
else:  # it must be delete
    print('Deleting TODO with id {}'.format(args.todo_id))
    response = requests.delete(BASE_URL + 'todos/{}'.format(args.todo_id))

if response and response.status_code < 400:  # should be 2XX response codes
    print('Success!\nGot response: {}'.format(response.json()))
else:
    print('Request did not work', response)
