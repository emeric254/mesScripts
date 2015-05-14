#!/usr/bin/env python
# -*- coding: utf-8 -*-

import commands, unicodedata, os, sys, getopt

nocommand = "-N/A-"

#### Test de présence des commandes shell et récupération de leur chemin ####
commandes_test = ['cat','hostname','last','hddtemp','df','ps','free','ping','grep','uniq','who','uname','sensors']
commandes = {}
for comm in commandes_test:
    (res,commande) = commands.getstatusoutput("/usr/bin/which %s" % comm)
    if res:
        print "La commande", comm, "n'est pas présente sur votre système."
	commandes[comm] = ""
    else:
        commandes[comm] = commande


def liste_hdd():
    # liste disques durs
    hdd = []
    if commandes['cat']:
        result = commands.getoutput("%s /proc/partitions" % commandes['cat']).split("\n")
        result.pop(0)
        for disque in result:
            if disque:
                disque = disque.split()[-1]
                if disque not in hdd:
                    hdd.append(disque)
    return hdd


def hdd_temp():
    # températures disque
    hdd = {}
    if commandes['hddtemp']:
        for disque in liste_hdd():
            temperature = commands.getoutput("%s -n /dev/%s" % (commandes['hddtemp'], disque))
            try:
                hdd[disque] = int(temperature)
            except:
                pass
        return hdd
    return nocommand


def hdd_usage():
    # espace disque
    hdd = {}
    if commandes['df'] and commandes['grep']:
        result = commands.getoutput("%s -P | %s -e '^/dev'" %(commandes['df'], commandes['grep']))
        for disque in result.split('\n'):
            hdd[disque.split()[0]+ '  '+str(disque.split()[5:])] = str(disque.split()[4][:-1])
        return hdd
    return nocommand


def distribution():
    # On récupère la première ligne du fichier /etc/issue qui contient généralement le nom et la version de la distribution Linux
    return open("/etc/issue", "r").readlines()[0][:-1].split("\\")[0]


def hostname():
    # On récupère le nom du système
    if commandes['hostname']:
        return commands.getoutput(commandes['hostname'])
    return nocommand


def kernel():
    # On récupère la version du noyau par la commande 'uname -r'
    if commandes['uname']:
        return commands.getoutput("%s -r" % commandes['uname'])
    return nocommand


def cpu():
    # On récupère le(s) processeur(s) installé(s) sur le serveur
    if commandes['cat'] and commandes['grep'] and commandes['uniq']:
        return commands.getoutput("%s /proc/cpuinfo | %s \"model name\" | %s" % (commandes['cat'], commandes['grep'], commandes['uniq'])).split(': ')[1]
    return nocommand


def uptime():
    # uptime
    if commandes['cat']:
        duree = float(commands.getoutput("%s /proc/uptime" % (commandes['cat'])).split()[0])
        secondes = int(duree%60)
        minutes = int(duree/60%60)
        heures = int(duree/60/60%24)
        jours = int(duree/60/60/24)
        return [duree,jours,heures,minutes,secondes]
    return nocommand


def avg_load():
    # average load
    if commandes['who']:
        return float(commands.getoutput("%s /proc/loadavg" % (commandes['cat'])).split()[0])
    return nocommand


def login_today():
    # connections aujourd'hui
    login = []
    if commandes['last'] and commandes['grep']:
        login = commands.getoutput("%s | %s \"$(LANG=C date +\"%%a %%b %%-d\")\"" % (commandes['last'], commandes['grep'])).split("\n")
        if not login:
            login = commands.getoutput("%s | %s \"$(LANG=C date +\"%%a %%b  %%-d\")\"" % (commandes['last'], commandes['grep'])).split("\n")
        return login
    return nocommand


def login_now():
    # utilisateurs connectés
    logins_connectes = []
    if commandes['who']:
        wholiste = commands.getoutput(commandes['who']).split('\n')
        for ligne in wholiste:
            if ligne:
                user = ligne.split()[0]
                if user not in logins_connectes:
                    logins_connectes.append(user)
        return logins_connectes
    return nocommand


def processus_liste():
    # liste processus
    psliste=[]
    if commandes["ps"]:
        result = commands.getoutput("%s -e" % (commandes['ps'])).split('\n')
        result.pop(0)
        for processus in result:
            if processus.split(":")[-1][3:]:
                psliste.append(processus.split(":")[-1][3:])
            else:
                psliste.append(processus)
        return psliste
    return nocommand


def ram_etat():
    # état mémoire
    ram = {}
    if commandes['cat'] and commandes['grep']:
        ram["install"] = commands.getoutput("%s /proc/meminfo | %s \"MemTotal\"" % (commandes['cat'], commandes['grep'])).split(":")[1]
    if commandes["free"]:
        result = commands.getoutput(commandes['free']).split("\n")
        memoire = result[1].split()[1:]
        #print memoire
        swap = result[3].split()[1:]
        #print swap
        return ram
    return nocommand


def ping(url):
    # ping avec le client (avg)
    if commandes["ping"]:
        return commands.getoutput("%s -c 1 %s" % (commandes['ping'], url)).split("\n")[-1].split("=")[-1].split("/")[1]
    return nocommand


def temp():
    # températures du système
    alltemp={}
    if commandes['sensors']:
        raw = commands.getoutput("%s" % commandes['sensors']).split("\n")
        for ligne in raw:
            if not ligne:
                raw.remove(ligne)
        x = 1
        for ligne in raw:
            if not x%3:
                (name, temp) = ligne.split(":")
                alltemp[name] = temp
            x +=1
        return alltemp
    return nocommand
