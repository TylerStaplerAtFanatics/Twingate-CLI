import requests
import json
import sys
import os
import urllib.parse

sys.path.insert(1, './libs')
sys.path.insert(1, './transformers')
import DataUtils
import GenericTransformers
import GroupsTransformers
import StdResponses
import StdAPIUtils

def get_group_list_resources(sessionname,token,JsonData):
    Headers = StdAPIUtils.get_api_call_headers(token)

    api_call_type = "POST"

    Body = """
            {
  groups(after: null, first:1000) {
    edges {
      node {
        id
        name
        createdAt
        updatedAt
        isActive
        type
        users {
            edges{
                node{
                    id
                    email
                    firstName
                    lastName
                }
            }
        }
        resources {
            edges{
                node{
                    id
                    name
                    address {
                        type
                        value
                    }
                    isActive
                }
            }
        }

      }
    }
    pageInfo {
      startCursor
      hasNextPage
    }
  }
}
    """

    return True,api_call_type,Headers,Body,None


def group_list(outputFormat,sessionname):
    StdAPIUtils.generic_api_call_handler(outputFormat,sessionname,get_group_list_resources,{},GroupsTransformers.GetListAsCsv,'groups')
