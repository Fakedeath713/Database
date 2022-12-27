import db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind = db.engine)
session = Session()

def oyunEkle(OyunSeriNumarasi, OyunAdi, SatisFiyati, UreticiFirmaNo, SaticiFirmaNo, OyunTuruNo, OyunAdedi, RafNumarasi):
    tr1 = db.Oyun(OyunSeriNumarasi, OyunAdi, SatisFiyati, UreticiFirmaNo, SaticiFirmaNo, OyunTuruNo, OyunAdedi, RafNumarasi)
    session.add(tr1)
    session.commit()
    
def musteriEkle(MusteriId, MusteriAdi, MusteriSoyadi, MusteriTel, AdresId):
    tr1 = db.MusteriDetay(MusteriId, MusteriAdi, MusteriSoyadi, MusteriTel, AdresId)
    session.add(tr1)
    session.commit()
    
def siparisEkle(SiparisNo, SiparisTarihi, ToplamTutar, KargoFirmaNo, MusteriId, OyunSeriNumarasi):
    tr1 = db.Siparis(SiparisNo, SiparisTarihi, ToplamTutar, KargoFirmaNo, MusteriId, OyunSeriNumarasi)
    session.add(tr1)
    session.commit()
    
def adresEkle(AdresId,AdresAdi,DaireNo,DaireAdi,SokakAdi,MahalleAdi,IlceNumarasi):
    tr1 = db.Adres(AdresId,AdresAdi,DaireNo,DaireAdi,SokakAdi,MahalleAdi,IlceNumarasi)
    session.add(tr1)
    session.commit()
while True:
    inp = input("1-OyunEkle\n2-MusteriEkle\n3-SiparisEkle\n4-AdresEkle\n")
    if int(inp) == 1:
        tmp = input("OyunSeriNumarasi, OyunAdi, SatisFiyati, UreticiFirmaNo, SaticiFirmaNo, OyunTuruNo, OyunAdedi, RafNumarasi giriniz..:")
        tmp = tmp.split(',')
        oyunEkle(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5],tmp[6],tmp[7])
    elif int(inp) == 2:
        tmp = input("MusteriId, MusteriAdi, MusteriSoyadi, MusteriTel, AdresId giriniz..:")
        tmp = tmp.split(',')
        musteriEkle(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4])
    elif int(inp) == 3:
        tmp = input("SiparisNo, SiparisTarihi, ToplamTutar, KargoFirmaNo, MusteriId, OyunSeriNumarasi giriniz..:")
        tmp = tmp.split(',')
        siparisEkle(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5])
    elif int(inp) == 4:
        tmp = input("AdresId,AdresAdi,DaireNo,DaireAdi,SokakAdi,MahalleAdi,IlceNumarasi giriniz..:")
        tmp = tmp.split(',')
        adresEkle(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4],tmp[5],tmp[6])
        