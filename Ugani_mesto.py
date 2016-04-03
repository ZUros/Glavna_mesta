print"UGANI GLAVNO MESTO DRZAVE"

from seznam_glavnih_mest import glavna_mesta
import random


def kviz(glavna_mesta):
    pogoj = True
    primer = 0

    while pogoj:

        if primer == 0:
            drzava = random.choice(glavna_mesta.keys())
            glavno_mesto = glavna_mesta[drzava]
            glavno_mesto = glavno_mesto.lower()

        Vnos_igralca = raw_input('Vpisi glavno mesto {}: '.format(drzava)).lower()

        if Vnos_igralca == glavno_mesto:
            print 'Vas odgovor je pravilen.'
            po_pravilnem_odgovoru = raw_input('Ali zelite nadaljevati (da/ne): ')
            if po_pravilnem_odgovoru == 'da':
                kviz(glavna_mesta)
            else:
                print 'Nasvidenje!'
            break


        else:
            primer = 0
            print 'Pravilen odgovor je: {}'.format(glavno_mesto)
            continue


kviz(glavna_mesta)
