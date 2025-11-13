import json
import os 


def save_user(user_name):
    with open(f"{os.getcwd()}/data/users.txt" , "a") as file:
        file.write(user_name + "\n")

def save_endpoints_data(endpoints_data:dict):
    try:
        with open(f"{os.getcwd()}/data/endpoints_data.json",'r') as file:
            data = json.load(file)
    except:
        data = []    
    
            
    with open(f"{os.getcwd()}/data/endpoints_data.json",'w') as out_file:
        data.append(endpoints_data)
        json.dump(data,out_file,indent=4)


def get_endpoints() -> dict:
    with open(f"{os.getcwd()}/data/endpoints_data.json",'r') as file:
        data = json.load(file)
        return data        