
ingreso_mensual = 25000
gasto_mensual = 800

if ingreso_mensual > 10000:
    if gasto_mensual < 7000:
        print("buen sueldo en el mundo")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("estas bien")
    else:
        print("estas gastando mucho")
elif ingreso_mensual > 1000:
    print("estas bien para latam")
elif ingreso_mensual > 500:
    print("estas bien en argentina")
elif ingreso_mensual > 200:
    print("estas bien en venezuela")
else:
    print("sos pobre")