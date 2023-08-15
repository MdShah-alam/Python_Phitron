

class Phone:
    color='cBufferCallback'
    features=['camera','water proof']
    
    def call():
        print('I have a Phone')
        
    def send_sms(number,text):
        sms=f'sending sms : {text}  to : {number} .'
        return sms      
        
my_phone=Phone
my_phone.call()

sms=my_phone.send_sms('01705897560','i missed to miss you')
print(sms)