def removechars(string):
    str_list = string.split(', ')
    for char in str_list[1]:
        str_list[0] = str_list[0].replace(char, '')
                
    return str_list[0]
    
if __name__ == '__main__':
    import sys
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        print removechars(test)
        
    test_cases.close()