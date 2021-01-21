def knightmove(x, y): 
    endloop=0
    while endloop==0:
        xcoord=x
        ycoord=y
        xcoord=xcoord.lower()
      
        if xcoord=='a':
            xcoord=1
        elif xcoord=='b':
            xcoord=2
        elif xcoord=='c':
            xcoord=3
        elif xcoord=='d':
            xcoord=4
        elif xcoord=='e':
            xcoord=5
        elif xcoord=='f':
            xcoord=6
        elif xcoord=='g':
            xcoord=7
        elif xcoord=='h':
            xcoord=8
        else:
            print ("The 'X' co-ordinate you entered is invalid")
            endloop=1   
    
        upleft_xcoord=xcoord-1
        upleft_ycoord=ycoord+2
        upright_xcoord=xcoord+1
        upright_ycoord=ycoord+2
        rightup_xcoord=xcoord+2
        rightup_ycoord=ycoord+1
        rightdown_xcoord=xcoord+2
        rightdown_ycoord=ycoord-1
        downright_xcoord=xcoord+1
        downright_ycoord=ycoord-2
        downleft_xcoord=xcoord-1
        downleft_ycoord=ycoord-2
        leftup_xcoord=xcoord-2
        leftup_ycoord=ycoord+1
        leftdown_xcoord=xcoord-2
        leftdown_ycoord=ycoord-1



        print ("The possible moves are: ")
        if upleft_xcoord>0 and upleft_ycoord<9:
            print ("Up to the left:", upleft_xcoord,",",upleft_ycoord)
        if upright_xcoord<9 and upright_ycoord<9:
            print ("Up to the right:", upright_xcoord,',',upright_ycoord)
        if rightup_xcoord<9 and rightup_ycoord<9:
            print ("Right then up:", rightup_xcoord,',',rightup_ycoord)
        if rightdown_xcoord<9 and rightdown_ycoord>0:
            print ("right then down:", rightdown_xcoord,',',rightdown_ycoord)
        if downright_xcoord<9 and downright_ycoord>0:
            print ("Down to the right:", downright_xcoord,',',downright_ycoord)
        if downleft_xcoord>0 and downleft_ycoord>0:
            print ("Down to the left:", downleft_xcoord,',',downleft_ycoord)
        if leftup_xcoord>0 and leftup_ycoord<9:
            print ("Left then up:", leftup_xcoord,',',leftup_ycoord)
        if leftdown_xcoord>0 and leftdown_ycoord>0:
            print ("Left then down:", leftdown_xcoord,',',leftdown_ycoord)
        endloop=1

x=input("what is the X co-ordinate? ")
y=input("what is the Y co-ordinate? ")
knightmove(x, y)