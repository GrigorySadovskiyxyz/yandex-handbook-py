n = input()
fn = int(n[2]) + int(n[1])
sn = int(n[1]) + int(n[0])
if fn >= sn:
    print(f"{fn}{sn}")
elif sn >= fn:
    print(f"{sn}{fn}")
