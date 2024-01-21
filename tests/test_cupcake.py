import cupcake as cc

# SIMPLES

def test_return_cupcake():
    cake = cc.Cupcake()
    assert(cake.name() == "cupcake")
    assert(cake.price() == 1)

def test_return_tough_cookie():
    tough_cookie = cc.Cookie()
    assert(tough_cookie.name() == "cookie")
    assert(tough_cookie.price() == 2)

def test_return_pain_au_chocolat():
    poc = cc.Pain_au_chocolat()
    assert(poc.name() == "pain au chocolat")
    assert(poc.price() == 3)




# Chocolate
def test_chocolate():
    cake = cc.Chocolate(cc.Cupcake())
    cookie = cc.Chocolate(cc.Cookie())
    poc_au_chocolat = cc.Chocolate(cc.Pain_au_chocolat())
    for pastry, name, price in [
        (cake, 'cupcake', 1.1),
        (cookie, 'cookie', 2.1),
        (poc_au_chocolat, 'pain au chocolat', 3.1),
    ]:
        assert(pastry.name() == f"{name} with chocolate")
        assert(pastry.price() == price)

def test_nuts():
    cake = cc.Nuts(cc.Cupcake())
    cookie = cc.Nuts(cc.Cookie())
    poc = cc.Nuts(cc.Pain_au_chocolat())
    for pastry, name, price in [
        (cake, 'cupcake', 1.2),
        (cookie, 'cookie', 2.2),
        (poc, 'pain au chocolat', 3.2),
    ]:
        assert(pastry.name() == f"{name} with nuts")
        assert(pastry.price() == price)

def test_sugar():
    cake = cc.Sugar(cc.Cupcake())
    cookie = cc.Sugar(cc.Cookie())
    poc = cc.Sugar(cc.Pain_au_chocolat())
    for pastry, name, price in [
        (cake, 'cupcake', 1.3),
        (cookie, 'cookie', 2.3),
        (poc, 'pain au chocolat', 3.3),
    ]:
        assert(pastry.name() == f"{name} with sugar")
        assert(pastry.price() == price)

def test_chocolate_nuts():
    cake = cc.Nuts(cc.Chocolate(cc.Cupcake()))
    cookie = cc.Nuts(cc.Chocolate(cc.Cookie()))
    assert(cake.name() == "cupcake with chocolate and nuts")
    assert(cookie.name() == "cookie with chocolate and nuts")


def test_nuts_chocolate():
    cake = cc.Chocolate(cc.Nuts(cc.Cupcake()))
    cookie = cc.Chocolate(cc.Nuts(cc.Cookie()))
    assert(cake.name() == "cupcake with nuts and chocolate")
    assert(cookie.name() == "cookie with nuts and chocolate")

def test_sugar():
    cake = cc.Sugar(cc.Cupcake())
    cookie = cc.Sugar(cc.Cookie())
    assert(cake.name() == "cupcake with sugar")
    assert(cookie.name() == "cookie with sugar")

def test_pain_au_chocolat_nuts_sugar():
    poc = cc.Nuts(cc.Sugar(cc.Pain_au_chocolat()))
    assert(poc.name() == "pain au chocolat with sugar and nuts")

