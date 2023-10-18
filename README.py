import random

r = True

while r:
  n = random.randint(1, 100)
  g = 0
  t = 0
  
  while g != n:
    if g == 0 : 
      print("sākam!")
    elif g > n: 
      print("vajag mazāk...")
    else: 
      print("vajag vairāk...")
    
    g = int(input("uzmini skaitli! "))
    
    t += 1
    
  else: print(f"Uzminēji! Tas ir { n }! Tev vajadzēja { t } mēģinājumus!")
  
  if t < 3 :
    print("Iespaidīgi!")
  elif t < 6: 
    print("Labi!")
  elif t < 9: 
    print("Varēja būt labāk...")
  else: 
    print("Patrenējies!")
    
  q = input("Gribi vēl spēlēt? yes/no: ")
  if q == "yes" or q == "yup": r = True
  elif q == "no" or q == "nope": 
    r = False 
    print("Atā!")
  else: 
    r = False 
    print("Atā stulbeni!")
