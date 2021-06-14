def Tower(n, fr, to, spare):
    if n == 1:
        print("Move disk 1 from", fr, "to", to)
        return
    Tower(n - 1, fr, spare, to)
    print("Move disk", n, "from", fr, "to", to)
    Tower(n - 1, spare, to, fr)

n = 3
Tower(n, 'A', 'B', 'C')
