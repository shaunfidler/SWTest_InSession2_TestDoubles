def int_sum(filename):
    with open(filename, "r+") as f:
        lines = f.readlines()
        if(len(lines) == 0):
            raise ValueError
        total_sum = 0
        for line in lines:
            line = line.replace("\n", '')

            if(not line.lstrip('+-').isdigit()):
                raise TypeError
                
            total_sum += int(line)

        f.write("\n" + str(total_sum))
        return total_sum