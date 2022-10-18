# microworks-b
- Django restframework Web Api for taking daily attendance of people

## Requirements

- Python3.8.10
- Djanog 4.1
- Django restframework

## Set up and Installation
- Clone the repository
```bash
git clone https://github.com/Michael-Otieno/microworks-b/
```
 - Create and activate virtual environment
 ```bash
 python3 -m venv .venv - source .venv/bin/activate  
 ```
 - Install dependencies
  ```bash
pip install -r requirements.txt 
 ```
 ## Structure
 | Endpoint | HTTP Method   | CRUD Method  | Result |
| :---:   | :---: | :---: |:---: |
| `attendance-list` | GET   | READ  |Get all attendance list  |
| `attendance/:id` | GET   | READ  |Get attendance detail  |
| `attendance-list` | POST  | CREATE  |Create a new attendance  |
| `attendance/:id` | PUT   | UPDATE  |Update atendance detail  |
| `attendance/:id` | DELETE  | DELETE |Delete atendance detail  |

## Use
- We can use [Postman](https://www.postman.com/) or `curl -i -H ` for testing the Rest Api
 
- Since anyone can make a post and get request to the API without authentication:
### Get list of attedance
 `Request GET  /attendance-list/`
 ```bash
 curl -i -H 'Accept: application/json' http://localhost:7000/attendance-list//
 ```

##### Response
```bash 
HTTP/1.1 200 OK
Date: Tue, 24 Feb 2022 07:36:30 GMT
Status: 200 OK
Connection: close
Content-Type: application/json
Content-Length: 1

[]

 ```
 
- ##### Request
 `POST /attendance-list/`
 ```bash
 curl -i -H 'Accept: application/json' -d 'full_name=Foo&email=foo@gmail.com&machine_id=121w&availability=Present' http://localhost:7000/attendance-list/
 ```

- ##### Response
```bash 
HTTP/1.1 201 Created
Date: Thu, 24 Feb 2011 12:36:30 GMT
Status: 201 Created
Connection: close
Content-Type: application/json
Location: /thing/1
Content-Length: 36

{"id":1,"full_name":"Foo","email":"foo@gmail.com","machine_id":"121w","availability":"Present"}

 ```
 
