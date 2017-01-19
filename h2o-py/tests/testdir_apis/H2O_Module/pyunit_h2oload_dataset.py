from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o

def h2oload_dataset():
    """
    Python API test: h2o.load_dataset(relative_path)
    """

    try:
        prostate = h2o.load_dataset("prostate")
        pyunit_utils.assert_is_type("H2OFrame", prostate.__class__.__name__)
    except Exception as e:
        assert False, "h2o.load_dataset() command not is working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oload_dataset)
else:
    h2oload_dataset()
