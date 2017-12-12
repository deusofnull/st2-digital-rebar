import requests
from st2common.runners.base_action import Action


class DigitalRebarBaseException(Exception):
    pass


class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)

        self.drp_server = self.config.get('drp_server', None)
        if not self.drp_server:
            raise ValueError('"drp_server" config value is required')
            # drp_server should be aproximately -> https://00.00.00.00/api/1.0/
        
        self.drp_username = self.config.get('drp_username', None)
        if not self.drp_username:
            raise ValueError('"drp_username" config value is required')

        self.drp_password = self.config.get('drp_password', None)
        if not self.drp_password:
            raise ValueError('"drp_password" config value is required')

        self.verify = self.config.get('verify_certificate', False)

    def getAPI(self, endpoint, params):
        r = requests.get(
            "%s%s" % (self.drp_server, endpoint),
            params=params,
            auth=(self.drp2_username, self.drp_password),
            verify=self.verify
        )
        if r.ok:
            return r.json() 
        else: 
            # return "url - %s%s \n response - %s" % (self.d42_server, endpoint, r)         
            return r


    def putAPI(self, endpoint, params=None, payload=None):
        r = requests.put(
            "%s%s" % (self.drp_server, endpoint),
            params=params,
            data=payload,
            auth=(self.drp_username, self.drp_password),
            verify=self.verify
        )
        if r.ok:
            return r.json()
        else:
            return r

    def postAPI(self, endpoint, params=None, payload=None):
        r = requests.post(
            "%s%s" % (self.drp_server, endpoint),
            params=params,
            data=payload,
            auth=(self.drp_username, self.drp_password),
            verify=self.verify
        )
        if r.ok:
            return r.json()
        else:
            return r

    def post(self, endpoint, headers=None, params=None, payload=None):

        url = "%s%s" % (self.drp_server, endpoint)
        r = requests.post(
                url=url,
                auth=(self.drp_username, self.drp_password),
                headers=headers,
                params=params,
                data=payload,
                verify=self.verify,
        )
        print("url: %s" % url)
        if r.ok:
            return r.json()
        else:
            # return "url - %s%s \n response - %s" % (self.d42_server, endpoint, r) 
            return r 