import pprint
import requests
import urllib

hasCountry = hasRegion = false

if Hook['params']['country'] is not None:
  hasCountry = true
if Hook['params']['region'] is not None:
  hasRegion = true

country = region = ""
if hasCountry:
  country = "?food dbo:country dbr:" + Hook['params']['country'] + " . "
if hasRegion:
  region = "?food dbo:region dbr:" + Hook['params']['region'] + " . " 
  
print(country)
print(region)


q = """PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbr: <http://dbpedia.org/resource/>
select distinct ?food
where {
?food rdf:type dbo:Food . """ + country + region + """}
LIMIT 100"""
params = {"query":q}
ash = urllib.urlencode(params)

DBpedia = "http://dbpedia.org/sparql?"+ash+"&format=json&run=+Run+Query+"


r = requests.get(DBpedia)
print(r.text)
