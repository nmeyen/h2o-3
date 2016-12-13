from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o

def h2oremove():
    """
    Python API test: h2o.remove(x)
    """
    # call with no arguments
    try:
        training_data = h2o.import_file(pyunit_utils.locate("smalldata/logreg/benign.csv"))
        pyunit_utils.assert_is_type("H2OFrame", training_data.__clas__.__name__)
        h2o.remove(training_data)
        training_data.nrow  # this command should generate an error since training_data should have been deleted.
    except Exception as e:
        assert "object has no attribute" in e.args[0], "h2o.remove() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oremove)
else:
    h2oremove()
