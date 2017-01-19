from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o

def h2oparse_setup():
    """
    Python API test: h2o.parse_setup(raw_frames, destination_frame=None, header=0, separator=None, column_names=None,
     column_types=None, na_strings=None)
    """
    try:
        col_types=['enum','numeric','enum','enum','enum','numeric','numeric','numeric']
        col_headers = ["CAPSULE","AGE","RACE","DPROS","DCAPS","PSA","VOL","GLEASON"]
        hex_key = "training_data.hex"

        fraw = h2o.import_file(pyunit_utils.locate("smalldata/prostate/prostate_cat.csv"), parse=False)
        setup = h2o.parse_setup(fraw, destination_frame=hex_key, header=1, separator=',', column_names=col_headers,
                                column_types=col_types, na_strings=["NA"])
        pyunit_utils.assert_is_type("H2OResponse", setup.__class__.__name__)
        assert setup["number_columns"]==len(col_headers), "h2o.parse_setup() command is not working."
    except Exception as e:
        assert False, "h2o.parse_setup() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oparse_setup)
else:
    h2oparse_setup()
