import pprint
import requests
import urllib
import json


hasCountry = hasRegion = False

if Hook['params'].has_key('country'):
  hasCountry = True
if Hook['params'].has_key('region'):
  hasRegion = True

country = region = ""
if hasCountry:
  country = "?food dbo:country dbr:" + Hook['params']['country'] + " . "
if hasRegion:
  region = "?food dbo:region dbr:" + Hook['params']['region'] + " . " 
  
q = """PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbr: <http://dbpedia.org/resource/>

select distinct ?food ?thumbnail ?label ?abstract 
where {
?food rdf:type dbo:Food . """ + country + region + """
  OPTIONAL {
           ?food dbo:abstract ?abstract .
           }
  OPTIONAL{
           ?food dbo:thumbnail ?thumbnail .
           }
  OPTIONAL{
           ?food rdfs:label ?label .
       }
}
"""
          
  
params = {"query":q}
ash = urllib.urlencode(params)

DBpedia = "http://dbpedia.org/sparql?"+ash+"&format=json&run=+Run+Query+"

#DBlink = DBpedia['value']


r = requests.get(DBpedia)
results = json.loads(r.text)

foods = {}

for result in results["results"]["bindings"]:
  
  if result['food'].has_key('value'):
    resource = result['food']['value']
    
    if result.has_key('label'):
      name = result['label']['value']
      lang = result['label']['xml:lang']
     
      if foods.has_key(resource):
        foods[resource]['name'][lang] = name
      else:
        foods[resource] = {}
        foods[resource]['name'] = {}
        foods[resource]['descr'] = {}
        foods[resource]['name'][lang] = name
        
        if result.has_key('thumbnail'):
          #food['img'] = result["thumbnail"]["value"]
          img = result['thumbnail']['value']
          foods[resource]['img'] = img

        if result.has_key('abstract'):
          desc = result['abstract']['value']
          foods[resource]['descr'] = desc

foods = json.dumps(foods)
#print(r.text)
print(foods)
