'''
Created on Jun 13, 2017

@author: meike.zehlike
'''
from data_structure import dataset
import numpy as np
import pandas as pd

def mean_difference(dataset, protected_column, non_protected=0, targets='all'):
    # TODO: Doku: dataset = python dataframe mit den Daten aus der CSV Datei
    # protected_column = name der Spalte, die den protection status angibt, der hier benutzt werden soll
    # non_protected = diejenige Kategorie (als Integer), die die advantaged group beschreibt, default 0
    # mean differences werden immer with respect to the non-protected group berechnet
    # gibt einen dataframe zurück mit den geschützten Kategorien als zeilenindex,
    # der target_column als column names und der mean difference als value

    if protected_column not in dataset.protected_cols:
        raise ValueError("given protected_column column name doesn't exist in dataset. Check spelling.")


    if targets == 'all':
        targets = dataset.target_cols

    result = pd.DataFrame()

    # get all protected attribute categories
    group_categories = dataset.data[protected_column].unique()

    for column_name in targets:
        if column_name not in dataset.target_cols:
            raise ValueError("given target column name doesn't exist in dataset. Check spelling.")
        else:
            result_col = pd.DataFrame()

            # calculate mean of target values for the non-protected group
            target_values_nonprotected = dataset.data.loc[dataset.data[protected_column] == non_protected, column_name]
            mean_nonprotected = np.mean(target_values_nonprotected, dtype=np.float64)

            # calculate mean of target values for all protected categories
            for category in group_categories:
                if category == non_protected:
                    # skip non_protected category, has been done above
                    continue
                else:
                    target_values_protected = dataset.data.loc[dataset.data[protected_column] == category, column_name]
                    mean = np.mean(target_values_protected, dtype=np.float64)
                    mean_diff = mean_nonprotected - mean
                    df = pd.DataFrame({column_name: [mean_diff]}, index=[category])
                    result_col = result_col.append(df)
        result = pd.concat([result, result_col], axis=1)
    return result
