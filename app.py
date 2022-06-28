import mimetypes
from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body = request.values.get('Body').lower()

    resp = MessagingResponse()
    
    if body == 'yes':
        resp.message("We are glad you enjoyed Drip2Duong Coffee!")
    elif body == 'no':
        resp.message("We are sorry to here that.")
    else:
        resp.message("Please respond to Drip2Duong with yes or no. If you wish to unsubscribe text stop")

    return Response(str(resp), mimetype="application/xml")

if __name__ == "__main__":
    app.run(debug=True)
