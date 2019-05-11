# checks-over-stripes
by @navar_jande on twitter

## dependancies
### using pipenv
current pipfile requires 3.7.3 in order to run
if not on 3.7.3 change to your version of python if you know how otherwise run without pipenv
### without pipenv
these programs require selenium in order to use so make sure you have it installed
if not run the following command
```
pip install selenium
```

## before you run
files that are editable by the user are conveniently located in the /user folder
### config.json
#### domain
a catch-all domain is required for all your nike accounts. look up how to set up a catch-all email if you dont already have one. supports only 1 catch all so far.
#### password
a valid password must have the following:
+ at least 8 characters in length
+ 1 upper case letter
+ 1 number

### proxylist.txt
currently only supporting ip auth proxies so paste them in this file, one proxy per line

## how to run
run this command in the folder in order to start the account creation process
```
python main.py
```
enter in how many accounts you would like to create.
do not touch anything and just let it run even if you see an error.
after all is done your accounts [email:password] to a file in the /user/ folder.
