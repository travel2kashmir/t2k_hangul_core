from __future__ import annotations

from ...core import Listings
from ...core import Listing
from ...core import Address
from ...core import Contact
from ...core import Review

from dataclasses import dataclass
from dataclasses import field

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, Float
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship

mapper_registry = registry()


# database from the hangul_core library
@dataclass
class ListingsTable(Listings):
    _active: bool = True
    id: int = field(init=False)


@dataclass
class ListingTable(Listing):
    _active: bool = True
    id: int = field(init=False)


@dataclass
class AddressTable(Address):
    _active: bool = True
    id: int = field(init=False)


@dataclass
class ReviewTable(Review):
    _active: bool = True
    id: int = field(init=False)


@dataclass
class ContactTable(Contact):
    _active: bool = True
    id: int = field(init=False)


# Database Structure
metadata_obj = MetaData()


# Table Listings
tbl_listings = Table(
    'listings',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('listing', String(50)),
    Column('language', String(50))
)

# Table Listing
tbl_listing = Table(
    'listing',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('property_id', Integer, ForeignKey('listings.id')),
    Column('property_name', String(50)),
    Column('property_country', String(50)),
    Column('star_rating', Integer),
    Column('property_latitude', Float),
    Column('property_longitude', Float),
    Column('property_phone', String(50)),
    Column('property_category', String(50)),
    Column('property_phone', String(50)),
    Column('property_brand', String(50)),
    Column('property_location_precision', String(50)),
    Column('property_established_year', String(50)),
    Column('property_description_title', String(50)),
    Column('property_description_body', String(50)),
    Column('property_description_date', String(50)),
)

mapper_registry.map_imperatively(ListingsTable, tbl_listings, properties={
    'listings': relationship(ListingTable, backref='listings', order_by=tbl_listing.c.id),
})

mapper_registry.map_imperatively(ListingTable, tbl_listing)

#
# # Table Address
# tbl_address = Table(
#     'address',
#     metadata_obj,
#     Column('id', Integer, primary_key=True),
#     Column('address_id', Integer, ForeignKey('listing.property_id')),
#     Column('property_addr1', String(50)),
#     Column('property_addr2', String(50)),
#     Column('property_addr3', String(50)),
#     Column('property_province', String(50)),
#     Column('property_street_address', String(50)),
#     Column('property_landmark', String(50)),
#     Column('property_postal_code', Integer),
# )
#
# mapper_registry.map_imperatively(ListingTable, tbl_listing, properties={
#     'property_address': relationship(AddressTable, backref='listing', order_by=tbl_address.c.id),
# })
#
# mapper_registry.map_imperatively(AddressTable, tbl_address)
