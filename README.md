# Energy Management Platform
Used Django Framework, follow the steps to start the project:
create venv and activate it
Install Requirements: (pip install requirements.txt)
run migrations ("python manage.py makemigrations" and then "python manage.py migrate")
run server with python manage.py runserver


API DOC:
it is necessary to create a super


REGISTER:
it is possible to register via:
"regiser/"
after doing so you will be registered as a "common" user with limited ability

LOGIN:
it is possible to login via:
"api/login/"
providing in the body request your "username" and "password"
a DRF Token	 will be provided which you will need to put as HEADER as "Authorization" : "Token 'Your DRF Token	'"

PERMISSION:
There are 3 types of permissions:
User
Technician
Admin

AS A USER YOU WILL BE ABLE TO
-------------------------------------------------------------------------------------
MetricSubscription   (CREATE, DELETE, RETRIEVE, UPDATE ,RETRIEVE within a specific Timeframe)

"metrics-subscription/": here you will be able to:

GET: all the available metrics subscriptions
POST: create a metric subscription

"metrics-subscription/<int:pk>/":
GET: get a single metrics subscriptions
PUT: edit a single metric subscription
DELETE: Delete a singular metric subscription

"metric-subscriptions-timeframe/":
GET: any metric subscription within a specific time frame, an examble could be "metric-subscriptions-timeframe/?start=2025-06-16T00:00:00&end=2025-07-17T23:59:59"
-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
devices-metrics (RETRIEVE)

"devices-metrics/<int:pk>/":
GET: you will be able to retrieve a specific device metric

-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------



AS A TECHNICIAN YOU WILL BE ABLE TO:
do everything listed above and:
-----------------------------------------------------------------------------------
devices-metrics (CREATE, RETRIEVE)

"devices-metrics/":
POST: Create a device metric (it is required to specify the site in the device metrics so that the services Checks for the Technician validity | if not provided then the API access will be forbidden)
-----------------------------------------------------------------------------------
 devices (CREATE, UPDATE, DELETE, RETRIEVE)

"devices/"
GET: by providing a valid "site" if the logged user is  Technician within the site it will retireve the devices of that site
POST: by providing a valid "site" if the logged user is  Technician within the site it will create the device within that site

"devices/<int:pk>/"
GET: a valid Technician will retireve the device of that site
PUT: a valid Technician will update the device of that site
DELETE: a valid Technician will delete the device of that site
-----------------------------------------------------------------------------------


AS A ADMIN YOU WILL BE ABLE TO:
do everything listed above and:
-----------------------------------------------------------------------------------
you will have access to assign technician roles and create and edit sites:
SITES

"sites/":
CREATE: a single site
GET: the list of all sites

"sites/<int:pk>/":
GET: retrieve single site

"sites/<int:pk>/update/":
UPDATE: single site

"sites/<int:pk>/delete/":
DELETE: single site

-----------------------------------------------------------------------------------
TECHNICIANS

"technicians/"
POST: Create a technician from an existing user
GET: the list of all technicians and their assigned sites

"technicians/<int:pk>/"
DELETE: a single technician
UPDATE: a single technician
RETRIEVE: a single technician























