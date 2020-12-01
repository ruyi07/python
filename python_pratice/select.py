# 查询工资

import money


def select():
    if money.saved_money == 1000:
        print(f"又延迟发工资了，现在余额{money.saved_money}")
    else:
        money.saved_money == 2000
        print(f"发工资啦，可以剁手了，现在余额:{money.saved_money}")
