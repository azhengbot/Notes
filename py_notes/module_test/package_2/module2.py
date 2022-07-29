"""
1. python -m py_notes.module_test.package_2.module2
2. python py_notes/module_test/package_2/module2.py

两种执行方式会导致 sys.path 不同
"""

import sys
from py_notes.module_test.dir.common import func

from py_notes.module_test.package_1.module1 import func1


def func2():
    print(f"package2 => module2 => sys.path: {sys.path}")
    print("----------")
    func1()
    print("----------")
    func()


func2()
