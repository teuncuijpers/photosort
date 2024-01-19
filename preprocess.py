import pickle


def main(): 
    with open(r"data/df.pickle", "rb") as f: 
        df = pickle.load(f)

    initial_length = len(df)
    df = df.drop_duplicates(subset=df.columns.tolist()[1:], keep="first")
    processed_length = len(df)
    print(f"Removed {initial_length-processed_length} duplicates, {processed_length} unique records remain.")

    with open(r"data\df_no_duplicates.pickle", "wb") as f:
        pickle.dump(df, f)

if __name__ == "__main__": 
    main()