import os
arr = os.listdir()
final_kg = {}
i = 0
for file in arr:
    if 'txt' in file:
        print(file)
        i += 1
        sample = open(file).readlines()
        for item in sample:
            item = item.strip().split('\t')
            item0 = int(item[0])
            item1 = int(item[1])
            if item0 > item1:
                temp_set = (item1, item0)
                if temp_set not in final_kg.keys():
                    final_kg[temp_set] = item[2]

            elif item0 < item1:
                temp_set = (item0, item1)
                if temp_set not in final_kg.keys():
                    final_kg[temp_set] = item[2]
        # break
final_kg_file = open('../data/recipe/kg_final0.txt', 'w')
for key in final_kg.keys():
    # line = str(key[0]) + '\t' + str(key[1]) + '\t' + final_kg[key] + '\n'
    line = str(key[0]) + '\t1\t' + str(key[1]) + '\n'
    final_kg_file.write(line)
print(len(final_kg), i)