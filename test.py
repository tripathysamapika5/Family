import sys
import os

project_dir = os.getcwd()
sys.path.append(project_dir)
sys.path.append(project_dir+'/src/tests')

import unittest

if __name__ == '__main__':
    testsuite = unittest.TestLoader().discover(start_dir = project_dir)
    unittest.TextTestRunner(verbosity=1).run(testsuite)