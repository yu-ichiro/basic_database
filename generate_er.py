from sys import argv

from eralchemy import render_er
from model import BaseObject


def render(output='./er.png'):
    render_er(BaseObject, output)


if __name__ == '__main__':
    if len(argv) > 1:
        render(argv[1])
    else:
        render()
