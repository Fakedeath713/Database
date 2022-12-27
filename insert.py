import db
import random
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind = db.engine)
session = Session()



#tr1 = db.Adres(random.randint(0, 100),"Ev",  1, "Caganlar", "Cumhuriyet", "Otuzikievler", 7)
#session.add(tr1)
#tr1 = db.Adres(random.randint(0, 100),"Sirket",  1, "Asiyan", "801.", "Kemal", 5)
#session.add(tr1)
#tr1 = db.Adres(random.randint(0, 100),"Ev",5, "Kitap", "404.", "Agim", 6)
#session.add(tr1)
#tr1 = db.Adres(random.randint(0, 100),"Sirket", 1, "Parmak", "Fatih", "Ebabi", 4)
#session.add(tr1)
#tr1 = db.Adres(random.randint(0, 100),"Okul", 3, "Mevlana Anadolu Lisesi", "Mevlana", "Celal", 2)
#session.add(tr1)
#
#session.commit()
#tr1 = db.Ulke(1, "Turkiye")
#
#session.add(tr1)
#
#session.commit()
#
#tr1 = db.Il(34, "Istanbul", 1)
#tr2 = db.Il(6, "Ankara", 1)
#tr3 = db.Il(1, "Adana", 1)
#tr4 = db.Il(54, "Sakarya", 1)
#
#session.add(tr1)
#session.add(tr2)
#session.add(tr3)
#session.add(tr4)
#
#session.commit()

#tr1 = db.Ilce(1, "Fatih", 34)
#tr2 = db.Ilce(2, "GaziOsmanPasa", 34)
#tr3 = db.Ilce(3, "Kecioren", 6)
#tr4 = db.Ilce(4, "Golbasi", 6)
#tr5 = db.Ilce(5, "Cukurova", 1)
#tr6= db.Ilce(6, "Imamoglu", 1)
#tr7 = db.Ilce(7, "Serdivan", 54)
#tr8 = db.Ilce(8, "Pamukova", 54)
#session.add(tr1)
#session.add(tr2)
#session.add(tr3)
#session.add(tr4)
#session.add(tr5)
#session.add(tr6)
#session.add(tr7)
#session.add(tr8)
#
#session.commit()

StandHarf1 = 'A'
StandHarf2 = 'B'
StandHarf3 = 'C'
#
#tr1 = db.Stand(StandHarf1)
#tr2 = db.Stand(StandHarf2)
#tr3 = db.Stand(StandHarf3)
#
#session.add(tr1)
#session.add(tr2)
#session.add(tr3)
#session.commit()
#
RafNumarasi1 = '1'
RafNumarasi2 = '2'
RafNumarasi3 = '3'
tr1 = db.Raf(RafNumarasi1, StandHarf1)
tr2 = db.Raf(RafNumarasi2, StandHarf2)
tr3 = db.Raf(RafNumarasi3, StandHarf3)

session.add(tr1)
session.add(tr2)
session.add(tr3)

session.commit()

#tr1 = db.OyunTuru(1, "Aksiyon")
#tr2 = db.OyunTuru(2, "Korku")
#tr3 = db.OyunTuru(3, "Yarış")
#tr4 = db.OyunTuru(4, "Ritim")
#
#session.add(tr1)
#session.add(tr2)
#session.add(tr3)
#session.add(tr4)
#
#session.commit()

#tr1 = db.KargoFirmasi(1, "Aras Kargo")
#tr2 = db.KargoFirmasi(2, "Sürat Kargo")
#
#session.add(tr1)
#session.add(tr2)
#
#session.commit()
#
#tr1 = db.UreticiFirmasi(1, "Valve")
#tr2 = db.UreticiFirmasi(2, "Blizzard")
#
#session.add(tr1)
#session.add(tr2)
#
#session.commit()
#
#tr1 = db.SaticiFirmasi(1, "Ubisoft")
#tr2 = db.SaticiFirmasi(2, "EA")
#
#session.add(tr1)
#session.add(tr2)
#
#session.commit()