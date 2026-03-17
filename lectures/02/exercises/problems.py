
"""Lecture 02 exercises (classes) - implement from scratch.
Any 14 / 16 problems solved count as 100%
"""

"""
1) Create class User with:
    name,
    method say_hi() which prints "Hello, I am {name}"
"""
class User:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f"Hello, I am {self.name}")

"""
2) BankAccount
Create class `BankAccount` with:
- `__init__(self, owner: str, balance: float = 0.0) -> None`
- `deposit(self, amount: float) -> None`
- `withdraw(self, amount: float) -> None`
Rules:
- Initial negative balance becomes `0.0`.
- Non-positive `deposit`/`withdraw` amounts are ignored.
- `withdraw` bigger than current balance is ignored.
"""
class BankAccount:
    def __init__(self, owner: str, balance:float=0.0):
        self.owner=owner
        if balance<0:
            self.balance=0.0
        else:
            self.balance=balance

    def deposit(self, amount:float):
        if amount>0:
            self.balance= self.balance+amount

    def withdraw(self, amount: float):
        if amount > 0:
            if amount <= self.balance:
                self.balance = self.balance- amount

"""
3) Team
Create class `Team` with:
- `__init__(self) -> None`
- `add(self, name: str) -> None`
- `__len__(self) -> int`
Rules:
- Members are stored in insertion order.
- Each instance has independent member storage.
"""
class Team:
  def __init__(self):
    self.members=[]
  def add(self,name:str):
    self.members.append(name)
  def __len__(self):
    c=0
    for i in self.members:
      c+=1
    return c


""" (Advanced, optional)
5) QueueState
Create class `QueueState`:
- `__init__(self) -> None` (initialize empty `items` list)
Methods:
- `push(self, item: str) -> None`
- `pop(self) -> str | None`
Rules:
- FIFO behavior.
- `pop` returns `None` when empty.
"""
class QueueState:
  def __init__(self):
    self.items=[]
  def push(self,item=str):
    self.items.append(item)
  def pop(self):
    if len(self.items)==0:
      return None
    a=self.items[0]
    self.items =self.items[1:]
    return a
    

""" (Advanced, optional)
6) Wallet + custom errors
Create:
- `class PaymentError(Exception): ...`
- `class InsufficientFunds(PaymentError): ...`
- `class Wallet` with:
  - `__init__(self, balance: float = 0.0) -> None`
  - `top_up(self, amount: float) -> None`
  - `pay(self, amount: float) -> None`
Rules:
- Initial balance must be >= 0.
- `top_up` and `pay` require amount > 0.
- If `pay` exceeds balance, raise `InsufficientFunds`.
"""
class PaymentError(Exception):
  pass
class InsufficientFunds(PaymentError):
  pass
class Wallet:
  def __init__(self, balance: float = 0.0):
    if balance<0:
      balance=0.0
    else:
      self.balance=balance
  def top_up(self, amount: float):
    if amount>0:
      self.balance=self.balance+amount
  def pay(self, amount: float):
    if amount<=0:
      return
    if amount>self.balance:
      raise InsufficientFunds()
    self.balance=self.balance-amount

"""
7) ShoppingCart
Create class `ShoppingCart` with:
- `__init__(self) -> None`
- `add_item(self, name: str, price: float, qty: int = 1) -> None`
- `total_items(self) -> int`
- `total_price(self) -> float`
Rules:
- `price < 0` or `qty <= 0` items are ignored.
- `repr` must include `ShoppingCart`.
"""
class ShoppingCart:
  def __init__(self):
    self.items=[]
  def add_item(self, name: str, price: float, qty: int = 1):
    if price >= 0 and qty > 0:
      item = {"name": name, "price": price, "qty": qty}
      self.items.append(item)
  def total_items(self):
    a=0
    for i in self.items:
      a=a+i["qty"]
    return a
  def total_price(self):
    b=0.0
    for j in self.items:
      b=b+(j["price"]*j["qty"])
    return b
  def __repr__(self):
    return f"ShoppingCart(items={len(self.items)})"

"""
8) Classroom (class attribute)
Create class `Classroom` with class attribute:
- `school_name = "Harbour Space"`
Methods:
- `__init__(self, group_name: str) -> None`
- `add_student(self, name: str) -> None`
- `__len__(self) -> int`
- `set_school_name(self, new_name: str) -> None`
Rules:
- `set_school_name` must update shared class attribute for all instances.
"""
class Classroom:
  school_name = "Harbour Space"
  def __init__(self,group_name:str):
    self.group_name=group_name
    self.students=[]
  def add_student(self,name:str):
    self.students.append(name)
  def __len__(self):
    a=0
    for i in self.students:
      a=a+1
    return a
  def set_school_name(self, new_name: str):
    Classroom.school_name=new_name

"""
9) Rectangle
Create class `Rectangle` with:
- `__init__(self, width: float, height: float) -> None`
- `area(self) -> float`
- `perimeter(self) -> float`
Rules:
- Store positive dimensions using absolute values.
"""
class Rectangle:
  def __init__(self, width: float, height: float):
    if width < 0:
      self.width = -width
    else:
      self.width = width   
    if height < 0:
      self.height = -height
    else:
      self.height = height
  def area(self):
    a=self.width*self.height
    return a
  def perimeter(self):
    b=2*(self.width+self.height)
    return b

