from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o

def h2oconnection():
    """
    Python API test: h2o.connection()
    """
    # call with no arguments
    try:
        temp = h2o.connection()
        pyunit_utils.assert_is_type("H2OConnection", temp.__class__.__name__)
    except Exception as e:
        assert False, "h2o.connection() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oconnection)
else:
    h2oconnection()
