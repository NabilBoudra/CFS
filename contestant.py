class contestant : 
    def __init__(self,handle,speed): 
        self.speed = speed
        self.handle = handle 
    def valid(self) : 
        maxRating=len(self.speed)-1
        answer = 0 
        for rating in range(0,maxRating+1) : 
            if self.speed[rating] != -1 : 
                answer += 1 
        if 0 == maxRating :
            return 1 
        else : 
            newSpeed = self.speed
            for rating in range(0,maxRating+1) : 
                if self.speed[rating] != -1  : 
                    nextRating =  -1 
                    for nxtRating in range(rating+1,maxRating+1) : 
                        if self.speed[nxtRating] != -1 : 
                            nextRating = nxtRating 
                            break 
                    if nextRating == -1  : 
                        break 
                    slope = (self.speed[rating]-self.speed[nextRating])/(rating-nextRating)
                    const = self.speed[rating]-rating*slope
                    for uRating in range(rating+1,nextRating) : 
                        newSpeed[uRating] = const+slope*uRating
                    break 
            
            if self.speed[0] == -1  : 
                smallestRating=secondSmallestRating=-1 
                for rating in range(0,maxRating+1) : 
                    if self.speed[rating] != -1 :
                        if smallestRating == -1  : 
                            smallestRating = rating 
                        else :
                            secondSmallestRating = rating 
                            break 
                slope = (self.speed[smallestRating]-self.speed[secondSmallestRating])/(smallestRating-secondSmallestRating)
                const = self.speed[smallestRating]-smallestRating*slope
                for rating in range(0,maxRating+1): 
                    if self.speed[rating] == -1 : 
                        newSpeed[rating] = slope*rating+const 
                    else: 
                        break
            if self.speed[maxRating] == -1 : 
                highestRating=secondHighestRating=-1
                for rating in range(maxRating,0-1,-1): 
                    if self.speed[rating] != -1 : 
                        if highestRating == -1 : 
                            highestRating = rating
                        else : 
                            secondHighestRating = rating 
                            break 
                slope = (self.speed[highestRating]-self.speed[secondHighestRating])/(highestRating-secondHighestRating)
                const = self.speed[highestRating]-highestRating*slope
                for rating in range(maxRating,0-1,-1): 
                    if self.speed[rating] == -1 : 
                        newSpeed[rating] = slope*rating+const
                    else : 
                        break 
            self.speed = newSpeed
            return 1 
        return 0 
    def compare(contestant1,contestant2,method="sum"):   
        maxRating=len(contestant1.speed)-1
        answer=0
        for rating in range(0,maxRating+1): 
            if method == "sum" : 
                answer += abs(contestant1.speed[rating]-contestant2.speed[rating])
            else : 
                answer = max(answer,abs(contestant1.speed[rating]-contestant2.speed[rating]))
        return answer 
    