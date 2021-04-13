fname=input('Input the filename:')
ext=fname.split('.')
if ext[-1]=='py':
    print("The extension of the file is: 'python'")
else:
    print('The extension of the file is:',ext[-1])
