sgd-regression
=================

This app creates and fits an `SGD`_ model based on parquet-formatted input data. The arguments to the program are asfollows: 

- ``train``: (str, required) local path or URI of a parquet file containing training data 
- ``test``: (str, required) local path or URI of a parquet file containing test data 
- ``alpha``: (float) alpha for the regressor; default ``.001`` 
- ``l1-ratio``: (float) l1 ratio to be used for the regressor; default ``.5`` 
- ``max-iter``: (int) maximum iterations; default ``5`` 
- ``tol``: (float) Stopping criterion; default ``None`` 
- ``label-col``: (str, required) name of label column in dataset; ``string`` input 
- ``feat-cols``: (str) names of columns in dataset to be used as features; input is one ``string`` with names delimited by commas. If no argument is provided, it is assumed that all columns but the label column are feature columns.

This app currently assumes that the input data is all numerical.

To run the app with default parameters while in the root directory, run the command

::

   mlflow run apps/sgd-regression -P train="insert/data/path/" -P test="insert/data/path/" -P label-col="insert.label.col"

.. _SGD: http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html
