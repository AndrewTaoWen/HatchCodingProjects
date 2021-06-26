def factorial(n):
  for i in range(n,1,-1) :
    if i == n:
      answer = n
    else:
      answer = i*answer
  return answer

number=int(input('number'))
print(factorial(number))
      
      

    