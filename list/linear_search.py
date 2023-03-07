def linear_search(list :any ,number:any):
    for i in range(len(list)):
        if list[i] == number:
            return i
    return -1

if __name__ == "__main__":
    print(linear_search(['rasd','234','ram','nis'],'nis'))