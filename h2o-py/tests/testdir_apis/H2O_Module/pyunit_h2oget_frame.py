from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o

def h2oget_frame():
    """
    Python API test: h2o.get_frame(frame_id)
    """
    try:
        frame1 = h2o.import_file(pyunit_utils.locate("smalldata/jira/hexdev_29.csv"))
        frame2 = h2o.get_frame(frame1.frame_id)
        pyunit_utils.assert_is_type("H2OFrame", frame2.__class__.__name__)
    except Exception as e:
        assert False, "h2o.get_frame() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oget_frame)
else:
    h2oget_frame()
