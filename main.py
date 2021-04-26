from DataOperations.DATE import DATE
from Kernel.Global import ctx
from Kernel.Global import browser
from Vendors.Gumtree.Gumtree import Gumtree
from Vendors.Morizon.Morizon import Morizon


class Main:

    def start(self):
        morizon = Morizon(ctx=ctx, url='https://www.morizon.pl/oferta/wynajem-mieszkanie-warszawa-wola-46m2-mzn2038639502#')
        morizon.start()
        # gumtree = Gumtree(ctx=ctx, url='https://www.gumtree.pl/a-mieszkania-i-domy-do-wynajecia/mokotow/2-osobne-pokoje-52m2-ul-pulawska-metro-sluzew/1009249580930912413740009')
        # gumtree.start()

if __name__ == "__main__":
    main = Main()
    main.start()
