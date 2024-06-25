# import json
# json_file = 'models.json'
# with open(json_file, 'r') as f:
#     data = json.load(f)

class World:
    

    def select_tail(self,map,x,y):
        x -= 1
        y -= 1

        if x % 5 == 0:
            x = x//5
        else:
            x = x//5 + 1

        if y % 5 == 0:
            y = y//5
        else:
            y = y//5 + 1

        if y < 0 or y >= len(map) or x < 0 or x >= len(map[0]):
            return None