"""
10) Playlist
Create class `Playlist` with:
- `__init__(self) -> None`
- `add(self, song: str) -> None`
- `__len__(self) -> int`
- `__iter__(self)`
- `__contains__(self, song: str) -> bool`
Rules:
- Preserve insertion order.
"""
class Playlist:
  def __init__(self):
    self.songs=[]
  def add(self, song: str):
    self.songs.append(song)
  def __len__(self):
    a=0
    for i in self.songs:
      a=a+1
    return a
  def __iter__(self):
    return iter(self.songs)
  def __contains__(self, song: str):
    for i in self.songs:
      if i == song:
        return True
    return False

"""
11) Product
Create class `Product` with:
- `__init__(self, name: str, price: float) -> None`
- `get_price(self) -> float`
- `set_price(self, value: float) -> None`
- `apply_discount(self, percent: float) -> None`
Rules:
- Negative price is clamped to `0`.
- Discount percent is clamped to `[0, 100]`.
"""
class Product:
  def __init__(self, name: str, price: float):
    self.name=name
    if price<0:
      self.price=0.0
    else:
      self.price=price
  def get_price(self):
    return self.price
  def set_price(self, value: float):
    if value<0:
      self.price=0.0
    else:
      self.price=value
  def apply_discount(self, percent: float):
    if percent<0:
      percent=0.0
    if percent>100:
      percent=100.0
    rr=self.price*(percent / 100)
    self.price=self.price-rr

"""
12) Person + Student (inheritance)
Create:
- `class Person` with `__init__(name)` and `describe()`
- `class Student(Person)` with `__init__(name, group)` and overridden `describe()`
Required format:
- `Person(name=Ana)`
- `Student(name=Bo, group=G2)`
"""
class Person:
    def __init__(self, name: str):
        self.name=name
    def describe(self):
        return f"Person(name={self.name})"

class Student(Person):
    def __init__(self, name: str, group: str):
        super().__init__(name)
        self.group = group

    def describe(self):
        return f"Student(name={self.name}, group={self.group})"
      
"""
13) Point2D (magic methods)
Create class `Point2D` with:
- `__init__(self, x: float, y: float) -> None`
- `distance_to(self, other: "Point2D") -> float`
- `__eq__(self, other: object) -> bool`
Rules:
- Euclidean distance.
- `repr` format: `Point2D(x, y)`.
"""
class Point2D:
    def __init__(self, x: float, y: float):
        self.x=x
        self.y= y

    def distance_to(self, other: "Point2D"):
        dx=self.x-other.x
        dy=self.y-other.y
        return (dx**2+dy**2)**0.5

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point2D):
            return False
        return self.x ==other.x and self.y==other.y

    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"

"""
14) Inventory
Create class `Inventory` with:
- `__init__(self) -> None`
- `add(self, name: str, qty: int = 1) -> None`
- `remove(self, name: str, qty: int = 1) -> None`
- `count(self, name: str) -> int`
- `__contains__(self, name: str) -> bool`
- `__len__(self) -> int`
Rules:
- Non-positive `qty` is ignored.
- Removing too much removes item completely (count becomes `0`).
"""
class Inventory:
  def __init__(self):
    self.stock={}
  def add(self, name: str, qty: int = 1):
    if qty>0:
      if name in self.stock:
        self.stock[name]=self.stock[name]+qty
      else:
        self.stock[name]=qty
  def remove(self, name: str, qty: int = 1):
    if qty > 0 and name in self.stock:
      current_qty = self.stock[name]
      if qty >= current_qty:
        del self.stock[name]
      else:
        self.stock[name] = current_qty - qty
  def count(self, name: str) -> int:
        if name in self.stock:
            return self.stock[name]
        return 0
  def __contains__(self, name: str):
        return name in self.stock
  def __len__(self):
        a = 0
        for name in self.stock:
            a = a + self.stock[name]
        return a
      

"""
15) CourseCatalog
Create class `CourseCatalog` with:
- `__init__(self) -> None`
- `add_course(self, code: str, title: str) -> None`
- `get_title(self, code: str) -> str | None`
- `__iter__(self)` returning `(code, title)` sorted by code
- `__len__(self) -> int`
"""
class CourseCatalog:
    def __init__(self):
        self.catalog = {}
    def add_course(self, code: str, title: str):
        self.catalog[code] = title
    def get_title(self, code: str):
        if code in self.catalog:
            return self.catalog[code]
        return None
    def __iter__(self):
        codes = list(self.catalog.keys())
        sorted_codes = sorted(codes)
        pairs = []
        for code in sorted_codes:
            title = self.catalog[code]
            pairs.append((code, title))  
        return iter(pairs)
    def __len__(self):
        a = 0
        for i in self.catalog:
            a = a + 1
        return a

"""
16) DefaultDict (magic methods)
Create class `DefaultDict` with:
- `__init__(self, default_factory=None) -> None`
- `__getitem__(self, key)`
- `__setitem__(self, key, value) -> None`
- `__contains__(self, key) -> bool`
- `__len__(self) -> int`
Rules:
- On missing key:
  - if `default_factory` is `None`, return `None`.
  - otherwise create value using `default_factory()`, store, return.
- If `default_factory` is not callable, treat it as `None`.
"""
class DefaultDict:
    def __init__(self, default_factory=None) :
        self.data = {}
        if callable(default_factory):
            self.default_factory = default_factory
        else:
            self.default_factory = None

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        
        if self.default_factory is None:
            return None
        
        new_value = self.default_factory()
        self.data[key] = new_value
        return new_value

    def __setitem__(self, key, value):
        self.data[key] = value

    def __contains__(self, key):
        return key in self.data

    def __len__(self):
        a = 0
        for i in self.data:
            a = a + 1
        return a