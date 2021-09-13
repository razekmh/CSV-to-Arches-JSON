import json


'''Define the source files'''
res_model_strc = "Activity Resource Model_tree.json"
# data_csv = "test_json_upload_data.csv"

'''read json from resource model structure'''
with open(res_model_strc, 'r') as file_rm:
    rm_json = json.load(file_rm)


'''read cascading json structure'''
def parse_json(node,type, parent_id=None):
    if type == "group":
        
        pass
    if type == "node":

        pass
    if type == "root":

        pass
    print(node)
    childrengroups = get_children('childrengroups',node)
    childrennodes = get_children('childrennodes',node)
    if childrengroups:
        # parent_id = node['']
        for childgroup in childrengroups:
            parse_json(childgroup)
    else:
        # print("no childrengroups")
        pass
    
    if childrennodes:
        for childnode in childrennodes:
            # print(childnode)
            pass

def get_children(childtype,node):
    return(node.get(childtype, None))


parse_json(rm_json)
