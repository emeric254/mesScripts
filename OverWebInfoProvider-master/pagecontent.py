#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Sensors

def corps(ipadress):
    # creation de la page

    page = '<head>\n'
    page += '<title>W. I. P.</title>\n'
    page += '<meta http-equiv="content-type" content="text/html;charset=utf-8" />\n'
    page += '<meta name="application-name" content="W. I. P.">\n'
    page += '<link rel="shortcut icon" type="image/x-icon" href="./images/favicon.ico" />\n'
    page += '<link rel="stylesheet" type="text/css" href="style.css" />\n'
    page += '</head>\n'

    page += '<body>\n'
    page += '<h1>Web Information Provider</h1>\n'
    page += '<div id="general">\n'
    page += '<h2>Informations Générales</h2>\n'
    page += '<div id="os"><b>Distribution :</b> %s</div>\n' % Sensors.distribution()
    page += '<div id="name"><b>Nom du système :</b> %s</div>\n' % Sensors.hostname()
    page += '<div id="kernel"><b>Noyau :</b> %s</div>\n' % Sensors.kernel()
    page += '<div id="cpu"><b>Processeur :</b> %s</div>\n' % Sensors.cpu()
    page += '<div id="ram"><b>Mémoire installée :</b> %s</div>\n' % Sensors.ram_etat()["install"]
    page += '<div id="uptime"><b>Uptime :</b> %sj %sh %sm %ss</div>\n' % (Sensors.uptime()[1],Sensors.uptime()[2],Sensors.uptime()[3],Sensors.uptime()[4])
    page += '<div id="avg-load"><b>Charge du système :</b> %s</div>\n' % Sensors.avg_load()
    page += '<div id="ipadress"><b>Votre adresse IP :</b> %s</div>\n' % ipadress
    page += '<div id="ping"><b>Ping :</b> %s ms</div>\n' % Sensors.ping(ipadress)
    page += '</div>\n'

    page += '<div id="advanced">\n'
    page += '<h2>Informations Complémentaires</h2>\n'

    page += '<div id="ram"><b>État mémoire :</b><ul>'
    page += '</ul></div>\n'

    page += '<div id="hdd-use"><b>Usage des disques :</b><ul>'
    hdd_df = Sensors.hdd_usage()
    for hdd in hdd_df:
        page += "<li><b> %s :</b> %s&#37;</li>" % (hdd, hdd_df[hdd])
    page += '</ul></div>\n'

    page += '<div id="hdd-temp"><b>Températures disques durs :</b><ul>'
    hdd_heat = Sensors.hdd_temp()
    if hdd_heat != "-N/A-":
        for hdd in hdd_heat:
            page += "<li><b> %s :</b> %s</li>" % (hdd, hdd_heat[hdd])
        page += '</ul></div>\n'

    page += '<div id="temp"><b>Températures :</b><ul>'
    sensors = Sensors.temp()
    for sensor in sensors:
        page += "<li><b> %s :</b> %s</li>" % (sensor, sensors[sensor])
    page += '</ul></div>\n'

    page += '<div id="activ-connect"><b>Connections actives :</b><ul>'
    for user in Sensors.login_now():
        page += "<li>%s</li>" % user
    page += '</ul></div>\n'

    page += '<div id="today-connect"><b>Connections aujourd\'hui :</b><ul>'
    for user in Sensors.login_today():
        page += "<li>%s</li>" % user
    page += '</ul></div>\n'

    page += '<div id="processus"><b>Processus en cours d\'éxecution:</b><ul>'
    for processus in Sensors.processus_liste():
        page += "<li>%s</li>" % processus
    page += '</ul></div>\n'
    page += '</div>\n'

    page += '<div id="footer">\n'
    page += '<p>Blabla ...</p>\n'
    page += '</div>\n'

    page += '</body>\n'
    return page
