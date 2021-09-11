import csv
import ast
# initializing the titles and rows list
def similarity(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    len3 = len(set.intersection(s1, s2))
    sim = 2 * len3 / (len1 + len2)
    return sim

def read_csv(filename):
    rows = []
    recipes = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        # extracting field names through first row
        fields = next(csvreader)
        print(fields)
        for row in csvreader:
            rows.append(row)
            recipes.append(row[1])
        print("Total no. of rows: %d" % (csvreader.line_num))
    return rows, recipes

def read_recipes(filename):
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        # extracting field names through first row
        fields = next(csvreader)
        print(fields)
        rows = [list(row) for row in csvreader]
        # for row in csvreader:
        #     rows.append(row)
        print("Total no. of rows: %d" % (csvreader.line_num))
    return rows

filename = 'user_item_dataset/interactions_validation.csv'
row_val, recipe_val = read_csv(filename)
filename = 'user_item_dataset/interactions_test.csv'
row_test, recipe_test = read_csv(filename)
filename = 'user_item_dataset/interactions_train.csv'
row_train, recipe_train = read_csv(filename)

print(len(recipe_val), len(set(recipe_val)))
print(len(recipe_test), len(set(recipe_test)))
print(len(recipe_train), len(set(recipe_train)))

recipe_full = read_recipes('user_item_dataset/PP_recipes.csv')
print(len(recipe_full))
# print(recipe_full[3])
# ['id', 'i', 'name_tokens', 'ingredient_tokens', 'steps_tokens', 'techniques', 'calorie_level', 'ingredient_ids']
recipe_dict = {}
for item in recipe_full:
    # print(item)
    i = item[1]
    name_tokens = ast.literal_eval(item[2])[1:-1]
    calorie_level = item[6]
    ingredient_ids = ast.literal_eval(item[7])
    recipe_dict[i] = {}
    recipe_dict[i]['name'] = set(name_tokens)
    recipe_dict[i]['calorie'] = calorie_level
    recipe_dict[i]['ingre'] = set(ingredient_ids)

    # print(name_tokens, '\t', calorie_level, '\t', ingredient_ids)
    # exit()
# print(recipe_dict)
# ids = i (integer)
ids = list(recipe_dict.keys())
print(ids[:20])
exit()


# start cal sim ...
file = open('graph.txt', 'a+')

for i in range(len(ids) - 1):
    print(i)
    for j in range(i+1, len(ids)):
        name_i = recipe_dict[ids[i]]['name']
        cal_i = recipe_dict[ids[i]]['calorie']
        ingre_i = recipe_dict[ids[i]]['ingre']

        name_j = recipe_dict[ids[j]]['name']
        cal_j = recipe_dict[ids[j]]['calorie']
        ingre_j = recipe_dict[ids[j]]['ingre']

        sim_name = similarity(name_i, name_j)
        if sim_name > 0.3:
            sim_ingre = similarity(ingre_i, ingre_j)
            if sim_ingre > 0.3:
                # print(i, j)
                # print(sim_name, sim_ingre)
                # print(name_i, name_j)
                pro = (sim_name + sim_ingre) / 2
                line = str(ids[i]) + '\t' + str(ids[j]) + '\t' + str(pro) + '\n'
                file.write(line)
        else:
            continue



