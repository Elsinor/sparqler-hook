import pprint
import requests
import urllib
import json

if Hook['params'].has_key('lng'):
    lng = Hook['params']['lng']
    if Hook['params'].has_key('lat'):
        lat = Hook['params']['lat']
        q = """PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        Prefix lgdo: <http://linkedgeodata.org/ontology/>
        Prefix geom: <http://geovocab.org/geometry#>
        Prefix ogc: <http://www.opengis.net/ont/geosparql#>

        Select *
        From <http://linkedgeodata.org> {
        ?uri
            a lgdo:Amenity ;
            rdfs:label ?name ;    
	    geom:geometry [
		ogc:asWKT ?g
	    ] .
            Filter(bif:st_intersects (?g, bif:st_point (""" + lng + ", " + lat+ """), 0.2)) .
        } Limit 10
        """
        
        params = {"query":q}
        ash = urllib.urlencode(params)
        LinkedGeoData = "http://linkedgeodata.org/sparql?"+ash+"&format=application%2Fsparql-results%2Bjson&timeout=0"#
        
        #DBlink = DBpedia['value']
        
        
        r = requests.get(LinkedGeoData)
        results = json.loads(r.text)
        
        
        geodat = {}
        
        for result in results["results"]["bindings"]:
          
          if result['name'].has_key('value'):
            name = result['name']['value']
        
            if result['uri'].has_key('value'):
              uri = result['uri']['value']
          
            geodat[uri] = {}
            geodat[uri]["name"] = name
            
        geodat = json.dumps(geodat)
        print(geodat)        
