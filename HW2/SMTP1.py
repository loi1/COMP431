def isitmail(self):
    charlist = list(self)
    if len(charlist) > 9 and self[0:4] == 'MAIL':
        del charlist[0:4]
        self = ''.join(charlist) #update string
        if (charlist[0].isspace() == False):
            return False
        while (charlist[0] == ' ' or charlist[0] == '	'):
            del charlist[0]
            if len(charlist) == 0:
                return False
        self = ''.join(charlist) #update string
        if len(charlist) == 0 or self[0:5] != 'FROM:':
            return False
        else:
            return True
    else:
        return False
def isitrcpt(self):
    charlist = list(self)
    if len(charlist) > 7 and self[0:4] == 'RCPT':
        del charlist[0:4]
        self = ''.join(charlist) #update string
        if (charlist[0].isspace() == False):
            return False
        while (charlist[0] == ' ' or charlist[0] == '	'):
            del charlist[0]
            if len(charlist) == 0:
                return False
        self = ''.join(charlist) #update string
        if len(charlist) == 0 or self[0:3] != 'TO:':
            return False
        else:
            return True
    else:
        return False
def isitdata(self):
    if len(self) > 3 and self[0:4] == 'DATA':
        if len(self) > 4 and self[4].isspace() == False:
            return False #DATAX
        if (self[4:].isspace() or not self[4:]):
            return True #DATA<whitespace> or DATA<nullspace>
        if len(self) > 4 and self[4].isspace():
            selfie = list(self)
            del selfie[0:4]
            while selfie[0].isspace == True:
                del selfie[0]
            if len(selfie) > 0 and selfie[0] != ' ' or selfie[0] != '   ':
                return -1 #DATA X
        return True
    return False
def checkmail():
    checkmail.goodsender = ''
    while 1<2:
        email = raw_input()
        print(email)
        charlist = list(email)
        checkmail.sender = ''
        
        if isitrcpt(email) == True or (isitdata(email) == True or isitdata(email) == -1):
            print '503 Bad sequence of commands'
            continue
        
        if isitmail(email) == True:
            #MAIL FROM:
            del charlist[0:4]
            email = ''.join(charlist) 
            charlist = list(email) 
            while (charlist[0] == ' ' or charlist[0] == '	'):
                del charlist[0]
            email = ''.join(charlist)
            charlist = list(email)
            del charlist[0:5]
            email = ''.join(charlist) 
            charlist = list(email)
            #<nullspace><path><nullspace>
            if len(charlist) == 0 or (charlist[0] != ' ' and charlist[0] != '	' and charlist[0] != '<'):
                print '501 Syntax error in parameters or arguments'
                continue
            #check for spaces
            while (charlist[0] == ' ' or charlist[0] == '	'):
                del charlist[0]
                if len(charlist) == 0:
                    break
            if len(charlist) == 0:
                print '501 Syntax error in parameters or arguments'
                continue
            #check for '<'
            if charlist[0] == '<':
                del charlist[0]
                if len(charlist) == 0:
                    print '501 Syntax error in parameters or arguments'
                    continue
            else:
                print '501 Syntax error in parameters or arguments'
                continue
            email = ''.join(charlist) #update string
            charlist = list(email) #update list
            #check for special char in local-part
            while charlist[0] != ' ' and charlist[0] != '	' and charlist[0] != '<' and charlist[0] != '>' and charlist[0] != '(' and charlist[0] != ')' and charlist[0] != '[' and charlist[0] != ']' and charlist[0] != '\\' and charlist[0] != '.' and charlist[0] != ',' and charlist[0] != ';' and charlist[0] != ':' and charlist[0] != '@' and charlist[0] != '"':
                checkmail.sender = checkmail.sender + charlist[0]
                del charlist[0]
                if len(charlist) == 0:
                    break
            if len(charlist) == 0:
                print '501 Syntax error in parameters or arguments'
                continue
            if charlist[0] == ' ' or charlist[0] == '	' or charlist[0] == '<' or charlist[0] == '>' or charlist[0] == '(' or charlist[0] == ')' or charlist[0] == '[' or charlist[0] == ']' or charlist[0] == '\\' or charlist[0] == '.' or charlist[0] == ',' or charlist[0] == ';' or charlist[0] == ':' or charlist[0] == '"':
                print '501 Syntax error in parameters or arguments'
                continue
            if charlist[0] == '@':
                checkmail.sender = checkmail.sender + charlist[0]
                del charlist[0]
                if len(charlist) == 0:
                    print '501 Syntax error in parameters or arguments'
                    continue
            if charlist[0].isalpha() == False and charlist[0].isdigit() == False:
                print '501 Syntax error in parameters or arguments'
                continue
            #check After '@'; confirmed that list is not empty!
            dotandarrow = False
            wrongchar = False
            nofirstletter = False
            while charlist[0] != '>' and len(charlist) != 0:
                #checks that first char is a letter
                if charlist[0].isalpha():
                    #checks for following chars that are letters or numbers while list is NOT empty
                    while len(charlist) != 0 and (charlist[0] != '.' and charlist[0] != '>'):
                        #if not a letter or number
                        if charlist[0].isdigit() == False and charlist[0].isalpha() == False:
                            wrongchar = True
                            break
                        else:
                            checkmail.sender = checkmail.sender + charlist[0]
                            del charlist[0]
                    if wrongchar == True:
                        break
                    if len(charlist) == 0:
                        break
                    if charlist[0] == '.':
                        checkmail.sender = checkmail.sender + charlist[0]
                        del charlist[0]
                        if len(charlist) == 0:
                            break
                        if len(charlist) != 0 and charlist[0] == '>':
                            dotandarrow = True
                        continue
                else:
                    nofirstletter = True
                    break
            if wrongchar == True or (dotandarrow == True or nofirstletter == True) or len(charlist) == 0:
                print '501 Syntax error in parameters or arguments'
                continue
            #step 6 - end with '>' and spaces
            if charlist[0] != '>':
                print '501 Syntax error in parameters or arguments'
                continue
            else:
                del charlist[0]
            if len(charlist) == 0:
                print '250 OK'
                checkmail.goodsender = checkmail.sender
                break
            if charlist[0] != ' ' and charlist[0] != '	':
                print '501 Syntax error in parameters or arguments'
                continue
            while (charlist[0] == ' ' or charlist[0] == '	'):
                del charlist[0]
                if len(charlist) == 0:
                    break
            if len(charlist) == 0:
                print '250 OK'
                checkmail.goodsender = checkmail.sender
                break
            else:
                print '501 Syntax error in parameters or arguments'
                continue
        else:
            print '500 Syntax error: command unrecognized'
            continue
        
