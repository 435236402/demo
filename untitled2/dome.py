from redis import StrictRedis

if __name__ == '__main__':
  sr = StrictRedis()
  # result = sr.set('name','itcast')
  # print(result)
  result = sr.get('name')
  # print(result)
  # result = sr.set('name','itheima')
  # print(result)
  # result = sr.delete('name')
  # print(result)
  result = sr.keys()
  print(result)