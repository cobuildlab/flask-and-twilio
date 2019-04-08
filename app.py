#!flask/bin/python
from flask import Flask, jsonify
from twilio.rest import Client
import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
from_number = os.environ['TWILIO_NUMBER']
client = Client(account_sid, auth_token)

app = Flask(__name__)

tasks = []


@app.route('/todo/api/v1.0/create-task', methods=['GET'])
def create_task():
    tasks.append({"id": len(tasks), "title": "Learn Python", "description": "Start with Flask first", "done": False})

    message = client.messages \
        .create(
        body="A Task was created",
        from_=from_number,
        to='+17869913467'
    )
    print(message)
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)
