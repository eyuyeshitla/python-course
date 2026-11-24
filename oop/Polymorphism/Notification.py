class EmailNotification:
    def send(self):
        print("Send email notification.")
        
class SmsNotification:
    def send(self):
        print("send sms notification.")
        
class PushNotification:
    def send(self):
       print("send push notification.")
    
def send_notification(message):
    message.send()
    
email =EmailNotification()
sms =SmsNotification()
push =PushNotification()


send_notification(email)
send_notification(sms)
send_notification(push)

print("Challenge completed.")

    
    