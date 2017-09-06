# -*- coding: UTF-8 -*-



# given a number, get its sqrt.


def exp2(x):
    return x*x

# 二分
def get_sqrt_bi(a, prec):
    low_val = 0.0
    high_val = a
    mid_val = low_val+(high_val-low_val)/2.0
    while abs(exp2(mid_val)-a) > prec:    # 如果不符合， 一直找
        # print mid_val
        if exp2(mid_val) < a:    # 找小了
            low_val = mid_val
        else:
            high_val = mid_val
        mid_val = low_val + (high_val - low_val) / 2.0
    return mid_val

print get_sqrt_bi(12.0, 0.00001)

# 每轮确定一位(while)。 如何确定一位: 顺序查找(while), 每次步进step。 step与轮数相关， 每轮缩0.1
def get_sqrt_seq(a, prec):
    val = 0
    step = 1.0    # 每一轮的查找step
    low_v = 0
    high_v = a
    while True:        # 每轮确定一位总是会结束的，不用关心确定到什么时候结束。
        val = low_v
        while val < high_v:
            if abs(exp2(val)-a) <= prec:
                return val
            if exp2(val) < a < exp2(val+step):
                low_v = val
                high_v = val+step
                step *= 0.1
                break
            val += step



print get_sqrt_seq(12.0, 0.00001)


