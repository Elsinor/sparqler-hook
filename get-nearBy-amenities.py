print('lol')
import pprint
import requests
import urllib
import json

x=1
if x==1:
    lng = "38.117665"
    print('lng: ' + lng + '<br>')
    if x==1:
        lat = "13.3678464"
        print('lat: ' + lat + '<br>')
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
       
