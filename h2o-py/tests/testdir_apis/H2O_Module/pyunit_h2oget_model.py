from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
from h2o.estimators.glm import H2OGeneralizedLinearEstimator

def h2oget_model():
    """
    Python API test: h2o.get_model(model_id)
    """
    try:
        training_data = h2o.import_file(pyunit_utils.locate("smalldata/logreg/benign.csv"))
        Y = 3
        X = [0, 1, 2, 4, 5, 6, 7, 8, 9, 10]

        model = H2OGeneralizedLinearEstimator(family="binomial", alpha=0, Lambda=1e-5)
        model.train(x=X, y=Y, training_frame=training_data)
        model2 = h2o.get_model(model.model_id)
        pyunit_utils.assert_is_type( model.__class__.__name__, model2.__class__.__name__)
        assert (model._model_json['output']['model_category']==model2._model_json['output']['model_category']) and \
               (model2._model_json['output']['model_category']=='Binomial'), "h2o.get_model() command is not working"

    except Exception as e:
        assert False, "h2o.get_model() command is not working"


if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oget_model)
else:
    h2oget_model()
