
"""Lecture 02 exercises (classes) - implement from scratch.
Any 14 / 16 problems solved count as 100%
"""

"""
1) Create class User with:
    name,
    method say_hi() which prints "Hello, I am {name}"
"""

from typing import Callable, DefaultDict
import math


class User:
	def __init__(self, name: str) -> None:
		self.name = name

	def say_hi(self):
		return print(f"Hello, I am {self.name}")
		

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
	def __init__(self, owner: str, balance: float = 0.0) -> None:
		self.owner = owner
		self.balance = balance if balance >= 0.0 else 0.0

	def deposit(self, amount: float):
		if amount < 0:
			return
		self.balance += amount 
	
	def withdraw(self, amount: float):
		if amount < 0 or amount > self.balance:
			return
		self.balance -= amount



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
	def __init__(self) -> None:
		self.members = []

	def add(self, name: str):
		self.members.append(name)

	def __len__(self) -> int:
		return len(self.members)

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
	def __init__(self) -> None:
		self.items = []

	def push(self, item: str) -> None:
		self.items.append(item)
	
	def pop(self) -> str | None:
		if len(self.items) == 0:
			return
		return self.items.pop(0)


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
	def __init__(self, balance: float = 0.0) -> None:
		self.balance = balance if balance >= 0.0 else 0.0

	def top_up(self, amount: float) -> None:
		self.balance += amount 

	def pay(self, amount: float) -> None:
		if amount > self.balance:
			raise InsufficientFunds()
		self.balance -= amount 

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
	def __init__(self) -> None:
		self.items = {}

	def add_item(self, name: str, price: float, qty: int = 1) -> None:
		if price < 0 or qty <= 0:
			return
		self.items[name]=(price, qty)

	def total_items(self) -> int:
		return sum(value[1] for key, value in self.items.items())

	def total_price(self) -> float:
		total_sum = 0
		print("**")
		print(self.items)
		for k, v in self.items.items():
			total_sum += (v[0] * v[1])
		return total_sum

	def __repr__(self) -> str:
		return "ShoppingCart"

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

	def __init__(self, group_name: str) -> None:
		self.students = []
		self.group_name = group_name

	def add_student(self, name: str) -> None:
		self.students.append(name)

	def __len__(self):
		return len(self.students)

	def set_school_name(self, new_name: str) -> None:
		Classroom.school_name = new_name

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
	def __init__(self, width: float, height: float) -> None:
		self.width = abs(width)
		self.height = abs(height)


	def area(self) -> float:
		return self.width * self.height

	def perimeter(self) -> float:
		return 2* self.width + 2 * self.height

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
	def __init__(self) -> None:
		self.songs = []

	def add(self, song: str) -> None:
		self.songs.append(song)

	def __len__(self) -> int:
		return len(self.songs)

	def __iter__(self):
		return iter(self.songs)

	def __contains__(self, song: str):
		return song in self.songs


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
	def __init__(self, name: str, price: float) -> None:
		self.name = name 
		self.price = price if price >= 0.0 else 0.0

	def get_price(self) -> float:
		return self.price

	def set_price(self, value: float):
		if value < 0.0:
			self.price = 0.0 
			return
		self.price = value

	def apply_discount(self, percent: float):
		self.price -= (self.price * percent / 100 )
		if self.price < 0.0:
			self.price = 0.0

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
	def __init__(self, name: str) -> None:
		self.name = name

	def describe(self):
		return f"Person(name={self.name})"

class Student(Person):
	def __init__(self, name: str, group: str) -> None:
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
	def __init__(self, x: float, y: float) -> None:
		self.x = x 
		self.y = y 
	
	def distance_to(self, other: "Point2D") -> float:
		return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
	
	def __eq__(self, value: object) -> bool:
		return isinstance(value, Point2D) and self.x == value.x and self.y == value.y

	def __repr__(self) -> str:
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
	def __init__(self) -> None:
		self.items = {}
	
	def add(self, name: str, qty: int =1):
		if qty < 0:
			return
		if name not in self.items:
			self.items[name] = qty
		else:
			self.items[name] += qty

	def remove(self, name: str, qty: int = 1) -> None:
		if qty < 0 or name not in self.items:
			return
		self.items[name] -= qty
		if self.items[name] == 0:
			del self.items[name]

	def count(self, name: str) -> int: 
		if name not in self.items:
			return 0
		return self.items[name]

	def __contains__(self, name: str):
		return name in self.items

	def __len__(self):
		return len(self.items)

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
	def __init__(self) -> None:
		self.courses = {}
		
	def add_course(self, code: str, title: str) -> None:
		self.courses[code] = title

	def get_title(self, code: str):
		return self.courses[code]

	def __iter__(self):
		keys = list(self.courses.keys())
		keys.sort()
		for k in keys:
			yield (k, self.courses[k])

	def __len__(self) -> int:
		return len(self.courses)

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
	def __init__(self, default_factory=None) -> None:
		self.dict = {}
		self.default_factory = default_factory if callable(default_factory) else None

	def __getitem__(self, key):
		if key not in self.dict:
			if self.default_factory:
				self.dict[key] = self.default_factory()
				return self.dict[key]
			else:
				return None 
		
		return self.dict[key]

	def __setitem__(self, key, value) -> None:
		self.dict[key] = value 

	def __contains__(self, key) -> bool :
		return key in self.dict

	def __len__(self):
		return len(self.dict)