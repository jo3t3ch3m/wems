# -*- coding: utf-8 -*-
# Put your commands here
COMMAND1 = "hi"
COMMAND2 = "am i a hacker?"
COMMAND3 = "who is the master"
COMMAND4 = "why do you have so many commands?"
COMMAND5 = "russian keyboard?"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command
         is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "Hi Minecraftman"
    
    elif command.find(COMMAND2) >= 0:
        response = "yes, you are destined to be a hackerF"
    elif command.find(COMMAND3) >= 0:
        response = "Kent is the master, all hail Kent"
    elif command.find(COMMAND4) >= 0:
        response = "the WEMS students are giving them to me"
    elif command.find(COMMAND5) >= 0:
        response = "йцукенгшщзхфывапролджэячсмитьбюъ"
            
        
    return response
