class Pegawai:
  def __init__(self, nama, gaji=0):
    self.nama = nama
    self.gaji = gaji
   def tunjangan(self, persen):
    self.gaji = self.gaji + (self.gaji * persen)
   def kerja(self):
    print(Self.nama, "Pekerjaanya")
   def __repr__(self):
    return "<Pegawai:\n nama = %s, gaji = %s" %(self.nama, self.gaji)
  class Koki(Pegawai):
    def __init__(self, nama):
      pegawai.__init__(self, nama, 100000)
    def kerja(self):
      print(self.nama, "Mebuat Makanan")
   class Pelayan(Pegawai):
      def __init__(self,nama):
        pegawai.__init__(self, nama 50000)
      def kerja(Self:
      print(self.nama, "Melayani Costumer")
    class PizzaRobot(Koki):
      def __init__(self, nama)
        koki.__init__(Self, nama)
       def kerja(self):
          print(Self.nama, "Membuat Pizza")
     if __name__ == "__main__":
        agus = PizzaRobot("Agus")
        print (agus)
        agus.kerja()
        agus.tunjungan(0.20)
        print(agus)
        print
        
        for kelas in pegawai, koki, Pelayan, PizzaRobot:
        objek = kelas(kelas.__name__)
        objek.kerja()
     
         
