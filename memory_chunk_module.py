def get_parsed_memory(memory):
    # kilobyte
    if memory[-1].upper() == 'K':       
        return int(memory[:-1]) * 1024
    # megabyte
    elif memory[-1].upper() == 'M':     
        return int(memory[:-1]) * 1024 * 1024
    # gigabyte
    elif memory[-1].upper() == 'G':     
        return int(memory[:-1]) * 1024 * 1024 * 1024
    # byte
    else: 
        return int(memory)

def getSize(filename):
    fileobject=open(filename,'r')
    fileobject.seek(0,2)
    size=fileobject.tell()
    return(size)
    
def get_total_chunk(filename, chunk_memory):
    return int(int((getSize(filename) / chunk_memory))+ (not((getSize(filename) / chunk_memory)).is_integer()))
