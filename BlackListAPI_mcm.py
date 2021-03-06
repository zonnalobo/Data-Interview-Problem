import memory_chunk_module as mcm

def initialize(filename):
    file_content = open(filename, "r")

    for i in range(total_chunk):
        lines = file_content.readlines(chunk_memory)
        if '\n' not in lines[len(lines)-1]:
            lines[len(lines)-1]=str(lines[len(lines)-1])+'\n'
        lines.sort()
        file = open(blacklist_temp_format.format(i), "w")
        file.write(''.join(lines))
        chunk_filenames.append(blacklist_temp_format.format(i))
        file.close()
        

def check_blacklist(name, phone_number):
    is_blacklisted = False
    check_data = [name, phone_number]

    for i in range(total_chunk):
        file = open(blacklist_temp_format.format(i), "r")
        lines = [line for line in file.readlines()]
        for item_point in lines:
            if (str(name) in item_point)&(str(phone_number) in item_point)&(len(str(name)+str(phone_number))==len(item_point)-2):
                is_blacklisted = True
                file.close()
                break
        if (is_blacklisted)or(len(lines)==0):
            break
    return is_blacklisted


# Global variables
chunk_memory = mcm.get_parsed_memory("10M")
chunk_filenames = []
blacklist = "blacklist.txt"
blacklist_temp_format = 'blacklist_{0}.txt'
total_chunk = mcm.get_total_chunk(blacklist, chunk_memory)


if __name__ == "__main__":
    initialize(blacklist)

    # Demo
    print(check_blacklist('Andi','1341441'))
