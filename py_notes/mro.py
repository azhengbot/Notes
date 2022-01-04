"""
1. 检查第一个列表的头元素（如 L[B1] 的头），记作 H。
2. 若 H 未出现在其它列表的尾部，则将其输出，并将其从所有列表中删除，然后回到步骤1；否则，取出下一个列表的头部记作 H，继续该步骤。
3. 重复上述步骤，直至列表为空或者不能再找出可以输出的元素。如果是前一种情况，则算法结束；如果是后一种情况，说明无法构建继承关系，Python 会抛出异常。
"""

# class F:
#     pass


# class E:
#     pass


# class D:
#     pass


# class B(D, E):
#     pass


# class C(D, F):
#     pass


# class A(B, C):
#     pass


# print(A.__mro__)

# L[object] = [object]
# L[D] = [D, object]
# L[E] = [E, object]
# L[F] = [F, object]
# L[B] = [B, D, E, object]
# L[C] = [C, D, F, object]
# L[A] = [A] + merge(L[B], L[C], [B], [C])
#      = [A] + merge([B, D, E, object], [C, D, F, object], [B], [C])
#      = [A, B] + merge([D, E, object], [C, D, F, object], [C])
#      = [A, B, C] + merge([D, E, object], [D, F, object])
#      = [A, B, C, D] + merge([E, object], [F, object])
#      = [A, B, C, D, E] + merge([object], [F, object])
#      = [A, B, C, D, E, F] + merge([object], [object])
#      = [A, B, C, D, E, F, object]

# (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.F'>, <class 'object'>)

################################################################
# class G:
#     ...


# class F:
#     pass


# class E:
#     pass


# class D:
#     pass


# class B(D, E):
#     pass


# class C(G, F):
#     pass


# class A(B, C):
#     pass


# print(A.__mro__)

# L[object] = [object]
# L[D] = [D, object]
# L[E] = [E, object]
# L[F] = [F, object]
# L[G] = [G, object]
# L[B] = [B, D, E, object]
# L[C] = [C, G, F, object]
# L[A] = [A] + merge(L[B], L[C], [B], [C])
#      = [A] + merge([B, D, E, object], [C, G, F, object], [B], [C])
#      = [A, B] + merge([D, E, object], [C, G, F, object], [C])
#      = [A, B, D] + merge([E, object], [C, G, F, object], [C])
#      = [A, B, D, E] + merge([object], [C, G, F, object], [C])
#      = [A, B, D, E, C] + merge([object], [G, F, object])
#      = [A, B, D, E, C, G] + merge([object], [F, object])
#      = [A, B, D, E, C, G, F] + merge([object], [object])
#      = [A, B, D, E, C, G, F, object]
# (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.C'>, <class '__main__.G'>, <class '__main__.F'>, <class 'object'>)


###################################################


class Z:
    ...


class X(Z):
    ...


class A(X):
    ...


class B:
    ...


class Y:
    ...


class M(B, A, Y):
    ...


print(M.__mro__)
