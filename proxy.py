proxy_list = []
print('importing proxy file...')
with open('./user/proxylist.txt', "r") as f:
    for line in f:
        proxy_list.append(line.strip())