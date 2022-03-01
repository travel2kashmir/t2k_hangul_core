from config import config
from credentials import credentials
from t2k_hangul_core import ConfigStore
from t2k_hangul_core.connectors.hotel_ads import Listing, Address, Contact


# from sqlalchemy import insert, delete, update, select
# from pandas import DataFrame

store = ConfigStore.get_instance()

store.load({
    **config,
    **credentials
})

# dbobj = Database(store)

addrObj = Address.from_dict({
    "addr1": "Rajbagh",
    "city": "Srinagar",
    "province": "Kashmir",
    "postal_code": "190014"
})
addrObj.to_simple_address_format()
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
    "id": "t2k_001",
    "name": "Hotel Rose Petal",
    "country": "India",
    "address": [addrObj],
    "star_rating": 5,
    "latitude": "231.22",
    "longitude": "12.52",
    "phone": [phone, email]
}
)
print(obj.to_json())


# Read https://docs.sqlalchemy.org/en/14/core/dml.html#sqlalchemy.sql.expression.Insert
# Inserting record one by one
# query = insert(listings).values(listing='t2k_001', language='english')
# conn = db.engine.connect()
# conn.execute(query)
# conn.commit()
#
# results = conn.execute(select([listings])).fetchall()
# df = DataFrame(results)
# df.columns = results[0].keys()
# df.head(4)

