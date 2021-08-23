import json
import uuid
from collections import defaultdict
from itertools import filterfalse


res_model_json = "Test JSON upload.json"
data_csv = "test_json_upload_data.csv"

res_model_json = "Activity Resource Model.json"


# read json from resource model structure
with open(res_model_json, 'r') as file_rm:
    rm_json = json.load(file_rm)


# copy nodegroup object
nodegroup_list = rm_json['graph'][0]['nodegroups']


# get node attributes
node_list = []

# print(rm_json['graph'][0]['nodes'])
for node in rm_json['graph'][0]['nodes']:
    node_list.append({
        'nodeid' : node['nodeid'],
        'nodegroup_id' : node['nodegroup_id'],
        'name' : node['name'],
        'istopnode' : node['istopnode'],
    })

base_structure = {}
for node in node_list:
    # print(node)
    for group in nodegroup_list:
        if node['nodegroup_id'] == group['nodegroupid']:
            pass
            # print(f"nodeid = {node['nodeid']}, groupid = {node['nodegroup_id']}, parentgroup = {group['parentnodegroup_id']}")

node_inventory = node_list.copy()

while len(node_inventory) > 0:
    for node in node_list:
        base_structure = defaultdict(list)
        # print(node['istopnode'])
        if node['istopnode']:
            base_structure["nodegroup_id"] = node['nodegroup_id']
            for check_node in node_list: 
                base_structure["children_groups"].extend([group['nodegroupid'] for group in nodegroup_list if group['parentnodegroup_id'] == check_node['nodegroup_id']])
            # base_structure["children_nodes"]
            # print(node)
            if node in node_inventory:
                node_inventory.remove(node)

    print(base_structure)    