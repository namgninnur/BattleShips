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
    if boat_type == 6: #middle section
        
        #Must be left/right
        if adjacents[0]+adjacents[2] == 0:
            if j+1 <= shape[1]:
                possibilities_df.iloc[i,j+1] = 7
                print('Cell',i,',',j+1,'has been marked as a 7-Unknown Boat as it adjoins a middle section that has to go in its direction - ref #032')
            if j-1 >= 0:
                possibilities_df.iloc[i,j-1] = 7
                print('Cell',i,',',j-1,'has been marked as a 7-Unknown Boat as it adjoins a middle section that has to go in its direction - ref #033')
            skip_df.iloc[i,j] = 1
        
        #Must be up/down
        elif adjacents[1]+adjacents[3] == 0:
            if i+1 <= shape[0]:
                possibilities_df.iloc[i+1,j] = 7
                print('Cell',i+1,',',j,'has been marked as a 7-Unknown Boat as it adjoins a middle section that has to go in its direction - ref #034')
            if i-1 >= 0:
                possibilities_df.iloc[i-1,j] = 7
                print('Cell',i-1,',',j,'has been marked as a 7-Unknown Boat as it adjoins a middle section that has to go in its direction - ref #035')
            skip_df.iloc[i,j] = 1

    #Single solver
    elif boat_type == 7: #7-UnknownBoat
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

def row_iterator(shape,possibilities_df,nums_df,skip_df,none_count):
    
    for i in range(0,shape[0]):
        row_boat_count = 0
        row_unknown_count = 0
        row_empty_count = 0
        #Count how many cells are boats
        for j in range(0,shape[1]):
            if type(possibilities_df.iloc[i,j]) is int and possibilities_df.iloc[i,j] >= 1:
                row_boat_count += 1
            elif type(possibilities_df.iloc[i,j]) is int and possibilities_df.iloc[i,j] == 0:
                row_empty_count += 1
        row_unknown_count = shape[1] - row_boat_count - row_empty_count
            
        #If the count matches the row total, mark the rest as empty
        if row_boat_count == nums_df.iloc[i,0]:
            for j in range(0,shape[1]):
                if type(possibilities_df.iloc[i,j]) is str:
                    possibilities_df.iloc[i,j] = 0
                    skip_df.iloc[i,j] = 1
                    none_count -= 1
                    print('Cell',i,',',j,'has been solved as 0-Empty as the row',i,'already has the maximum number of boats - ref #013')

        #if the number of unknown cells + known boats = row total, mark the rest as 7=Boat-Unknown
        if row_unknown_count + row_boat_count == nums_df.iloc[i,0]:
            for j in range(0,shape[1]):
               if type(possibilities_df.iloc[i,j]) is str:
                possibilities_df.iloc[i,j] = 7
                print('Cell',i,',',j,'has been marked as "7-Boat-Unknown" as it must be a boat to satisfy the row',i,'total - ref #014')

    return(possibilities_df,skip_df,none_count)

        
def col_iterator(shape,possibilities_df,nums_df,skip_df,none_count):
    
    for j in range(0,shape[1]):
        col_boat_count = 0
        col_unknown_count = 0
        col_empty_count = 0
        #Count how many cells are boats
        for i in range(0,shape[0]):
            if type(possibilities_df.iloc[i,j]) is int and possibilities_df.iloc[i,j] >= 1:
                col_boat_count += 1
            elif type(possibilities_df.iloc[i,j]) is int and possibilities_df.iloc[i,j] == 0:
                col_empty_count += 1
        col_unknown_count = shape[0] - col_boat_count - col_empty_count
            
        #If the count matches the col total, mark the rest as empty
        if col_boat_count == nums_df.iloc[j,1]:
            for i in range(0,shape[0]):
                if type(possibilities_df.iloc[i,j]) is str:
                    possibilities_df.iloc[i,j] = 0
                    skip_df.iloc[i,j] = 1
                    none_count -= 1
                    print('Cell',i,',',j,'has been solved as 0-Empty as the col',j,'already has the maximum number of boats - ref #015')

        #if the number of unknown cells + known boats = col total, mark the rest as 7=Boat-Unknown
        if col_unknown_count + col_boat_count == nums_df.iloc[j,1]:
            for i in range(0,shape[0]):
               if type(possibilities_df.iloc[i,j]) is str:
                possibilities_df.iloc[i,j] = 7
                print('Cell',i,',',j,'has been marked as "7-UnknownBoat" as it must be a boat to satisfy the col',j,'total - ref #014')

    return(possibilities_df,skip_df,none_count)