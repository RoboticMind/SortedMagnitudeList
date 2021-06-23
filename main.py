import requests
import json
import sys
import pprint

def RPC_call(method, params, rpcuser, rpcpassword):
	url="http://127.0.0.1:15715/"
	if len(params) > 0:
		if type(params) == str:		
			payload = json.dumps({"jsonrpc":1.0,"method": method, "params": [params],"id":"test"})
		else:
			payload = json.dumps({"jsonrpc":1.0,"method": method, "params": params,"id":"test"})
	else:
		payload = json.dumps({"jsonrpc":1.0,"method": method,"id":"test"})
	
	headers = {'content-type': "text/plain", 'cache-control': "no-cache"}
	request_one = requests.Session()
	request_one.auth = (rpcuser,rpcpassword)
	response = request_one.request("POST", url, data=payload, headers=headers)
	
	if json.loads(response.text)["result"] != None:
		response = json.loads(response.text)["result"]	
		return response
	else:
		print(response.text)		
		return -1


RPC_username = input("enter your RPC username: ")
RPC_password = input("enter your RPC password: ")


#test the RPC connection
if RPC_call("help",[],RPC_username,RPC_password) == -1:
	sys.exit()

#get the actual relevent data
allData=RPC_call("currentcontractaverage",[],RPC_username,RPC_password)
mags=allData["contract"]["magnitudes"]

#sort it
sortedMags = sorted(mags.items(), key=lambda item: item[1]) #ref: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

#print it nicely
pprinter = pprint.PrettyPrinter(indent=4)
pprinter.pprint(sortedMags)



