#task1
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next

    def contains(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def replace(self, old_value, new_value):
        current = self.head
        while current:
            if current.value == old_value:
                current.value = new_value
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

linked_list = LinkedList()
while True:
    print("\n1. Додати елемент у список\n2. Видалити елемент зі списку\n3. Показати вміст списку\n4. Перевірити, чи є значення у списку\n5. Замінити значення у списку\n6. Вийти")
    choice = int(input("Ваш вибір: "))
    if choice == 1:
        value = int(input("Введіть значення: "))
        linked_list.add(value)
    elif choice == 2:
        value = int(input("Введіть значення: "))
        linked_list.remove(value)
    elif choice == 3:
        linked_list.display()
    elif choice == 4:
        value = int(input("Введіть значення: "))
        print("Знайдено" if linked_list.contains(value) else "Не знайдено")
    elif choice == 5:
        old_value = int(input("Старе значення: "))
        new_value = int(input("Нове значення: "))
        linked_list.replace(old_value, new_value)
    elif choice == 6:
        break

#task2
class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = DoublyNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def remove(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current = self.head
        while current and current.value != value:
            current = current.next
        if current:
            if current.next:
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next

    def contains(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def replace(self, old_value, new_value):
        current = self.head
        while current:
            if current.value == old_value:
                current.value = new_value
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

dll = DoublyLinkedList()
while True:
    print("\n1. Додати елемент у список\n2. Видалити елемент зі списку\n3. Показати елементи списку\n4. Перевірити чи є значення в списку\n5. Замінити значення в списку\n6. Вийти")
    choice = int(input("Ваш вибір: "))
    if choice == 1:
        value = input("Введіть значення: ")
        dll.add(value)
    elif choice == 2:
        value = input("Введіть значення: ")
        dll.remove(value)
    elif choice == 3:
        dll.display()
    elif choice == 4:
        value = input("Введіть значення: ")
        print("Знайдено" if dll.contains(value) else "Не знайдено")
    elif choice == 5:
        old_value = input("Старе значення: ")
        new_value = input("Нове значення: ")
        dll.replace(old_value, new_value)
    elif choice == 6:
        break

#task3
class FixedStack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, value):
        if len(self.stack) < self.size:
            self.stack.append(value)
        else:
            print("Стек переповнений!")

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Стек порожній!")
            return None

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack = []

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            print("Стек порожній!")
            return None

stack = FixedStack(5)
while True:
    print("\n1. Помістити елемент у стек\n2. Виштовхнути елемент зі стеку\n3. Показати кількість елементів\n4. Перевірити чи порожній стек\n5. Очистити стек\n6. Показати верхній елемент\n7. Вийти")
    choice = int(input("Ваш вибір: "))
    if choice == 1:
        value = int(input("Введіть значення: "))
        stack.push(value)
    elif choice == 2:
        print("Видалено:", stack.pop())
    elif choice == 3:
        print("Кількість елементів:", stack.count())
    elif choice == 4:
        print("Стек порожній" if stack.is_empty() else "Стек не порожній")
    elif choice == 5:
        stack.clear()
        print("Стек очищено!")
    elif choice == 6:
        print("Верхній елемент:", stack.peek())
    elif choice == 7:
        break

#task4
class DynamicStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Стек порожній!")
            return None

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack = []

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            print("Стек порожній!")
            return None

#HW_Data_Structures
def display_menu():
    print("\nМеню:")
    print("1. Додати нове число в список")
    print("2. Видалити всі входження числа зі списку")
    print("3. Показати вміст списку")
    print("4. Перевірити чи є значення в списку")
    print("5. Замінити значення у списку")
    print("6. Вийти")

numbers = list(map(int, input("Введіть набір чисел через пробіл: ").split()))

while True:
    display_menu()
    choice = int(input("Ваш вибір: "))

    if choice == 1:
        number = int(input("Введіть число: "))
        if number in numbers:
            print("Число вже є у списку!")
        else:
            numbers.append(number)
            print("Число додано.")

    elif choice == 2:
        number = int(input("Введіть число для видалення: "))
        numbers = [n for n in numbers if n != number]
        print("Число видалено, якщо воно було у списку.")

    elif choice == 3:
        order = input("Показати список (з початку/з кінця)? (початок/кінець): ").strip().lower()
        if order == "початок":
            print("Список:", numbers)
        elif order == "кінець":
            print("Список (з кінця):", numbers[::-1])
        else:
            print("Неправильний вибір!")

    elif choice == 4:
        number = int(input("Введіть число для перевірки: "))
        if number in numbers:
            print("Число є у списку.")
        else:
            print("Числа немає у списку.")

    elif choice == 5:
        old_value = int(input("Введіть значення для заміни: "))
        new_value = int(input("Введіть нове значення: "))
        replace_all = input("Замінити всі входження? (так/ні): ").strip().lower()
        if replace_all == "так":
            numbers = [new_value if n == old_value else n for n in numbers]
        elif replace_all == "ні":
            for i in range(len(numbers)):
                if numbers[i] == old_value:
                    numbers[i] = new_value
                    break
        else:
            print("Неправильний вибір!")

    elif choice == 6:
        print("Програма завершена.")
        break

    else:
        print("Неправильний вибір! Спробуйте знову.")
