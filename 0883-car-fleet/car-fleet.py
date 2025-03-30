class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carList = []

        for index in range(len(position)):
            carList.append((position[index], speed[index]))
        
        carList.sort()
        arrivals = []

        for p,s in carList:
            arrivals.append((target-p)/s)

        numFleets = 0
        for index in range(len(arrivals)-1):
            top = arrivals.pop()

            if arrivals[-1] <= top:
                arrivals[-1] = top
            else:
                numFleets += 1

        return numFleets + bool(arrivals)
            
            

        


        