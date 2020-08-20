import random
class Node:
    def __init__(self, color, num, next=None):
        self.color = color
        self.num = num
        self.next = next
    
    def get_color(self):
        return self.color
    
    def get_num(self):
        return self.num
    
    def set_color(self, year):
        self.color = color
    
    def set_num(self, highlight):
        self.num = num

class Stack:
    def __init__(self, limit):
        self.top = None
        self.length = 0
        self.limit = limit

    def is_empty(self):
        return self.length == 0
    
    def is_full(self):
        return self.length == self.limit
    
    def push(self, color, num):
        # Condition is_full
        if self.is_full():
            print ("Sorry I'm full") 
        else:
            self.top = Node(color, num, self.top)
            self.length += 1

    def pop(self):
        #condition is_empty
        if self.is_empty():
            print ("Sorry I reached my limits")
        else:
            poped_node = self.top
            self.top = poped_node.next
            self.length -= 1
            return poped_node.get_color(), poped_node.get_num()



def print_cards(player):
    
    print("--"*10)
    print("player %d" % player)
    print("--"*10)

    for i in range(1, 6):
        card = deck.pop()
        print (f" {i}.  {card[0]}-{card[1]} ")


deck = Stack(20)

colors = ["red", "blue", "green", "yellow"]

for i in range(20):
    deck.push(random.choice(colors), random.randint(1, 9))

print_cards(1)
print_cards(2)

print("\n\n")
print("--"*10)
print(f"Top card: {deck.top.color}-{deck.top.num}")
print("--"*10)





    


