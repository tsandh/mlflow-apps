# Copyright 2018 Databricks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import pandas
import train_linear
import utils
# Trains a single-machine scikit-learn Elastic Net model on the provided data file, 
# producing a pickled model file. Uses MLflow tracking APIs to log the model file,
# and the model's training loss.

#Parsing arguments.
parser = argparse.ArgumentParser()
parser.add_argument("training_data_path", help="Path to training parquet dataset file.",
                    type=str)
parser.add_argument("test_data_path", help="Path to test parquet dataset file.",
                    type=str)
parser.add_argument("alpha", help="Alpha value for SGD regressor.",
                    type=float)
parser.add_argument("l1_ratio", help="L1 ratio for SGD regressor. "
    "See http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html "
    "for more details.",
                    type=float)
parser.add_argument("label_col", help="Name of label column.",
                    type=str)
parser.add_argument("--max-iter", help="Maximum number of passes over the training data.",
                    type=int)
parser.add_argument("--tol", help="The stopping criterion.",
                    type=float)
parser.add_argument("--feat-cols", help="List of feature column names. "
                        "Input must be a single string with columns delimited by commas.",
                    type=lambda s: [str(i) for i in s.split(',')])

args = parser.parse_args()

# Reading the parquet file into a pandas dataframe.
training_pandas_data = pandas.read_parquet(args.training_data_path)
test_pandas_data = pandas.read_parquet(args.test_data_path)

feat_cols = utils.get_feature_cols(args.feat_cols, args.label_col, list(training_pandas_data))

# Train the model based on the parameters provided.
train_linear.train(training_pandas_data, test_pandas_data, args.label_col, feat_cols, 
                    args.alpha, args.l1_ratio, args.max_iter, args.tol, args.training_data_path, args.test_data_path)
