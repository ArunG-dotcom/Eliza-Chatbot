# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:07:37 2020

@author: reach
"""

import reference, re, random# importing reference and re short from regular expresions


# searching for patterns in reference.psychobabble_responses match user response

        
def get_response(input1): # making variables and putting them to use
    
    for pattern in reference.psychobabble_patterns:
        match = re.search(reference.psychobabble_patterns[pattern], input1) # helps return both key and value
        #print(match)
  
    
   #reference.psychobabble_responses[pattern]
        x = random.choice(reference.psychobabble_responses[pattern])
        if match:
            return reference.format_response(match, x ) # taking off {0} and getting input
        
#print(get_response())
breakpoint()

def Eliza():
    input1 = input('Welcome My name is Eliza. Ask me whatever you want, I will try the best of my ability to assist you.') # getting input from user
    input1.replace( '.', '') # using input and replacing . 
    input1.replace('!','') # using input and replacing !
    cont = True
    while cont == True: # checking
        if input1 == "quit":
            cont == False
        else:
            input1 = input(get_response(input1))

Eliza()
    

#random response from reference.psychobabble_responses based


#inside loop if userinput is quit once falls the program ends
       