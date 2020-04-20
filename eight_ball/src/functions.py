"""
===========================================
Author: Codiacs
Github: github.com/MicroOptimization
===========================================
"""
import random

def get_message():
    possible_messages = ["It is certain.", 
                         "It is decidedly so.",
                         "Without a doubt.",
                         "Yes, definitely.",
                         "You may rely on it.",
                         "As I see it, yes.",
                         "Most likely.",
                         "Outlook good.",
                         "Yes.",
                         "Signs point to yes.",
                         "Reply hazy, try again.",
                         "Ask again later.",
                         "Better not tell you now.",
                         "Cannot predict now.",
                         "Concentrate and ask again.",
                         "Don't count on it.",
                         "My reply is no.",
                         "My sources say no.",
                         "Outlook not so good.",
                         "Very doubtful."]
    
    index = random.randint(0, len(possible_messages))
    message = possible_messages[index]
    
    return message

print(get_message())