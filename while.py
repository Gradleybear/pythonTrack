start_num = 55#provide some start number
end_num =89 #provide some end number that you stop when you hit
count_by =12 #provide some number to count by

# write a while loop that uses break_num as the ongoing number to
#   check against end_num
start_num = 5
end_num = 100
count_by = 2

break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)

limit = 40
# write your while loop hereb
nearest_square= 1
i=0
while (i+1)**2 < limit:
    i+=1
    nearest_square= i**2
    print(nearest_square, i)


print(nearest_square)
