import pandas as pd

def export_to_csv(dataframe, filename):
    dataframe.to_csv(filename, index=False)

def filter_dataframe(df, query, columns):
    query = query.lower()
    return df[df[columns].apply(lambda x: x.str.lower().str.contains(query)).any(axis=1)]
