from git import Repo
import os


def clone_repo(link, name):
    Repo.clone_from(link, os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "repos", name))


if __name__ == '__main__':
    clone_repo("https://github.com/HarsheetKakar/Vim", "vim")
