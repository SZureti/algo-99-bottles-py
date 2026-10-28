def bottle_song():
    # Base case is 0, so write if condition for 0
    #if num == 0:
       # print ("No more bottles of beer on the wall, no more bottles of beer.")
		# return ("No more bottles of beer on the wall, no more bottles of beer.")
	
	# set starting number
    num = 99
	#save starting number because it's used again ata the end
	
    starting_num = num

	# create while loop to count down from 99 to 1
    while num > 0:
        # 1 is the only one that isn't plural so write if condition for that
         if num == 1:
            current_bottle = "1 bottle"
         else:
            current_bottle = f"{num} bottles"

         if num - 1 == 0:
             next_bottle = "no more bottles"
         elif num - 1 == 1:
             next_bottle = "1 bottle"
         else:
		# write condition for 2 through 99
             next_bottle = f"{num - 1} bottles"
		
		# print first line of song
         print(f"{current_bottle} of beer on the wall, {current_bottle} of beer.")
        
		# second line
         print(f"Take one down and pass it around, {next_bottle} of beer on the wall.")
        # print a blank line for spacing
         print()

		# decrease number
         num -= 1
         print("No more bottles of beer on the wall, no more bottles of beer.")
         print(f"Go to the store and buy some more, {starting_num} bottles of beer on the wall.")
         print()
    
bottle_song()
