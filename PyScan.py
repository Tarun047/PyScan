import sys
import FileProcessor
import NetWire
import DataCenter
import time
import Visuals
from pprint import pprint

_my_key = "<your_api_key_here>"
def check_hash(cs):
    iCon = NetWire.Connector(_my_key, cs)
    iCon.getConnection()
    return iCon.getInfo()


cs = FileProcessor.Loader(sys.argv[1]).compute()
D = DataCenter.Loader()
result = D.query(cs)
if result == None:
    result = check_hash(cs)
    if result['response_code']!=1:
        print("Hash Not Found: Please Wait while we retrieve result")
        iUploader = NetWire.Uploader(_my_key,(sys.argv[1],open(sys.argv[1],'rb')))
        iUploader.initUpload()
        time.sleep(30)
        t = 20
        result = check_hash(cs)
        while result['response_code']!=1:
            print("Retrieving....")
            result = check_hash(cs)
            print(t)
            t+=20
            time.sleep(30)
    D.insert(cs,result,result['positives'])
Visuals.Application(res = result)

