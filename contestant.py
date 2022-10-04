def convertToPractical(rating) : 
    return rating//100-8
def convertToActual(rating) : 
    return (rating+8)*100
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
        if answer == 1 :
            return 0 
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
        self.speed=newSpeed
        return 1 
    def compare(contestant1,contestant2,method="sum"):   
        maxRating=len(contestant1.speed)-1
        answer=0
        for rating in range(0,maxRating+1): 
            if method == "sum" : 
                answer += (contestant1.speed[rating]-contestant2.speed[rating])**2
            else : 
                answer = max(answer,abs(contestant1.speed[rating]-contestant2.speed[rating]))
        return answer
