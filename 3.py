# Rest and Rest API
# REST:-It is an architectural Guideline to develop Web API
# REST-API:-The API which is developed using REST  is knowns as REST API/RESTful API.
# all the application can communicate with REST Web API ,so that all can communicate with it(API(REST does not depends on any language.))
# HOW REST WEB API WORKS:-
# Application(Client)-->Web API-->Web Application-->Database-->Web Application-->web API-->Application(Client) 

# Client make http request to API
# API will communicate to web application/Database(if needed)
# web Application/Database provides required data to API
# API returns Response Data To CLient.

#Data is in the form of JSON,XML data
# REST API
# CRUD operations:-
# Operation--HTTP methods--Descriptions
# Create--POST--Creating/Posting/Inserting Data
# Read--GET--Readng/Getting/Retrieving Data
# Update--PUT/PATCH--Complete Update-PUT/Partial Update-PATCH
# Delete--DELETE--Deleting Data

# Students API Resource
#  http://xyz.com/api/student
# base url:-xyz.com
# naming convention:-api
# End point:-student 

# Request-Response
# Request for All Students
# Request :-GET:/api/students,Response:-[{'id':1,'name':'Slim'},{'id':2,'name':'shady'}......]

# Request for one student having id=1 
# Request:-GET:/api/students/1,Response:-[{'id':1,'name':'Slim'}]

# Request Posting/Creating/Iserting Data
# Request:-POST:api/students {'name':'yo'},Response:-{'id':3,'name':'yo'}

# Request for updating Data,id=1 
# Request:-PUT or PATCH:-/api/students/1 {'name':'anu'},Response:-[{'id':1,'name':'anu'}]

# Request for Deleting Data,id=1 
# Request:-DELETE:/api/students/1,Response:-{'id':1,'name':'anu'}