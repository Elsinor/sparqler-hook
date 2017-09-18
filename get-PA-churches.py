import pprint
import requests
import urllib
import json

q = """PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbc: <http://dbpedia.org/resource/Category:>
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>

select distinct ?church ?label ?lat ?long
where 
{
   ?church dct:subject dbc:Churches_in_Palermo . 
   ?church rdfs:label ?label .
   ?church geo:lat ?lat .
   ?church geo:long ?long .
}
"""
          
  
params = {"query":q}
ash = urllib.urlencode(params)

DBpedia = "http://dbpedia.org/sparql?"+ash+"&format=json&run=+Run+Query+"

#DBlink = DBpedia['value']


r = requests.get(DBpedia)
results = json.loads(r.text)

churches = {}

for result in results["results"]["bindings"]:
  
  if result['church'].has_key('value'):
    resource = result['church']['value']

    if result.has_key('label'):
      name = result['label']['value']
      lang = result['label']['xml:lang']      
          
      if churches.has_key(resource):
        churches[resource]['name'][lang] = name
      else:
        churches[resource] = {}
        churches[resource]['name'] = {}
        churches[resource]['name'][lang] = name
        
        lat = result['lat']['value']
        churches[resource]['lat'] = lat
        long = result['long']['value']
        churches[resource]['long'] = long
      
        if result.has_key('thumbnail'):
          #church['img'] = result["thumbnail"]["value"]
          img = result['thumbnail']['value']
          churches[resource]['img'] = img

churches = json.dumps(churches)
#print(r.text)
print(churches)
