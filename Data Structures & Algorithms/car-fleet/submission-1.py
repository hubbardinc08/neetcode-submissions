class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        data = []
        for i in range(len(position)):
            data.append([position[i], speed[i]])
        
        data.sort(key=lambda x: x[0], reverse=True)
    
        for car in data:
            if (len(fleets) == 0):
                fleets.append(car)
            else:
                if ((target - car[0]) / car[1] > (target - fleets[-1][0]) / fleets[-1][1]):
                    fleets.append(car)
        
        return len(fleets)

