from typing import List,TextIO

#file = open('HTV_DATA.csv')    #sample data file can be changed

def csv_to_list(csv_file: TextIO) -> List[List[str]]:

    csv_file.readline()

    data = []
    for line in csv_file:
        data.append(line.strip().split(','))
    return data

def give_recommended_product(product_code: int) -> List[int]:
    file = open('HTV_DATA.csv')   
    data = csv_to_list(file)
    Recommendation = []
    for i in range(len(data)):
        if int(data[i][0]) == product_code:
            for j in range(1, len(data[i])):
                #print("hiii")
                if data[i][j] != '' and int(data[i][j]) != product_code:
                    Recommendation.append(int(data[i][j]))
    return Recommendation
