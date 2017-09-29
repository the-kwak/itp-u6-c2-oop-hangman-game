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
            hit_locations = [i for i in range(len(self.answer))
            if attempt.lower() ==self.answer[i].lower()]
            
            for i in hit_locations:
                self.masked_list[i] = attempt.lower()
            self.masked = ''.join(self.masked_list)
            self.hit = True
        else:
            self.hit = False
        self.miss = not self.hit
        
        return(GuessAttempt(attempt, self.hit or None, self.miss or None))
    

class HangmanGame(object):
    pass
