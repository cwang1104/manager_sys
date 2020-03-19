from application import db



class CarsInfo(db.Model):
    __tablename__ = 'cars_info'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(200, 'utf8mb4_bin'), server_default=db.FetchedValue(), info='????')
    brand = db.Column(db.String(200, 'utf8mb4_bin'), server_default=db.FetchedValue(), info='??')
    cars_local = db.Column(db.String(collation='utf8mb4_bin'), info='?????')
    arctic = db.Column(db.String(200, 'utf8mb4_bin'), server_default=db.FetchedValue(), info='??')
    regist_date = db.Column(db.String(20, 'utf8mb4_bin'), index=True, server_default=db.FetchedValue(), info='????')
    mileage = db.Column(db.String(200, 'utf8mb4_bin'), server_default=db.FetchedValue(), info='????')
    gear = db.Column(db.String(200, 'utf8mb4_bin'), server_default=db.FetchedValue(), info='??')
    emissions = db.Column(db.String(200, 'utf8mb4_bin'), server_default=db.FetchedValue(), info='????')
    price = db.Column(db.String(200, 'utf8mb4_bin'), server_default=db.FetchedValue(), info='??')
    img_desc = db.Column(db.String(200, 'utf8mb4_bin'), info='????')
    describe = db.Column(db.Text(collation='utf8mb4_bin'), info='????')
    created_date = db.Column(db.DateTime, info='????')
    picture1 = db.Column(db.String(2000, 'utf8mb4_bin'), server_default=db.FetchedValue(), info='?1')
    picture2 = db.Column(db.String(2000, 'utf8mb4_bin'), server_default=db.FetchedValue(), info='?2')
    picture3 = db.Column(db.String(2000, 'utf8mb4_bin'), server_default=db.FetchedValue(), info='?3')
    picture4 = db.Column(db.String(2000, 'utf8mb4_bin'), server_default=db.FetchedValue(), info='?4')
    picture5 = db.Column(db.String(2000, 'utf8mb4_bin'), server_default=db.FetchedValue(), info='?5')
    picture6 = db.Column(db.String(2000, 'utf8mb4_bin'), server_default=db.FetchedValue(), info='?6')

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])