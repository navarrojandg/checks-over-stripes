import datetime
from randomnames import RandomNames
from randomdob import RandomBirthday
from nikeaccount import NikeAccount
from proxy import proxy_list

number_of_accounts = int(input("How many accounts do you wish to create? - "))

# create random names class
random_names = RandomNames()
#create random dob class
random_dob = RandomBirthday()


nike_accounts = []
while len(nike_accounts) < number_of_accounts:
    i = 0
    j = 0
    if len(proxy_list) > 0:
        try:
            proxy = proxy_list[j]
        except IndexError:
            j = 0
            proxy = proxy_list[j]
        finally:
            nike_account = NikeAccount(random_names.get_random(),random_dob.get_random(),i, proxy)

    else:
        nike_account = NikeAccount(random_names.get_random(),random_dob.get_random(),i)
    nike_account.create()
    if nike_account.created == True:
        nike_accounts.append(nike_account.export())
    i += 1
    j += 1
    
filename = "{}-checks-over-stripes.txt".format(datetime.datetime.now().strftime("%m%d%y"))
print('writing accounts to file: [/user/{}]'.format(filename))
with open("./user/{}".format(filename), "a+") as f:
    for acc in nike_accounts:
        f.write(acc + '\n')


