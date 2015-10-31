#8.1
def answer():
    return 42

#8.2
def hotel_cost(nights):
    return 140 * nights

#8.3
def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city=="Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

#8.4
def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city=="Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    if days>=7:
        return days * 40 - 50
    elif days>=3:
        return days * 40 - 20
    else:
        return days*40

#8.5
def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city=="Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    if days>=7:
        return days * 40 - 50
    elif days>=3:
        return days * 40 - 20
    else:
        return days*40

def trip_cost(city, days):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days)

#8.6
def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city=="Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    if days>=7:
        return days * 40 - 50
    elif days>=3:
        return days * 40 - 20
    else:
        return days*40

def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

#8.7
def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city=="Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    if days>=7:
        return days * 40 - 50
    elif days>=3:
        return days * 40 - 20
    else:
        return days*40

def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

print trip_cost("Los Angeles", 5, 600)
