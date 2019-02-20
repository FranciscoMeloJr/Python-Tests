class Exp:

    def __init__(self, sentence, time=0):
    	self.sentence = sentence
    	self.time = time

    def get_sentence(self):
    	return self.sentence

    def set_sentence(self, tobe_sent):
    	self.sentence = tobe_sent

    def print_sentence(self):
    	print(self.sentence)