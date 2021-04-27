from DataOperations.DATE import DATE
from Kernel.Global import ctx
from Kernel.Global import browser
from Vendors.DomiPortal.DomiPortal import DomiPortal
from Vendors.Domy.Domy import Domy
from Vendors.Gratka.Gratka import Gratka
from Vendors.Gumtree.Gumtree import Gumtree
from Vendors.Morizon.Morizon import Morizon
from Vendors.Olx.Olx import Olx
from Vendors.Otodom.Otodom import Otodom


class Main:

    def start(self):
        # morizon = Morizon(ctx=ctx, url='https://www.morizon.pl/oferta/wynajem-mieszkanie-warszawa-wola-46m2-mzn2038639502#')
        # morizon.start()
        # gumtree = Gumtree(ctx=ctx, url='https://www.gumtree.pl/a-mieszkania-i-domy-do-wynajecia/mokotow/2-osobne-pokoje-52m2-ul-pulawska-metro-sluzew/1009249580930912413740009')
        # gumtree.start()
        # olx = Olx(ctx=ctx, url='https://www.olx.pl/d/oferta/2-pokoje-42m-ulica-lwowska-kamienica-wysoki-standard-CID3-IDJBb1q.html?isPreviewActive=0&sliderIndex=3')
        # olx.start()
        # gratka = Gratka(ctx=ctx, url='https://gratka.pl/nieruchomosci/nowe-mieszkanie-warszawa-wlochy-ul-pola-karolinskie-2/ob/16975545')
        # gratka.start()
        # domy = Domy(ctx=ctx, url='https://domy.pl/mieszkanie/warszawa-wola-karolkowa-2-pokoje-2500-pln-34m2-wfb/dol1735626885   ')
        # domy.start()
        # domiPortal = DomiPortal(ctx=ctx, url='https://www.domiporta.pl/nieruchomosci/wynajme-mieszkanie-dwupokojowe-warszawa-mokotow-etiudy-rewolucyjnej-39m2/152764390')
        # domiPortal.start()

        otodom = Otodom(ctx=ctx, url='https://www.otodom.pl/pl/oferta/dwupokojowe-mieszkanie-na-zoliborzu-artystycznym-ID4bd17.html')
        otodom.start()

        # links = [
        #     "https://domy.pl/mieszkanie/warszawa-wola-2-pokoje-3000-pln-60m2-wba/dol1735293161",
        #     "https://domy.pl/mieszkanie/warszawa-wola-gieldowa-2-pokoje-2400-pln-45m2-wba/dol1735566616",
        #     "https://domy.pl/mieszkanie/warszawa-wola-4-pokoje-2188000-pln-118m2-sba/dol1735538750",
        #     "https://domy.pl/mieszkanie/warszawa-wola-brylowska-3-pokoje-870000-pln-58m2-sba/dol1735099537"
        # ]
        # for link in links:
        #     domy = Domy(ctx=ctx, url=link)
        #     domy.start()



if __name__ == "__main__":
    main = Main()
    main.start()
