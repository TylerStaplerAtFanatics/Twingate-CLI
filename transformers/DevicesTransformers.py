import json
import pandas as pd

def GetListAsCsv(jsonResults):

    DeviceList = jsonResults['data']['devices']['edges']
    dfItem = pd.json_normalize(DeviceList)
    return dfItem


def GetUpdateAsCsv(jsonResults,objectname):
    # {"data":{"deviceUpdate":{"ok":true,"error":null,"entity":{"id":"RGV2aWNlOjE5MzI2OQ==","name":"DESKTOP-FFPADSA","isTrusted":true}}}}
    IsOk = jsonResults['data']['deviceUpdate']['ok']
    IsError = jsonResults['data']['deviceUpdate']['error']
    EntityID = jsonResults['data']['deviceUpdate']['entity']['id']
    EntityName = jsonResults['data']['deviceUpdate']['entity']['name']
    EntityIsTrusted = jsonResults['data']['deviceUpdate']['entity']['isTrusted']
    data = [[IsOk,IsError,EntityID,EntityName,EntityIsTrusted]]
    df = pd.DataFrame(data, columns = ['APIResponseOK', 'APIResponseError','DeviceID','DeviceName','isTrusted'])
    return df

def GetShowAsCsv(jsonResults,objectname):

    id = jsonResults['data']['device']['id']
    name = jsonResults['data']['device']['name']
    isTrusted = jsonResults['data']['device']['isTrusted']
    osName = jsonResults['data']['device']['osName']
    deviceType = jsonResults['data']['device']['deviceType']

    data = [[id,name,isTrusted,osName,deviceType]]
    df = pd.DataFrame(data, columns = ['id', 'name','isTrusted','osName','deviceType'])
    return df
