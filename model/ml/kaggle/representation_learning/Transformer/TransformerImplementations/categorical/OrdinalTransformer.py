import numpy as np
import category_encoders as ce

class OrdinalTransformer():

    def __init__(self, column_id):
        self.column_id = column_id
        self.applicable = True


    def fit(self, dataset, ids):
        self.encoder = ce.OrdinalEncoder()
        column_data = np.matrix(dataset.values[ids, self.column_id], dtype='str').A1
        self.encoder.fit(column_data)

    def transform(self, dataset, ids):
        column_data = np.matrix(dataset.values[ids, self.column_id], dtype='str').A1
        transformed = self.encoder.transform(column_data)
        #self.transformed_size = transformed.shape[1]
        return np.matrix(transformed.values)

    def get_feature_names(self, dataset):
        internal_names = []
        #test = self.encoder.category_mapping[0]['mapping']
        #for map_pair in test:
        internal_names.append(str(self.column_id) + '#' + str(dataset.columns[self.column_id]) + "#" + "ordinal")

        return internal_names

    def get_involved_columns(self):
        return [self.column_id]
