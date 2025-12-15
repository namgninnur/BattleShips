

def get_puzzle_data(puzzle_ref):
    puzzle_ref = int(puzzle_ref)
    if puzzle_ref == 6:
        data = {
        "col1": [None,None,None,None,None,None,None,None,None,None],
        "col2": [None,None,None,None,None,None,None,None,None,None],
        "col3": [None,None,None,None,None,None,None,None,None,1],
        "col4": [None,None,None,None,None,None,5,None,None,None],
        "col5": [None,None,None,None,None,None,None,None,None,None],
        "col6": [None,None,None,None,None,None,None,None,None,None],
        "col7": [None,None,None,6,None,None,None,None,None,None],
        "col8": [None,None,None,None,None,None,None,None,None,None],
        "col9": [6,None,None,None,None,None,None,None,None,None],
        "col10": [None,None,None,None,None,None,None,None,None,1]
        }
        nums = {
        "rows": [3,1,2,1,2,1,4,2,2,2],
        "cols": [4,0,4,1,2,0,5,1,1,2]
        }
        ships = {
        "1cell": [4],
        "2cell": [3],        
        "3cell": [2],
        "4cell": [1],
        }
    elif puzzle_ref == 5:

        data = {
        "col1": [None,None,None,None,None,None,None,None,None,None],
        "col2": [None,None,None,None,None,None,None,None,None,None],
        "col3": [None,None,None,None,1,None,None,None,None,None],
        "col4": [None,None,None,None,None,None,None,None,None,None],
        "col5": [None,None,None,None,None,2,None,None,None,None],
        "col6": [None,None,None,None,None,None,None,None,None,None],
        "col7": [None,None,None,None,None,None,7,None,None,None],
        "col8": [None,None,None,None,None,None,None,None,None,None],
        "col9": [None,None,None,None,None,None,None,1,None,None],
        "col10": [None,None,None,None,None,None,None,None,None,None]
        }
        nums = {
        "rows": [0,6,0,2,2,2,1,2,4,1],
        "cols": [3,1,2,2,4,1,5,1,1,0]
        }
        ships = {
            "1cell": [4],
            "2cell": [3],
            "3cell": [2],
            "4cell": [1],
        }
    elif puzzle_ref == 4:
        data = {
        "col1": [None,None,None,None,None,None,None,2,None,None],
        "col2": [None,None,None,None,None,None,None,None,None,None],
        "col3": [None,None,None,None,None,None,None,None,None,None],
        "col4": [None,None,None,None,None,None,None,None,None,None],
        "col5": [None,None,None,None,None,None,None,None,None,None],
        "col6": [None,None,None,None,None,None,None,None,None,None],
        "col7": [None,None,None,None,None,None,None,None,None,None],
        "col8": [None,None,None,None,None,None,None,None,None,None],
        "col9": [None,None,None,1,None,None,4,None,None,None],
        "col10": [None,None,None,None,None,None,None,None,None,None]
        }
        nums = {
        "rows": [0,3,2,2,0,2,3,3,2,3],
        "cols": [4,0,3,0,4,3,3,0,3,0]
        }
        ships = {
            "1cell": [4],
            "2cell": [3],
            "3cell": [2],
            "4cell": [1],
        }
    elif puzzle_ref == 3:
        data_3 = {
        "col1": [None,None,None,None,None,None,None,None],
        "col2": [None,None,None,None,None,None,None,None],
        "col3": [None,None,None,None,None,None,None,None],
        "col4": [None,None,None,None,0,None,None,None],
        "col5": [None,None,None,None,None,None,None,None],
        "col6": [None,None,None,None,None,None,None,None],
        "col7": [None,None,0,None,None,None,None,None],
        "col8": [None,None,None,None,None,None,None,None]
        }
        nums_3 = {
        "rows": [4,1,3,1,5,0,2,3],
        "cols": [0,6,0,2,4,1,3,3]
        }
        ships_3 = {
            "1cell": [4],
            "2cell": [3],
            "3cell": [2],
            "4cell": [1],
        }
    elif puzzle_ref == 2:
        data_2 = {
        "col1": [None,None,None,None,None,None],
        "col2": [None,None,1,None,None,None],
        "col3": [None,None,None,None,None,None],
        "col4": [None,None,None,None,None,None],
        "col5": [None,None,None,None,None,None],
        "col6": [None,None,None,None,None,None]
        }
        nums_2 = {
        "rows": [2,0,4,0,4,0],
        "cols": [0,2,2,1,3,2]
        }
        ships_2 = {
            "1cell": [3],
            "2cell": [2],
            "3cell": [1],
            "4cell": [0],
        }
    elif puzzle_ref == 1:
        data_1 = {
        "col1": [None,None,None,None,None,None],
        "col2": [None,None,None,None,None,None],
        "col3": [None,None,None,None,None,None],
        "col4": [None,None,None,None,2,None],
        "col5": [None,None,None,None,None,None],
        "col6": [None,None,0,None,None,None]
        }
        nums_1 = {
        "rows": [4,0,1,3,1,1],
        "cols": [0,3,1,3,0,3]
        }
        ships_1 = {
            "1cell": [3],
            "2cell": [2],
            "3cell": [1],
            "4cell": [0],
        }
    elif puzzle_ref == 0:

        data = {
        "col1": [None,None,None,None,None,None],
        "col2": [None,None,None,None,None,None],
        "col3": [None,None,6,None,None,None],
        "col4": [5,None,None,None,None,None],
        "col5": [None,None,None,None,None,None],
        "col6": [None,None,None,None,None,None]
        }
        nums = {
        "rows": [3,0,4,0,3,0],
        "cols": [2,2,2,2,1,1]
        }
        ships = {
            "1cell": [3],
            "2cell": [2],
            "3cell": [1],
            "4cell": [0],
        }
    else:
        print('Invalid puzzle_ref')
    
    return (data, nums, ships)

