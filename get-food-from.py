import pprint
import requests
import urllib
#import json

from SPARQLWrapper import SPARQLWrapper, JSON


empDB = []
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
  
print(country)
print(region)


q = """PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbr: <http://dbpedia.org/resource/>
select distinct ?food ?thumbnail
where {
?food rdf:type dbo:Food . """ + country + region + """
  OPTIONAL {
           ?food <http://dbpedia.org/ontology/thumbnail> ?thumbnail .
       }
}
LIMIT 100"""
params = {"query":q}
ash = urllib.urlencode(params)

DBpedia = "http://dbpedia.org/sparql?"+ash+"&format=json&run=+Run+Query+"

#DBlink = DBpedia['value']


r = requests.get(DBpedia)
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
  PREFIX dbo: <http://dbpedia.org/ontology/>
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
  PREFIX dbr: <http://dbpedia.org/resource/>
  select distinct ?food ?thumbnail  
  where {
    ?food rdf:type dbo:Food . """ + country + region + """
      OPTIONAL {
             ?food <http://dbpedia.org/ontology/thumbnail> ?thumbnail .
       }
  }
LIMIT 100
""")

# JSON example
print '\n\n*** JSON Example'
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
for result in results["results"]["bindings"]:
    print result["food"]["value"]
