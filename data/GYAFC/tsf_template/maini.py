#
# import unicodedata
# def remove_control_characters(s):
#     return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")
# with open("test.1", "r") as f:
#     n= f.readlines()
#     lili=[]
#     for item in n:
#         i=remove_control_characters(item)
#         lili.append(i)
# # print(lili)
# with open('text.txt', 'w') as f:
#     for item in lili:
#         f.write("%s\n" % item)


with open("train.0.tsf", encoding='utf8') as form:
    with open("train.1.tsf", encoding='utf8') as inform:
        with open("train.1-0.tsf", "w", encoding='utf8') as zh:
            # Read first file
            informlines = inform.readlines()
            # Read second file
            formlines = form.readlines()
            # Combine content of both lists
            # combine = list(zip(ylines,xlines))
            # Write to third file
            for i in range(len(informlines)):
                line = informlines[i].strip() + '\t' + formlines[i]
                zh.write(line)
