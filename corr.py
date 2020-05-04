import numpy as np
import pandas as pd
import pandas_datareader.data as web
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.optimize as sco
import pickle

# Basically all this does is take a stock icon and then finds all the positively correlated stocks (table1) and
# negatively correlated stocks (table2). Right now it displays the top 5. The stock index data is taken from some 
# index pickle file which I've generated so this should work as is. 


def get_pos_corr_stocks(pickle_filename="corr_pairs.pickle", key=""):
    #loading pickle object:
    pickle_in = open(pickle_filename,"rb")
    corr_data = pickle.load(pickle_in)
    table = corr_data.sort_values(ascending=False, axis=0, by='Correlation')
    table = table[3363:]
    output_table = pd.DataFrame(columns = ['stock1', 'stock2', 'Correlation'])
    if key == "":    
        return table[:50]
    
    else:
        count=0
        pick_in = open("stock_index", "rb")
        stock_index = pickle.load(pick_in)
        
        check = 0
        for x in stock_index['name']:
            if x == key:
                check = 1
                break;
        if check == 0:
            print("Key not found")
            return 0
        
        for index, row in table.iterrows():
            if row['stock1'] == key:
                output_table = output_table.append(row)
                count = count +1
            if count == 5:
                break;
        return output_table;
                    
            

def get_neg_corr_stocks(pickle_filename="corr_pairs.pickle", key=""):
    #loading pickle object:
    pickle_in = open(pickle_filename,"rb")
    corr_data = pickle.load(pickle_in)
    output_table = pd.DataFrame(columns = ['stock1', 'stock2', 'Correlation'])

    
    if key == "":
        return corr_data[:50]
    else:
        count=0
        
        pick_in = open("stock_index", "rb")
        stock_index = pickle.load(pick_in)
        
        check = 0
        for x in stock_index['name']:
            if x == key:
                check = 1
                break;
        if check == 0:
            print("Key not found")
            return 0
            
        for index, row in corr_data.iterrows():
            if row['stock1'] == key:
                output_table = output_table.append(row)
                count = count +1
            if count == 5:
                break
            else:
                continue
        return output_table;

def get_correlated_pairs(backtest_window_s="2018-08-01",backtest_window_e="2019-01-01", positive_corr_bound=0.9,
                          negative_corr_bound=-0.9,pickle_filename="dict.pickle", key=""):
    
    positively_correlated_stocks = get_pos_corr_stocks(key=key)#Get +ve Corr
    #print("positive table made")
    negatively_correlated_stocks = get_neg_corr_stocks(key=key)#Get -ve Corr
    #print("negative table made")
    MSG="INVALID QUERY"
    try: 
        if positively_correlated_stocks == 0:
            return MSG, MSG
    except:
        return positively_correlated_stocks, negatively_correlated_stocks

table1, table2 = get_correlated_pairs(key="ICON")