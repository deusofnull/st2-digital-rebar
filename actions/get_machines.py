from lib.base_action import BaseAction


class GetMachines(BaseAction):

    def run(self, address=None, uuid=None, limit=100,available=None, name=None):
        uri = '/api/v3/machines'
        headers = {'Accept':'application/json', 'Content-Type': 'application/json'} 
        params = {
            'address': address, 
            'uuid': uuid, 
            'limit': limit, 
            'available': available, 
            'name': name
        }
        
        response = drp.get(uri=uri, headers=headers, params=params) 

        if type(response) is dict:
            return response 
        else:
            return response.text 
