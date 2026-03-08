from typing import Iterable,Any
class InsertItem:

    def __init__(self,iterable: Iterable[Any]):
        self.iterable = list(iterable)


    def delete(self,index_to_delete:int) -> list[Any]:
        for i in range(index_to_delete,len(self.iterable)-1):
            self.iterable[i]=self.iterable[i+1]
        self.iterable.pop()

        return self.iterable

test=InsertItem([10,20,30,40,50])
result=test.delete(2)
print(result)


