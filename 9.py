class Calculator:
  def __init__(self):
    self.result = 0
  
  def add(self,num):
    self.result += num
    return self.result
  
  def sub(self,num):
    self.result -= num
    return self.result
  
  def reset(self):
    self.result = 0
    return self.result
  
  def set(self, num):
    self.result = num
    return self.result
cal1 = Calculator()

print(cal1.add(4))
print(cal1.add(5))
print(cal1.sub(4))
print(cal1.sub(2))
print(cal1.reset())
print(cal1.set(32))
