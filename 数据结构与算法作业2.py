from collections.abc import Sequence
from typing import Any

from scipy.interpolate import insert


class Set:

    def __init__(self,iterable:Sequence[Any]):
        self.iterable = list(iterable)

    def insert_last(self,element:Any) -> bool:
        for index,item in enumerate(self.iterable):
            if item==element:
                return False
        self.iterable.append(element)
        return True

    def set_check(self,element:Any) -> bool:
       for index,item in enumerate(self.iterable):
           if item==element:
               return True
       return False

    def set_delete(self,element:Any) -> bool:
        for index,item in enumerate(self.iterable):
            if item==element:
                self.iterable.remove(element)
                return True
        return False

    def set_show(self) ->None:
        print(self.iterable)


New_set=Set(['saber','archer','berserker','assassin','rider','caster','lancer'])
New_set.set_check('saber')
New_set.set_delete('saber')
New_set.set_show()
New_set.insert_last('saber')
New_set.set_show()


class Binary:
    def __init__(self,iterable:Sequence[Any]):
        List=list(iterable)
        length=len(List)
        for i in range (length-1):
            if List[i]>List[i+1]:
                a=List[i+1]
                List[i+1]=List[i]
                List[i]=a
        self.list=List

    def __getitem__(self, index):
        return self.list[index]

    def insert(self,value):
        new_list=[]
        inserted=False
        for i in range(len(self.list)):
            if not inserted and value < self.list[i]:
                new_list.append(value)
                inserted=True
            new_list.append(self.list[i])
        if not inserted:
            new_list.append(value)

        self.list=new_list



thelist=Binary([1,2,8,4,5])
thelist.insert(6)
print(thelist.list)