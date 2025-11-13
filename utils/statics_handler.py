from utils import file_handler
from time import time

def save_statics(endpoint_data:dict):
    data = file_handler.get_endpoints()
    if data:
        for end_p in data:
            if end_p['url'] == endpoint_data['url'] and end_p["method"] == endpoint_data["method"]:
                end_p['stats']['total_requests_received'] += 1
                end_p['stats']["avg_handling_time"] = endpoint_data['time']
                file_handler.save_endpoints_data(endpoint_data) 
                return
        endpoint_data['stats'] = {'total_requests_received':1}
        file_handler.save_endpoints_data(endpoint_data)     
            
               
                

