import json

def save_user(user_name):
    with open(r"C:\analiza\week_four_test\data\users.txt" , "a") as file:
        file.write(user_name + "\n")

def save_endpoints_data(endpoints_data:dict):
    try:
        with open('data/endpoints_data.json','r') as file:
            data = json.load(file)
    except:
        data = []    
    
            
    with open('data/endpoints_data.json','w') as out_file:
        data.append(endpoints_data)
        json.dump(data,out_file,indent=4)


def load_data():
    with open('data/endpoints_data.json','r') as file:
        data = json.load(file)
        return data        