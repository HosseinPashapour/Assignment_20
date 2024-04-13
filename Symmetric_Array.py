userList = input('Please Enter a list of numbers seperated by a space: ').split(' ')

if len(userList) % 2 != 0:
    for i in range(0, (len(userList) // 2)):
        if userList[i] != userList[-1-i]:

            print('❌Your Array Not symmetric❌')
            exit()

    print('✅Your Array are symmetric✅')
else:
    print('❌Your Array Not symmetric❌')
