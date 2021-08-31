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
        'nodegroupid' : node['nodegroup_id'],
        'name' : node['name'],
        'istopnode' : node['istopnode'],
    })

base_structure = {}
for node in node_list:
    # print(node)
    for group in nodegroup_list:
        if node['nodegroupid'] == group['nodegroupid']:
            pass
            # print(f"nodeid = {node['nodeid']}, groupid = {node['nodegroup_id']}, parentgroup = {group['parentnodegroup_id']}")

node_inventory = node_list.copy()
nodegroup_inventory = nodegroup_list.copy()
node_inventory.remove([node for node in node_inventory if node['istopnode']][0])
# print(nodegroup_inventory)

# topnode has no nodegroupid  
# 

base_structure = defaultdict(list)
for main_node in node_list:
    if main_node['istopnode']:
        base_structure["nodegroupid"] = main_node['nodeid']
        break
    # print(base_structure)
    # break
    group_structure = []
for nodegroup in nodegroup_list:
    if nodegroup['parentnodegroup_id']:
        pass
    else:
        group_structure.append({
            'nodegroupid' : nodegroup['nodegroupid'],
            'parentgroup' : None,
            "childrengroups" : [],
            "childrennodes" : [],
            })
        nodegroup_inventory.remove(nodegroup)

print(group_structure)

def check_group(group_structure,checkgroup):
    insertion_detected = False
    # place a group in its location within the structure
    for nodegroup in group_structure:
        if checkgroup['parentnodegroup_id'] == nodegroup['nodegroupid']:
            nodegroup['childrengroups'].append({
            'nodegroupid' : checkgroup['nodegroupid'],
            'parentgroup' : None,
            "childrengroups" : [],
            "childrennodes" : [],
            })
            insertion_detected = True
            break

        if not insertion_detected: 
            nodegroup['childrengroups'], insertion_detected = check_group(nodegroup['childrengroups'],checkgroup)
            print(nodegroup,"\n\n")
    return (group_structure, insertion_detected)

while len(nodegroup_inventory) > 0:
    for nodegroup in nodegroup_inventory:
        group_structure, insertion_detected = check_group(group_structure, nodegroup)
        if insertion_detected: 
            nodegroup_inventory.remove(nodegroup)

    


print(len(group_structure))
print(group_structure)
print(len(node_inventory))
        

    

        # check if the parnet exists 


# while len(node_inventory) > 0:
#     for node in node_list:
#         base_structure = defaultdict(list)
#         # print(node['istopnode'])
#         if node['istopnode']:
#             base_structure["nodegroup_id"] = node['nodegroup_id']
#             for check_node in node_list: 
#                 # base_structure["children_groups"].extend([group['nodegroupid'] for group in nodegroup_list if group['parentnodegroup_id'] == check_node['nodegroup_id']])
#                 print([group['nodegroupid'] for group in nodegroup_list if group['parentnodegroup_id'] == check_node['nodegroup_id']])
#             # base_structure["children_nodes"]
#             # print(node)
#             if node in node_inventory:
#                 node_inventory.remove(node)

    # print(base_structure)    