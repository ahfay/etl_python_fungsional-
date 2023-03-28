from base import conn_psg
import pandas as pd

def load_dataframe_psg(df,conn, name_table):
    df = pd.read_csv(df)
    df.to_sql(name_table, conn, if_exists="replace",index=False)
    conn.close()

path = 'clean/nyc_tlc_yellow_trips_2018_subset_1_CLEAN.csv'

def main():
    print('[Load] Start')
    print('[Load] to PostgreSQL')
    load_dataframe_psg(path, conn_psg,'etl_clean')
    print('[Load] End')