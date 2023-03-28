import pandas as pd
from ekstrak import ekstrak_dataframe
from ekstrak import path_file_dataframe


def split_date_and_time(column_datetime):
    date_time_str = column_datetime.astype('str')
    date_time_expand = date_time_str.str.split('T',expand=True)
    return date_time_expand

def drop_column_old(df,column_old):
    return df.drop(column_old, axis=1)

def transfrom():
    dataframe = ekstrak_dataframe(path=path_file_dataframe())
    print('[Transform] Split Column pickup_datetime')
    pickup_date_time = split_date_and_time(dataframe.pickup_datetime)
    print('[Transform] Split Column dropoff_datetime')
    dropoff_date_time = split_date_and_time(dataframe.dropoff_datetime)
    dataframe = dataframe.assign(
        pickup_date = pickup_date_time[0],
        pickup_time = pickup_date_time[1],
        dropoff_date = dropoff_date_time[0],
        dropoff_time = dropoff_date_time[1]
    )
    print('[Transform] Drop Columns Old')
    dataframe = drop_column_old(dataframe,['pickup_datetime','dropoff_datetime'])
    dataframe.to_csv('clean/nyc_tlc_yellow_trips_2018_subset_1_CLEAN.csv',index=False)
    
def main():
    print('[Transform] Start')
    transfrom()
    print('[Transform] End')
    print('[====================]')