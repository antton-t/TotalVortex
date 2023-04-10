import pandas as pd

def main() ->int:
    
    data = pd.read_csv('./physionet.org/files/Raw_Data/s01_ex01_s01.txt')
    print(data)
    data = data.filter(regex="^(?!.*Other).*$")
    data.to_csv('filter.csv')
    data = pd.read_csv('filter.csv', header=None)
    print(data)
    print("-------------")
    print(data[3])
    print("-------------")
    print(data[4])
    print("-------------")
    print(data[5])
    print("-------------")
    print(data[6])
    print("-------------")
    print(data[7])


    return 0

if __name__ == "__main__":
    SystemExit(main())