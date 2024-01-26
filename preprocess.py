import pickle


def main(): 
    with open(r"data/df.pickle", "rb") as f: 
        df = pickle.load(f)

    initial_length = len(df)
    df.drop_duplicates(subset=df.columns.tolist()[1:], keep="first", inplace=True)
    print(f"Removed {initial_length-len(df)} duplicates, {len(df)} unique records remain.")

    with open(r"data\df_no_duplicates.pickle", "wb") as f:
        pickle.dump(df, f)

if __name__ == "__main__": 
    main()