import json
import re
# import the config file
print('importing config file...')
with open('./user/config.json') as config_file:
    config = json.load(config_file)

# validate password here
password = config["password"]
if len(password) < 8 or re.search('[0-9]', password) is None or re.search('[A-Z]', password) is None:
    # means invalid password
    print('your password [{}] is invalid. using [{}] instead.'.format(password, "Navarjande2019"))
    config["password"] = "Navarjande2019"
