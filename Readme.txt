All APIs are secured. 
Please use this Token: 694abb9b9651e6e31c936cc3eabf1be5686ea1be or genrate a new one using the first API below


1- To Generate a Token:

Request type: POST
URL:  http://127.0.0.1:8000/api/api-token-auth/
Request body:
{
	"username":"Django",
	"password":"Meta@123"
}



2- To Create a booking 

request type: POST
URL: http://127.0.0.1:8000/api/booking/
Request Body:
{
	"name": "McDonald",
	"no_of_guests": 4 ,
	"booking_date": "2023-10-25 09:30"
	
}


3- To Get all bookings

request type: GET
URL: http://127.0.0.1:8000/api/booking/


4- To Get a Single booking

request type: GET
URL: http://127.0.0.1:8000/api/booking/1



5- To Get all Menu Items

request type: GET
URL: http://127.0.0.1:8000/api/menu-items/


6- To Get a single menu item

request type: GET
URL: http://127.0.0.1:8000/api/menu-items/1

