def friends(*name) :
    for n in name :
        print(n.title())

friends('alice', 'paul')
print('-------')
friends('cindy', 'sally', 'david', 'tom')
