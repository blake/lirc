''' Set up paths to components, including in-tree development. '''

import glob
import sys
import os.path


HERE = os.path.abspath(os.path.dirname(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
if os.path.exists(os.path.join(HERE, '_client.so')):
    os.unlink(os.path.join(HERE, '_client.so'))
if os.path.exists(os.path.join(HERE, '..', 'lib', '.libs', '_client.so')):
    # development tree Makefile.am creates lib/libs/_client.so
    # after 'make install'; plain 'make' isn't enough.
    os.symlink(os.path.join('..', 'lib', '.libs', '_client.so'),
               os.path.join(HERE, '_client.so'))
else:
    # 'python setup.py' artifact:
    SRC = glob.glob(os.path.join(HERE, '../_client.cpython*.so'))
    if len(SRC) == 1:
        os.symlink(os.path.join(SRC[0]), os.path.join(HERE, '_client.so'))