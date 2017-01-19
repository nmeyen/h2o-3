from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o

def h2odeep_copy():
    """
    Python API test: h2o.deep_copy(data, xid)
    """
    try:
        new_name = "new_frame"
        training_data = h2o.import_file(pyunit_utils.locate("smalldata/logreg/benign.csv"))
        training_copy = h2o.deep_copy(training_data, new_name)
        pyunit_utils.assert_is_type(training_data.__class__.__name__, training_copy.__class__.__name__)
        assert training_data.nacnt()==training_copy.nacnt(), "h2o.deep_copy() command is not working."
        training_copy.insert_missing_values(fraction=0.9)   # randomly added missing values with high probability
        assert not(training_data.nacnt()==training_copy.nacnt()), "h2o.deep_copy() command is not working."
    except Exception as e:
        assert False, "h2o.deep_copy() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2odeep_copy)
else:
    h2odeep_copy()
