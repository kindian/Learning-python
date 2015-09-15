#import webbrowser for browser based operation
import webbrowser
#import os for file and directory related operation
import os
#os.chdir('path') will change the current working directory to 'path' mentioned
os.chdir('C:\Python34\Lib\site-packages')
def Checkout_urls():
    with open('url_list.txt', 'r') as ul:
        for line in ul:
            webbrowser.open(line)
            
#url_list.txt contains the list of urls to open

def add_urls(url):
    with open('url_list.txt', 'a') as au:
        au.write('\n')
        au.write(url)
    with open('url_list.txt', 'r') as l:
        for line in l:
            print(line)

#while calling function add_urls(), provide the new url as arguement to add in the url_list.txt file
