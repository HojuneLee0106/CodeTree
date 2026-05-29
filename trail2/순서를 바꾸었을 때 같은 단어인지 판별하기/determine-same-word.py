word1 = input()
word2 = input()
word_1=list(word1)
word_2=list(word2)
word_1.sort()
word_2.sort()
answer=True
if len(word1)!=len(word2):
    print("No")
else:
    for i in range(len(word1)):
        if word_1[i]!=word_2[i]:
            answer=False
            break
    if answer:
        print("Yes")
    else:
        print("No")
# Please write your code here.
