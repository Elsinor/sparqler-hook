import pprint
import requests
import urllib
import json



data_b = []
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
PREFIX foaf: <http://xmlns.com/foaf/spec/>
select distinct ?food ?thumbnail ?name
where {
?food rdf:type dbo:Food . """ + country + region + """
  OPTIONAL {
           ?food <http://dbpedia.org/ontology/thumbnail> ?thumbnail .
           ?food <http://xmlns.com/foaf/spec/name> ?name .
       }
}
LIMIT 100"""

           
  
  
params = {"query":q}
ash = urllib.urlencode(params)

DBpedia = "http://dbpedia.org/sparql?"+ash+"&format=json&run=+Run+Query+"

#DBlink = DBpedia['value']


r = requests.get(DBpedia)
results = json.loads(r.text)
for result in results["results"]["bindings"]:
  food = {}
  
  if result["food"].has_key('value'):
    food['uri'] = result["food"]["value"]
    
  if result.has_key('thumbnail'):
    food['img'] = result["thumbnail"]["value"]
  
  if result.has_key('name'):
    food['name'] = result["name"]["value"]
    
  data_b.append(food)

print(data_b[0]);
print(data_b)
