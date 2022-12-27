from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, CHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker , validates
from sqlalchemy_utils import database_exists, create_database

engine = create_engine('postgresql+psycopg2://postgres:713317azer@localhost/game')
if not database_exists(engine.url):
    create_database(engine.url)
print(database_exists(engine.url))

base = declarative_base()

class Stand (base):
    
    __tablename__ = "Stand"
    
    StandHarf = Column(CHAR, primary_key = True)
    
    def __init__ (self, StandHarf):
        self.StandHarf = StandHarf

class Raf (base):
    
    __tablename__ = "Raf"
    
    RafNumarasi = Column(CHAR, primary_key = True)
    StandHarf   = Column(CHAR, ForeignKey('Stand.StandHarf'), nullable = False)
    
    def __init__ (self, RafNumarasi, StandHarf):
        self.RafNumarasi = RafNumarasi
        self.StandHarf = StandHarf

class OyunTuru(base):
    __tablename__ = "OyunTuru"
    
    OyunTuruNo = Column(Integer, primary_key = True)
    OyunTuruAdi = Column(String)
    
    def __init__ (self, OyunTuruNo, OyunTuruAdi):
        self.OyunTuruNo = OyunTuruNo
        self.OyunTuruAdi = OyunTuruAdi

class Oyun(base):
    __tablename__ = "Oyun"
    OyunSeriNumarasi = Column(Integer, primary_key = True)
    OyunAdi = Column(String)
    SatisFiyati = Column(Integer)
    UreticiFirmaNo = Column(Integer, ForeignKey('UreticiFirmasi.FirmaNo'))
    SaticiFirmaNo = Column(Integer, ForeignKey('SaticiFirmasi.FirmaNo'))
    OyunTuruNo = Column(Integer, ForeignKey('OyunTuru.OyunTuruNo'))
    OyunAdedi = Column(Integer)
    RafNumarasi = Column(CHAR,ForeignKey('Raf.RafNumarasi'))
    
    def __init__(self, OyunSeriNumarasi, OyunAdi, SatisFiyati, UreticiFirmaNo, SaticiFirmaNo, OyunTuruNo, OyunAdedi, RafNumarasi):
        self.OyunSeriNumarasi = OyunSeriNumarasi
        self.OyunAdi = OyunAdi
        self.SatisFiyati = SatisFiyati
        self.UreticiFirmaNo = UreticiFirmaNo
        self.SaticiFirmaNo = SaticiFirmaNo
        self.OyunTuruNo = OyunTuruNo
        self.OyunAdedi = OyunAdedi
        self.RafNumarasi = RafNumarasi
    

class Ulke(base):
    __tablename__ = "Ulke"
    
    UlkeId  = Column(Integer, primary_key = True)
    UlkeAdi = Column(String)
    
    def __init__(self, UlkeId, UlkeAdi):
        self.UlkeId   = UlkeId
        self.UlkeAdi = UlkeAdi
        
class Il(base):
    __tablename__ = "Il"
    
    IlNum  = Column(Integer, primary_key = True)
    IlAdi  = Column(String)
    UlkeId = Column(Integer, ForeignKey('Ulke.UlkeId'))
    
    def __init__(self, IlNum, IlAdi, UlkeId):
        self.IlNum = IlNum
        self.IlAdi = IlAdi
        self.UlkeId = UlkeId

class Ilce(base):
    __tablename__ = "Ilce"
    
    IlceNum  = Column(Integer, primary_key = True)
    IlceAdi = Column(String)
    IlNum = Column(Integer, ForeignKey('Il.IlNum'))
    
    def __init__(self, IlceNum, IlceAdi, IlNum):
        self.IlceNum = IlceNum
        self.IlceAdi = IlceAdi
        self.IlNum = IlNum
  
        
class Adres(base):
    __tablename__ = "Adres"
    
    AdresId = Column(Integer, primary_key=True)
    AdresAdi = Column(String)
    DaireNo = Column(CHAR)
    DaireAdi = Column(String)
    SokakAdi = Column(String)
    MahalleAdi = Column(String)
    IlceNumarasi = Column(Integer,ForeignKey('Ilce.IlceNum'))
    
    @validates("DaireAdi")
    def DaireAdiKontrol(self,key,DaireAdi):
        while True:
            if len(DaireAdi)==1:
                DaireAdi = input('DaireAdi Tekrar Giriniz(1 den uzun olmalı)..:')
            else:
                return DaireAdi
    
    @validates("MahalleAdi")
    def MahalleAdiKontrol(self,key,MahalleAdi):
        while True:
            if MahalleAdi[0]=='ğ':
                MahalleAdi = input('MahalleAdi Tekrar Giriniz(ğ ile baslayamaz)..:')
            else:
                return MahalleAdi
    
    
    
    
    def __init__(self,AdresId,AdresAdi,DaireNo,DaireAdi,SokakAdi,MahalleAdi,IlceNumarasi):
        self.AdresId = AdresId
        self.AdresAdi = AdresAdi
        self.DaireNo = DaireNo
        self.DaireAdi = DaireAdi
        self.SokakAdi = SokakAdi
        self.MahalleAdi = MahalleAdi
        self.IlceNumarasi = IlceNumarasi
        
