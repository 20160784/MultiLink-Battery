from time import sleep

def tx(ttype, t, p):
    if ttype == data:
        sleep(2)
        t += 2
        p += 280
    elif ttype == ack:
        sleep(3)
        t += 3
        p += 280
    elif ttype == pspoll:
        sleep(3)
        t += 3
        p += 280
    elif ttype == beacon:
        sleep(3)
        t += 3
        p += 280
    return t, p


def rx(rtype, t, p):
    if rtype == data:
        sleep(2)
        t += 2
        p += 130
    elif rtype == ack:
        sleep(3)
        t += 3
        p += 130
    elif rtype == pspoll:
        sleep(3)
        t += 3
        p += 130
    elif rtype == beacon:
        sleep(3)
        t += 3
        p += 280
    return t, p


def idle(t, p):
    sleep(3)
    t += 3
    p = t * 0.9 + p
    return t, p


def doze(t, p):
    sleep(3)
    t += 3
    p = t * 0.09 + p
    return t, p


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = 0
    pspoll = 0
    ack = 0
    beacon = 0

    # ap
    print("ap")
    ap_t = 0  # ap latency
    ap_p = 0  # ap power
    # ap_tp=[ap_t, ap_p]
    ap_t, ap_p = idle(ap_t, ap_p)
    print(ap_t, ap_p)
    ap_t, ap_p = tx(beacon, ap_t, ap_p)
    print(ap_t, ap_p)
    ap_t, ap_p = tx(data, ap_t, ap_p)
    print(ap_t, ap_p)
    ap_t, ap_p = doze(ap_t, ap_p)
    print(ap_t, ap_p)
    ap_t, ap_p = idle(ap_t, ap_p)
    print(ap_t, ap_p)
    ap_t, ap_p = tx(beacon, ap_t, ap_p)
    print(ap_t, ap_p)
    ap_t, ap_p = rx(pspoll, ap_t, ap_p)
    print(ap_t, ap_p)
    ap_t, ap_p = tx(data, ap_t, ap_p)
    print(ap_t, ap_p)
    ap_t, ap_p = doze(ap_t, ap_p)
    print(ap_t, ap_p)

    # data1=tx(data, ap_t, ap_p)

    # sta1
    print("sta")
    sta_t = 0  # sta latency
    sta_p = 0  # sta power
    sta_tp = []
    sta_t, sta_p = idle(sta_t, sta_p)
    print(sta_t, sta_p)
    sta_t, sta_p = rx(beacon, sta_t, sta_p)
    print(sta_t, sta_p)
    sta_t, sta_p = rx(data, sta_t, sta_p)
    print(sta_t, sta_p)
    sta_t, sta_p = doze(sta_t, sta_p)
    print(sta_t, sta_p)
    sta_t, sta_p = idle(sta_t, sta_p)
    print(sta_t, sta_p)
    sta_t, sta_p = rx(beacon, sta_t, sta_p)
    print(sta_t, sta_p)
    sta_t, sta_p = tx(pspoll, sta_t, sta_p)
    print(sta_t, sta_p)
    sta_t, sta_p = rx(data, sta_t, sta_p)
    print(sta_t, sta_p)
    sta_t, sta_p = doze(sta_t, sta_p)
    print(sta_t, sta_p)

    print("시간:", ap_t)
    print("총 파워소모량:", ap_p + sta_p)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
