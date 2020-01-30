while (1<2):
    try:
        email = raw_input()
    except EOFError:
        break
    print(email)
    charlist = list(email)
#step 1 - 'MAIL'
    if len(email) == 0 or email[0:4] != 'MAIL':
        print 'ERROR -- mail-from-cmd'
        continue
    else:
        del charlist[0:4]
        email = ''.join(charlist) #update string
        charlist = list(email) #update list
#step 2 - Spaces
    if len(charlist) == 0 or (charlist[0] != ' ' and charlist[0] != '	'):
        print 'ERROR -- mail-from-cmd'
        continue
    while (charlist[0] == ' ' or charlist[0] == '	'):
        del charlist[0]
        if len(charlist) == 0:
            print 'ERROR -- mail-from-cmd'
            break
    if len(charlist) == 0:
        continue
    email = ''.join(charlist) #update string
    charlist = list(email) #update list
#step 3 - 'FROM:'
    if len(email) == 0 or email[0:5] != 'FROM:':
        print 'ERROR -- mail-from-cmd'
        continue
    else:
        del charlist[0:5]
        email = ''.join(charlist) #update string
        charlist = list(email) #update list
#step 4 - more Spaces
    if len(charlist) == 0 or (charlist[0] != ' ' and charlist[0] != '	' and charlist[0] != '<'):
        if len(charlist) == 0:
            print 'ERROR -- path'
            continue
        print 'ERROR -- nullspace'
        continue
    #check for spaces
    while (charlist[0] == ' ' or charlist[0] == '	'):
        del charlist[0]
        if len(charlist) == 0:
            break
    if len(charlist) == 0:
        print 'ERROR -- path'
        continue
    #check for '<'
    if charlist[0] == '<':
        del charlist[0]
        if len(charlist) == 0:
            print 'ERROR -- char'
            continue
    else:
        print 'ERROR -- path'
        continue
    email = ''.join(charlist) #update string
    charlist = list(email) #update list
    #at this point we confirmed that charlist is NOT empty
#step 5 - <local-part>
    #first letter
    
    
    #if charlist[0].isalpha() == False:
    #    if charlist[0] == '@':
    #        print 'ERROR -- local-part'
    #        continue
    #    print 'ERROR -- char'
    #    continue
    #else:
    #    del charlist[0]
    #    if len(charlist) == 0:
    #        print 'ERROR -- mailbox'
    #        continue


    email = ''.join(charlist) #update string
    #check for special char in local-part
    while charlist[0] != ' ' and charlist[0] != '	' and charlist[0] != '<' and charlist[0] != '>' and charlist[0] != '(' and charlist[0] != ')' and charlist[0] != '[' and charlist[0] != ']' and charlist[0] != '\\' and charlist[0] != '.' and charlist[0] != ',' and charlist[0] != ';' and charlist[0] != ':' and charlist[0] != '@' and charlist[0] != '"':
        del charlist[0]
        if len(charlist) == 0:
            break
    if len(charlist) == 0:
        print 'ERROR -- mailbox'
        continue
    if charlist[0] == ' ' or charlist[0] == '	' or charlist[0] == '<' or charlist[0] == '>' or charlist[0] == '(' or charlist[0] == ')' or charlist[0] == '[' or charlist[0] == ']' or charlist[0] == '\\' or charlist[0] == '.' or charlist[0] == ',' or charlist[0] == ';' or charlist[0] == ':' or charlist[0] == '"':
        if charlist[0] == ' ' or charlist[0] == '	':
            print 'ERROR -- SP'
            continue
        print 'ERROR -- special'
        continue
    if charlist[0] == '@':
        del charlist[0]
        if len(charlist) == 0:
            print 'ERROR -- mailbox'
            continue
    if charlist[0].isalpha() == False and charlist[0].isdigit() == False:
        print 'ERROR -- letter'
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
                    del charlist[0]
            if wrongchar == True:
                break
            if len(charlist) == 0:
                break
            if charlist[0] == '.':
                del charlist[0]
                if len(charlist) == 0:
                    break
                if len(charlist) != 0 and charlist[0] == '>':
                    dotandarrow = True
                continue
        else:
            nofirstletter = True
            break
    if wrongchar == True:
        print 'ERROR -- let-dig-str'
        continue
    if dotandarrow == True or nofirstletter == True:
        print 'ERROR -- letter'
        continue
    if len(charlist) == 0:
        print 'ERROR -- path'
        continue
    if charlist[0] != '>':
        print 'ERROR -- path'
        continue
#step 6 - end with '>' and spaces
    else:
        del charlist[0]
    if len(charlist) == 0:
        print 'Sender ok'
        continue
    if charlist[0] != ' ' and charlist[0] != '	':
        print 'ERROR -- SP'
        continue
    while (charlist[0] == ' ' or charlist[0] == '	'):
        del charlist[0]
        if len(charlist) == 0:
            break
    if len(charlist) == 0:
        print 'Sender ok'
    else:
        print 'ERROR -- SP'
