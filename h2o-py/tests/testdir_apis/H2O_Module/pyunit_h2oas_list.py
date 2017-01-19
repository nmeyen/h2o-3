from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o

def h2oas_list():
    """
    Python API test: h2o.as_list(data, use_pandas=True, header=True)
    Copied from pyunit_frame_as_list.py
    """
    try:
        iris = h2o.import_file(path=pyunit_utils.locate("smalldata/iris/iris_wheader.csv"))

        res1 = h2o.as_list(iris, use_pandas=False)
        pyunit_utils.assert_is_type("list", res1.__class__.__name__)
        res1 = list(zip(*res1))
        assert abs(float(res1[0][9]) - 4.4) < 1e-10 and abs(float(res1[1][9]) - 2.9) < 1e-10 and \
           abs(float(res1[2][9]) - 1.4) < 1e-10, "incorrect values"
    except Exception as e:
        assert False, "h2o.as_list() command not is working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oas_list)
else:
    h2oas_list()
