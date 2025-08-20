import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-e4c3c-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

def format_year_range(starting_year):
    end_year = starting_year + 4  # Assuming a 4-year program
    return f"{starting_year}-{str(end_year)[-2:]}"

data = {
    "42733034": {
        "name": "Harsha ",
        "major": "CSE Data Science",
        "starting_year": 2022,
        "total_attendance": 10,
        "status": "Present",
        "year": "3rd year",
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "42733037": {
        "name": "Karen Mohan",
        "major": "CSE Data Science",
        "starting_year": 2022,
        "total_attendance": 8,
        "status": "Present",
        "year": "3rd year",
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "42733038": {
        "name": "Krishna Charitha",
        "major": "CSE Data Science",
        "starting_year": 2022,
        "total_attendance": 11,
        "status": "Present",
        "year": "2nd year",
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "42733045": {
        "name": "Likhitha",
        "major": "CSE Data Science",
        "starting_year": 2023,
        "total_attendance": 17,
        "status": "Present",
        "year":"3rd year",
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "42733047": {
        "name": "Lokeshwar",
        "major": "CSE Data Science",
        "starting_year": 2020,
        "total_attendance": 15,
        "status": "Present",
        "year": "4th year",
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "42733054": {
        "name": "Nanda Kishor",
        "major": "CSE Data Science",
        "starting_year": 2023,
        "total_attendance": 17,
        "status": "Present",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34"
    }
}

# Convert starting year to year range
for key, value in data.items():
    starting_year = value['starting_year']
    value['starting_year'] = format_year_range(starting_year)
    ref.child(key).set(value)