def checkrcpt():
    rcptgood = False
    checkrcpt.rcptlist = []
    while 1<2:
        email = raw_input()
        print(email)
        charlist = list(email)
        rcpt = ''

        if isitdata(email) == -1 and rcptgood == True:
            print '501 Syntax error in parameters or arguments'
            continue
        if isitmail(email) == True or ((isitdata(email) == True or isitdata(email) == -1)and rcptgood == False):
            print '503 Bad sequence of commands'
            continue
        if isitdata(email) == True and rcptgood == True:
            print '354 Start mail input; end with <CRLF>.<CRLF>'
            break
        
        if isitrcpt(email) == True:
            #MAIL FROM:
            del charlist[0:4]
            email = ''.join(charlist) 
            charlist = list(email) 
            while (charlist[0] == ' ' or charlist[0] == '	'):
                del charlist[0]
            email = ''.join(charlist)
            charlist = list(email)
            del charlist[0:3]
            email = ''.join(charlist) 
            charlist = list(email)
            #<nullspace><path><nullspace>
            if len(charlist) == 0 or (charlist[0] != ' ' and charlist[0] != '	' and charlist[0] != '<'):
                print '501 Syntax error in parameters or arguments'
                continue
            #check for spaces
            while (charlist[0] == ' ' or charlist[0] == '	'):
                del charlist[0]
                if len(charlist) == 0:
                    break
            if len(charlist) == 0:
                print '501 Syntax error in parameters or arguments'
                continue
            #check for '<'
            if charlist[0] == '<':
                del charlist[0]
                if len(charlist) == 0:
                    print '501 Syntax error in parameters or arguments'
                    continue
            else:
                print '501 Syntax error in parameters or arguments'
                continue
            email = ''.join(charlist) #update string
            charlist = list(email) #update list
            #check for special char in local-part
            while charlist[0] != ' ' and charlist[0] != '	' and charlist[0] != '<' and charlist[0] != '>' and charlist[0] != '(' and charlist[0] != ')' and charlist[0] != '[' and charlist[0] != ']' and charlist[0] != '\\' and charlist[0] != '.' and charlist[0] != ',' and charlist[0] != ';' and charlist[0] != ':' and charlist[0] != '@' and charlist[0] != '"':
                rcpt = rcpt + charlist[0]
                del charlist[0]
                if len(charlist) == 0:
                    break
            if len(charlist) == 0:
                print '501 Syntax error in parameters or arguments'
                continue
            if charlist[0] == ' ' or charlist[0] == '	' or charlist[0] == '<' or charlist[0] == '>' or charlist[0] == '(' or charlist[0] == ')' or charlist[0] == '[' or charlist[0] == ']' or charlist[0] == '\\' or charlist[0] == '.' or charlist[0] == ',' or charlist[0] == ';' or charlist[0] == ':' or charlist[0] == '"':
                print '501 Syntax error in parameters or arguments'
                continue
            if charlist[0] == '@':
                rcpt = rcpt + charlist[0]
                del charlist[0]
                if len(charlist) == 0:
                    print '501 Syntax error in parameters or arguments'
                    continue
            if charlist[0].isalpha() == False and charlist[0].isdigit() == False:
                print '501 Syntax error in parameters or arguments'
                continue
            #check After '@'; confirmed that list is not empty!
            dotandarrow = False
            wrongchar = False
            nofirstletter = False
            while charlist[0] != '>' and len(charlist) != 0:
                #checks that first char is a letter
                if charlist[0].isalpha():
                    #checks for following chars that are letters or numbers while list is NOT empty
                    while len(charlist) != 0 and (charlist[0] != '.' and charlist[0] != '>'):
                        #if not a letter or number
                        if charlist[0].isdigit() == False and charlist[0].isalpha() == False:
                            wrongchar = True
                            break
                        else:
                            rcpt = rcpt + charlist[0]
                            del charlist[0]
                    if wrongchar == True:
                        break
                    if len(charlist) == 0:
                        break
                    if charlist[0] == '.':
                        rcpt = rcpt + charlist[0]
                        del charlist[0]
                        if len(charlist) == 0:
                            break
                        if len(charlist) != 0 and charlist[0] == '>':
                            dotandarrow = True
                        continue
                else:
                    nofirstletter = True
                    break
            if wrongchar == True or (dotandarrow == True or nofirstletter == True) or len(charlist) == 0:
                print '501 Syntax error in parameters or arguments'
                continue
            #step 6 - end with '>' and spaces
            if charlist[0] != '>':
                print '501 Syntax error in parameters or arguments'
                continue
            else:
                del charlist[0]
            if len(charlist) == 0:
                print '250 OK'
                checkrcpt.rcptlist.append(rcpt)
                rcptgood = True
                continue
            if charlist[0] != ' ' and charlist[0] != '	':
                print '501 Syntax error in parameters or arguments'
                continue
            while (charlist[0] == ' ' or charlist[0] == '	'):
                del charlist[0]
                if len(charlist) == 0:
                    break
            if len(charlist) == 0:
                print '250 OK'
                checkrcpt.rcptlist.append(rcpt)
                rcptgood = True
                continue
            else:
                print '501 Syntax error in parameters or arguments'
                continue
        else:
            print '500 Syntax error: command unrecognized'
            continue
def checkdata():
    checkdata.message = ''
    while 1<2:
        msg = raw_input()
        print(msg)
        if (msg == '.'):
            print '250 OK'
            break
        else:
            checkdata.message = checkdata.message+msg+'\n'
while 1<2:
    #reset all data for new cycle
    #mailgood = False
    rcptgood = False
    datagood = False
    sender = ''
    rcptlist = []
    rcptprint = ''
    message = ''

    try:
        checkmail()
    except EOFError:
        break
    try:
        checkrcpt()
    except EOFError:
        break  
    try:
        checkdata()
    except EOFError:
        break
    
    sender = checkmail.goodsender
    message = 'From: <'+sender+'>\n'
    rcptlist = checkrcpt.rcptlist
    for rcpt in rcptlist:
        message = message+'To: <'+rcpt+'>\n'
    #if checkdata.message == '':
        #message = message.rstrip('\n') #should be message[:-1] but w/e
    #else:
    message = message+checkdata.message
    #print sender
    #print rcptlist 
    #print message
    for rcpt in rcptlist:
        f= open('forward/'+rcpt,"a+")
        f.write(message)
        f.close()
    
