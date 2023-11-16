import sys

from tg_cli.libs import DataUtils

sys.path.insert(1, './libs')
sys.path.insert(1, './responses')

def login(apikey,tenant,sessionname):

    FULLURL = tenant

    DataUtils.StoreAuthToken(apikey,tenant,sessionname)
    DataUtils.StoreTenant(tenant,sessionname)
    print("Session Created: "+sessionname)

def logout(sessionname):
    DataUtils.DeleteSessionFiles(sessionname)
    print("Session deleted: "+sessionname)

def listSessions():
    SessionList,IsError = DataUtils.listSessions()
    if(IsError):
        print("Error retrieving session list.")
        exit(1)
    else:
        print(SessionList)
