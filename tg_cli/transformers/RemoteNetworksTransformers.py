from tg_cli.transformers import GenericTransformers

def GetShowAsCsv(jsonResults):
    columns = ['id','name','isActive','resources','connectors']
    return GenericTransformers.GetShowAsCsvNoNesting(jsonResults, 'remoteNetwork', columns)

def GetListAsCsv(jsonResults):
    columns = ['id','name','isActive','resources','connectors']
    return GenericTransformers.GetListAsCsv(jsonResults, columns)
