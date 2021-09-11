def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

def test_restaurant_data():
    kg = open('../restaurant/kg_final.txt').readlines()
    user = open('../restaurant/ratings_final.txt').readlines()
    print(len(kg), len(user))
    kg1 = []
    u = []
    kg2 = []
    for row in kg:
        row = row.strip().split('\t')
        k1 = int(row[0])
        k2 = int(row[2])
        kg1.append(k1)
        kg1.append(k2)

    for row in user:
        row = row.strip().split('\t')
        user = int(row[0])
        k3 = int(row[1])
        u.append(user)
        kg2.append(k3)
    print(len(set(kg1)), len(set(kg2)), len(set(u)))

def test_recipe_data():
    filtered_u_i = []
    kg = open('kg_final0.txt').readlines()
    user = open('ratings_final0.txt').readlines()
    print(len(kg), len(user))
    # 348273 673321

    kg1 = []
    u = []
    kg2 = []
    for row in kg:
        row = row.strip().split('\t')
        k1 = int(row[0])
        k2 = int(row[2])
        kg1.append(k1)
        kg1.append(k2)

    for row in user:
        row = row.strip().split('\t')
        u0 = int(row[0])
        k3 = int(row[1])
        u.append(u0)
        kg2.append(k3)

    print(len(set(kg1)), len(set(kg2)), len(set(u)))
    # 102717 170510 24957
    exit()

    intersection = set.intersection(set(kg1), set(kg2))
    print(len(intersection), type(intersection))

    u_new = []
    kg_new = []

    for row in user:
        row0 = row.strip().split('\t')
        u0 = int(row0[0])
        k3 = int(row0[1])
        if k3 in intersection:
            u_new.append(u0)
            kg_new.append(k3)
            filtered_u_i.append(row)
    u_idx = list(set(u_new))
    kg_idx = list(set(kg_new))

    temp = []
    for i in range(len(u_idx)):
        temp.append(i)
    u_dict = dict(zip(u_idx, temp))

    temp = []
    for i in range(len(kg_idx)):
        temp.append(i)
    kg_dict = dict(zip(kg_idx, temp))

    # make new kg files ...
    extra_kg = list(set(kg1) - intersection)
    print(extra_kg, len(intersection), len(kg_idx))

    temp = []
    for i in range(len(kg_idx), len(set(kg1))):
        temp.append(i)
    kg_dict2 = dict(zip(extra_kg, temp))
    new_kg_file = open('kg_final.txt', 'w')

    final_kg_dict = Merge(kg_dict, kg_dict2)
    print(len(final_kg_dict), len(kg_dict) + len(kg_dict2))

    for row in kg:
        row0 = row.strip().split('\t')
        kg_0 = int(row0[0])
        kg_1 = int(row0[2])
        score = row0[1]
        line = str(final_kg_dict[kg_0]) + '\t' + score + '\t' + str(final_kg_dict[kg_1]) + '\n'
        # print(line)
        new_kg_file.write(line)

test_recipe_data()