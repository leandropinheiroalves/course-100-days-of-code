# 100DaysOfCode Day 3 - Treasure Island

print('''
### ##  ###  #   ## # # ##  ### 
 #  # # #   # # #   # # # # #   
 #  ##  ##  ###  #  # # ##  ##  
 #  # # #   # #   # # # # # #   
 #  # # ### # # ##  ### # # ### 
                                
    ###  ## #    #  ### ##      
     #  #   #   # # # # # #     
     #   #  #   ### # # # #     
     #    # #   # # # # # #     
    ### ##  ### # # # # ##                                                                                                                                               
 ''')
print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')

choice1 = input('''You're at a cross road. Where do you want to go? Type "left" or "right"\n''').lower()

if choice1 == 'left':
    print('You come to a lake. There is an island in the middle of the lake.')
    choice2 = input('Type "wait" to wait for a boat or type "swim" to swim across.\n').lower()
    if choice2 == 'wait':
        print('You arrive at the island unharmed. There is a house with 3 doors.')
        choice3 = input('One red, one yellow and one blue. Which color do you choose?\n').lower()
        if choice3 == 'blue':
            print('You enter a room of beasts. Game Over.')
        elif choice3 == 'yellow':
            print('You entered a burning room. Game Over.')
        elif choice3 == 'red':
            print('You found the treasure! You Win!')
    else:
        print('The lake is full of crocodiles. Game Over.')
else:
    print('You fell into a hole. Game Over.')
