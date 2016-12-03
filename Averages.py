def calculateAverage(times, startIndex, endIndex): #WCA-style average calculator
    times=times[startIndex:endIndex]
    length=len(times)
    if times.count("DNF")>1:
        return "DNF"
    
    if "DNF" in times:
        times.remove("DNF")
        worst="DNF"
        
        best=min(times)
        times.remove(best)
        
        return round(sum(times)/(length-2), 2), best, worst
    
    else:
        best=min(times)
        worst=max(times)
        
        times.remove(best)
        times.remove(worst)
        
        return "%.2f" % round(sum(times)/(length-2), 2)

def calculateMean(times): #Standard arithmetic mean
    return "%.2f" % round(sum(times)/len(times), 2)

def calculateBest(times):
    return "%.2f" % min(times)

def calculateWorst(times):
    return "%.2f" % max(times)
