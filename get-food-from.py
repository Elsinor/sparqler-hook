country = Hook['params']['country']
region = Hook['params']['region']
print(country)
print(test)

import pprint
import requests
import urllib

q = """PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbr: <http://dbpedia.org/resource/>
select distinct ?food
where {
?food rdf:type dbo:Food .
?food dbo:country dbr:Italy .
}
LIMIT 100"""
params = {"query":q}
ash = urllib.urlencode(params)

DBpedia = "http://dbpedia.org/sparql?"+ash+"&format=json&run=+Run+Query+"


r = requests.get(DBpedia)
print(r.text)