#class KargoAdresi(Adres):
#    __tablename__ = "KargoAdresi"
#    AdresId = Column(Integer, primary_key=True)
#    AdresAdi = Column(String)
#    DaireNo = Column(CHAR)
#    DaireAdi = Column(String)
#    SokakAdi = Column(String)
#    MahalleAdi = Column(String)
#    IlceNumarasi = Column(Integer,ForeignKey('Ilce.IlceNum'))
#    KargoAdresId = Column(None, ForeignKey('Adres.AdresId'), primary_key = True)
    
#class FaturaAdresi(Adres):
#    __tablename__ = "FaturaAdresi"
#    FaturaAdresId = Column(None, ForeignKey('Adres.AdresId'), primary_key = True)
#    __mapper_args__ = {
#        'polymorphic_identity' : 'Fatura Adresi'
#    }

class MusteriDetay(base):
    __tablename__ = "MusteriDetay"
    
    MusteriId = Column(Integer, primary_key=True)
    MusteriAdi = Column(String)
    MusteriSoyadi = Column(String)
    MusteriTel = Column(String)
    AdresId = Column(Integer,ForeignKey('Adres.AdresId'), nullable = False)
    
    @validates("MusteriTel")
    def validate_MusteriTel(self, key, MusteriTel):
        while True:
            if len(MusteriTel) == 10:
                return MusteriTel
            else:
                MusteriTel = input('MusteriTel Tekrar giriniz(10 numaradan olusmali)..:')
                
    @validates("MusteriSoyadi")
    def MusteriSoyadiUpper(self,key,MusteriSoyadi):
        MusteriSoyadi=MusteriSoyadi.upper()
        return MusteriSoyadi
        
        

    def __init__(self, MusteriId, MusteriAdi, MusteriSoyadi, MusteriTel, AdresId):
        self.MusteriId = MusteriId
        self.MusteriAdi = MusteriAdi
        self.MusteriSoyadi = MusteriSoyadi
        self.MusteriTel = MusteriTel
        self.AdresId = AdresId
        
class Siparis(base):
    __tablename__ = "Siparis"
    
    SiparisNo = Column(Integer, primary_key = True)
    SiparisTarihi = Column(String)
    ToplamTutar = Column(Integer)
    KargoFirmaNo = Column(Integer ,ForeignKey('KargoFirmasi.FirmaNo'), nullable = False)
    MusteriId = Column(Integer ,ForeignKey('MusteriDetay.MusteriId'), nullable = False)
    OyunSeriNumarasi = Column(Integer, ForeignKey('Oyun.OyunSeriNumarasi'), nullable = False)
    
    def __init__(self, SiparisNo, SiparisTarihi, ToplamTutar, KargoFirmaNo, MusteriId, OyunSeriNumarasi):
        self.SiparisNo = SiparisNo
        self.SiparisTarihi = SiparisTarihi
        self.ToplamTutar = ToplamTutar
        self.KargoFirmaNo = KargoFirmaNo
        self.MusteriId = MusteriId
        self.OyunSeriNumarasi = OyunSeriNumarasi
        
class UreticiFirmasi(base):
    __tablename__ = "UreticiFirmasi"
    FirmaNo = Column(Integer, primary_key = True)
    FirmaAdi = Column(String)
    
    def __init__(self, FirmaNo, FirmaAdi):
        self.FirmaNo = FirmaNo
        self.FirmaAdi = FirmaAdi

class SaticiFirmasi(base):
    __tablename__ = "SaticiFirmasi"
    FirmaNo = Column(Integer, primary_key = True)
    FirmaAdi = Column(String)
    
    def __init__(self, FirmaNo, FirmaAdi):
        self.FirmaNo = FirmaNo
        self.FirmaAdi = FirmaAdi

class KargoFirmasi(base):
    __tablename__ = "KargoFirmasi"
    FirmaNo = Column(Integer, primary_key = True)
    FirmaAdi = Column(String)
    
    def __init__(self, FirmaNo, FirmaAdi):
        self.FirmaNo = FirmaNo
        self.FirmaAdi = FirmaAdi



base.metadata.create_all(engine)