deg, min, sec  = 60, 10, 45
fm = sec / 60
fd = (fm + min) /60
ang = deg + fd
pi = 3.14159265359
rad = 180 / pi
arad = ang / rad
print(deg, "°", min, "'", sec, '" =', arad, "radian(s)")