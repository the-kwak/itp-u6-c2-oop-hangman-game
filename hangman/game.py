from .exceptions import *


class GuessAttempt(object):
    
    def __init__(self, letter, hit = None, miss = None):
        self.letter = letter
        if hit and miss:
            raise InvalidGuessAttempt()
        self.hit = hit or False
        self.miss = miss or False
    
    def is_hit(self):
        return self.hit
    
    def is_miss(self):
        return self.miss


class GuessWord(object):
    
    def __init__(self, answer):
        
        if not answer:
            raise InvalidWordException()
            
        self.answer = answer
        self.masked =''.join(['*' for i in answer])
    
    # This needs to take in the object from GuessAttempt and look at the attmept.letter so it can return GuessAttempt.hit()
    # or miss() will wok on that one next
    def perform_attempt(self, attempt):
        if attempt > 1 or not attempt :
            raise InvalidGuessedLetterException()
    

class HangmanGame(object):
    pass
