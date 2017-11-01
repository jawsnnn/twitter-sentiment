import re
import sys
import string
import json

rawfile = sys.argv[1]

counter = 0

# Declare geo data dictionary
geo_data= {
    "type":"FeatureCollection"
    , "features" : []
    }

with open(rawfile, 'r') as fr:
    for line in fr:
        #print "PREPROCESSED: "+re.sub(r'[\r\n]', '', line)
        if re.sub(r'[\r\n]', '', line):
            try:
                data = json.loads(re.sub(r'[\r\n]', '', line))
                counter+= 1
                if data['place']:
                    print(data['place'])
            except KeyError as ke:
                print("Ignoring non-english lines")
                print(ke)
                continue
            except Exception as e:
                print(line)
                raise e
print(geo_data)
