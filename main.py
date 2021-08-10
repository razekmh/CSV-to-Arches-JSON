import csv
import json
import uuid
import yaml

# parameters
res_model_json = "Activity Resource Model.json"
data_csv = "Activity Resource Model_data.csv"

# read json from resource model
with open(res_model_json, 'r') as file_rm:
    rm_json = json.load(file_rm)

# copy nodegroup object
nodegroup_list = rm_json['graph'][0]['nodegroups']

# get global parameters
graphid = rm_json['graph'][0]['cards'][0]['graph_id']

# get node attributes
node_list = []
for node in rm_json['graph'][0]['nodes']:
    node_list.append({
        'nodeid' : node['nodeid'],
        'nodegroup_id' : node['nodegroup_id'],
        'name' : node['name'],
    })
node_list[0]

# open data file
with open(data_csv) as file_act_data:
    act_data = csv.DictReader(file_act_data)
    for row in act_data:
        global data_dict
        data_dict = row
print(data_dict)


def create_json(resources):

    json_data = {}
    resources_list = {'resources' : resources}
    json_data['business_data'] = resources_list
    return json_data


def create_res(graphid, cards, legacy_id=''):
    # create resource instance
    id = legacy_id
    if id == '':
        id = str(uuid.uuid4())
    res = {}
    res['resourceinstance'] = {
        "resourceinstanceid" : id, "graph_id" : str(graphid), "legacyid" : id}
    tiles =[]
    for card in cards:
        tiles.append(create_tile(card, id, card[1]['UUID']))
    res['tiles'] = tiles
    return res


def create_tile(card, resid, nodegroup_id, parent=None):
    # create tile
    tile = {}
    tile['tileid'] = str(uuid.uuid4())
    tile['resourceinstance_id'] = resid
    tile['nodegroup_id'] = nodegroup_id
    tile['sortorder'] = 0
    tile['parenttile_id'] = None
    tile['data'] = Build_data(card)
    return tile

def Build_data(card):
    data = {}
    for key in [key for key in card[1].keys() if key != 'UUID']:
        data[card[1][key]] = csv_row[key]
    return data

print("Done!")