konu=("peziza" ,"varia")
konuu=""
for i in range(len(konu)):
    if i == 0:
        konuu = konuu + konu[i]
    else:
        konuu = konuu + "_" + konu[i]
print(konuu)