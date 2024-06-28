def print_hexagon_grid(rows, cols):
    for row in range(rows):
        if row==0:    
            for part in range(3): 
                for col in range(cols):
                    if part == 0:  
                        if (row + col) % 2 == 0:
                            if row == 0:
                                print("   ___   ", end="")
                        
                
                        else:
                            print("   ", end="")
                    elif part == 1: 
                        if (row + col) % 2 == 0:
                            print(" /     \\ ", end="")
                        else:
                            print("___", end="")
                    elif part == 2:  
                        if (row + col) % 2 == 0:
                            print(" \\ ___ / ", end="")
                        else:
                            print("   ", end="")
                print() 
        if row < rows - 1 and row % 2 == 0 :
            for part in range(3):  
                for col in range(cols):
           
                  if part == 1: 
                    if (row + col) % 2 == 0:
                        print(" /     \\ ", end="")
                    else:
                        print("___", end="")
                  elif part == 2: 
                    if (row + col) % 2 == 0:
                        print(" \\ ___ / ", end="")
                    else:
                
                        print("   ", end="")
                if part > 0:
                    print()
              
        if row < rows-1 and row % 2 == 1:
            for part in range(3):  
                for col in range(cols):
                    
                    if part == 1:  
                        if (row + col) % 2 == 1:
                            print(" /     \\ ", end="")
                        else:
                            print("___", end="")
                    elif part == 2:  
                        if (row + col) % 2 == 1:
                            print(" \\ ___ / ", end="")
                        else:
                            print("   ", end="")
                if part > 0:    
                    print()
           


if __name__ == "__main__":
    rows, cols = map(int, input("Enter the number of rows and columns for the grid : ").split())
    print_hexagon_grid(rows, cols)
