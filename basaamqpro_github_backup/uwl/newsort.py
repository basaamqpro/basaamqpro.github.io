un = [6, 4, 3, 8, 9, 5, 7, 2]

for x in range(len(un)):
    passtotherightx = un[x]
    for y in range(len(un) - 1):
        current_pos_y = un[y]
        print("passtotherightx:", passtotherightx)
        print("current_pos_y:", current_pos_y)
        if passtotherightx > current_pos_y:


            if passtotherightx > un[y+1]:
                futurey = un[y+1]
                futurex = passtotherightx

                un[y+1] = futurex
                
                un[x] = futurey
                break
            elif passtotherightx < un[y+1]:
                #  un[x] = current_pos_y
                pass
        elif passtotherightx < current_pos_y:
            memoryx =  passtotherightx
            memymnus_one = un[y-1] # less number than currentpos y
            if memymnus_one > memoryx:
                pass
            elif memymnus_one < memoryx:
                un[x] = memymnus_one #un[x] is the numer on the left
            un[y-1] = passtotherightx
            # un[x] = memymnus_one
            break

            
print("un:", un)        
        
        