# Marking diagonals of known boats are 0-Empty cells
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

#Marking adjacent cells of known boats as 0-Empty or 7-Unknown Boat based on the known boat type
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

#Determing what directions a boat can extend to
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

#Updating a 7-UnknownBoat cell to a specific boat type
def update_boat_type(boat_type,i,j,shape,possibilities_df,skip_df,none_count,adjacents,finished_boats_df,remaining_ships_df):
    if boat_type == 6: #middle section
        
        #Must be left/right
        if adjacents[0]+adjacents[2] == 0:
            if j+1 <= shape[1] and type(possibilities_df.iloc[i,j+1]) is str:
                possibilities_df.iloc[i,j+1] = 7
                print('Cell',i,',',j+1,'has been marked as a 7-Unknown Boat as it adjoins a middle section that has to go in its direction - ref #032')
            if j-1 >= 0 and type(possibilities_df.iloc[i,j-1]) is str:
                possibilities_df.iloc[i,j-1] = 7
                print('Cell',i,',',j-1,'has been marked as a 7-Unknown Boat as it adjoins a middle section that has to go in its direction - ref #033')
            skip_df.iloc[i,j] = 1
        
        #Must be up/down
        elif adjacents[1]+adjacents[3] == 0:
            if i+1 <= shape[0] and type(possibilities_df.iloc[i+1,j]) is str:
                possibilities_df.iloc[i+1,j] = 7
                print('Cell',i+1,',',j,'has been marked as a 7-Unknown Boat as it adjoins a middle section that has to go in its direction - ref #034')
            if i-1 >= 0 and type(possibilities_df.iloc[i-1,j]) is str:
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

        #Boat of max length=4 (i.e. quad), mark ends as end-boats
        if i+3 < shape[0] and type(possibilities_df.iloc[i+3,j]) is int and possibilities_df.iloc[i+3,j] > 1 and type(possibilities_df.iloc[i+2,j]) is int and possibilities_df.iloc[i+2,j] > 1 and type(possibilities_df.iloc[i+1,j]) is int and possibilities_df.iloc[i+1,j] > 1:
            possibilities_df.iloc[i,j] = 4
            none_count -= 1
            print('Cell',i,',',j,'has been solved as a 4-Down boat section as it is a known boat section that has three boat sections below it, with a max boat length of 4 - ref #061')
        elif i-3 > 0 and type(possibilities_df.iloc[i-3,j]) is int and possibilities_df.iloc[i-3,j] > 1 and type(possibilities_df.iloc[i-2,j]) is int and possibilities_df.iloc[i-2,j] > 1 and type(possibilities_df.iloc[i-1,j]) is int and possibilities_df.iloc[i-1,j] > 1:
            possibilities_df.iloc[i,j] = 2
            none_count -= 1
            print('Cell',i,',',j,'has been solved as a 2-Up boat section as it is a known boat section that has three boat sections above it, with a max boat length of 4 - ref #062')
        elif j+3 < shape[1] and type(possibilities_df.iloc[i,j+3]) is int and possibilities_df.iloc[i,j+3] > 1 and type(possibilities_df.iloc[i,j+2]) is int and possibilities_df.iloc[i,j+2] > 1 and type(possibilities_df.iloc[i,j+1]) is int and possibilities_df.iloc[i,j+1] > 1:
            possibilities_df.iloc[i,j] = 3
            none_count -= 1
            print('Cell',i,',',j,'has been solved as a 3-Right boat section as it is a known boat section that has three boat sections to the right of it, with a max boat length of 4 - ref #063')
        elif j-3 > 0 and type(possibilities_df.iloc[i,j-3]) is int and possibilities_df.iloc[i,j-3] > 1 and type(possibilities_df.iloc[i,j-2]) is int and possibilities_df.iloc[i,j-2] > 1 and type(possibilities_df.iloc[i,j-1]) is int and possibilities_df.iloc[i,j-1] > 1:
            possibilities_df.iloc[i,j] = 5
            none_count -= 1
            print('Cell',i,',',j,'has been solved as a 5-Left boat section as it is a known boat section that has three boat sections to the left of it, with a max boat length of 4 - ref #064')
        
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

