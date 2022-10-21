
from pyexpat import model

import pandas as pd

from sqlalchemy import null


class ModelsZO:

    def __init__(self, df):
        self.train_set, self.test_set = self.split_test_train(df)
        self.zR = null
        self.oR = null

    def split_test_train(self, df):
        test_size = round(len(df) * .30)
        test_set = df.sample(test_size)
        train_set = df.drop(test_set.index.values.tolist(), axis = 0)

        return train_set, test_set

    def zeroR(self, target_attribute):
        frequency_table = pd.value_counts(self.train_set[target_attribute]).to_frame()
        target = self.train_set[target_attribute].mode()

        return frequency_table, target

    def oneR(self):
        pass



def main():

    df = pd.read_csv('C:\Users\52332\Downloads\Datos\dataset.csv')

    models = ModelsZO(df)

    # Zero R

    frecuency_table, target = models.zeroR('Clase')

    print('Tabla de frecuencia:\n\n', frecuency_table)
    print('Target: ', target)



main()