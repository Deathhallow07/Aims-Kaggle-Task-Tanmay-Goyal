import pandas
import numpy
data = pandas.DataFrame({'A': [1, numpy.nan, 3], 'B': [4, 5, numpy.nan]})
def mean_imputer(data):
    # ORDINAL ENCODER
    data_non_numeric = data.select_dtypes('number')
    cols_to_encode = data_non_numeric.columns
    mean_dict = {}
    for i in cols_to_encode:
        sum = 0
        count = 0
        for j in range(len(data[i])):
            if pandas.isna(data.loc[j, i]) == True:
                pass
            else:
                sum = sum + data.loc[j, i]
                count = count + 1

        mean_dict[i] = sum/count


    for i in cols_to_encode:
        for j in range(len(data[i])):
            if pandas.isna(data.loc[j, i]) == True:
                data.loc[j, i] = mean_dict[i]
            else:
                pass

        
          
   
    return data


new_data = mean_imputer(data=data)
new_data.to_csv("output.csv")
print(new_data)






