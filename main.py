import csv
import json
import uuid
# import yaml

# TODO
# multiple instances per resource:
#   group the rows according to the resourceID
#   create multiple tiles per attribute
#
# cascading stracture:
#   check for parent tiles and create them >> unchecked
# 
# concepts:
#   check attribute type
#   find coorrespending concept
# 
# checks:
#   Does it support all datatypes? (GeoJSON??)
#   Does it take paramenters? 
#   Clean up the code


# parameters
res_model_json = "Activity Resource Model.json"
data_csv = "Activity Resource Model_data.csv"

res_model_json = "Test JSON upload.json"
data_csv = "test_json_upload_data.csv"

# read json from resource model structure
with open(res_model_json, 'r') as file_rm:
    rm_json = json.load(file_rm)

# copy nodegroup object
nodegroup_list = rm_json['graph'][0]['nodegroups']
# print(nodegroup_list)
# get graphid from the first card
print(nodegroup_list)
graphid = rm_json['graph'][0]['cards'][0]['graph_id']

# get node attributes
node_list = []
print(rm_json['graph'][0]['nodes'])
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
    

def create_res(graphid, grouped_nodes, row, legacy_id=''):
    # create resource instance
    id = legacy_id
    if id == '':
        id = str(uuid.uuid4())
    res = {}
    res['resourceinstance'] = {
        "resourceinstanceid" : id, "graph_id" : str(graphid), "legacyid" : id}
    tiles =[]
    for item in grouped_nodes.items():
        if item[0]:
            tiles.extend(create_tile(item, id, row))
    res['tiles'] = tiles
    return res


def create_tile(card, resid, row, parent=None, tiles=None, tileid=str(uuid.uuid4())):
    # create tile
    # print(card)
    if not parent: 
        tiles = []
    tile = {}   
    tile['tileid'] = tileid
    tile['resourceinstance_id'] = resid
    tile['nodegroup_id'] = card[0]
    tile['sortorder'] = 0
    tile['parenttile_id'] = None
    tile['data'] = build_data(card, row)
    
    for nodegroup in nodegroup_list:
        if tile['nodegroup_id'] == nodegroup['nodegroupid'] and nodegroup['parentnodegroup_id'] is not None:
                print(nodegroup['parentnodegroup_id'])
                parenttile_id = str(uuid.uuid4())
                tile['parenttile_id'] = parenttile_id
                tiles.append(tile)
                create_tile(card=(nodegroup['parentnodegroup_id'],None), resid=resid, row=row, tiles=tiles, tileid=parenttile_id)
    if tile not in tiles:
        tiles.append(tile)
    # print(card)
    # here check for parent and then recurseive call to the same function with the parent ID to create a parent tile
    # create_tile(None, resid,  
    return tiles

def build_data(card,row):
    data = {}
    # print(card, "/n/n/n")
    # print(data_dict)
    if card[1] is None:
        print("empty card")
        return data
    card_data = card[1]
    for value in card_data:
        if value['name'] in row.keys():
            data[value['nodeid']] = row[value['name']]
    return data


def create_json(resources):

    json_data = {}
    resources_list = {'resources' : resources}
    json_data['business_data'] = resources_list
    return json_data



def build_json():
    resources = []
    with open(data_csv) as file_act_data:
        act_data = csv.DictReader(file_act_data)
        for row in act_data:
            resources.append(create_res(graphid, grouped_nodes, row))
    
    built = create_json(resources)
    # print(built)
    with open(f'{data_csv[:-4]}.json', 'w') as fp:
        json.dump(built, fp)
    # return built

build_json()

print("Done!")