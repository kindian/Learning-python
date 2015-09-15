import urllib.request
theurl = 'https://teamforge-stg.nam.nsroot.net/sf/sfmain/do/home'
username = 'kp95270'
password = 'password'
passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, theurl, username, password)
authhandler = urllib.request.HTTPBasicAuthHandler(passman)
opener = urllib.request.build_opener(authhandler)

urllib.request.install_opener(opener)
pagehandle = urllib.request.urlopen(theurl)
