#init python: 
#    import pygame
#    #variables
#    WIN = False
#    ATTEMPTS = 12
#    SCORE = 0
    
#    def playBinaryTwoBIT():
#        my_list = list()
#        number_of_tiles = 8
#        #first tile x value to use for incrementing
#        p=550
#        #Number that determines number of tiles in a row (see innner if statement)
#        n = 0
#        #first tile y value for tiles 
#        o = 350
#        #puts x and y value into set for the list appending
#        m = (p,o)
#        #adds set to list
#        MY_LIST.append(m)
#        #loop value for generating tile space
#        q=0
#        while (number_of_tiles -1 > q):
#            #increment value for x increase for wider gap decrease for narrower
#            p +=150
#            #increments the column value
#            n += 1
#            # the value you set n equal to will determine the ammount of columns
#            if (n==4):
#                #set as new y value for second row can be entered to give more rows (CHANGE for other tiles)
#                o += 150
#                #resets x value for tile placement in new row change to same value above of the x firts tile
#                p = 550
#                #resets n so that new  rows will be able to be made
#                n= 0
#            #adds iteration to loop
#            q +=1
#            #takes new values and puts them in list
#            m = (p,o)
#            my_list.append(m)
#        #puts starting list in new format
#        x = list(my_list)
#        #shuffles values to randomize values
#        random.shuffle(x)
#        #colors
#        BLUE = (0,70,200)
        
#    class MatchGame(renpy.Displayable):
#        def __init__(self, back=None, base+None, springback=0.1, rotate=0.1, can_drag=__default_can_drag, doubleclick=.33, **kwargs):
            
#            renpy.Displayable.__init__(self, **kwargs)
            
#            self.cards = {}
            
#            self.stacks = []
            
#            self.back = renpy.easy.displayable_or_none(back)
            
#            self.base = renpy.easy.displayable_or_none(base)
        