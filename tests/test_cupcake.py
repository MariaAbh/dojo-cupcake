import cupcake as cc

def test_return_cupcake():
    cake = cc.Cupcake()
    assert(cake.name() == "cupcake")
    assert(cake.price() == 1)

def test_return_tough_cookie():
    tough_cookie = cc.Cookie()
    assert(tough_cookie.name() == "cookie")
    assert(tough_cookie.price() == 2)

def test_chocolate():
    cake = cc.Chocolate(cc.Cupcake())
    cookie = cc.Chocolate(cc.Cookie())
    assert(cake.name() == "cupcake with chocolate")
    assert(cake.price() == 1.1)
    assert(cookie.name() == "cookie with chocolate")

def test_nuts():
    cake = cc.Nuts(cc.Cupcake())
    cookie = cc.Nuts(cc.Cookie())
    assert(cake.name() == "cupcake with nuts")
    assert(cookie.name() == "cookie with nuts")

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

