import numpy as np
import pandas as pd

#Creation of DataFrame from Dictionary of Series
TestSheet={ 'Alex': pd.Series([90, 91, 97],  index=['NMS_TC','OTN_TC','WDM_TC']),
'Steve': pd.Series([80, 50, 100],  index=['NMS_TC','OTN_TC','WDM_TC']),
'Ram': pd.Series([100, 150, 200],  index=['NMS_TC','OTN_TC','WDM_TC']),
}
TestResultDF = pd.DataFrame(TestSheet)
TestResultDF1=pd.DataFrame()
print(TestResultDF)
#Adding/Modifying Row
TestResultDF.loc['NMS_TC'] = [95, 96, 93]
print(TestResultDF)
TestResultDF.loc['UI_TC'] = [85, 86, 83]
print(TestResultDF)
#Removing a Row
TestResultDF1 = TestResultDF.drop('WDM_TC', axis=0)
print(TestResultDF)
print(TestResultDF1)
#Removing a column
TestResultDF1 = TestResultDF.drop('Steve', axis=1)
print(TestResultDF1)
print("head")
print(TestResultDF1.head(2))
print(TestResultDF1.tail(2))
print(TestResultDF1.describe())
print(TestResultDF1.info())
print(TestResultDF1.shape)