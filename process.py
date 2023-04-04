import pandas as pd

def main() ->int:
    
    data = pd.read_csv('./physionet.org/files/Raw_Data/s01_ex01_s01.txt', header = None)
    print(data)
    data = data.drop(data.filter(regex='Other').columns, axis=1)
    print(type(data))
    return 0

if __name__ == "__main__":
    SystemExit(main())