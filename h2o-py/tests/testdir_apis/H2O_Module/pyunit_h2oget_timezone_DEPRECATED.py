from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o

def h2oget_timezone():
    """
    Python API test: h2o.get_timezone()
    Deprecated, use h2o.cluster().timezone.

    Copy from pyunit_get_set_list_timezones.py
    """
    try:
        origTZ = h2o.get_timezone()
        print("Original timezone: {0}".format(origTZ))

        timezones = h2o.list_timezones()
        pyunit_utils.assert_is_type("H2OFrame", timezones.__class__.__name__)
        assert timezones.nrow==460, "h2o.get_timezone() returns frame with wrong row number."
        assert timezones.ncol==1, "h2o.get_timezone() returns frame with wrong column number."
    except Exception as e:
        assert False, "h2o.get_timezone() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oget_timezone)
else:
    h2oget_timezone()
