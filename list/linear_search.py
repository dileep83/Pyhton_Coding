from twosum import solution
def linear_search(list :any ,number:any):
    for i in range(len(list)):
        if list[i] == number:
            return i
    return -1

def list_sum(list :int):
    sum = 0
    for i in list:
        sum += i
    return sum

if __name__ == "__main__":
    print(linear_search(['rasd','234','ram','nis'],'nis'))
    print(list_sum([1,24,534,654,75]))
    