import day
Sunday = 0
Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6
starting_day_str = input("What day are you leaving?")
trip_length_str = input("How long will you be gone?")
starting_day_int = int(starting_day_str)
trip_length_int = int(trip_length_str)
computing_length = starting_day_int + trip_length_int
return_day = (computing_length - 7)
print("You will be back on: ", return_day)