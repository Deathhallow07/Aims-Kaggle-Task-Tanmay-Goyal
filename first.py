import pandas
data = pandas.read_csv("archive/drug200.csv")
def ordinal_smart_encoder(data):
    # ORDINAL ENCODER
    data_non_numeric = data.select_dtypes(exclude='number')
    cols_to_encode = data_non_numeric.columns
    for i in cols_to_encode:
        col_encoding = {}
        for j in range(len(data[i])):
            if data.loc[j, i] in col_encoding:
                #print("I RAN")
                data.loc[j, i] = col_encoding[data.loc[j, i]]  
            elif col_encoding == {}: # len(list(col_encoding.values())) == 0
                col_encoding[data.loc[j, i]] = 0
                data.loc[j, i] = 0  
            else: 
                last_number_assigned = list(col_encoding.values())[-1]
                col_encoding[data.loc[j, i]] = last_number_assigned + 1
                data.loc[j, i] = last_number_assigned + 1
    return data
new_data = ordinal_smart_encoder(data=data)






