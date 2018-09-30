def initialize(filename):
    file_content = open(filename, "r")

    lines = file_content.readlines()
    if '\n' not in lines[len(lines)-1]:
        lines[len(lines)-1]=str(lines[len(lines)-1])+'\n'
    lines.sort()
    file = open(blacklist_temp_format.format(0), "w")
    file.write(''.join(lines))
    file.close()
        

def check_blacklist(name, phone_number):
    is_blacklisted = False
    check_data = [name, phone_number]

    file = open(blacklist_temp_format.format(0), "r")
    lines = [line for line in file.readlines()]
    for item_point in lines:
        if (str(name) in item_point)&(str(phone_number) in item_point)&(len(str(name)+str(phone_number))==len(item_point)-2):
            is_blacklisted = True
            file.close()
            break
    return is_blacklisted


# Global variables
blacklist = "blacklist.txt"
blacklist_temp_format = 'blacklist_{0}.txt'


if __name__ == "__main__":
    initialize(blacklist)

    # Demo
    print(check_blacklist('Andi','1341441'))
