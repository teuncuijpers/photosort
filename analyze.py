"""
Analysis script to determine: 
- some exploratory data analysis
- which cameras/resolutions have taken pictures and whether it's possible to distinguish the photo owner's camera(s) from other's cameras. 
- distribution of pictures over time, indicative of events/timespaces in which many photos were taken. 
"""

import pickle
import duckdb
import pandas

def main(): 
    with open(r"data/df_no_duplicates.pickle", "rb") as f: 
        df = pickle.load(f)

    print(df.head(3))

    # counts
    duckdb.sql("select count(*) as count, CameraMake, CameraModel from df group by CameraMake, CameraModel order by count(*) desc limit 20").show()
    duckdb.sql("select Filepath from df where df.CameraMake IS NULL and df.CameraModel IS NULL limit 20 offset 100").show()

if __name__ == "__main__": 
    main()