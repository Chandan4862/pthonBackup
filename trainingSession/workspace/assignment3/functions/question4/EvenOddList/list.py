def EvenOdd(list):
    dict={"EVEN":[],"ODD":[]}
    for i in list:
        if i&1==0:
            dict["EVEN"].append(i)
        else:
            dict["ODD"].append(i)
    return dict
