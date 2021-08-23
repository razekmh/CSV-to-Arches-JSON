import json
import uuid


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
    })


for node in node_list:
    # print(node)
    for group in nodegroup_list:
        if node['nodegroup_id'] == group['nodegroupid']:
            print(f"groupid = {node['nodegroup_id']}, parentgroup = {group['parentnodegroup_id']}")