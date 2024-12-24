import keyboard

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
    for i in arena:
        print(" ".join(i), "\n")


"""for i in arena1:
    for j in i:
        arena_unpacked.append(j)"""
arena_unpacked = [j for i in arena for j in i]

#print(arena_unpacked)
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
        if direction == "w" and arena[y-1][x]== " ":
            self.__y -=1
        elif direction == "s" and arena[y+1][x]== " ":
            self.__y +=1
        elif direction =="a" and arena[y][x-1]== " ":
            self.__x -=1       
        elif direction =="d" and arena[y][x+1]== " ":
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
            


             
        



knight = hero()


print(knight.cords, "\n")

#knight.cords = (2,2)

knight.move_hero()




