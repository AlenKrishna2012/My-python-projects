import webbrowser
def open_url():
    while True:
        url = input(' Enter URL (e.g., "example.com" only) : ') #Enter url
        url_real = 'https://' + url #add htpp://
        
        yn = input(f' Do you want to open the URL "{url_real}"? (y/n): ')# takes input to go back or not
        
        if yn.lower() == 'y':
            webbrowser.open(url_real)#if user enter y opens url
            break  
        elif yn.lower() == 'n':#if user enter n it starts from beginning
            continue
        else:
            print(' Invalid option. Please choose y or n.')#if not y/n print invalid option
while True:
	open_url()
	
	print('\n')