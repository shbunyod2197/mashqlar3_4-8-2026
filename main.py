# 21
roy = [0, 1, 2, 3]

x = list(map(lambda a: a + 10, roy))
print(x)

# 22
roy = ["x", "y", "z"]
natija = [f"harf: {i}" for i in roy]
print(natija)

# 23
roy = [50, 100, 150]
natija = [i / 2 for i in roy]
print(natija)  # [25.0, 50.0, 75.0]

# 24
roy = ["5", "6", "7"]
natija = [int(i)**2 for i in roy]
print(natija)  # [25, 36, 49]

# 25
roy = [8, 9, 10]
natija = [i**2 for i in roy]
print(natija)

# 26
roy = ["hi", "hello"]
natija = [len(i) + 1 for i in roy]
print(natija)

# 27
roy = [12, 24, 36]
natija = [i / 12 for i in roy]
print(natija)

# 28
roy = ["A", "B", "C"]
natija = [i.lower() for i in roy]
print(natija)

# 29
roy = [3, 5, 7]
natija = [str(i * 10) for i in roy]
print(natija)

# 30
roy = ["1", "2", "3"]
natija = [int(i) + 100 for i in roy]
print(natija)
