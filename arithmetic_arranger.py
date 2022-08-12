def arithmetic_arranger(problems,arg=False):
    import re
    list = problems
    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    #-----------Error Handling start----------------#
    if len(list)>5:
        return 'Error: Too many problems.'
        
    for lst in list:
        if not re.findall(r".*\s[+,-]\s.*",lst):
            return "Error: Operator must be '+' or '-'."
            
        if not re.findall(r"^\d{1,}\s[+,-]\s\d{1,}$",lst):
            return "Error: Numbers must only contain digits."
            
        if not re.findall(r"^\d{1,4}\s[+,-]\s\d{1,4}$",lst):
            return "Error: Numbers cannot be more than four digits."
            
    #-----------Error Handling End----------------#
    for lst in list:
        split_list_elem = lst.split(" ")
        #find the highest length of the operand
        length = 0
        for elem in split_list_elem:
            if length < len(elem):
                length = len(elem)

        first_operand = split_list_elem[0].rjust(length+2)
        second_operand = split_list_elem[1] + " " + split_list_elem[2].rjust(length)
        if split_list_elem[1] == "+":
            result = str(int(split_list_elem[0]) + int(split_list_elem[2])).rjust(length+2)
        else:
            result = str(int(split_list_elem[0]) - int(split_list_elem[2])).rjust(length+2)
        first_line.append(first_operand)
        second_line.append(second_operand)
        third_line.append('-'*(length+2))
        fourth_line.append(result)
        if lst != list[-1]:
            first_line.append(" "*4)
            second_line.append(" "*4)
            third_line.append(" "*4)
            fourth_line.append(" "*4)
    
    if arg:
        arranged_problems = ''.join(first_line)+'\n'+''.join(second_line)+'\n'+''.join(third_line)+'\n'+''.join(fourth_line)
    else:
        arranged_problems = ''.join(first_line)+'\n'+''.join(second_line)+'\n'+''.join(third_line)
   
    return arranged_problems
   