# zmienna = "  taki piekny dzien  "
# zmienna = zmienna.split()
# print(zmienna)
#
#
# for i in zmienna:
#     print(i)
a = ['aaa;sss;ddd\n', 'aaa1;sss1;ddd\n', 'aaa2;sss2;ddd\n']
for i, v in enumerate(a):
    vSplit = v.split(";")
    if vSplit[1] == "sss":
        print(vSplit[2])