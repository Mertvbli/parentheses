class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        """Метод проверяет стек на пустоту. Метод возвращает True или False."""
        if len(self.stack) == 0:
            print(True)
        else:
            print(False)

    def push(self, value):
        """Метод добавляет новый элемент на вершину стека."""
        self.stack.append(value)

    def pop(self):
        """Метод удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека."""
        self.stack.pop()
        return self.stack.pop()

    def peek(self):
        """Метод возвращает верхний элемент стека, но не удаляет его. Стек не меняется."""
        return self.stack[-1]

    def size(self):
        """Метод возвращает количество элементов в стеке."""
        return len(self.stack)


st = input("Введите строку: ")
s = Stack()
s.push(st)
b = len(st)
x = 0
if len(st) % 2 == 0:
    for idx, i in enumerate(st):
        if i == '(' and st[x - 1] == ')' or i == '[' and st[x - 1] == ']' or i == '{' and st[x - 1] == '}':
            x -= 1
        elif b // 2 == abs(x):
            print('Сбалансированно')
            break
    else:
        print("Несбалансированно")
else:
    print("Нечётное количество скобок!")
