import cupcake as cc

def assert_float_equal(a, b):
    err = (.2 + .1) - .3
    assert(abs(a-b) < 10*err)

# SIMPLES

def test_return_cupcake():
    cake = cc.Cupcake()
    assert(cake.name() == "cupcake")
    assert_float_equal(cake.price(), 1)

def test_return_tough_cookie():
    tough_cookie = cc.Cookie()
    assert(tough_cookie.name() == "cookie")
    assert_float_equal(tough_cookie.price(), 2)

def test_return_pain_au_chocolat():
    poc = cc.Pain_au_chocolat()
    assert(poc.name() == "pain au chocolat")
    assert_float_equal(poc.price(), 3)


# Single Topping
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
        assert_float_equal(pastry.price(), price)

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
        assert_float_equal(pastry.price(), price)

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
        assert_float_equal(pastry.price(), price)

# two toppings
def test_chocolate_nuts():
    for pastry_cls, name, price in [
        (cc.Cupcake, 'cupcake', 1.3),
        (cc.Cookie, 'cookie', 2.3),
        (cc.Pain_au_chocolat, 'pain au chocolat', 3.3),
    ]:
        pastry = cc.Nuts(cc.Chocolate(pastry_cls()))
        assert(pastry.name() == f"{name} with chocolate and nuts")
        assert_float_equal(pastry.price(), price)

        pastry = cc.Chocolate(cc.Nuts(pastry_cls()))
        assert(pastry.name() == f"{name} with nuts and chocolate")
        assert_float_equal(pastry.price(), price)

def test_chocolate_sugar():
    for pastry_cls, name, price in [
        (cc.Cupcake, 'cupcake', 1.4),
        (cc.Cookie, 'cookie', 2.4),
        (cc.Pain_au_chocolat, 'pain au chocolat', 3.4),
    ]:
        pastry = cc.Sugar(cc.Chocolate(pastry_cls()))
        assert(pastry.name() == f"{name} with chocolate and sugar")
        assert_float_equal(pastry.price(), price)

        pastry = cc.Chocolate(cc.Sugar(pastry_cls()))
        assert(pastry.name() == f"{name} with sugar and chocolate")
        assert_float_equal(pastry.price(), price)

def test_nuts_sugar():
    for pastry_cls, name, price in [
        (cc.Cupcake, 'cupcake', 1.5),
        (cc.Cookie, 'cookie', 2.5),
        (cc.Pain_au_chocolat, 'pain au chocolat', 3.5),
    ]:
        pastry = cc.Sugar(cc.Nuts(pastry_cls()))
        assert(pastry.name() == f"{name} with nuts and sugar")
        assert_float_equal(pastry.price(), price)

        pastry = cc.Nuts(cc.Sugar(pastry_cls()))
        assert(pastry.name() == f"{name} with sugar and nuts")
        assert_float_equal(pastry.price(), price)

# three toppings
def test_chocolate_nuts_sugar():
    for pastry_cls, name, price in [
        (cc.Cupcake, 'cupcake', 1.6),
        (cc.Cookie, 'cookie', 2.6),
        (cc.Pain_au_chocolat, 'pain au chocolat', 3.6),
    ]:
        pastry = cc.Chocolate(cc.Sugar(cc.Nuts(pastry_cls())))
        assert(pastry.name() == f"{name} with nuts and sugar and chocolate")
        assert_float_equal(pastry.price(), price)

        pastry = cc.Chocolate(cc.Nuts(cc.Sugar(pastry_cls())))
        assert(pastry.name() == f"{name} with sugar and nuts and chocolate")
        assert_float_equal(pastry.price(), price)

        pastry = cc.Nuts(cc.Sugar(cc.Chocolate(pastry_cls())))
        assert(pastry.name() == f"{name} with chocolate and sugar and nuts")
        assert_float_equal(pastry.price(), price)

        pastry = cc.Nuts(cc.Chocolate(cc.Sugar(pastry_cls())))
        assert(pastry.name() == f"{name} with sugar and chocolate and nuts")
        assert_float_equal(pastry.price(), price)

        pastry = cc.Sugar(cc.Nuts(cc.Chocolate(pastry_cls())))
        assert(pastry.name() == f"{name} with chocolate and nuts and sugar")
        assert_float_equal(pastry.price(), price)

        pastry = cc.Sugar(cc.Chocolate(cc.Nuts(pastry_cls())))
        assert(pastry.name() == f"{name} with nuts and chocolate and sugar")
        assert_float_equal(pastry.price(), price)

def test_pain_au_chocolat_nuts_sugar():
    poc = cc.Nuts(cc.Sugar(cc.Pain_au_chocolat()))
    assert(poc.name() == "pain au chocolat with sugar and nuts")

