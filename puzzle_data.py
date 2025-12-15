from battleships import puzzle_ref

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
