import keyboard
import random

arena = [
    ["|", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "|"],#-13
    ["|", " ", " ", " ", " ", " ", "#", "#", " ", " ", " ", "|"],#-12
    ["|", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", "|"],#-11
    ["|", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", "|"],#-10
    ["|", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", "|"],#-9
    ["|", " ", " ", " ", "#", "#", " ", "#", "#", " ", " ", "|"],#-8
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],#-7
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],#-6
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],#-5
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],#-4
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],#-3
    ["|", " ", " ", " ", "|", " ", "|", " ", " ", " ", " ", "|"],#-2
    ["|", "_", "_", "_", "|", "H", "|", "_", "_", "_", "_", "|"] #-1
]

def print_arena():
    keys = [key for key in inventary]
    
    counter = 0
    for i in arena:
        
        if counter != len(inventary):
            print(f"{" ".join(i)} {counter}: {inventary[keys[counter]]}")
            counter+=1
        else:
            print(" ".join(i))

"""for i in arena1:
    for j in i:
        arena_unpacked.append(j)"""
arena_unpacked = [j for i in arena for j in i]

class hero():
    def __init__(self,x=5,y=-1):
        self.__x = x
        self.__y = y
    
    @property
    def cords(self):
        return self.__x, self.__y
    
    @cords.setter #проверить не сначала
    def cords(self,cords):
        self.__x,self.__y =cords
   
    def move_to(self,direction):
        x,y = self.cords
        possible_moves = [" ", "s", "с", "л", "з"]
        if direction == "w" and arena[y-1][x] in possible_moves:
            self.pick_up_item(y-1,x)
            self.__y -=1
        elif direction == "s" and arena[y+1][x] in possible_moves:
            self.pick_up_item(y+1,x)
            self.__y +=1
        elif direction =="a" and arena[y][x-1] in possible_moves:
            self.pick_up_item(y,x-1)
            self.__x -=1       
        elif direction =="d" and arena[y][x+1] in possible_moves:
            self.pick_up_item(y,x+1)
            self.__x+=1
        print(self.cords)
        arena[y][x] = "z"
        arena[self.__y][self.__x] = "H"
        print_arena()
        

    """def move_left(self):
        x,y = self.cords
        if arena[y][x-1]== " ":
            self.__x -=1       
            print(self.cords)
            arena[self.__y][self.__x] = "H"
            arena[y][x] = "z"
            print_arena()
    
    def move_right(self):
        x,y = self.cords
        if arena[y][x+1]== " ":
            self.__x +=1       
            print(self.cords)
            arena[self.__y][self.__x] = "H"
            arena[y][x] = "z"
            print_arena()
    
    def move_up(self):
        x,y = self.cords
        if arena[y-1][x]== " ":

            self.__y -=1
            print(self.cords)
            arena[self.__y][self.__x] = "H"
            arena[y][x] = "z"
            print_arena()
    def move_down(self):
        x,y = self.cords
        if arena[y+1][x]== " ":
            self.__y +=1      
            print(self.cords)
            arena[self.__y][self.__x] = "H"
            arena[y][x] = "z"
            print_arena()
    прототипы функций"""
    
    def move_hero(self):
        try:
            print_arena()
            keyboard.add_hotkey("w", lambda: self.move_to("w"))
            keyboard.add_hotkey("s", lambda: self.move_to("s"))
            keyboard.add_hotkey("a", lambda:self.move_to("a"))
            keyboard.add_hotkey("d", lambda:self.move_to("d"))
            keyboard.wait()
        except IndexError:
            print("НЕВОЗМОЖНО ДВИГАТЬСЯ")#по сути не работает т.к. arena[y][x+1]== " " не даёт уйти за пределы 

    def pick_up_item(self,new_y, new_x):
        inventory_norm = {"з":"essence","л":"catcher","с":"wall","s":"sword"}
        unpacked = [i for i in inventory_norm]
        #print(unpacked)
        item_name="---"
        if arena[new_y][new_x] in unpacked:
            item_name=inventory_norm[arena[new_y][new_x]] 
            print(item_name)
            inv.set_item(item_name)
        print(inv.inventary)
        #print(inv.essence, "sdasdad")
        



class inventory(): #меч(1) зелье здоровья(3)(з) ловушка(3)(л) стена(5)(с)
    
    def __init__(self):
        self.items = {
            "sword": False,
            "essence": 0,
            "wall": 0,
            "catcher": 0
        }

        self.inventary = {"Меч":f"{self.items["sword"]}", "Зелье здоровья": f"{self.items["essence"]}", "Стена": f"{self.items["wall"]}", "Ловушка": f"{self.items["catcher"]}"}
    
    def set_item(self,item_name):
        self.items[item_name]+=1
        self.inventary = {"Меч":f"{self.items["sword"]}", "Зелье здоровья": f"{self.items["essence"]}", "Стена": f"{self.items["wall"]}", "Ловушка": f"{self.items["catcher"]}"}

        #каждый раз обновляется, чтобы был актуальный список

    def create_item(self, item ,count):
        for i in range(count):
            while True:
                obj_x = random.randint(0,11)
                obj_y = random.randint(0,len(arena)-1)
                if arena[obj_y][obj_x] == " ": 
                    arena[obj_y][obj_x] = f"{item}"
                    break
        

    def show_arena_items(self):
        arena[-2][5] = 's'
        self.create_item("л",3)
        self.create_item("з",3)
        self.create_item("с", 5)

        
    def use_item(self):
        pass



knight = hero()
inv = inventory()

#test
inventary = inv.inventary
knight.pick_up_item(1,2)
#test

inv.show_arena_items()
knight.move_hero()

print(knight.cords, "\n")

#knight.cords = (2,2)





