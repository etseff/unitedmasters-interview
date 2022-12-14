# UnitedMasters Interview

## Overview
I have designed a Flask web app with 3 routes: home page, generate short URL page,
retrieve long URL page. I used bits of the HTML and styling from the
[Flask tutorial project](https://github.com/pallets/flask/tree/main/examples/tutorial)
to save time on the basic styling of the application. I've added comments throughout the code
to explain functionality or point out future work opportunities.

## Data Model:
For this implementation, I have decided that the URL mappings will be stored in two key-value maps
stored locally using the ```Storage``` class. I have decided on two key-value maps for efficiency
in queries of both directions (long URL to short URL, and short URL to long URL). If this project were being pushed to production, I would have used some sort of cloud-based key-value store such as AWS DynamoDB. A consideration for maintaining two maps is ensuring consistency between the maps. The current functionality supported only inserts into to the two maps, but implementing delete/update functionality would exacerbate this issue.

## Assumptions:
Note: Given the resources, I would normally confirm these questions with a PM

* The shortened URL is assigned a new domain, "http://elieurlgenerator.com/"
* The shortened URL extension is 10 characters

## Outstanding Questions:
* Is one of the actions likely to be more common than the other? (e.g. generating a short URL is much more common than retrieving a long URL from a short URL)?

## Run the Service:
1. Clone the repository
2. Navigate into the directory: ```cd unitedmasters-interview```
3. Instantiate a virtual environment: ```python3 -m venv venv```, ```. venv/bin/activate```
4. Install relevant packages: ```pip install flask```, ```pip install validators```
5. Run the app: ```flask --app url run``` (The app will be running at http://127.0.0.1:5000)

## Time Spent
3 hours



