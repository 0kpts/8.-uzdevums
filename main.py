def dragon(start:int, end:int):
  default = 3
  for i in range(start, end):
    if i < 100:
      default += 3
    else:
      default += 2
  
  return {
    "heads": default,
    "eyes": default * 2,
    "years": end,
  }

if __name__ == "__main__":
  print(dragon(start=0, end=120))