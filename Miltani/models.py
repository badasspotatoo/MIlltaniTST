from Miltani import db

class Implementasi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rules = db.Column(db.String(20), nullable=False)
    sumberdaya = db.Column(db.String(120), nullable=False)
    investasi = db.Column(db.String(200), nullable=False)
    implementasi = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return '{} {} {} {}'.format(self.rules, self.sumberdaya, self.investasi, self.implementasi)

class Keuntungan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rules = db.Column(db.String(20), nullable=False)
    pengetahuan = db.Column(db.String(200), nullable=False)
    keuangan = db.Column(db.String(200), nullable=False)
    keuntungan = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '{} {} {} {}'.format(self.rules, self.pengetahuan, self.keuangan, self.keuntungan)

class Rancangan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rules = db.Column(db.String(200), nullable=False)
    implementasi = db.Column(db.String(200), nullable=False)
    keuntungan = db.Column(db.String(200), nullable=False)
    rancangan = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '{} {} {} {}'.format(self.rules ,self.implementasi, self.keuntungan, self.rancangan)