# UOCIS322 - Project 6 #

### Author: Justin Noah

### Contact: jnoah@uoregon.edu

### Description

This project is an ACP Brevet time calculator. Any brevets submitted are added to a mongo database and the last brevet submitted using the 'Submit' button can be retrieved using the 'Display' button.

This webapp front-end is written with bootstrap and jquery as well as HTML/CSS/JavaScript. The front-end communicates with the back-end python/flask app. In turn the back-end communicates with another service called api, which manages the MongoDB storage backend. The front-end never touches api.

In total, there are three docker services for this project:
- brevets - HTML/CSS/JavaScript, jQuery, Bootstrap front-end served by a python/flask back-end.
- api - A python/flask/flask-restful RESTful API the brevets back-end uses to communicate with the MongoDB storage service
- db - A standalone MongoDB service, communicated to (only) by the api service

### Algorithm

#### Open
To calculate the open time: control distance is rounded and clamped at the brevet control distance, then all brevet controls are iterated through and if the clamped distance is over the control distance, the control distance is subtracted from the clamped distance and divided by that control's max speed. This time is then the time to shift by and is added to the brevet start time resulting in the opening time.

#### Close
To calculate the close time: like with the open method, close starts by clamping the control time at the brevet control distance. Then special cases are considered, such as the control is less than or equal to 60km case and the control distance being the same as the brevet control distance. If the control is not special, then the method iterates through the brevet controls. While iterating, firstly, any brevet control distances above the given brevet control distance is skipped. Then the method checks if the clamped distance is between two brevet controls. If so, it then checks for a clampped distance less than 600 and simply divides the control by the min speed of 15kph if so, otherwise it adds the max time for the 600km brevet and adds the remainder distance divided by the minimum speed for that control (601km-1000km is 11.428kph). The start time is then shifted by the time calculated resulting in the closing time.

### Setup and Usage Instructions

Run:

```docker compose up --build```

Use:

Open ```http://localhost:5002``` in your favorite browser

---------------------

Sources:

https://mongodb.com

https://pymongo.readthedocs.io

https://developer.mozilla.org

https://docs.docker.com

https://stackoverflow.com/questions/1394020/jquery-each-backwards

https://stackoverflow.com/questions/499405/change-the-selected-value-of-a-drop-down-list-with-jquery
