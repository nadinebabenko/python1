info=input("Please input a string that is 10 chars long")
infolen=len(info)
if infolen > 10:
    print("Too long")
elif infolen < 10:
    print("Too short")
else:
    print("Perfect length")

#2

string_list=list(info)
print(f"First char: {string_list[0]}, last char: {string_list[-1]}")
# 3
for i in range(0,infolen):
    print(string_list[0:i+1])
