# return (value / base, value % base)
def divide_with_remainder(value, base):
	quotient = 0
	remainder = value
	while remainder >= base:
		remainder -= base
		quotient += 1

	return (quotient, remainder)

#return log=floor(log_{base}{value}) with reaminder = value - base ** log
def log_with_remainder(value, base):
    log = 0
    q = base
    r = 0

    while  q <= value:
        q = base * q
        log = log + 1

    r = value - int( q / base )
    return (log, r)

def stein_none_rescursive(n,d):
    s = 0
    flag_log_phase = True
    r = n
    l = []
    last_s = 0
    l.append((r, s))

    while len(l) > 0:
        (r, s) = l.pop()
        if flag_log_phase:
            n = r
            while n > 0:
                (n, r) = log_with_remainder(n, d)
                l.append((r, 0))
            flag_log_phase = False
            last_s = 0
        else:
            if s == 0:
                s = last_s 
                if r < d:
                    s = (d+1) ** s + r
                    l.append((r, s))
                    last_s = 0
                else:   
                    s = (d+1) ** s
                    l.append((r, s))
                    l.append((r, 0))
                    flag_log_phase = True
            else:
                s += last_s
                last_s = s
    return s - 1


#ref: https://code.sololearn.com/cG7lp29a4cwM/#py
def stein(n,d):
  s = 0
  i = 0
  while n > 0:
    r=n%d
    n=n//d
    s+=r*(d+1)**stein(i,d)
    i+=1
  return s


def gs(n,d):
    return stein(n,d) - 1

for t in range(2,100):
    print("t=%d" % t)
    for i in range(2,5):
        #print(gs(t,i))
        p=stein_none_rescursive(t,i)
        #print(p)
        if gs(t,i) != p:
           print("something is worng.")
           break
        t=p
        if(t==0): break; # added
