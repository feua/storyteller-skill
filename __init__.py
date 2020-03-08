from mycroft import MycroftSkill, intent_file_handler


class Storyteller(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('storyteller.intent')
    def handle_storyteller(self, message):
        self.speak_dialog('storyteller')
	#provaprovaprova

def create_skill():
    return Storyteller()

