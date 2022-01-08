import numpy as np
import pandas as pd

def build_data_dict(data, datadict):
# pull info from the multiple data dictionaries into the single data.columns
    dd = {}
    for colname in data.columns:
        # instantiate the column as a key
        print(f'looking for {colname}...')
        dd[colname] = None
        for k,v in datadict.items():
            # access each dataframe looking for the colname
            first_col = v.iloc[:-2,0]
            try:
                # search if the first column of each dataframe contains the columnname, and get its value
                matching_idx = np.where(first_col.str.contains(colname))[0][0]
            except IndexError as error:
                print(f'{error} for {colname} in {k}')
            else:
                # access the description of the column based on the found index - if the idx is found, break of out the df loop and progress 
                # to next column
                str_descr = v.iloc[:,1].loc[matching_idx]
                dd[colname] = str_descr
                print(f'{colname} found. breaking out of df {k}')
                break
                
    # put the dictionary together and return dataframe
    df_output = pd.DataFrame.from_dict(dd, orient='index').reset_index().rename({'index':'col', 0:'descr'}, axis='columns')
    return df_output


def parse_df_strings(df):
    output = df.copy()
    output['emp_length'] = output['emp_length'].replace({'< 1 year': '0'}).str.extract(r'(\d+)').astype(float)
    for col in ['int_rate', 'revol_util']:
        # the optional ?\d+ is used to manage cases such as 21%
        output[col] = output[col].str.extract(r'(\d+\.?\d+)').astype(float)
    output['term'] = output['term'].str.extract(r'(\d+)').astype(float)
    return output.reset_index(drop=True)