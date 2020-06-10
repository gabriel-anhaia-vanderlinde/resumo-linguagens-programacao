# Desafio FizzBuzz
# Neste problema, você deverá exibir uma lista de 1 a 100, um em cada linha, com as seguintes exceções:

# Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
# Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
# Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número'.

def edivisivel(a, b):
    if a % b == 0:
        return True
    else:
        return False

def fizzbuzz(num):
    if edivisivel(num, 3) and edivisivel(num, 5):
        return 'FizzBuzz'
    elif edivisivel(num, 3):
        return 'Fizz'
    elif edivisivel(num, 5):
        return 'Buzz'
    else:
      return num
     

assert fizzbuzz(3) == 'Fizz'   
assert fizzbuzz(6) == 'Fizz'
assert fizzbuzz(9) == 'Fizz'

assert fizzbuzz(5) == 'Buzz'
assert fizzbuzz(10) == 'Buzz'

assert fizzbuzz(15) == 'FizzBuzz'
assert fizzbuzz(30) == 'FizzBuzz'
assert fizzbuzz(11) == 11
        
assert edivisivel(4, 2) == True
assert edivisivel(5, 2) == False

for i in range(1, 100 + 1):
    fb = fizzbuzz(i)
    print(fb)



    

  
print('Teste OK!')