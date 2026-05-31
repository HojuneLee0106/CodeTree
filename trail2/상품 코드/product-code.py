product_name, product_code = input().split()
product_code = int(product_code)
class product:
    def __init__(self,name="codetree", code=50):
        self.name=name
        self.code=code
P1=product()
P2=product(product_name, product_code)
print("product",P1.code,"is",P1.name)
print("product",P2.code,"is",P2.name)
# Please write your code here.