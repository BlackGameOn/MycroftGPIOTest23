from mycroft import MycroftSkill, intent_handler
import RPi.GPIO as GPIO

GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

class BuzzerControle(MycroftSkill):
    
    def __init__(self):
        MycroftSkill.__init__(self)
        

    @intent_handler('buzzer_skill.intent')
    def handle_buzzer_skille(self, message):
        self.speak_dialog('buzzer_skill')
        GPIO.output(20,False)
        GPIO.output(21,False)

def create_skill():
    return BuzzerControle()

