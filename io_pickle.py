import pickle

# The name of the file where we will store the object
shoplistfile = 'shoplist.data'
# The list of things to buy
shoplist = ['apple', 'mango', 'carrot']

# Write to the file
f = open(shoplistfile, 'wb')
# 在写入二进制模式下打开的，这一过程叫封装
# Dump the object to a file
pickle.dump(shoplist, f)
f.close()

# Destroy the shoplist variable
# 虽然删除了这个变量，但是其中的对象持续的保留着
del shoplist

# Read back from the storage
f = open(shoplistfile, 'rb')
# Load the object from the file
# 再用load函数返回对象，叫做拆封
storedlist = pickle.load(f)
print(storedlist)

