# AWS Lambda python template 🐍

This is a template for those project where they use AWS lambda along with python.
This template has some opinionated configs that you can get rid of them if you don't want.
Some of this configs are:

1. MyPy linter to check static typing.
2. Flake8 linter to check code format.
3. ISort util that adjust your imports.
4. Black util to format your code.
5. Pre-Commit util to check your code with the above tools before you commit your changes.
6. Pytest as the default test runner
7. Coverage tool configured
8. Moto util to fake aws tools integrations

## Setup locally 👨‍💻

To setup your python environment properly you have to:

1. Create a python environment using python3.8
2. Install pipenv with `pip install pipenv`
3. Install dependencies running `pipenv install --dev --skip-lock`
4. Install pre-commit and enable it with `pip install pre-commit && pre-commit install`

# Tests

1. To run tests just execute `pytest` in the terminal
2. If you want to see the coverage of your project run `coverage run && coverage report`

## Mypy helps 🍾

Also this template will provide some utilities that will help MyPy linter and will make your ~~life~~ development easier.

These utilities includes:

1. HTTP Req/Res types for `API Gateway <-> Lambda` integration
2. `DynamoDBClient` class for dynamodb queries
3. MyPy boto3 types library

## Collaboration 🫶

Of course if you don't agree with some naming or decisions that this repo provide you are free to change it and if you think
we can enhance our template just submit a PR! 🤘

Some things that we are needing:

1. CI pipeline
2. CD pipeline
3. Any other contribution that you think will help is warm welcome
