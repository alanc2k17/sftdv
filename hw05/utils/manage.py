def add_user(username, password):
    f = open('data/credentials.csv', 'a')
    f.write('\n' + str(username) + ',' + str(password))
    f.close()

def get_users():
    f = open('data/credentials.csv', 'r')
    contents = f.read().split('\n')
    user_list = dict()
        
    for item in contents:
        user_list[item.split(',')[0]] = item.split(',')[1]

    return user_list
