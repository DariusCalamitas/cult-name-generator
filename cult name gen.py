import json
import random

f = open('Names.json')
names_import = json.load(f)
names_human = names_import["human_names"]
names_cult = names_import["cult_names"]

def human_name_generate():
    #First Name
    first_name = (random.choice(names_human["first_names"]) + " ").title()

    #Last Name
    last_name_keys = list(names_human["last_names"].keys())
    last_name_category = random.choice(last_name_keys)
    last_names_list = names_human["last_names"][last_name_category]
    last_name = (random.choice(last_names_list)).title()

    #Nickname
    if random.randint(1, 2) == 1:
        middle_name_keys = list(names_human["nicknames"].keys())
        middle_name_category = random.choice(middle_name_keys)
        middle_names_list = names_human["nicknames"][middle_name_category]
        middle_name = ("\"" + random.choice(middle_names_list) + "\" ").title()
    else:
        middle_name = ""

    #Prefix
    if random.randint(1, 2) == 1:
        prefix = random.choice(names_human["prefixes"])
    else:
        prefix = ""


    return(first_name + middle_name + prefix + last_name)

def cult_name_generate():

    #Type of following
    following_type = (random.choice(names_cult["cult_synonyms"])).title()

    #Object of Worship
    adjective_keys = list(names_cult["cult_worship_cause"]["adjectives"].keys())
    adjective_category = random.choice(adjective_keys)
    adjective_list = names_cult["cult_worship_cause"]["adjectives"][adjective_category]
    adjective = (random.choice(adjective_list)).title()

    worship_object_keys = list(names_cult["cult_worship_cause"]["objects_of_worship"].keys())
    worship_object_category = random.choice(worship_object_keys)
    worship_objects_list = (names_cult["cult_worship_cause"]["objects_of_worship"][worship_object_category])
    worship_object = (random.choice(worship_objects_list)).title()
    return(following_type + " of the " + adjective + " " + worship_object)

print(
    "\n~" + cult_name_generate() + "~\n"
)

for _ in range(random.randint(3, 7)):
    print(human_name_generate())