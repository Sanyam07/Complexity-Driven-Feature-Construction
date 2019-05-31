import pickle
import openml
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer
from sklearn.base import BaseEstimator
import time
from fastsklearnfeature.transformations.IdentityTransformation import IdentityTransformation
from fastsklearnfeature.transformations.HigherOrderCommutativeTransformation import HigherOrderCommutativeTransformation
from fastsklearnfeature.transformations.MinMaxScalingTransformation import MinMaxScalingTransformation
from fastsklearnfeature.transformations.PandasDiscretizerTransformation import PandasDiscretizerTransformation
from fastsklearnfeature.transformations.ImputationTransformation import ImputationTransformation
from fastsklearnfeature.transformations.OneHotTransformation import OneHotTransformation
from fastsklearnfeature.transformations.FastGroupByThenTransformation import FastGroupByThenTransformation
from fastsklearnfeature.transformations.MinusTransformation import MinusTransformation
from fastsklearnfeature.transformations.OneDivisionTransformation import OneDivisionTransformation
from fastsklearnfeature.transformations.binary.NonCommutativeBinaryTransformation import NonCommutativeBinaryTransformation


from fastsklearnfeature.configuration.Config import Config
import copy
import numpy as np
from typing import List, Set

def replaceColumnTransformer(value: ColumnTransformer, counter):
	NewClass = type(value.__class__.__name__ + str(time.time()).replace('.',''), value.__class__.__bases__, dict(value.__class__.__dict__))
	return NewClass(value.transformers, value.remainder, value.sparse_threshold, value.n_jobs, value.transformer_weights)

def replaceFeatureUnion(value: FeatureUnion, counter):
	NewClass = type(value.__class__.__name__ + str(time.time()).replace('.',''), value.__class__.__bases__,
					dict(value.__class__.__dict__))
	return NewClass(value.transformer_list, value.n_jobs, value.transformer_weights)

def replacePipeline(value: Pipeline, counter):
	NewClass = type(value.__class__.__name__ + str(time.time()).replace('.',''), value.__class__.__bases__,
					dict(value.__class__.__dict__))
	return NewClass(value.steps, value.memory)

def replaceFunctionTransformer(value: FunctionTransformer, counter):
	NewClass = type(value.__class__.__name__ + str(time.time()).replace('.',''), value.__class__.__bases__,
					dict(value.__class__.__dict__))
	return NewClass(value.func, value.inverse_func, value.validate, value.accept_sparse, value.pass_y, value.check_inverse, value.kw_args, value.inv_kw_args)

def replaceIdentityTransformation(value: IdentityTransformation, counter):
	NewClass = type(value.__class__.__name__ + str(time.time()).replace('.',''), value.__class__.__bases__,
					dict(value.__class__.__dict__))
	return NewClass(value.number_parent_features)

def replaceHigherOrderCommutativeTransformation(value: HigherOrderCommutativeTransformation, counter):
	NewClass = type(value.__class__.__name__ + str(time.time()).replace('.',''), value.__class__.__bases__,
					dict(value.__class__.__dict__))
	return NewClass(value.method, None, value.number_parent_features)

def replaceMinMaxScalingTransformation(value: MinMaxScalingTransformation, counter):
	NewClass = type(value.__class__.__name__ + str(time.time()).replace('.',''), value.__class__.__bases__,
					dict(value.__class__.__dict__))
	return NewClass()

def replacePandasDiscretizerTransformation(value: PandasDiscretizerTransformation, counter):
	NewClass = type(value.__class__.__name__ + str(time.time()).replace('.',''), value.__class__.__bases__,
					dict(value.__class__.__dict__))
	return NewClass(value.number_bins, value.qbucket)

def replaceImputationTransformation(value: ImputationTransformation, counter):
	NewClass = type(value.__class__.__name__ + str(time.time()).replace('.',''), value.__class__.__bases__,
					dict(value.__class__.__dict__))
	return NewClass(value.strategy)

def replaceOneHotTransformation(value: OneHotTransformation, counter):
	NewClass = type(value.__class__.__name__ + str(time.time()).replace('.',''), value.__class__.__bases__,
					dict(value.__class__.__dict__))
	return NewClass(value.value, value.value_id, value.raw_feature)

