import json 

data_1 = './data/data_1.json'
data_2 = './data/data_2.json'
schema = './schema/schema_1.json'
#Creating a function that will open and load the json file.
def readfile(file, dump_location):
    read_file = open(file)
    data = json.load(read_file)
    dump_data = json.dumps(data, indent=4)
    dump_file = open(dump_location, 'w')
    read_file.close
    dump_file.write(dump_data)
    dump_file.close()
    

# readfile(data_1)
# readfile(data_2)


def getMessage(file):
    with open(data_1) as file:
        data = json.load(file)
        for key, value in data.items():
            if key == "message":
                    new_value =  value
                    for key, value in new_value.items():
                        data_required = value
                        data_required["required"] = False
                        # print(data_required)
                        pass
                    
            elif key == "attributes":
                attribute_data = data["attributes"]
                for key, value in attribute_data.items():
                    # print(key)
                    pass
                   
                    
                
readfile(data_1, schema)