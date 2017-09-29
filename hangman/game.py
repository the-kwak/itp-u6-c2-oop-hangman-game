from .exceptions import *


class GuessAttempt(object):
    
    def __init__(self, letter, hit = None, miss = None):
        self.letter = letter
        if hit and miss:
            raise InvalidGuessAttempt()
        
        # use or to choose True or False
        self.hit = hit or False
        self.miss = miss or False
    
    # These functions will return either True or False
    def is_hit(self):
        return self.hit
    
    def is_miss(self):
        return self.miss


class GuessWord(object):
    
    def __init__(self, answer = None):
        # Return invalid if answer is empty
        if not answer:
            raise InvalidWordException()
        self.answer = answer
        self.masked =''.join(['*' for i in answer])
        self.masked_list = list(self.masked)
        self.hit = bool
        self.miss = bool
    
    # This needs to take in the object from GuessAttempt and look at the attmept.letter so it can return GuessAttempt.hit()
    # or miss() will wok on that one next
    def perform_attempt(self, attempt):
        if len(attempt) > 1 or not attempt :
            raise InvalidGuessedLetterException()
            
        if attempt.lower() in self.answer.lower():
            self.masked =''.join([attempt.lower() if self.answer[i].lower() == attempt.lower() 
            else list(self.masked)[i] for i in range(len(self.answer))])
            self.hit = True
        else:
            self.hit = False
        self.miss = not self.hit
        
        return(GuessAttempt(attempt, self.hit or None, self.miss or None))
    

class HangmanGame(object):
    pass
