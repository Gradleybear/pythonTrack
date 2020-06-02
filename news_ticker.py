#Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long.
#You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline.
#If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.

#Remember that break works in both for and while loops. Use whichever loop seems most appropriate.
# Consider adding print statements to your code to help you resolve bugs.
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
i = 140
j=0
char_count=0
while j<= i and j<len(headlines):
  if len(headlines[j])+char_count > i:
    print("skipping the {}".format(headlines[j]))
    j+=1
    continue
  elif char_count >= i:
    print("exiting loop")
  else:
    news_ticker= news_ticker+ ' ' + headlines[j]
    char_count+= len(headlines[j])
    print("Adding {} of length {}".format(headlines[j], len(headlines[j])))
  j+=1
print(news_ticker,len(news_ticker))
# write your loop here



print(news_ticker)
