from lib.base_action import BaseAction


class GetMachines(BaseAction):

    def run(self, address=None, uuid=None, limit=100, name=None):
        
        uri = '/api/v3/machines'
        
        params = {
            'Address': address, 
            'Uuid': uuid, 
            'limit': limit, 
            'Name': name
        }
        
        response = self.getAPI(endpoint=uri, params=params) 

        if type(response) is list or type(response) is dict:
            return response 
        else:
            return response.text 
