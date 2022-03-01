
from t2k_hangul_core import Listing, Address, Contact, ListingsTable, tbl_listings
from t2k_hangul_core.utils.db import DBConnection
from sqlalchemy import insert, select, text
from pandas import DataFrame

with DBConnection() as db:
    customer = db.session.query(tbl_listings).filter_by(id=10)

    result = db.session.execute(select(tbl_listings).filter_by(id=10)).all()
    print(result.language)

# from t2k_hangul_core.utils import db
#

#
#
# from sqlalchemy import MetaData
#
# metadata = MetaData(db.engine)
#
# tbl_listings.metadata.create_all(db.engine)
#
# store = ConfigStore.get_instance()
#
# store.load({
#     **config,
#     **credentials
# })

# dbobj = Database(store)

addrObj = Address.from_dict({
    "property_addr1": "Rajbagh",
    "property_city": "Srinagar",
    "property_province": "Srinagar",
    "property_postal_code": "190014"
})
addrObj.convert_to_google

phone = Contact.from_dict(
    {
        "type": "mobile",
        "value": "9632911213"
    })

email = Contact.from_dict({
    "type": "email",
    "value": "saqib.mj@gmail.com"
})

obj = Listing.from_dict({
    "property_id": "t2k_001",
    "property_name": "Hotel Rose Petal",
    "property_country": "India",
    "property_address": [addrObj],
    "star_rating": 5,
    "property_latitude": "231.22",
    "property_longitude": "12.52",
    "property_phone": [phone, email]
}
)
print(obj)

# Read https://docs.sqlalchemy.org/en/14/core/dml.html#sqlalchemy.sql.expression.Insert
# Inserting record one by one
query = insert(tbl_listings).values(listing='t2k_001', language='english')
conn = db.engine.connect()
conn.execute(query)
conn.commit()

results = conn.execute(select([tbl_listings])).fetchall()
df = DataFrame(results)
df.columns = results[0].keys()
df.head(4)
