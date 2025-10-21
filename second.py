import pandas
data = pandas.read_csv("archive/drug200.csv")
def ordinal_smart_encoder(data):
    # ORDINAL ENCODER
    data_non_numeric = data.select_dtypes(exclude='number')
    cols_to_encode = data_non_numeric.columns
    for i in cols_to_encode:
        col_encoding = {}
        for j in range(len(data[i])):
            data.loc[j, data.loc[j, i]] = 1
          
    data = data.fillna(0)
    return data
new_data = ordinal_smart_encoder(data=data)
new_data.to_csv("output.csv")
print(new_data)






