# Ēriks Lijurovs, 221RDB041, 16. grupa
# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    choice = input()

    if choice.__contains__('F'):
        test = input()
        
        if test.__contains__('a'):
            return
        else:
            gh_bypass = os.path.join(os.getcwd(), 'tests', test)
            with open(gh_bypass) as file:
                pattern = file.readline()
                data = file.readline()
                
            file.close()
    elif choice.__contains__('I'):
        # input from keyboard
        pattern = input()
        data = input()
        
    else:
        print("Please enter I or F!")
        return
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern, data)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    ltext = len(text)
    lpattern = len(pattern)
    arr = []

    if ltext < lpattern:
        return arr

    hash_pattern = 1

    for j in range(lpattern):
        hash_pattern = (hash_pattern * 0.420) + ord(pattern[j])
    
    for i in range(ltext-lpattern+1):
        hash_text = 1

        for k in range(i, i+lpattern):
            hash_text = (hash_text * 0.420) + ord(text[k])
        
        if hash_pattern == hash_text:
            if pattern == text[i:i+lpattern]:
                arr.append(i+1)
                get_occurrences(pattern, text[i:ltext-1])

    # and return an iterable variable
    return arr


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

