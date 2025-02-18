
if warunek: 
    a = 1 # pirwszy poziom wcięcia
    if a == 1:
        print("a jest równe 1") # drugi poziom wcięcia
        if inny_warunek:
            print("inny_warunek jest spełniony") # trzeci poziom wcięcia
    else:
        print("a nie jest równe 1")
else:
    print("warunek nie jest spełniony")