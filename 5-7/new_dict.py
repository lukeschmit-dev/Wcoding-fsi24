# 1. Create a dictionary called player_one with:
#    a "username" property set to "N00BMAX"
#    a "points" property set to 9001

player_one = {"username": "N00BMAX", "points": 9001}

#    b. Print out its missing "achievements" property in a way that doesn't crash
ach = player_one.get("achievements")
print(ach)

#    c. Set the "achievements" property to ["First Kill", "Last Death"], but
#        only if it is not already present in the dictionary.
#        Then, print out player_one.

if "achievements" not in player_one:
    player_one["achievements"] = ["First Kill", "Last Death"]

print(player_one)