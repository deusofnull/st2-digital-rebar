from lib.base_action import BaseAction 
import json 


class CreateMachine(BaseAction):

    def run(self, address=None, available=None, bootenv=None, name=None, 
            profile=None, profiles=None, uuid=None, stage=None, os=None, 
            description=None, serial_number=None,):

        uri = '/api/v3/machines'

        payload= {
            "Address": address,
            "Available": available, 
            "BootEnv": bootenv,
            "Profiles": profiles,
            "Profile": profile,
            "Uuid": uuid,
            "Name": name,
            "Stage": stage,
            "OS": os,
            "Description": description,
        }

        response = self.postAPI(endpoint=uri, payload=json.dumps(payload))

        if type(response) is list or type(response) is dict:
            return response
        else:
            return response.text
