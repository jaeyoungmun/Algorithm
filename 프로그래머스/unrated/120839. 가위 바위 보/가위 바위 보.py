def solution(rsp):
    rsp = rsp.replace('0','1')
    rsp = rsp.replace('2','0')
    rsp = rsp.replace('5','2')
    rsp = rsp.replace('1','5')
    return rsp