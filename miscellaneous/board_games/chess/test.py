class DummyA:
    pass
class DummyB:
    pass
class DummyC:
    pass
class DummyD:
    pass

exA = DummyA()
exB = DummyB()
exC = DummyC()
exD = DummyD()

type_list = []
type_list.append(type(exA))
type_list.append(type(exB))
type_list.append(type(exD))

print(DummyC in type_list)