class Tes:
    def method_A(self):
        print("Ini adalah method A.")

    def method_B(self):
        print("Method B sedang memanggil method A:")
        self.method_A()  # Memanggil method A di dalam method B

    def method_C(self):
        print("Method C sedang memanggil method B:")
        self.method_B()  # Memanggil method B di dalam method C

# Membuat objek kelas Tes
objek_tes = Tes()

# Memanggil method C yang pada gilirannya memanggil method B, dan method B memanggil method A
objek_tes.method_C()
