
# coding: utf-8

determinant = u"a synonyme etc. etc un une de du dès lors le la les des notre votre tout tous toute toutes chaque chacune chacun"
cc =  u" mais ou et donc or ni car"
cs = u" que quand comme si lorsque puisque quoique"
preposition = u" à dans par pour en vers avec sans sous sur contre" +u" chez près parmi entre loin durant pendant avant après au-dessus au-dessous grâce malgré quelqu en En on On"
prenom_relatifs = u" qui quoi dont où lequel laquelle lesquels duquel lesquelles desquels desquelles quelque quel telque quelques" 
sujets = u" je tu il elle nous vous ils elles"
cod_coi = u" me te lui en y leur moi toi eux ma ta ton mon son sa uns unes se autre autres cette cet"
pronoms = u" au ce ça cela ceci celui celle celui-ci celle-là ceux celles ceux-ci ceux-là celles-ci celles-là"+u" mien mienne tien tienne sien sienne nôtre vôtre miens miennes tiennes siens siennes nôtres vôtres leurs"
negations = u" ne pas plus jamais aucun aucune non"
LISTE_ETRE = " ".join([u'été', u'étée', u'étées', u'étés', u'étant', u'suis', u'es', u'est', 'sommes', u'êtes', 'sont', 'serai', 'seras', 
              'sera', 'serons', 'serez', 'seront', 'serais', 'serait', 'serions', 'seriez', 'seraient', u'étais', u'était', 
              u'étions', u'étiez', u'étaient','fus', 'fut', u'fûmes', u'fûtes', 'furent', 'sois', 'soit', 'soyons', 'soyez',
              'soient', 'fusse', 'fusses', u'fût', 'fussions', 'fussiez', 'fussent', u'être'])

LISTE_AVOIR = " ".join(['a','ayant', 'eu', 'eue', 'eues', 'eus', 'ai', 'as', 'avons', 'avez', 'ont', 'aurai', 'auras', 'aura', 'aurons',
               'aurez', 'auront', 'aurais', 'aurait', 'aurions', 'auriez', 'auraient', 'avais', 'avait', 'avions', 'aviez',
               'avaient', 'eut', u'eûmes', u'eûtes', 'eurent', 'aie', 'aies', 'ait', 'ayons', 'ayez', 'aient', 'eusse','eusses',
               u'eût', 'eussions', 'eussiez', 'eussent', 'avoir'])
tweet = u"quil jme qd min lyc jlui cest jai jsuis gen vium vid gro jle quon call black of dum toujour rt dun nest dune "
autres= u"oui même aux nos vos déjà bonjour alors aussi fois encore sinon "
prison = "nombreux article"

StopWordsFr = prison + tweet + autres + determinant + cc + cs + preposition + prenom_relatifs + sujets + cod_coi + pronoms + negations + LISTE_ETRE + LISTE_AVOIR

liste_ais = u"anglais frais harnais jais jamais mais marais palais rabais relais"
liste_as = u"amas bras canevas frimas gars glas judas lilas matelas repas verglas"
liste_es = u"abcès accès après cyprès décès dès excès progrès succès très"
liste_is = u"vis brebis châssis colis pis parvis ris rubis tapis torticolis"
liste_ois = u"anchois carquois fois parfois pois quelquefois toutefois"
liste_ours = u"concours cours discours recours secours toujours velours"
liste_ous = u"absous dessous dissous remous sous vous"
liste_us = u"abus confus dessus inclus intrus jus obus pus refus talus"
autres_s = u"ailleurs certes corps héros néanmoins pers plusieurs poids pouls puits remords sans temps volontiers https paris"
ListeS = liste_ais + liste_as + liste_es + liste_is + liste_ois + liste_ours + liste_ous + liste_us + autres_s




