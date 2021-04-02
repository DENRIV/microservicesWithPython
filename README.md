# microservicesWithPython


Micro Services with Python


1. Install

pip install web.py

2. Run

Python webservices.py

Server
http://0.0.0.0:8080/


3. Test
http://localhost:8080/paises

4. Info
#Codes :
#	      400 : '400 Bad Request',
#              404 : '404 Not Found',
#              405 : '405 Method Not Allowed',
#              409 : '409 Conflict'


5. CURL

# Curl Linux or Curl Win.10


# OUTPUT, Generate a File : "out.json"
# curl -o out.json http://localhost:8080/paises

# GET Method
# curl -v http://localhost:8080/paises

.
# POST method
# curl -X POST http://localhost:8080/paises -d "{\"code\": \"51\",  \"nombre\" : \"PE\",  \"iso\" : \"51\" }" 
# curl -d @request.json -H "Content-Type: application/json" http://localhost:8080/paises

.
# PUT Method
# curl -d @request.json -H 'Content-Type: application/json' -X PUT http://localhost:8080/paises?code=51&nombre=PE&iso=51


# DELETE Method
# curl -X DELETE http://localhost:8080/paises?code=33


6. postman
# https://www.postman.com/

# POST method
# http://localhost:8080/paises?code=51&nombre=PE&iso=51

# GET Method
# http://localhost:8080/paises

# PUT Method
# http://localhost:8080/paises?code=51&nombre=PERULAND&iso=51

# DELETE Method
# http://localhost:8080/paises?code=51
