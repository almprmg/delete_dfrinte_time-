import os
import pandas as pd
import io

timefram = "1m"

path = f"..//data//{timefram}"

files = os.listdir(path)
list_tiker = [i[:-4] for i in files]


for tiker in list_tiker:

    df = pd.read_csv(f"../data//{timefram}//{tiker}.csv",index_col=0)
    if 'Unnamed: 0' in df.columns:
        df =df.drop('Unnamed: 0', axis=1)
   
    if 'Date'  in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        df['TimeDiff'] = df['Date'].diff()
    else:
        df.index = pd.to_datetime(df.index)
        
        df['TimeDiff'] =  df.index.to_series().diff()


    rows_to_delete = df[df['TimeDiff'] > pd.Timedelta(minutes=2)].index

        # حذف الصفوف المحددة
    df = df.drop(rows_to_delete)

    df = df.drop('TimeDiff', axis=1)
    df.to_csv(f"C://Users//dell//Desktop//module Python for Analysis Tradr//data//{timefram}//{tiker}.csv")
import winsound

winsound.MessageBeep()


