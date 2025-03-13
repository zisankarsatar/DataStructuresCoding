"""
 String Combinations Consisting only of 0, 1 and ?
•⁠  ⁠For this popular algorithm interview question, the input will be a string consisting only of the characters 0, 1 and?, 
where the ? acts as a wildcard that can be either a 0 or 1, and your goal is to print all possible combinations of the string. 
For evample, if the string is "011?0" then your program should output a set of all strings, which are: ["01100", "01110"].
"""

def patterns(str, all):
    #if str is empty
    if len(str) == 0:
        return all
     
    #if str[0
    if str[0] != "?":
        for i in range(0, len(all)):
            all[i].append(str[0])
    else:
        for i in range(0, len(all)):
            temp = list(all[i])
            all.append(temp)
        for i in range(0, len(all)):
            if i < len(all)/2:
                all[i].append('0')
            else:
                all[i].append('1')
                
    return patterns(str[1:], all)


print(patterns('011?0?', [[]]))
                