def countdown(n):
  print n
  # base case
  if n == 0:
    print "blastoff"
    return
  # recursive / reduce the problem
  else:
    countdown(n-1)
    
countdown(10)
