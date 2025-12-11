def diagonals_of_known_boat(boat_type,i,j,shape,possibilities_df,skip_df,none_count):
    if i+1 < shape[0] and j+1 < shape[1] and type(possibilities_df.iloc[i+1,j+1]) is str:
        possibilities_df.iloc[i+1,j+1] = 0
        skip_df.iloc[i+1,j+1] = 1
        none_count -= 1
        print('Cell',i+1,',',j+1,'has been solved as 0-Empty as it diagonally touches a known boat - ref #001')

    if i+1 < shape[0] and j-1 >= 0 and type(possibilities_df.iloc[i+1,j-1]) is str:
        possibilities_df.iloc[i+1,j-1] = 0
        skip_df.iloc[i+1,j-1] = 1
        none_count -= 1
        print('Cell',i+1,',',j-1,'has been solved as 0-Empty as it diagonally touches a known boat - ref #002')

    if i-1 >= 0 and j+1 < shape[1] and type(possibilities_df.iloc[i-1,j+1]) is str:
        possibilities_df.iloc[i-1,j+1] = 0
        skip_df.iloc[i-1,j+1] = 1
        none_count -= 1
        print('Cell',i-1,',',j+1,'has been solved as 0-Empty as it diagonally touches a known boat - ref #003')

    if i-1 >= 0 and j-1 >= 0 and type(possibilities_df.iloc[i-1,j-1]) is str:
        possibilities_df.iloc[i-1,j-1] = 0
        skip_df.iloc[i-1,j-1] = 1
        none_count -= 1
        print('Cell',i-1,',',j-1,'has been solved as 0-Empty as it diagonally touches a known boat - ref #004')

    return(possibilities_df,skip_df,none_count)


def adjacents_of_known_boat(boat_type,i,j,shape,possibilities_df,skip_df,none_count):
    
    #Up
    if i-1 >= 0 and type(possibilities_df.iloc[i-1,j]) is str:
        if possibilities_df.iloc[i,j] in [1,3,4,5]:
            possibilities_df.iloc[i-1,j] = 0
            skip_df.iloc[i-1,j] = 1
            none_count -= 1
            print('Cell',i-1,',',j,'has been solved as 0-Empty as it touches a known boat edge - ref #005')
        elif possibilities_df.iloc[i,j] == 2:
            possibilities_df.iloc[i-1,j] = int(7)
            print('Cell',i-1,',',j,'has been marked as 7-UnknownBoat as it touches a known boat join - ref #009')
                
    #Right
    if j+1 < shape[1] and type(possibilities_df.iloc[i,j+1]) is str:
        if possibilities_df.iloc[i,j] in [1,2,4,5]:
            possibilities_df.iloc[i,j+1] = 0
            skip_df.iloc[i,j+1] = 1
            none_count -= 1
            print('Cell',i,',',j+1,'has been solved as 0-Empty as it touches a known boat edge - ref #006')
        elif possibilities_df.iloc[i,j] == 3:
            possibilities_df.iloc[i,j+1] = int(7)
            print('Cell',i,',',j+1,'has been marked as 7-UnknownBoat as it touches a known boat join - ref #010')
            
    #Down
    if i+1 < shape[0] and type(possibilities_df.iloc[i+1,j]) is str:
        if possibilities_df.iloc[i,j] in [1,2,3,5]:
            possibilities_df.iloc[i+1,j] = 0
            skip_df.iloc[i+1,j] = 1
            none_count -= 1
            print('Cell',i+1,',',j,'has been solved as 0-Empty as it touches a known boat edge - ref #007')
        elif possibilities_df.iloc[i,j] == 4:
            possibilities_df.iloc[i+1,j] = int(7)
            print('Cell',i+1,',',j,'has been marked as 7-UnknownBoat as it touches a known boat join - ref #011')

    #Left
    if j-1 >= 0 and type(possibilities_df.iloc[i,j-1]) is str:
        if possibilities_df.iloc[i,j] in [1,2,3,4]:
            possibilities_df.iloc[i,j-1] = 0
            skip_df.iloc[i,j-1] = 1
            none_count -= 1
            print('Cell',i,',',j-1,'has been solved as 0-Empty as it touches a known boat edge - ref #008')
        elif possibilities_df.iloc[i,j] == 5:
            possibilities_df.iloc[i,j-1] = int(7)
            print('Cell',i,',',j-1,'has been marked as 7-UnknownBoat as it touches a known boat join - ref #012')
            
    return(possibilities_df,skip_df,none_count)

