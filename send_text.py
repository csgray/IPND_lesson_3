# Lesson 3.3: Use Classes
# Mini-Project: Send Text

# It can be important for businesses to automate sending
# text messages. In this mini-project we'll uses classes
# to send a text message using Twilio, a library we'll
# download from the Internet and add to Python.

from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC42d533b71291fb33db31de0897575c56"
auth_token  = "de657151d1b9831dc03b9f6ce6e6821c"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Don't make this weird.",
    to="+19079877227",    # Replace with your phone number
    from_="+12256865082") # Replace with your Twilio number
print message.sid

# What is a class?
# Classes create an object template with functions and qualities that can be 
# reused to create multiple objects with the same basic parameters

# What is an instance of a class?
# An instance is a particular example of a class. An instance uses the same
# functions but has different specific parameters to be unique.

# What is another analogy for classes?
# Books are a type of class with individual novels being instances. Books all
# have a cover, title page, chapters, etc. but novels fill in those variables
# with their own information.