class Parent:
	def my(self):
		print('调用父类方法')


class Child(Parent):
    def my(self):
        print('调用子类方法')

c = Child()
c.my()

class Counter:
    _seCount = 0
    puCount = 0

    def count(self):
        self._seCount += 1
        self.puCount += 1
        print(self._seCount)

co = Counter()
for i in range(7):
    co.count()
print("se:" + str(co._seCount))
print("pu:" + co.puCount)
