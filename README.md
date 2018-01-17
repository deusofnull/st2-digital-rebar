# Digital Rebar Stackstorm Action Pack 
## With PoC Device42 provisioning automation 

# actions: 
- create_dhcp_resrvation: creates a DHCP reservation for machines MAC -> IP address  
- create_machine:  creates a machine object on DRP
- get_machines: gets machines from DRP with a filter. 
- provisioning_automation:  gets device on D42, creates it on DRP, makes DHCP reservation for machine.  This is an action chain that depends on having the [device42](https://github.com/StackStorm-Exchange/stackstorm-device42) stackstorm action pack installed.  

# rules
- provisioning_automation_rule:  listens for d42 lifecycle event webhooks and kicks off the provisioning_automation action chain when they occur. 

# installation:
execute: 
```$ st2 pack install https://github.com/deusofnull/st2-digital-rebar/tree/master/actions``` 

Fill config file ```digitalrebar.yaml.example```  with your relevent environment information and move the file to:  
```/opt/stackstorm/configs/digitalrebar.yaml```




 