def replaceFastGroupByThenTransformation(value: FastGroupByThenTransformation, counter):
	NewClass = type(value.__class__.__name__ + str(time.time()).replace('.',''), value.__class__.__bases__,
					dict(value.__class__.__dict__))
	return NewClass(value.method, None)

def replaceMinusTransformation(value: MinusTransformation, counter):
	NewClass = type(value.__class__.__name__ + str(time.time()).replace('.',''), value.__class__.__bases__,
					dict(value.__class__.__dict__))
	return NewClass()

def replaceOneDivisionTransformation(value: OneDivisionTransformation, counter):
	NewClass = type(value.__class__.__name__ + str(time.time()).replace('.',''), value.__class__.__bases__,
					dict(value.__class__.__dict__))
	return NewClass()

def replaceNonCommutativeBinaryTransformation(value: NonCommutativeBinaryTransformation, counter):
	NewClass = type(value.__class__.__name__ + str(time.time()).replace('.',''), value.__class__.__bases__,
					dict(value.__class__.__dict__))
	return NewClass(value.method, None)


def get_name(counter: List[int]):
	counter[0] += 1
	return 'n' + str(counter[0])


def replace_with_new_wrapper(pip, counter: List[int] = [0]):
	my_class = pip
	if isinstance(pip, Pipeline):
		for step_counter in range(len(pip.steps)):
			pip.steps[step_counter] = (get_name(counter), replace_with_new_wrapper(pip.steps[step_counter][1], counter))
		my_class = replacePipeline(pip, counter)
	elif isinstance(pip, FeatureUnion):
		for step_counter in range(len(pip.transformer_list)):
			pip.transformer_list[step_counter] = (get_name(counter), replace_with_new_wrapper(pip.transformer_list[step_counter][1], counter))
		my_class = replaceFeatureUnion(pip, counter)
	elif isinstance(pip, ColumnTransformer):
		for step_counter in range(len(pip.transformers)):
			pip.transformers[step_counter] = (get_name(counter), replace_with_new_wrapper(pip.transformers[step_counter][1], counter), pip.transformers[step_counter][2])
		my_class = replaceColumnTransformer(pip, counter)
	elif isinstance(pip, FunctionTransformer):
		my_class = replaceFunctionTransformer(pip, counter)

	#my transformations
	elif isinstance(pip, IdentityTransformation):
		my_class = replaceIdentityTransformation(pip, counter)
	elif isinstance(pip, HigherOrderCommutativeTransformation):
		my_class = replaceHigherOrderCommutativeTransformation(pip, counter)
	elif isinstance(pip, MinMaxScalingTransformation):
		my_class = replaceMinMaxScalingTransformation(pip, counter)
	elif isinstance(pip, PandasDiscretizerTransformation):
		my_class = replacePandasDiscretizerTransformation(pip, counter)
	elif isinstance(pip, ImputationTransformation):
		my_class = replaceImputationTransformation(pip, counter)
	elif isinstance(pip, OneHotTransformation):
		my_class = replaceOneHotTransformation(pip, counter)
	elif isinstance(pip, FastGroupByThenTransformation):
		my_class = replaceFastGroupByThenTransformation(pip, counter)
	elif isinstance(pip, MinusTransformation):
		my_class = replaceMinusTransformation(pip, counter)
	elif isinstance(pip, OneDivisionTransformation):
		my_class = replaceOneDivisionTransformation(pip, counter)
	elif isinstance(pip, NonCommutativeBinaryTransformation):
		my_class = replaceNonCommutativeBinaryTransformation(pip, counter)

	return my_class

def candidate2openml(max_feature, classifier, task):
	original = copy.deepcopy(max_feature.pipeline)
	try:
		# openml
		my_pipeline = Pipeline([('features', max_feature.pipeline),
								('classifier', classifier(**max_feature.runtime_properties['hyperparameters']))
								])

		my_pipeline.steps[0] = (my_pipeline.steps[0][0], replace_with_new_wrapper(my_pipeline.steps[0][1]))

		my_run = openml.runs.run_model_on_task(my_pipeline, task, avoid_duplicate_runs=False)
		my_run.publish()
		my_run.push_tag('ComplexityDriven')
	except:
		print("error: " + str(max_feature))
		pickle.dump(my_pipeline, open('/tmp/my_pipeline', 'wb'))
	max_feature.pipeline = original