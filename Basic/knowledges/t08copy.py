# ------------------- 工具
# id(obj)   # 返回obj在内存中的地址
# obj1 is obj2  # 关键字is，比较前后两个obj的内存地址释放相同
# obj1 == obj2  # 运算符==， 比较前后两个obj的值是否形同

print(id(1))
# 140737143349648
print(id([1, 2, 'list']))
# 2717596078536

# ----------------- 复制操作 =
i1 = 88
i2 = i1
print(id(i1))  # 140737143352432
print(id(i2))  # 140737143352432
print(i1 is i2)  # True
i2 += 2
print(i1 is i2)  # False
print(id(i2))  # 140737143352496
# 为了节省内存，python在其内部实现时设计了共享内存的机制，
# 在进行赋值操作（=）时，并不会为新变量开辟一块新的内存空间，而是用类似指针的标记指向原变量的内存地址，共用这一块地址
# 仅仅是这样的话会在修改一个变量的时候对其他变量也产生影响，python对这种情况也做了处理，会在必要的时候为新变量再开辟地址

# 也不能说在赋值的新变量改变时，就会为新变量开辟新空间，看一下list的例子
l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = l1
print(l2 == l3) # True
print(l2 is l3) # False
print(id(l1))   # 2561117802952
print(id(l2))   # 2561117803464
print(id(l3))   # 2561117802952
l3[1] = 99
print('l3:', l3)    # l3: [1, 99, 3]
print('l1:', l1)    # l1: [1, 99, 3]
# 不只是外层的list，其内的元素也都是在共享内存的
l3.append(7)
print('l3:', l3)    # l3: [1, 99, 3, 7]
print('l1:', l1)    # l1: [1, 99, 3, 7]

# ---------------- 浅copy——copy()
l4 = [1, 2, 3, ['str1', 'str2']]
l5 = l4.copy()
print(l4 is l5) # False
# l5是l4.copy()产生的，l6开辟了新空间

print(id(l4))   # 1500684497032
print(id(l5))   # 1500684483528

# 看看其中元素的内存地址情况
print(id(l5[1]))    # 140737143349680
print(id(l4[1]))    # 140737143349680

print(id(l5[-1]))    # 1750710890632
print(id(l4[-1]))    # 1750710890632
# 对于浅copy来说，只是在内存中重新创建了开辟了一个空间存放一个新列表，但是新列表中的元素与原列表中的元素是公用的。

# 然后改变其内的值，再观察，发现就像上面说的重新开辟了空间
l5[1] = 99
print('l5:', l5)    # l5: [1, 99, 3, ['str1', 'str2']]
print('l4:', l4)    # l4: [1, 2, 3, ['str1', 'str2']]
print(id(l5[1]))    # 140737143352784   # # 进行了改变值操作，新开内存地址
print(id(l4[1]))    # 140737143349680

# 但是呢，当我想要改变其中可变数据类型list时，
l5[3][1] = 9
print(l5)   # [1, 99, 3, ['str1', 9]]
print(l4)   # [1, 2, 3, ['str1', 9]]
# 就像第1部分的例子一样，还在共享内存


print('--------------------------------')
#---------------------- 深copy——deepcopy()
import copy
l6 = [4,5,6,['str6', 'str7']]
l7 = copy.deepcopy(l6)

print(l7 is l6) # False
# l7是copy.deepcopy(l6)产生的，l6开辟了新空间

print(id(l6))   # 1971465103752
print(id(l7))   # 1971465104648

# 看看其中元素的内存地址情况
print(id(l7[1]))    # 140737143349680
print(id(l6[1]))    # 140737143349680

print(id(l7[-1]))    # 2754395918536
print(id(l6[-1]))    # 2754395841992
# 对于深copy来说，列表是在内存中重新创建的，列表中可变的数据类型是重新创建的，列表中的不可变的数据类型是公用的。

# 然后改变其内的值，再观察，发现就像上面说的重新开辟了空间
l7[1] = 99
print('l7:', l7)    # l7: [4, 99, 6, ['str6', 'str7']]
print('l6:', l6)    # l6: [4, 5, 6, ['str6', 'str7']]
print(id(l7[1]))    # 140737143352784   # 进行了改变值操作，新开内存地址
print(id(l6[1]))    # 140737143349776

# 在深copy后，再改变其内部的可变数据类型
l7[3][1] = 9
print(l7)   # [4, 99, 6, ['str6', 9]]
print(l6)   # [4, 5, 6, ['str6', 'str7']]
# 也不会发生联动改变，可以理解为真正的新开内存复制了一份，两者之间的改动完全不会相互影响

# 对于深copy来说，列表是在内存中重新创建的，列表中可变的数据类型是重新创建的，列表中的不可变的数据类型是公用的。

