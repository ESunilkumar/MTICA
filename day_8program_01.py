def kelvintofarenheit(temperature):
    assert (temperature>=0),"colder than absolute zero at mtca!"
    res=((temperature-273)*1.8)+32
    return res
try:
    print(kelvintofarenheit(-50))
except Exception as ob:
    print(ob)
try:
    print(kelvintofarenheit(273))
except Exception as ob:
    print(ob)
try:
    print(kelvintofarenheit(503))
except Exception as ob:
    print(ob)
try:
    print(kelvintofarenheit(-5))
except Exception as ob:
    print(ob)

print("thank you")
