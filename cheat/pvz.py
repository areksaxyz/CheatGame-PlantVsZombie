import pymem

pm = pymem.Pymem("popcapgame1.exe")

address = 0x248B63F8

suns = pm.read_int(address)

print("suns:", suns)

user_input = int(input("berapa banyak matahari yang ingin anda miliki?"))

pm.write_int(address, user_input)

print("Sukses Hacked suns!")