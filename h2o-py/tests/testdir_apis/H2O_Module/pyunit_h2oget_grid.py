from __future__ import print_function
from builtins import str
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
from h2o.grid.grid_search import H2OGridSearch
from h2o.estimators.gbm import H2OGradientBoostingEstimator

def h2oget_grid():
    """
    Python API test: h2o.get_grid(grid_id)

    Copy from pyunit_gbm_random_grid.py
    """
    try:
        air_hex = h2o.import_file(path=pyunit_utils.locate("smalldata/airlines/allyears2k_headers.zip"), destination_frame="air.hex")
        myX = ["DayofMonth","DayOfWeek"]

        hyper_parameters = {
            'learn_rate':[0.1,0.2],
            'max_depth':[2,3],
            'ntrees':[5,10]
        }

        search_crit = {'strategy': "RandomDiscrete",
                       'max_models': 5,
                       'seed' : 1234,
                       'stopping_rounds' : 3,
                       'stopping_metric' : "AUTO",
                       'stopping_tolerance': 1e-2
                       }

        air_grid = H2OGridSearch(H2OGradientBoostingEstimator, hyper_params=hyper_parameters, search_criteria=search_crit)
        air_grid.train(x=myX, y="IsDepDelayed", training_frame=air_hex, distribution="bernoulli")

        fetched_grid = h2o.get_grid(str(air_grid.grid_id))
        pyunit_utils.assert_is_type('H2OGridSearch', fetched_grid.__class__.__name__)
        assert(len(air_grid.get_grid())==5)
        assert (len(air_grid.get_grid())==len(fetched_grid.get_grid())), "h2o.get_grid() is command not working."
    except Exception as e:
        assert False, "h2o.get_grid() command is not working."


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oget_grid)
else:
    h2oget_grid()
