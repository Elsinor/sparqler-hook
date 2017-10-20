import pprint
import requests
import urllib
import json

print('lol')
if Hook['params'].has_key('lng'):
    lng = Hook['params']['lng']
    print('lng: ' + lng + '<br>')
    if Hook['params'].has_key('lat'):
        lat = Hook['params']['lat']
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
        amenities = {}

        for result in results["results"]["bindings"]:
        
        if result['church'].has_key('value'):
            resource = result['church']['value']

            if result.has_key('label'):
            name = result['label']['value']
            lang = result['label']['xml:lang']      
                
            if amenities.has_key(resource):
                amenities[resource]['name'][lang] = name
            else:
                amenities[resource] = {}
                amenities[resource]['name'] = {}
                amenities[resource]['name'][lang] = name
                
                lat = result['lat']['value']
                amenities[resource]['lat'] = lat
                long = result['long']['value']
                amenities[resource]['long'] = long
            
                if result.has_key('thumbnail'):
                #church['img'] = result["thumbnail"]["value"]
                img = result['thumbnail']['value']
                amenities[resource]['img'] = img

        amenities = json.dumps(amenities)
        #print(r.text)
        #print(amenities)
