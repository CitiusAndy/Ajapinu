def calculateAverage(times):
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
        
        return round(sum(times)/(length-2), 2), best, worst
