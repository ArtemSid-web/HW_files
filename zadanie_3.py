m_dic = {}

with open('1.txt', 'rt', encoding='utf-8') as f_1:
    s_1 = []
    c = 0
    for line in f_1.readlines():
        c += 1
        s_1.append(line.strip())
    s_1.insert(0, '1.txt')
    s_1.insert(1, str(c))
    m_dic[str(c)] = s_1

with open('2.txt', 'rt', encoding='utf-8') as f_1:
    s_2 = []
    x = 0
    for line in f_1.readlines():
        x += 1
        s_2.append(line.strip())
    s_2.insert(0, '2.txt')
    s_2.insert(1, str(x))
    m_dic[str(x)] = s_2

with open('3.txt', 'rt', encoding='utf-8') as f_1:
    s_3 = []
    z = 0
    for line in f_1.readlines():
        z += 1
        s_3.append(line.strip())
    s_3.insert(0, '3.txt')
    s_3.insert(1, str(z))
    m_dic[str(z)] = s_3

d_sort = dict(sorted(m_dic.items(), key=lambda x: x[0]))

with open('res.txt', 'w', encoding='utf-8') as f:
    for i in d_sort.values():
        for k in i:
            f.write(f'{k}\n')

with open('res.txt', 'r', encoding='utf-8') as a:
    for j in a.readlines():
        print(j.strip())