def col_completed_boat_checker(shape,possibilities_df,nums_df,skip_df,none_count,finished_boats_df,remaining_ships_df):
    import math
    for j in range(0,shape[1]):
        for i in range(0,shape[0]):
            #For each cell, that is a boat of some-type but not in a completed boat, check if the boat can be completed and removed from the completed boat count.
            if math.isnan(finished_boats_df.iloc[i,j]) is True and type(possibilities_df.iloc[i,j]) is int and possibilities_df.iloc[i,j] > 0:
                if possibilities_df.iloc[i,j] == 1:
                    finished_boats_df.iloc[i,j] = 1 
                    remaining_ships_df.iloc[0,0] -= 1
                    print('Cell',i,',',j,'has been provided as single boat in the starting data and a single boat has been removed from the remaining available ships - ref #040')
                elif possibilities_df.iloc[i,j] == 4:
                    if i+1 < shape [0] and possibilities_df.iloc[i+1,j] == 2:
                        finished_boats_df.iloc[i,j] = 2
                        finished_boats_df.iloc[i+1,j] = 2
                        remaining_ships_df.iloc[0,1] -= 1
                        print('A completed boat of length 2 has been founds in cells',i,',',j,' and ',i+1,',',j,' and thus a double boat has been removed from the remaining available ships - ref #041')
            
                    elif i+2 < shape [0] and possibilities_df.iloc[i+1,j] == 6 and possibilities_df.iloc[i+2,j] == 2: 
                        finished_boats_df.iloc[i,j] = 3
                        finished_boats_df.iloc[i+1,j] = 3
                        finished_boats_df.iloc[i+2,j] = 3
                        remaining_ships_df.iloc[0,2] -= 1
                        print('A completed boat of length 3 has been founds in cell',i,',',j,' to ',i+2,',',j,' and thus a triple boat has been removed from the remaining available ships - ref #042')
                    
                    elif i+3 < shape [0] and possibilities_df.iloc[i+1,j] == 6 and possibilities_df.iloc[i+2,j] == 6 and possibilities_df.iloc[i+3,j] == 2: 
                        finished_boats_df.iloc[i,j] = 4
                        finished_boats_df.iloc[i+1,j] = 4
                        finished_boats_df.iloc[i+2,j] = 4
                        finished_boats_df.iloc[i+3,j] = 4
                        remaining_ships_df.iloc[0,3] -= 1
                        print('A completed boat of length 4 has been founds in cell',i,',',j,' to ',i+3,',',j,' and thus a quad boat has been removed from the remaining available ships - ref #043')
                
                elif possibilities_df.iloc[i,j] == 2:
                    if i-1 > 0 and possibilities_df.iloc[i-1,j] == 4:
                        finished_boats_df.iloc[i,j] = 2
                        finished_boats_df.iloc[i-1,j] = 2
                        remaining_ships_df.iloc[0,1] -= 1
                        print('A completed boat of length 2 has been founds in cells',i,',',j,' and ',i-1,',',j,' and thus a double boat has been removed from the remaining available ships - ref #048')
            
                    elif i-2 > 0 and possibilities_df.iloc[i-1,j] == 6 and possibilities_df.iloc[i-2,j] == 4: 
                        finished_boats_df.iloc[i,j] = 3
                        finished_boats_df.iloc[i-1,j] = 3
                        finished_boats_df.iloc[i-2,j] = 3
                        remaining_ships_df.iloc[0,2] -= 1
                        print('A completed boat of length 3 has been founds in cell',i,',',j,' to ',i-2,',',j,' and thus a triple boat has been removed from the remaining available ships - ref #049')
                    
                    elif i-3 > 0 and possibilities_df.iloc[i-1,j] == 6 and possibilities_df.iloc[i-2,j] == 6 and possibilities_df.iloc[i-3,j] == 4: 
                        finished_boats_df.iloc[i,j] = 4
                        finished_boats_df.iloc[i-1,j] = 4
                        finished_boats_df.iloc[i-2,j] = 4
                        finished_boats_df.iloc[i-3,j] = 4
                        remaining_ships_df.iloc[0,3] -= 1
                        print('A completed boat of length 4 has been founds in cell',i,',',j,' to ',i-3,',',j,' and thus a quad boat has been removed from the remaining available ships - ref #050')
    return (finished_boats_df,remaining_ships_df)
    
