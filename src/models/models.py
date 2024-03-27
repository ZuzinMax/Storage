from sqlalchemy import Table, Column, Integer, String, MetaData, Float, ForeignKey

metadata = MetaData()

users = Table('users', metadata
              , Column('user_id', Integer, primary_key = True)
              , Column('user_name', String, nullable = False)
              , Column('password', String, nullable = False))

items = Table('items', metadata
              , Column('item_id', Integer, primary_key = True)
              , Column('item_name', String, nullable = False)
              , Column('item_weight', Float, nullable = False))

places = Table('places', metadata
                , Column('place_id', Integer, primary_key = True)
                , Column('place_name', String, nullable = False)
                , Column('max_weight', Float, nullable = False)
                , Column('remaining_weight', Float))


storage = Table('storage', metadata
                , Column('id', Integer, primary_key = True)
                , Column('id_item', Integer, ForeignKey("items.item_id"), nullable = False)
                , Column('item', String, ForeignKey("items.item_name"), nullable = False)
                , Column('weight', Float, ForeignKey("items.item_weight"),nullable = False)
                , Column('id_place', Integer, ForeignKey("places.place_id"), nullable = False)
                , Column('place', String, ForeignKey("places.place_name"),nullable = False)
                , Column('quantity', Integer, nullable = False)
                , Column('total_weight', Float))
