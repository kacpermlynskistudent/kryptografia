from stegano import lsbset
from stegano.lsbset import generators
#for small image
secret_message = "Hello World!"
secret_image = lsbset.hide("./100kb.png",secret_message,generators.eratosthenes())
secret_image.save("./100kb.png")

#for medium image

secret_message = "Ala ma kota"
secret_image = lsbset.hide("./1mb.png",secret_message,generators.eratosthenes())
secret_image.save("./1mb.png")

#for high image

secret_message = "Kryptografia"
secret_image = lsbset.hide("./10mb.png",secret_message,generators.eratosthenes())
secret_image.save("./10mb.png")
