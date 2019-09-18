class Kotak(object):
  def __init__(self, p l, t):
      self.panjang = p
      self.lebar = l
      self.tinggi = t
      
  def hitungVolume(self) :
    return self.panjang * self.lebar * \
           self.tinggi
           
  def cetakData(self):
    print("panjang\t: ", self.panjang)
    print("lebar\t: ", self.lebar)
    print("tinggi\t: ", self.tinggi)
    
  def cetakVolume(self):
    print("Volume\t= ", self.hitungVolume())
    
# mendefenisikan kelas turunan (subclass)
class KotakWarna(Kotak):
  def __init__(Self, p, l, t, w):
      self.panjang = p
      self.lebar = l 
      self.tinggi = t
      self.warna = w
    def cetakData(self):
    print("panjang\t: ", self.panjang)
    print("lebar\t: ", self.lebar)
    print("tinggi\t ", self.tinggi)
    print("warna\t ", self.warna)
    
  def main()
  # membuat objek KotakWarna
  kotakwarna1 = kotakWarna(6, 5, 5, "merah")
  
  # menggunakan objek
  kotakwarna1.cetakData()
  kotakwarna1.cetakvolume()
  
  if __name__ =="__main__:
     main()
