import os
import json
from ast import parse
from ast2json import ast2json


def construct(filename):
    with open(filename, "r") as f:
        code = f.read()
        abstract_tree = parse(code)
    return ast2json(abstract_tree)


if __name__ == '__main__':
    print(construct(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "ast_test.py")))
