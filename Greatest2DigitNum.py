def LargestPair(num):

  res = 0
  s = str(num)

  for i in range(len(s) - 1):
      if int(s[i] + s[i+1]) > res:
        res = int(s[i] + s[i+1])
  return res


# keep this function call here
print(LargestPair(input("Enter the number:")))