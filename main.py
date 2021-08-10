import csv
import json
import uuid
import yaml

# TODO
# read the resource model structure JSON
# extract the nodes attributes
# group nodes to based on nodegroup_id

# Read the data csv
# for each new resource create JSON resource
# create tile for each group
# check for parent tiles and create them

# Create the data JSON object

# parameters
res_model_json = "Activity Resource Model.json"
data_csv = "Activity Resource Model_data.csv"

# read json from resource model structure
with open(res_model_json, 'r') as file_rm:
    rm_json = json.load(file_rm)

# copy nodegroup object
nodegroup_list = rm_json['graph'][0]['nodegroups']

# get graphid from the first card
graphid = rm_json['graph'][0]['cards'][0]['graph_id']

# get node attributes
node_list = []
for node in rm_json['graph'][0]['nodes']:
    node_list.append({
        'nodeid' : node['nodeid'],
        'nodegroup_id' : node['nodegroup_id'],
        'name' : node['name'],
    })

# gruop nodes based on the nodegroup_id
grouped_nodes = {}
for node in node_list:
        nodegroup_id = node["nodegroup_id"]
        if nodegroup_id in grouped_nodes:
                grouped_nodes[nodegroup_id].append(node)
        else:
                grouped_nodes[nodegroup_id] = [node]

# open data file
with open(data_csv) as file_act_data:
    act_data = csv.DictReader(file_act_data)
    for row in act_data:
        global data_dict
        data_dict = row


def create_res(graphid, grouped_nodes, legacy_id=''):
    # create resource instance
    id = legacy_id
    if id == '':
        id = str(uuid.uuid4())
    res = {}
    res['resourceinstance'] = {
        "resourceinstanceid" : id, "graph_id" : str(graphid), "legacyid" : id}
    tiles =[]
    for item in grouped_nodes.items():
        tiles.extend(create_tile(item, id))
    res['tiles'] = tiles
    return res


def create_tile(card, resid, parent=None, tiles=None):
    # create tile
    if not parent: 
        tiles = []
    tile = {}   
    tile['tileid'] = str(uuid.uuid4())
    tile['resourceinstance_id'] = resid
    tile['nodegroup_id'] = nodegroup_id
    tile['sortorder'] = 0
    tile['parenttile_id'] = None
    tile['data'] = Build_data(card)
    tiles.append(tile)
    # here check for parent and then recurseive call to the same function with the parent ID to create a parent tile
    # create_tile(None, resid,  
    return tiles

def Build_data(card):
    data = {}
    # print(card, "/n/n/n")
    # print(data_dict)
    if card is None:
        return data
    card_data = card[1]
    for value in card_data:
        if value['name'] in data_dict.keys():
            data[value['nodeid']] = data_dict[value['name']]
    return data


def create_json(resources):

    json_data = {}
    resources_list = {'resources' : resources}
    json_data['business_data'] = resources_list
    return json_data



def build_json():
    resources = create_res(graphid, grouped_nodes)
    
    built = create_json(resources)
    print(built)
    return built

build_json()

print("Done!")