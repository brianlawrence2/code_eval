import sys

def fizzbuzz(first_divisor, second_divisor, number):
  if number % first_divisor == 0 and number % second_divisor == 0:
    return 'FB'
  elif number % first_divisor == 0:
    return 'F'
  elif number % second_divisor == 0:
    return 'B'
  else:
    return number

def fizzbuzzer(first_divisor, second_divisor, num):
  """
  @param first_divisor: The first divisor passed in
  @param second_divisor: The second divisor passed in
  @param length: The number to count
  """
  output = []
  for i in range(1,num+1):
    output.append(fizzbuzz(first_divisor, second_divisor, i))
      
  return ' '.join(str(x) for x in output)


if __name__ == '__main__':
  test_cases = open(sys.argv[1], 'r')
  
  output = []
  for test in test_cases:
  
    test_params = test.split()
    first_divisor = int(test_params[0])
    second_divisor = int(test_params[1])
    num = int(test_params[2])
    
    output.append(fizzbuzzer(first_divisor,second_divisor,num))
  
  print(' \n'.join(output),end="")
    
  test_cases.close()