#broot force methods
def reverse_words_in_a_string(string):
    print(string)
    string_list = string.split()
    reversed_string_list = []
    for i in range(len(string_list)-1,0,-1):
        reversed_string_list.append(string_list[i])
    reverse_string = ' '.join(reversed_string_list)
    print(reverse_string)
    return reversed_string_list
    
def optimize(string):
    print(string)
    left = 0
    right = len(string)-1
    temp = ""
    ans = ""
    while(left<=right):
        ch = string[left]
        if ch != " ":
            temp += ch    
        elif ch == " ":
            if ans != "" :
                ans = temp + " " + ans
            else : ans = temp
            temp =""
        
        left+=1
    if temp!="":
        if ans != "" :
            ans = temp + " " + ans
        else : ans = temp
    print("ans : %s",ans)
    return ans
    
if __name__ == '__main__':
    ans = optimize("TUF is great for interview preparation")
    print(ans)