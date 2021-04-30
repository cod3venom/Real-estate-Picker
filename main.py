from Kernel.Bootloader.Loader import Loader
from Kernel.Global import ctx
import sys


class Main:

    def start(self):
        boot_loader = Loader(ctx=ctx, ipAddress=sys.argv[1], port=sys.argv[2])
        boot_loader.load()


if __name__ == "__main__":
    main = Main()
    main.start()
