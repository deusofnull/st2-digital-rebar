from lib.base_action import BaseAction
import json

class Create_DHCP_Reservation(BaseAction):

    def run(self, address=None, options=None, strategy=None, token=None):

        if strategy is None:
            strategy = "MAC"

        uri = '/api/v3/reservations/'

        payload = {
            "Addr": address,
            "Options": [{
                "Code": 1,
                "Value": "255.255.255.0"
            }],
            "Strategy": strategy,
            "Token": token 
        }

        response = self.postAPI(endpoint=uri, payload=json.dumps(payload))

        if type(response) is list or type(response) is dict:
            return response
        else:
            return response.text

