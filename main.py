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

        # otodom = Otodom(ctx=ctx, url='https://www.otodom.pl/pl/oferta/dwupokojowe-mieszkanie-na-zoliborzu-artystycznym-ID4bd17.html')
        # otodom.start()

        links = [
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-trzypokojowe-warszawa-srodmiescie-krzywe-kolo-42m2/152720291",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-dwupokojowe-warszawa-praga-poludnie-marii-rodziewiczowny-50m2/152492572",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-kawalerke-warszawa-srodmiescie-noakowskiego-31m2/152759024",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-trzypokojowe-warszawa-bemowo-apeninska-76m2/152555702",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-czteropokojowe-warszawa-srodmiescie-gornoslaska-110m2/151840442",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-trzypokojowe-warszawa-bemowo-szczotkarska-56m2/152501368",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-trzypokojowe-warszawa-bialoleka-odkryta-64m2/152475850",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-trzypokojowe-warszawa-ursynow-polinezyjska-69m2/152761309",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-kawalerke-warszawa-zoliborz-wojska-polskiego-al-19m2/152716419",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-warszawa-ursynow-farbiarska-90m2/152716814",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-dwupokojowe-warszawa-mokotow-fort-pilsudskiego-64m2/152686104",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-trzypokojowe-warszawa-mokotow-100m2/152686103",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-czteropokojowe-warszawa-mokotow-piaseczynska-120m2/152459968",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-czteropokojowe-warszawa-mokotow-komputerowa-119m2/152117262",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-warszawa-mokotow-al-wyscigowa-84m2/152736422",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-czteropokojowe-warszawa-mokotow-jasminowa-104m2/152728116",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-trzypokojowe-warszawa-zoliborz-jasnodworska-67m2/152694198",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-czteropokojowe-warszawa-mokotow-wielicka-127m2/152582590",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-trzypokojowe-warszawa-mokotow-bobrowiecka-88m2/152559110",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-kawalerke-warszawa-wola-kolejowa-35m2/152536925",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-dwupokojowe-warszawa-wola-grzybowska-32m2/152531638",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-warszawa-mokotow-143m2/152517226",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-trzypokojowe-warszawa-wilanow-ksiedza-prymasa-augusta-hlonda-67m2/152512465",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-trzypokojowe-warszawa-srodmiescie-dobra-75m2/152482283",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-dwupokojowe-warszawa-praga-poludnie-zwyciezcow-51m2/152473465",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-warszawa-srodmiescie-grzybowska-157m2/152325516",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-trzypokojowe-warszawa-mokotow-czerniakowska-58m2/152322041",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-trzypokojowe-warszawa-wilanow-al-rzeczypospolitej-104m2/152307304",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-trzypokojowe-warszawa-mokotow-sielecka-98m2/152054212",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-dwupokojowe-warszawa-wilanow-bruzdowa-70m2/152011561",
            "https://www.domiporta.pl/nowe/ogloszenie/minska_69_warszawa-praga_poludnie_600202",
            "https://www.domiporta.pl/nowe/ogloszenie/minska_69_warszawa-praga_poludnie_600216",
            "https://www.domiporta.pl/nowe/ogloszenie/minska_69_warszawa-praga_poludnie_600212",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-trzypokojowe-warszawa-ochota-szczesliwice-dobosza-63m2/151476933",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-dwupokojowe-warszawa-srodmiescie-muranow-ciasna-33m2/151476932",
            "https://www.domiporta.pl/nieruchomosci/sprzedam-mieszkanie-dwupokojowe-warszawa-targowek-brodno-ludwika-kondratowicza-38m2/151467594",
        ]
        for link in links:
            domiportal = DomiPortal(ctx=ctx, url=link)
            domiportal.start()



if __name__ == "__main__":
    main = Main()
    main.start()
