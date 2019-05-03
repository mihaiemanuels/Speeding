def caught_speeding(speed, is_birthday):
    
    if is_birthday:
            speeding = speed - 5
    
    else:
        speeding = speed
    
    if speeding > 80:
        print ('Big Tiket')
    elif speeding > 60:
        print ('Small Tiket')
    else:
        print("No Tiket")
        
## caught_speeding(85,True)
## caught_speeding(82,False)
