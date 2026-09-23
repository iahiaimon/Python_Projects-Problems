
def create_character(name, strength, intelligence, charisma):
    full_dot = '●'
    empty_dot = '○'
    if not isinstance(name , str):
        print( "The character name should be a string")
    elif name == "":
        print( "The character should have a name")
    elif len(name)> 10 : 
        print( "The character name is too long")
    elif " " in name :
        print( "The character name should not contain spaces")
    stats = [strength, intelligence, charisma]

    if not all(isinstance(stat, int)for stat in stats):
        print( "All stats should be integers")
    elif any(stat < 1 for stat in stats):
        print( "All stats should be no less than 1")
    elif any(stat > 4 for stat in stats):
        print( "All stats should be no more than 4")
    elif sum(stats)!=7:
        print( "The character should start with 7 points")
    
    f_str = f"STR {full_dot*strength}{empty_dot*(10-strength)}"
    f_int = f"INT {full_dot*intelligence}{empty_dot*(10-intelligence)}"
    f_cha = f"CHA {full_dot*charisma}{empty_dot*(10-charisma)}"
    print((f"{name}\n{f_str}\n{f_int}\n{f_cha}"))

create_character("imon",5,3,1)