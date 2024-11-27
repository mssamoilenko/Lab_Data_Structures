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
