# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import sys

from fjord.core import Fjord
from fjord.exceptions import FjordException


def main():
    try:
        Fjord()
    except FjordException as e:
        print(e)
        
        return e.code
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
