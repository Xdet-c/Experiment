from sqlalchemy import create_engine, Column, Integer, String, BigInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# mengubungkan dan melakukan pengaturan
engine  = create_engine("mysql+pymysql://root:1234@localhost:3306/sekolah", echo=False)
conn    = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
base    = declarative_base()

# membuat table
class Buku(base):
    __tablename__ = "buku"

    id = Column(Integer, primary_key=True)
    nama_buku = Column(String(60))
    nama_penulis = Column(String(95))
    noSeri = Column(BigInteger)

base.metadata.create_all(engine)

'''
# menambahkan data ke dalam table
buku1 = Buku(nama_buku="Sizen", nama_penulis="WIw", noSeri=353235)
#memanfaatkan session
session.add(buku1)
session.commit()
'''

# show data di table

## mendapatkan semua data
getall = session.query(Buku)

for buku in getall:
    print(Buku.id, Buku.nama_buku, Buku.nama_penulis, Buku.noSeri)


print()
print()
print()

# mendapatkan data secara berurutan
geturut = session.query(Buku).order_by(Buku.nama_buku)

for buku in geturut:
    print(buku.nama_buku)
print()

# mendapatkan data tertentu

sepsificdata = session.query(Buku).filter(Buku.nama_buku == "Komunikasi itu ada seninya").first()
print(sepsificdata.nama_buku, sepsificdata.nama_penulis)
print()


# mendapatkan jumlah data
buku_count = session.query(Buku).count()
print(buku_count)
print()


## update data 
'''
buku_update_name = session.query(Buku).filter(Buku.nama_buku == "mein khanf").first()
buku_update_name.nama_buku = "Belajar javascript dari nol"

buku_update_author = session.query(Buku).filter(Buku.nama_penulis == "Adolf hitler").first()
buku_update_author.nama_penulis = "mlya sandikhov"

buku_update_noseri = session.query(Buku).filter(Buku.noSeri == "353235").first()
buku_update_noseri.noSeri = "3654355"

session.commit()'''


## versi lebih rapih

'''
buku = session.query(Buku).filter(Buku.nama_buku == "Masttery").first()


if buku:
    buku.nama_buku = "Python itu ada seninya"
    buku.nama_penulis = "dyman"
    buku.noSeri = "67676767"

#session.commit()
'''

### delete data di table
'''
hapus_data =  session.query(Buku).filter(Buku.nama_penulis == "dyman").first()
session.delete(hapus_data)
session.commit()
'''

