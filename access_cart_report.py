from datetime import datetime

format_date = "%m/%d/%Y"
format_time = '%H:%M:%S'
t = '10:04:00'

time1 = datetime.strptime(t,format_time)

filename = 'orari.txt'
i = 1




def is_date(first_value_in_line):
    try:
        res = bool(datetime.strptime(first_value_in_line, format_date))
    except ValueError:
        res = False
    return res


def calculate_access_cart_report():
    time_totali = datetime.strptime('00:00:01', format_time) - datetime.strptime('00:00:01', format_time)

    with open(filename) as orari:
        lines = orari.readlines()
        # print(lines)
        for line in range(1, len(lines), 2):
            # print(lines[line])
            first_value_in_line = lines[line].split()[0:1]
            first_value_str = str(first_value_in_line[0])
            # print(first_value_str)

            if is_date(first_value_str):
                first_value_str_list = first_value_str.split('/')
                # print(first_value_str_list[2], first_value_str_list[1], first_value_str_list[0])
                d = datetime(int(first_value_str_list[2]), int(first_value_str_list[0]), int(first_value_str_list[1]))
                # print(first_value_str_list)
                if d.weekday() < 5:
                    # new_rrjesht = str(lines[line + 1])
                    #print(f'{lines[line].split()[0:1][0]} => eshte dite jave , {lines[line + 2].split()[0:1][0]} => eshte orari')
                    t2 = str(lines[line + 2].split()[0:1][0])
                    # print(t2)
                    time2 = datetime.strptime(t2,format_time)
                    if time2 > time1:

                        delta_time =  time2 - time1
                        # print(delta_time)
                        time_totali = time_totali + delta_time
                        print(time_totali)
                    else:
                        delta_time = time1 - time2
                        # print(delta_time)
                        time_totali = time_totali - delta_time
                        print(time_totali)


# print(is_date('05:45:17'))

calculate_access_cart_report()
