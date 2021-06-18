import sys

from Kernel.Bootloader.ArgParser import ArgParser
from Kernel.Config.Logo import Logo
from Kernel.Global import ctx


class Main:

    def start(self):
        try:
            Logo()
            arg_parser = ArgParser()
        except KeyboardInterrupt:
            ctx.Logger.Print(10, ctx.LogLevel.Info)
            sys.exit(0)



if __name__ == "__main__":

    main = Main()
    main.start()
