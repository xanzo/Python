Forfatteren til den afleverede kode, kører python version 2.7.3,
og alt kode der er afleveret er skrevet heri.

Koden er skrevet på en 64bit computer, og jalle libraries er derfor hentet
spicifikt til 64 bit.

Alle libraries der er hentet, er alle hentet fra hjemmesiden
http://www.lfd.uci.edu/~gohlke/pythonlibs/
senest den 02-04-2014

De libraries jeg har hentet er:
numpy:        numpy-MKL-1.8.1-win-amd64-py2.7
http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

matplotlib:   matplotlib-1.3.1.win-amd64-py2.7
http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib

dateutil:     python-dateutil-2.2.win-amd64-py2.7
http://www.lfd.uci.edu/~gohlke/pythonlibs/#python-dateutil

pyparsing:    pyparsing-2.0.1.win-amd-py2.7
http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyparsing

six:          six-1.6.1.win-amd64-py2.7
http://www.lfd.uci.edu/~gohlke/pythonlibs/#six

Bemærk at dateutil, pyparsing og six IKKE bliver brugt direkte i koden som
numpy og matplotlib. Dette er grundet disse 3 libraries er krævet for at
matplotlib kan fungere efter hensigten i den afleverede kode.

Efter disse libraries er installeret korrekt, skulle koden meget gerne kunne
compiles uden problemer