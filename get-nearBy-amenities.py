import pprint
import requests
import urllib
import json

if Hook['params'].has_key('lng'):
    lng = Hook['params']['lng']
    if Hook['params'].has_key('lat'):
        lat = Hook['params']['lat']
        q = """PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
        Prefix lgdo: <http://linkedgeodata.org/ontology/>

        Select *
        From <http://linkedgeodata.org> {
        ?uri
            a lgdo:Amenity ;
            rdfs:label ?name ;    
            geo:lat ?lat ;
            geo:long ?long .

            Filter(bif:st_intersects (bif:st_point (?long, ?lat), bif:st_point (""" + lng + ", " + lat+ """), 0.1)) .
        }
        """

        params = {"query":q}
        ash = urllib.urlencode(params)

        LinkedGeoData = "http://linkedgeodata.org/sparql?"+ash+"&format=json&run=+Run+Query+"

        #DBlink = DBpedia['value']


        r = requests.get(LinkedGeoData)
        results = json.loads(r.text)

        print (results)

