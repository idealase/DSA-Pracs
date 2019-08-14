import platform, time


def gen_report():
    print("\n\nExecution Information...")

    # time report
    time_now = time.localtime()
    print("Date: " + str(time_now[2]) + "-" + str(time_now[1]) + "-" +
          str(time_now[0]))
    print("Time: " + str(time_now[3])+ ":" + str(time_now[4]) + ":" +
          str(time_now[5]))

    # system information
    print("Python " + str(platform.python_version()))
    print(platform.machine(), platform.platform(), platform.processor())