def available_directions_for_boat(boat_type,i,j,shape,possibilities_df):
    
    #Up,Right,Down,Left
    adjacents = [None,None,None,None]
    upper_adj = None
    right_adj = None
    lower_adj = None
    left_adj = None

    #Up
    #If the adjacent upper cell is in the grid but is 0-Empty, mark as impossible direction
    if i-1 >= 0 and type(possibilities_df.iloc[i-1,j]) is int and possibilities_df.iloc[i-1,j] == 0:
        adjacents[0] = 0
    #Else if the adjacent upper cell is out of bounds, mark as impossible direction
    elif i-1 < 0:
        adjacents[0] = 0
    #Else - mark as potential direction
    else:
        adjacents[0] = 1
               
    #Right
    if j+1 < shape[1] and type(possibilities_df.iloc[i,j+1]) is int and possibilities_df.iloc[i,j+1] == 0:
        adjacents[1] = 0
    elif j+1 >= shape[1]:
        adjacents[1] = 0
    else:
        adjacents[1] = 1
    
    #Down
    if i+1 < shape[0] and type(possibilities_df.iloc[i+1,j]) is int and possibilities_df.iloc[i+1,j] == 0:
        adjacents[2] = 0
    elif i+1 >= shape[0]:
        adjacents[2] = 0
    else:
        adjacents[2] = 1
    
    #Left
    if j-1 >= 0 and type(possibilities_df.iloc[i,j-1]) is int and possibilities_df.iloc[i,j-1] == 0:
        adjacents[3] = 0
    elif j-1 < 0:
        adjacents[3] = 0
    else:
        adjacents[3] = 1
    
    return(adjacents)

def update_boat_type(boat_type,i,j,shape,possibilities_df,skip_df,none_count,adjacents,finished_boats_df,remaining_ships_df):
    #Single solver
    if boat_type == 7:
        if adjacents[0]+adjacents[1]+adjacents[2]+adjacents[3] == 0:
            possibilities_df.iloc[i,j] = 1
            skip_df.iloc[i,j] = 1
            none_count -= 1
            finished_boats_df.iloc[i,j] = 1 
            remaining_ships_df.iloc[0,0] -= 1
            print('Cell',i,',',j,'is as single boat and thus a single boat has been removed from the remaining available ships - ref #036')        

        #Boat length of two plus solver
        elif adjacents[0]+adjacents[1]+adjacents[2] == 0 and type(possibilities_df.iloc[i,j-1]) is int:
            if possibilities_df.iloc[i,j-1] in [3,6,7]:
                possibilities_df.iloc[i,j] = 5
                none_count -= 1
                print('Cell',i,',',j,'has been solved as a 5-Left facing end section of boat as it a known boat surrounded by empty cells on 3 sides and a known boat on the left - ref #018')
        elif adjacents[1]+adjacents[2]+adjacents[3] == 0 and type(possibilities_df.iloc[i-1,j]) is int:
            if possibilities_df.iloc[i-1,j] in [4,6,7]:
                possibilities_df.iloc[i,j] = 2
                none_count -= 1
                print('Cell',i,',',j,'has been solved as a 2-Up facing end section of boat as it a known boat surrounded by empty cells on 3 sides and a known boat on the top - ref #019')
        elif adjacents[2]+adjacents[3]+adjacents[0] == 0 and type(possibilities_df.iloc[i,j+1]) is int:
            if possibilities_df.iloc[i,j+1] in [5,6,7]:
                possibilities_df.iloc[i,j] = 3
                none_count -= 1
                print('Cell',i,',',j,'has been solved as a 3-Right facing end section of boat as it a known boat surrounded by empty cells on 3 sides and a known boat on the right - ref #020')
        elif adjacents[3]+adjacents[0]+adjacents[1] == 0 and type(possibilities_df.iloc[i+1,j]) is int:
            if possibilities_df.iloc[i+1,j] in [2,6,7]:
                possibilities_df.iloc[i,j] = 4
                none_count -= 1
                print('Cell',i,',',j,'has been solved as a 4-Down facing end section of boat as it a known boat surrounded by empty cells on 3 sides and a known boat below - ref #021')             
                    
        #Boat of three plus in-between solver
        if i+1 < shape[0] and type(possibilities_df.iloc[i+1,j]) is int and possibilities_df.iloc[i+1,j] > 1:
            if i-1 >= 0 and type(possibilities_df.iloc[i-1,j]) is int and possibilities_df.iloc[i-1,j] > 1:
                possibilities_df.iloc[i,j] = 6
                none_count -= 1
                print('Cell',i,',',j,'has been solved as a 6-Middle boat section as it is a known boat section that has two boat sections above and below it - ref #022')
        elif j+1 < shape[1] and type(possibilities_df.iloc[i,j+1]) is int and possibilities_df.iloc[i,j+1] > 1:
            if j-1 >= 0 and type(possibilities_df.iloc[i,j-1]) is int and possibilities_df.iloc[i,j-1] > 1:
                possibilities_df.iloc[i,j] = 6
                none_count -= 1
                print('Cell',i,',',j,'has been solved as a 6-Middle boat section as it is a known boat section that has two boat sections to the left and right of it - ref #023')

    return(possibilities_df,skip_df,none_count,finished_boats_df,remaining_ships_df)