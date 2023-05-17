import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # gets address from command line
    address = " ".join(sys.argv[1:])

else:
    # gets address from clipboard
    address = pyperclip.paste()


webbrowser.open('https://www.google.com/maps/place/' + address)