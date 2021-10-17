import numpy as np
import pandas as pd
from apyori import apriori                   #change line 4 and 5 to"from apyori import apriori" if doesnt work
#from mlxtend.frequent_patterns import association_rules
from typing import List,TextIO

def recommend_products(
    product_code: int) -> List[int]:
    df = pd.read_csv('HTV_DATA.csv') #sample data given by loblaws
    num_rows = len(df.index)
    num_rows, num_col = df.shape
    num_col = df.shape[1]
    df.values.tolist()
    D= []
    for i in range(len(df)):
        D.append([str(df.values[i, j]) for j in range(0, num_col) if str(df.values[i,j])!= 'nan'])
    association_rules = apriori (D, min_support= 0.01, min_confidence =0.25, min_lift = 3, min_length = 1)
    association_list = list(association_rules)
#we now have all association rules falling into the given criteria
    Reccomend = {}
    for product in association_list:
        collection = product[0]
        products = [item for item in collection]
        Recommend[products[0]] = products[1:]

    R = Recommend[str(product_code)]
    New_R = []
    for item in R:
        New_R.append[int(item)]
    return New_R
