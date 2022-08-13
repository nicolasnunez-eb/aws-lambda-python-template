# AWS Lambda python template

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

## Mypy helps

Also this template will provide some utilities that will help MyPy linter and will make your ~~life~~ development easier.

These utilities includes:
1. Some types inside the aws_utils directory
2. MyPy boto3 types library
