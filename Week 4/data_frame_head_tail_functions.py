import numpy as np
import pandas as pd

#Creation of DataFrame from Dictionary of Series
TestSheet={ 'Alex': pd.Series([90, 91, 97],  index=['NMS_TC','OTN_TC','WDM_TC']),
'Steve': pd.Series([80, 50, 100],  index=['NMS_TC','OTN_TC','WDM_TC']),
'Ram': pd.Series([100, 150, 200],  index=['NMS_TC','OTN_TC','WDM_TC']),
}
TestResultDF = pd.DataFrame(TestSheet)
print("First 2")
print(TestResultDF.head(2))
print("Last 2")
print(TestResultDF.tail(2))
print("Describe")
print(TestResultDF.describe())
print("Information")
print(TestResultDF.info())
print("Shape is :")
print(TestResultDF.shape)