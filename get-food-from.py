country = Hook['params']['country']
print(country)

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

print(ash)

DBpedia = "http://dbpedia.org/sparql?"+ash+"&format=json&run=+Run+Query+"


print(DBpedia)

r = requests.get(DBpedia)
print(r.text)
