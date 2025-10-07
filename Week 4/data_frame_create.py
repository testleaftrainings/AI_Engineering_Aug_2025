import numpy as np
import pandas as pd

# initialize list of lists
data = [['Alex', 10], ['Sabari', 15], ['Syed', 14]]
# Create the pandas DataFrame
empdf = pd.DataFrame(data, columns=['Name', 'Experience in Years'])
print(empdf)


array1 = np.array([10,20,30])
array2 = np.array([100,200,300])
array3 = np.array([-10,-20,-30, -40])
# Create Data frame using ndarray
#dFrame4 = pd.DataFrame(array1)
#print(dFrame4)
dFrame5 = pd.DataFrame([array1, array2,array3], columns=[ 'A', 'B', 'C', 'D'])
print(dFrame5)

# Create Data frame using Dictionary
listDict = [{'a':10, 'b':20}, {'a':5, 'b':10, 'c':20}]
df = pd.DataFrame(listDict)
print(df)


#Creation of DataFrame from Dictionary of Lists
dictState = {'State': ['Assam', 'Delhi', 'Kerala'],  'GArea': [78438, 1483, 38852] ,
'VDF' : [2797, 6.72,1663]}
dFrameState = pd.DataFrame(dictState)
print(dFrameState)

#Creation of DataFrame Using Series
seriesA = pd.Series ([1000,2000,3000], index = ['EmpClusterA', 'EmployeeClusterB', 'EmployeeClusterC'])
seriesB = pd.Series ([4000,5000], index = ['EmpClusterD', 'EmployeeClusterE'])
dFrame7 = pd.DataFrame([seriesA, seriesB])
print(dFrame7)

dFrame7['TotalHours'] = [10000,15000]
print(dFrame7)

dFrame7['EmpClusterA'] = [2000,3000]

#Creation of DataFrame from Dictionary of Series
TestSheet={ 'Alex': pd.Series([90, 91, 97],  index=['NMS_TC','OTN_TC','WDM_TC']),
'Steve': pd.Series([80, 50, 100],  index=['NMS_TC','OTN_TC','WDM_TC']),
'Ram': pd.Series([100, 150, 200],  index=['NMS_TC','OTN_TC','WDM_TC'])
}
TestResultDF = pd.DataFrame(TestSheet)
TestResultDF1=pd.DataFrame()
print(TestResultDF)

#Adding Row
TestResultDF.loc['UI_TC'] = [85, 86, 83]
#print(TestResultDF)
#Modifying Row
TestResultDF.loc['NMS_TC'] = [95, 96, 93]
#print(TestResultDF)

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

print(TestResultDF1)
print(TestResultDF1.describe())
print(TestResultDF1.info())
print(TestResultDF1.shape)

