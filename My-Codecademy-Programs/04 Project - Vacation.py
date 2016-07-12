def hotel_cost(nights):
    return nights * 140;
    
def plane_ride_cost(city):
    if (city=="Charlotte"):
        return 183;
    elif (city=="Tampa"):
        return 220;
    elif (city=="Pittsburgh"):
        return 222;
    elif (city=="Los Angeles"):
        return 475;
        
def rental_car_cost(days):
    cost1=days*40;
    if (days>=7):
        cost1=cost1-50;
        return cost1;
    elif (days>=3):
        cost1=cost1-20;
        return cost1;
    else:
        return cost1;
    
def trip_cost(city, days, spending_money):
    sum1 = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money;
    return sum1;
    
print ("Cities List:\n1. Charlotte\n2. Tampa\n3. Pittsburgh\n4. Los Angeles");
cityName = str(raw_input("\nEnter city name: "));
days = int(raw_input("\nEnter number of days of stay: "));
spenmon = int(raw_input("\nEnter additional money you are carrying for spending: "));
print ("\n\nTotal Trip Cost: " + str(trip_cost (cityName, days, spenmon)));
x = raw_input("\n\nPress any key to exit.");
