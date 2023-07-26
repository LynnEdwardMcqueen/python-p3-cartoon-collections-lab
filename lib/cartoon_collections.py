def roll_call_dwarves(dwarf_names):
    i = 1
    for dwarf in dwarf_names:
        print(f"{i}. {dwarf}")
        i += 1

def summon_captain_planet(call_list):
    # return [call.capitalize().join("!") for call in call_list]
    ret_val = [call.capitalize() for call in call_list]
    for i in range( len(ret_val)):
        ret_val[i] += "!"
    return ret_val


def long_planeteer_calls(call_list):
    for call in call_list:
        if len(call) > 4:
            return True
    
    return False

def find_the_cheese(snack_list):
    target_cheeses = ["cheddar", "gouda", "camembert"]

    for target_cheese in target_cheeses:
        if target_cheese in snack_list:
            return target_cheese
    
    return None


roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"])
print(summon_captain_planet(["earth", "wind", "fire", "water", "heart"]))
print(find_the_cheese(["crackers", "gouda", "thyme"]))
print(find_the_cheese(["tomato soup", "cheddar", "oyster crackers", "gouda"]))
print(find_the_cheese(["garlic", "rosemary", "bread"]))
print( long_planeteer_calls(["puff", "go", "two"]))
print( long_planeteer_calls(["two", "go", "industrious", "bop"]))