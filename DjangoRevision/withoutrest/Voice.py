from googlevoice import Voice
from googlevoice.util import input

def send(number, message):
    user = 'gani835@gmail.com'
    password = 'pravallikaganesh'

    voice = Voice()
    voice.login(user, password)

    #number = input('Number to send message to: ') # use these for command method
    #message = input('Message text: ')

    voice.send_sms(number, message)