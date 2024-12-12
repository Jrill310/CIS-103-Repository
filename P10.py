def main():
    text = '''
       Python was conceived in the late 1980’s by Netherlands programmer
Guido Van Rossum and rolled out in 1991. Developing the language
was a hobby project for Van Rossum to keep him occupied over
Christmas, though he soon began implementing the language at
his employer Centrum Wiskunde & Informatica (CWI). The name of
the language was inspired by Monty Python’s Flying Circus, and
today users of this code often work in references to Monty Python.
Python is one of the most popular programming languages in the
world. As a scripting language that can automate a complex series
of tasks, Python is used on the back end of many web applications,
games, and digital and animated special effects. Sites like YouTube
and Instagram are among some of the titans that rely on this
language to support both front-end and back-end functionality.    
        '''
    print(text)

# ---------------------------------
    little = 'little'
    titan = 'titan'
    Length = len(text)
    print ("overall length:",Length)
    nospace = text.strip()
    nospacelength = len(nospace)
    print ('length with no beginning or end spaces:',nospacelength)
    the = text.count('the')
    The = text.count('The')
    these = The + the
    print ('uses of the word "the":',these)
    if little in text:
        print ('"little" is in this text')
    else:
        print ('"little" is not in this text')
    if titan in text:
        print ('"titan" is in this text')
    else:
        print ('"titan" is not in this text')
    appl = nospace.find('appl')
    print ('position of "appl":',appl)
    text2 = text
    text2 = text2.replace('python','PYTHON')
    print (text2)

# ---------------------------------

    return
main()
