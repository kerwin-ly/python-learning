
# w => write, r => read,
# f = open('./demo.txt', 'a')
#
# f.write('add content')
# f.close()

# get all content
# print(f.read())

# get content
# for each_line in f:
#     print(each_line)

# demo: read the file, save kerwin's content in kerwin.txt
f = open('./demo.txt')
content = []
for each_line in f:
    print(each_line)
    (user, info) = each_line.split(':')

    if (user == 'kerwin'):
        content.append(info)
fw = open('./kerwin.txt', 'w')
fw.writelines(content)
f.close()
fw.close()