def row_completed_boat_checker(shape,possibilities_df,nums_df,skip_df,none_count,finished_boats_df,remaining_ships_df):
    import math
    for i in range(0,shape[0]):
        for j in range(0,shape[1]):
            #For each cell, that is a boat of some-type but not in a completed boat, check if the boat can be completed and removed from the completed boat count.
            if math.isnan(finished_boats_df.iloc[i,j]) is True and type(possibilities_df.iloc[i,j]) is int and possibilities_df.iloc[i,j] > 0:
                if possibilities_df.iloc[i,j] == 1:
                    finished_boats_df.iloc[i,j] = 1 
                    remaining_ships_df.iloc[0,0] -= 1
                    print('Cell',i,',',j,'has been provided as single boat in the starting data and a single boat has been removed from the remaining available ships - ref #037')
                elif possibilities_df.iloc[i,j] == 3:
                    if j+1 < shape [1] and possibilities_df.iloc[i,j+1] == 5:
                        finished_boats_df.iloc[i,j] = 2
                        finished_boats_df.iloc[i,j+1] = 2
                        remaining_ships_df.iloc[0,1] -= 1
                        print('A completed boat of length 2 has been founds in cells',i,',',j,' and ',i,',',j+1,' and thus a double boat has been removed from the remaining available ships - ref #038')
            
                    elif j+2 < shape [0] and possibilities_df.iloc[i,j+1] == 6 and possibilities_df.iloc[i,j+2] == 5: 
                        finished_boats_df.iloc[i,j] = 3
                        finished_boats_df.iloc[i,j+1] = 3
                        finished_boats_df.iloc[i,j+2] = 3
                        remaining_ships_df.iloc[0,2] -= 1
                        print('A completed boat of length 3 has been founds in cell',i,',',j,' to ',i,',',j+2,' and thus a triple boat has been removed from the remaining available ships - ref #039')
                    
                    elif j+3 < shape [0] and possibilities_df.iloc[i,j+1] == 6 and possibilities_df.iloc[i,j+2] == 6 and possibilities_df.iloc[i,j+3] == 5: 
                        finished_boats_df.iloc[i,j] = 4
                        finished_boats_df.iloc[i,j+1] = 4
                        finished_boats_df.iloc[i,j+2] = 4
                        finished_boats_df.iloc[i,j+3] = 4
                        remaining_ships_df.iloc[0,3] -= 1
                        print('A completed boat of length 4 has been founds in cell',i,',',j,' to ',i,',',j+3,' and thus a quad boat has been removed from the remaining available ships - ref #051')
                
                elif possibilities_df.iloc[i,j] == 5:
                    if j-1 > 0 and possibilities_df.iloc[i,j-1] == 3:
                        finished_boats_df.iloc[i,j] = 2
                        finished_boats_df.iloc[i,j-1] = 2
                        remaining_ships_df.iloc[0,1] -= 1
                        print('A completed boat of length 2 has been founds in cells',i,',',j,' and ',i,',',j-1,' and thus a double boat has been removed from the remaining available ships - ref #052')
            
                    elif j-2 > 0 and possibilities_df.iloc[i,j-1] == 6 and possibilities_df.iloc[i,j-2] == 3: 
                        finished_boats_df.iloc[i,j] = 3
                        finished_boats_df.iloc[i,j-1] = 3
                        finished_boats_df.iloc[i,j-2] = 3
                        remaining_ships_df.iloc[0,2] -= 1
                        print('A completed boat of length 3 has been founds in cell',i,',',j,' to ',i,',',j-2,' and thus a triple boat has been removed from the remaining available ships - ref #053')
                    
                    elif j-3 > 0 and possibilities_df.iloc[i,j-1] == 6 and possibilities_df.iloc[i,j-2] == 6 and possibilities_df.iloc[i,j-3] == 3: 
                        finished_boats_df.iloc[i,j] = 4
                        finished_boats_df.iloc[i,j-1] = 4
                        finished_boats_df.iloc[i,j-2] = 4
                        finished_boats_df.iloc[i,j-3] = 4
                        remaining_ships_df.iloc[0,3] -= 1
                        print('A completed boat of length 4 has been founds in cell',i,',',j,' to ',i,',',j-3,' and thus a quad boat has been removed from the remaining available ships - ref #050')
    
    return (finished_boats_df,remaining_ships_df)