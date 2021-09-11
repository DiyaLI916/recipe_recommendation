import csv
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

filename = '/Users/diyali/Desktop/user_item_dataset/interactions_validation.csv'
row_val, recipe_val = read_csv(filename)
filename = '/Users/diyali/Desktop/user_item_dataset/interactions_test.csv'
row_test, recipe_test = read_csv(filename)
filename = '/Users/diyali/Desktop/user_item_dataset/interactions_train.csv'
row_train, recipe_train = read_csv(filename)

recipe_ratings = open('../data/recipe/ratings_final0.txt', 'w')
final_u_i = []
total_row = []
total_row = row_train + row_test + row_val

for row in total_row:
    user = row[4]
    item = row[5]
    rating = float(row[3])
    score = -1
    if rating >= 4:
        score = 1

    elif rating <=2 and rating > 0:
        score = 0

    if score > -1:
        line = user + '\t' + item + '\t' + str(score) + '\n'
        final_u_i.append(line)
        recipe_ratings.write(line)
    # exit()

print(len(recipe_val), len(set(recipe_val)))
print(len(recipe_test), len(set(recipe_test)))
print(len(recipe_train), len(set(recipe_train)))
# 673321
print(len(final_u_i))