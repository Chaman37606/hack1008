def gcd(m,n):
  
  for i in range(1,min(m,n)+1):
   if (m%i==0)and(n%i==0):
    cf=i
  return(cf)


s=gcd(28,14) 
print(s) 
  	  
