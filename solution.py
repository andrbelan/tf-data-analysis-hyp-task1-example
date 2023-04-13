import pandas as pd
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import scipy as sp

chat_id = 412238846 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    table = np.array([[x_success, x_cnt - x_success], [y_success, y_cnt - y_success]])
    pv=st.chi2_contingency(table)[1]/2 
    if pv > 0.09:
      return False
    else:
      return True
