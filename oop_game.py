import keyboard
import random
import time

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
    print(keys)

    counter = 0
    print("Используйте предметы на соответствующие клавиши:\n(1)Меч(бейй)\n(2)Зелье здоровья восстанавливает),\n(3)Cтена: можно поставить в радиусе 1 клетки,\n(4)Ловушка: можно поставить в радиусе 1 клетки")
    print(f"Здоровье равно {knight.health}")
    for i in arena:
        if counter != len(inventary):
            inv.update_inventory()
            print(f"{" ".join(i)} {keys[counter]}: {inv.inventary[keys[counter]]}")
            counter+=1
        else:
            print(" ".join(i))

"""for i in arena1:
    for j in i:
        arena_unpacked.append(j)"""
arena_unpacked = [j for i in arena for j in i]

class hero():
    def __init__(self,x=5,y=-1,hp=0):
        self.__x = x
        self.__y = y
        self.__hp = 4
    
    @property
    def cords(self):
        return self.__x, self.__y
    
    @property
    def health(self):
        return self.__hp
    
    @health.setter
    def health(self,damage):
        self.__hp+=damage

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
            while True:
                if keyboard.is_pressed("w"):
                    knight.move_to("w")
                    time.sleep(0.3)  # Добавляем паузу, чтобы предотвратить слишком частые срабатывания
                elif keyboard.is_pressed("s"):
                    knight.move_to("s")
                    time.sleep(0.3)
                elif keyboard.is_pressed("a"):
                    knight.move_to("a")
                    time.sleep(0.3)
                elif keyboard.is_pressed("d"):
                    knight.move_to("d")
                    time.sleep(0.3)
                elif keyboard.is_pressed("1"):
                    inv.use_item_2("м")
                    time.sleep(0.3)
                elif keyboard.is_pressed("2"):
                    inv.use_item_2("essence")
                    time.sleep(0.3)
                elif keyboard.is_pressed("3"):
                    inv.use_item_2("wall")
                    time.sleep(0.3)
                elif keyboard.is_pressed("4"):
                    inv.use_item_2("catcher")
                    time.sleep(0.3)

            
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
    
    def update_inventory(self):
        self.inventary = {"Меч":f"{self.items["sword"]}", "Зелье здоровья": f"{self.items["essence"]}", "Стена": f"{self.items["wall"]}", "Ловушка": f"{self.items["catcher"]}"}


    def set_item(self,item_name):
        self.items[item_name]+=1
        self.update_inventory()

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

    def return_direction(self):
        print("НАЖМИ НАПРАВЛЕНИЕ УЖЕ 3 НОЧИ W A S D")
        while True:
            if keyboard.is_pressed("d"):
                cord = "d"
                break
            elif keyboard.is_pressed("a"):
                cord = "a"
                break
            elif keyboard.is_pressed("s"):
                cord = "s"
                break
            elif keyboard.is_pressed("w"):
                cord = "w"
                break
        return cord
        
    
        
    def use_item_2(self,item):
        if item =="м" and self.items["sword"]!=0:
            self.sword_attack(knight.cords)
        elif (item =="catcher" and self.items["catcher"]>0) or (item =="wall" and self.items["wall"]):
            self.items[item]-=1
            self.update_inventory()
            self.place_item(knight.cords,item)
        elif item == "essence" and self.items["essence"]>0:
            self.items[item]-=1
            self.update_inventory()
            self.heal()
        else:
            print("Не хватает предмета")

        #для меча отдельно прописать атаку в 3 клетки вперед
        pass
    def place_item(self,cords,item):#для стены  ловушек, ловушки можно подбирать
        x,y = cords
        cords_around = {"d":[y,x+1],"a":[y,x-1],"w":[y-1,x],"s":[y+1,x]}
        if item == "wall":
            item = "#"
            direction = self.return_direction()#возвращает w a s d
            arena[cords_around[direction][0]][cords_around[direction][1]]=item
            print_arena()
        elif item == "catcher":
            item = "Л"
            direction = self.return_direction()#возвращает w a s d
            arena[cords_around[direction][0]][cords_around[direction][1]]=item
            print_arena()
            
            
    def sword_attack(self,cords):
        x,y = cords
        cord = self.return_direction() # 
        #cords_around = {"d":[[y+i],[x+1]], "a":[[y-i],[x-1]], "s":[[y+1],[x+i]], "w":[[y-1],[x+i]]} не вышло

        if cord == "d":
            for i in range(-1,2):
                arena[y+i][x+1]+="$"#наверное это как-то потом оптимизирую, потому что щас 3 ночи ага
            print_arena()
            for i in range(-1,2):
                arena[y+i][x+1]=arena[y+i][x+1][:-1]
        elif cord == "a":
            for i in range(-1,2):
                arena[y-i][x-1]+="$"#наверное это как-то потом оптимизирую, потому что щас 3 ночи ага
            print_arena()
            for i in range(-1,2):
                arena[y-i][x-1]=arena[y-i][x-1][:-1]
        elif cord == "s":
            for i in range(-1,2):
                arena[y+1][x+i]+="$"#наверное это как-то потом оптимизирую, потому что щас 3 ночи ага
            print_arena()
            for i in range(-1,2):
                arena[y+1][x+i]=arena[y+1][x+i][:-1]
        elif cord == "w":
            for i in range(-1,2):
                arena[y-1][x-i]+="$"#наверное это как-то потом оптимизирую, потому что щас 3 ночи ага (сделать список позиций((1.1),(1.-1)))
            print_arena()
            for i in range(-1,2):
                arena[y-1][x-i]=arena[y-1][x-i][:-1]    

        
        pass
    
    def heal(self):
        knight.health=1
        print_arena()
        pass

knight = hero()
inv = inventory()

#test
inventary = inv.inventary#лень название думать, пусть будет через а
knight.pick_up_item(1,2)
#test

inv.show_arena_items()
knight.move_hero()


print(knight.cords, "\n")

#knight.cords = (2,2)





