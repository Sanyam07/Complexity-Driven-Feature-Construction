from fastsklearnfeature.transformations.NumericUnaryTransformation import NumericUnaryTransformation
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np
from fastsklearnfeature.candidates.CandidateFeature import CandidateFeature
from typing import List
import sympy

class discretize(sympy.Function):
    @classmethod
    def eval(cls, x):
        if isinstance(x, discretize): #idempotent
            return x


class PandasDiscretizerTransformation(BaseEstimator, TransformerMixin, NumericUnaryTransformation):
    def __init__(self, number_bins, qbucket=False):
        self.number_bins = number_bins
        self.qbucket = qbucket
        name = 'discretize'
        NumericUnaryTransformation.__init__(self, name)

    def fit(self, X, y=None):
        if not self.qbucket:
            _, self.bins = pd.cut(X[:,0], bins=self.number_bins, retbins=True, labels=range(self.number_bins))
        else:
            _, self.bins = pd.qcut(X[:,0], q=self.number_bins, retbins=True, labels=range(self.number_bins))
        return self

    def transform(self, X):
        bucket_labels = pd.cut(X[:,0], bins=self.bins, labels=range(self.number_bins),
                               include_lowest=True).__array__()
        bucket_labels[np.isnan(bucket_labels)] = -1
        return np.reshape(bucket_labels, (len(X), 1))

    def is_applicable(self, feature_combination: List[CandidateFeature]):
        if not super(PandasDiscretizerTransformation, self).is_applicable(feature_combination):
            return False
        if isinstance(feature_combination[0].transformation, PandasDiscretizerTransformation):
            return False
        if 'number_distinct_values' in feature_combination[0].properties and feature_combination[0].properties['number_distinct_values'] <= self.number_bins:
            return False

        return True

    def get_sympy_representation(self, input_attributes):
        return discretize(input_attributes[0])

    def derive_properties(self, training_data, parents: List[CandidateFeature]):
        properties = {}
        # type properties
        properties['type'] = training_data.dtype

        try:
            # missing values properties
            properties['missing_values'] = False #nan -> -1

            # range properties
            properties['has_zero'] = True

            if 'missing_values' in parents[0].properties:
                if parents[0].properties['missing_values'] == True:
                    properties['min'] = -1
                else:
                    properties['min'] = 0
            else:
                properties['min'] = np.nanmin(training_data)

            properties['max'] = self.number_bins - 1
        except:
            # was nonnumeric data
            pass

        if 'missing_values' in parents[0].properties:
            if parents[0].properties['missing_values'] == True:
                properties['number_distinct_values'] = self.number_bins + 1
            else:
                properties['number_distinct_values'] = self.number_bins
        else:
            properties['number_distinct_values'] = self.number_bins #estimate

        return properties