from flask import Blueprint, render_template, request
from website import db
from .models.dbmodels import Cart, CartEntries

views = Blueprint('views', __name__)


top_10 = [{'item_name':'Coke', 'quantity':12,'unit':'Cans' },{'item_name':'Whole milk', 'quantity':1,'unit':'Gallon'},
          {'item_name':'Doritos', 'quantity':1,'unit':'Pack' },{'item_name':'Eggs', 'quantity':12,'unit':'Numbers'},
          {'item_name':'White bread', 'quantity':1,'unit':'Pack' },{'item_name':'Wheat bread', 'quantity':1,'unit':'Numbers'},
          {'item_name':'Hass Avocado', 'quantity':1,'unit':'Each' },{'item_name':'Banana', 'quantity':1,'unit':'Lb'},
          {'item_name':'Chicken', 'quantity':1,'unit':'Lb' },{'item_name':'Mozzarella', 'quantity':1,'unit':'Lb'}]

@views.route('/', methods=['GET', 'POST'])
def home():
    cart = Cart.query.all()
    if not cart:
        shoplist = Cart(item_name = 'Coke', quantity = 12, unit = 'Cans')
        db.session.add(shoplist)
        db.session.commit()
        shoplist = Cart(item_name = 'Whole milk', quantity = 1, unit = 'Gallon')
        db.session.add(shoplist)
        db.session.commit()
        shoplist = Cart(item_name = 'Doritos', quantity = 1, unit = 'Pack')
        db.session.add(shoplist)
        db.session.commit()
        shoplist = Cart(item_name = 'Eggs', quantity = 12, unit = 'Numbers')
        db.session.add(shoplist)
        db.session.commit()
        shoplist = Cart(item_name = 'White bread', quantity = 12, unit = 'Pack')
        db.session.add(shoplist)
        db.session.commit()
        shoplist = Cart(item_name = 'Wheat bread', quantity = 12, unit = 'Pack')
        db.session.add(shoplist)
        db.session.commit()
        shoplist = Cart(item_name = 'Hass Avocado', quantity = 1, unit = 'Each')
        db.session.add(shoplist)
        db.session.commit()
        shoplist = Cart(item_name = 'Banana', quantity = 1, unit = 'Lb')
        db.session.add(shoplist)
        db.session.commit()
        shoplist = Cart(item_name = 'Chicken', quantity = 1, unit = 'Lb')
        db.session.add(shoplist)
        db.session.commit()
        shoplist = Cart(item_name = 'Mozzarella', quantity = 1, unit = 'Lb')
        db.session.add(shoplist)
        db.session.commit()
    return render_template("index.html")


@views.route('/shoppingcart',methods=['GET', 'POST'])
def shoppingcart():
    if request.method == 'POST':
        location = request.form.get('location')
        storename = request.form.get('storename')
        coke = request.form.get('coke')
        milk = request.form.get('milk')
        chips = request.form.get('chips')
        eggs = request.form.get('eggs')
        wbread = request.form.get('wbread')
        whbread = request.form.get('whbread')
        avo = request.form.get('avo')
        banana = request.form.get('banana')
        meat = request.form.get('meat')
        cheese = request.form.get('cheese')
        if coke:
            coke_price = float(coke)
            cartlist = CartEntries(location = location, store_name = storename, price = coke_price, sl_item = 1 )
            db.session.add(cartlist)
            db.session.commit()
        if milk:
            milk_price = float(milk)
            cartlist = CartEntries(location = location, store_name = storename, price = milk_price, sl_item = 2 )
            db.session.add(cartlist)
            db.session.commit()
        if chips:
            chips_price = float(chips)
            cartlist = CartEntries(location = location, store_name = storename, price = chips_price, sl_item = 3 )
            db.session.add(cartlist)
            db.session.commit()
        if eggs:
            eggs_price = float(eggs)
            cartlist = CartEntries(location = location, store_name = storename, price = eggs_price, sl_item = 4 )
            db.session.add(cartlist)
            db.session.commit()
        if wbread:
            wbread_price = float(wbread)
            cartlist = CartEntries(location = location, store_name = storename, price = wbread_price, sl_item = 5 )
            db.session.add(cartlist)
            db.session.commit()
        if whbread:
            whbread_price = float(whbread)
            cartlist = CartEntries(location = location, store_name = storename, price = whbread_price, sl_item = 6 )
            db.session.add(cartlist)
            db.session.commit()
        if avo:
            avo_price = float(avo)
            cartlist = CartEntries(location = location, store_name = storename, price = avo_price, sl_item = 7 )
            db.session.add(cartlist)
            db.session.commit()
        if banana:
            banana_price = float(banana)
            cartlist = CartEntries(location = location, store_name = storename, price = banana_price, sl_item = 8 )
            db.session.add(cartlist)
            db.session.commit()
        if meat:
            meat_price = float(meat)
            cartlist = CartEntries(location = location, store_name = storename, price = meat_price, sl_item = 9 )
            db.session.add(cartlist)
            db.session.commit()
        if cheese:
            cheese_price = float(cheese)
            cartlist = CartEntries(location = location, store_name = storename, price = cheese_price, sl_item = 10 )
            db.session.add(cartlist)
            db.session.commit()
    return render_template('shoppingcart.html') 

@views.route('/dashboard',methods=['GET', 'POST'])
def dashboard():
            query = '''SELECT c.item_name as Item_Name, REPLACE(ce.store_name,'_' , ' ') as Store_Name, MIN(ce.price) as Minimum_Price,  strftime('%d-%m-%Y', ce.[date]) as Date 
            FROM cart_entries as ce
            JOIN cart as c
            ON c.id = ce.sl_item
            GROUP BY c.item_name, ce.store_name, ce.[date]
            ORDER BY ce.[date] , c.id
                '''
            cartentries = db.engine.execute(query)
            return render_template('dashboard.html', cartentries=cartentries) 
