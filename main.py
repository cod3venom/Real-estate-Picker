from Kernel.Global import ctx
from Kernel.Global import browser
from Vendors.Morizon.Morizon import Morizon


class Main:

    def start(self):
        morizon = Morizon(ctx=ctx, url='https://www.morizon.pl/oferta/wynajem-mieszkanie-warszawa-wola-46m2-mzn2038639502#')
        morizon.start()


if __name__ == "__main__":
    main = Main()
    main.start()
