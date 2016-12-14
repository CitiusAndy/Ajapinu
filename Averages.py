def calculateAverage(times, startIndex, endIndex): #WCA-style average calculator
    """
    Calculates WCA-style averages. Can be used to select specific interval of times from the time list.

    Args:
        times: a times list which consists of floats
        startIndex: the starting index which corresponds to Python slicing
        endIndex: the ending index which corresponds to Python slicing
        
    Returns:
        average time in float with 2 decimal places
    """
    times=times[startIndex:endIndex]
    length=len(times)
    
    if times.count("DNF")>1:
        return "DNF"
    
    if "DNF" in times:
        times.remove("DNF")
        worst="DNF"
        
        best=min(times)
        times.remove(best)
    
    else:
        best=min(times)
        worst=max(times)
        
        times.remove(best)
        times.remove(worst)
        
    return "%.2f" % round(sum(times)/(length-2), 2)

def calculateMean(times): #Standard arithmetic mean
    """
    Calculates arithmetic mean.
    Args:
        a list of floats
    Returns:
        a float of arithmetic mean with 2 decimal places
    """
    return "%.2f" % round(sum(times)/len(times), 2)

def calculateBest(times):
    """
    Calculates the best time in a list.
    Args:
        a list of floats
    Returns:
        a float of the best time with 2 decimal places
    """
    return "%.2f" % min(times)

def calculateWorst(times):
    """
    Calculates the worst time in a list.
    Args:
        a list of floats
    Returns:
        a float of the worst time with 2 decimal places
    """
    return "%.2f" % max(times)
