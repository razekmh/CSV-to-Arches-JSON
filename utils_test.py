import json
import uuid
from collections import defaultdict
from itertools import filterfalse

'''TODO
- Build the group structure
    - find top node
    - find first level nodes
    - recurse over the rest of the groups to find the next levels ..
- Add node info'''


'''Define the source files'''
res_model_json = "Test JSON upload.json"
# data_csv = "test_json_upload_data.csv"
res_model_json = "Activity Resource Model.json"

'''read json from resource model structure'''
with open(res_model_json, 'r') as file_rm:
    rm_json = json.load(file_rm)

'''get nodegroups'''
nodegroup_list = rm_json['graph'][0]['nodegroups']

'''get nodes'''
node_list = []
# print(rm_json['graph'][0]['nodes'])
for node in rm_json['graph'][0]['nodes']:
    node_list.append({
        'nodeid' : node['nodeid'],
        'nodegroupid' : node['nodegroup_id'],
        'name' : node['name'],
        'istopnode' : node['istopnode'],
        'datatype' : node['datatype'],
        'config' : node['config'],
    })

'''create cascading group strcture'''
nodegroup_links =[]
for group in nodegroup_list:
    if group['parentnodegroup_id']:
        nodegroup_links.append((group['parentnodegroup_id'],group['nodegroupid']))
    else:
        nodegroup_links.append(("Root",group['nodegroupid']))

def get_nodes(node):
    d = {}
    d['nodegroupid'] = node
    group_info = [group for group in nodegroup_list if group['nodegroupid'] == node]
    if len(group_info) > 0:
        group_info = group_info[0]
        d['cardinality'] = group_info['cardinality']
        d['legacygroupid'] = group_info['legacygroupid']
        d['parentnodegroup_id'] = group_info['parentnodegroup_id']
        d['childrennodes'] = [node for node in node_list if node['nodegroupid'] == d['nodegroupid']]
    children = get_children(node)
    
    if children:
        d['childrengroups'] = [get_nodes(child) for child in children]

    return d

def get_children(node):
    return [x[1] for x in nodegroup_links if x[0] == node]

'''export the structure to a json file'''
tree = get_nodes('Root')
# print(json.dumps(tree, indent=4))
with open(f'{res_model_json[:-4]}_tree.json', 'w') as tr:
        json.dump(tree, tr)