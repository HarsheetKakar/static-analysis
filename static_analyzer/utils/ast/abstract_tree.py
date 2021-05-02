import os
import json
from ast import parse
from ast2json import ast2json


class AST_maker:
    def __init__(self, filepath):
        self.filepath = filepath
        self.__ast = None

    @property
    def abstract_tree(self):
        return self.__ast

    def construct(self):
        with open(self.filepath, "r") as f:
            code = f.read()
            abstract_tree = parse(code)
        self.__ast = ast2json(abstract_tree)
        return self


if __name__ == '__main__':
    ast = AST_maker(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "ast_test.py")).construct()
    console.log(abstract_tree)
