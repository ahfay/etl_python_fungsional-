import pandas as pd

def path_file_dataframe():
    return 'source/nyc_tlc_yellow_trips_2018_subset_1.csv'

def ekstrak_dataframe(path):
    df = pd.read_csv(path)
    return df


def main():
    print('[Ekstrak] Start')
    print('[Ekstrak] From {}'.format(path_file_dataframe()))
    print('[Ekstrak] End')
    print('[====================]')