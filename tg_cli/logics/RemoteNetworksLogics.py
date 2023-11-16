import sys

sys.path.insert(1, './libs')
sys.path.insert(1, './transformers')
from tg_cli.transformers import GenericTransformers, RemoteNetworksTransformers
from tg_cli.libs import StdAPIUtils

def get_network_list_resources(token,JsonData):
    Headers = StdAPIUtils.get_api_call_headers(token)

    api_call_type = "POST"
    variables = { "cursor":JsonData['cursor']}

    Body = """
    query listGroup($cursor: String!)
        {
          remoteNetworks(after: $cursor, first:null) {
            pageInfo {
              endCursor
              hasNextPage
            }
            edges {
              node {
                id
        name
        updatedAt
        createdAt
        isActive
        connectors{
            edges{
                node{
                    id
                    name
                }
            }
        }
        resources{
            edges{
                node{
                    id
                    name
                }
            }
        }
              }
            }

          }
        }
    """

    return True,api_call_type,Headers,Body,variables

def get_network_show_resources(token,JsonData):
    Headers = StdAPIUtils.get_api_call_headers(token)

    api_call_type = "POST"
    variables = {"itemID":JsonData['itemid']}
    Body = """
         query
            getObj($itemID: ID!){
          remoteNetwork(id:$itemID) {
            id
    name
    updatedAt
    createdAt
    isActive
    connectors{
        edges{
            node{
                id
                name
            }
        }
    }
    resources{
        edges{
            node{
                id
                name
            }
        }
    }
              }
          }
    """

    return True,api_call_type,Headers,Body,variables

def item_show(outputFormat,sessionname,itemid):
    j = StdAPIUtils.generic_api_call_handler(sessionname,get_network_show_resources,{'itemid':itemid})
    output,r = StdAPIUtils.format_output(j,outputFormat,RemoteNetworksTransformers.GetShowAsCsv)
    print(output)
    
def item_list(outputFormat,sessionname):
    ListOfResponses = []
    hasMorePages = True
    Cursor = "0"
    while hasMorePages:
        j = StdAPIUtils.generic_api_call_handler(sessionname,get_network_list_resources,{'cursor':Cursor})
        hasMorePages,Cursor = GenericTransformers.CheckIfMorePages(j,'remoteNetworks')
        ListOfResponses.append(j['data']['remoteNetworks']['edges'])
    output,r = StdAPIUtils.format_output(ListOfResponses,outputFormat,RemoteNetworksTransformers.GetListAsCsv)
    print(output)
