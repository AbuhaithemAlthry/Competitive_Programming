def gradingStudents(grades):
    # Write your code here
    intarr=[]
    for gra in grades:
        if gra < 38:
            intarr.append(gra)
        else:
            x=5-(gra%5)
            if x<3:
                intarr.append(gra+x)
            else:
                intarr.append(gra)
    return intarr
