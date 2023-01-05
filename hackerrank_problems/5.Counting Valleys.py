def countingValleys(steps, path):
    # Write your code here
    seale=0
    mount=0
    for ele in path:
        if ele == 'U':
            seale+=1
        elif ele == 'D':
            seale-=1
        if seale == 0 and ele == 'U':
            valley+=1
    return valley
