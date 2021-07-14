from __future__ import annotations
from typing import List

import os
import urlAvasDemon
import urlBladeBunny
import urlCAD
import urlEarthsong
import urlFinder
import urlLFG
import urlQ2Q
import urlRoomie
import urlTwoKinds
import urlWebToons
from htmlCreator import buildMainPage

os.makedirs('webcomic', exist_ok=True)

visible: List[str]
comics: List[str]
files: List[str]
pages: List[str]
nextTag = []
nextAttr = []
nextStr = []
urlBase = []


class Webcomic:
    def __init__(self, name, file, page_count, visibility):
        self.name = name
        self.file = file
        self.pages = page_count
        self.visible = visibility


comic_list = []

# XKCD
display = True
comic_name = "XKCD"
filename = "xkcd"
urlMain = "http://www.xkcd.com/"
urlFirstPage = "http://xkcd.com/1/"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
urlBase.append('http://xkcd.com')
nextLinkParent = False
search_end = '#'
total_pages = urlFinder.urlBuild(
    urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent, search_end)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Ava's Demon
display = True
comic_name = "Ava's Demon"
filename = "avasDemon"
urlMain = "http://www.AvasDemon.com"
urlFirstPage = "http://www.AvasDemon.com/pages.php#0001"
total_pages = urlAvasDemon.urlBuild(urlFirstPage, filename, urlMain)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))

# Blade Bunny
# webpage doesn't like to reload...need to fix that, possibly run like webtoons?
display = True
comic_name = "Blade Bunny"
filename = "bladeBunny"
urlMain = "https://readcomiconline.to/Comic/Blade-Bunny"
urlFirstPage = "https://readcomiconline.to/Comic/Blade-Bunny/Issue-1?id=42534"
urlVol1End = "https://readcomiconline.to/Comic/Blade-Bunny/Issue-5?id=87724#29"
urlVol2 = "https://readcomiconline.to/Comic/Blade-Bunny-Vol-2/Issue-1?id=94715"
total_pages = urlBladeBunny.urlBuild(urlFirstPage, filename, urlMain, urlVol1End, urlVol2)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))

# Balazo
display = True
comic_name = "Balazo - Stories in Pretty Pictures"
filename = "balazo"
urlMain = "http://balazo.net/"
urlFirstPage = "http://balazo.net/2010/08/starting-tomorrow/"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# The Bully's Bully
display = True
comic_name = "The Bully's Bully"
filename = "bullysBully"
urlMain = "https://web.archive.org/web/20160904004355/http://bullysbully.com:80/"
urlFirstPage = (
    "https://web.archive.org/web/20160902045430/http://bullysbully.com/comic/chapter-1/the-bullys-bully-cover-2/")
nextTag.append("a")
nextAttr.append("class")
nextStr.append("comic-nav-base comic-nav-next")
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Subnormality
display = True
comic_name = "Subnormality"
filename = "subnormality"
urlMain = "http://www.viruscomix.com/subnormality.html"
urlFirstPage = "http://www.viruscomix.com/page324.html"
# search 1
nextTag.append("img")
nextAttr.append("src")
nextStr.append('subnext.*')
# search 2
nextTag.append("img")
nextAttr.append("src")
nextStr.append("nextIIC.gif")
urlBase.append('http://www.viruscomix.com/')
nextLinkParent = True
search_end = 'subnormality.html'
total_pages = urlFinder.urlBuild(
    urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent, search_end)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]


# Will need something like Avas Demon for this (completely jQuery-button events for next page)
# Carciphona
display = False
comic_name = "Carciphona"
filename = "carciphona"
# urlMain = "https://carciphona.com/"
# urlFirstPage = "https://carciphona.com/read.php#volume=1&chapter=1&page=-1&lang=en"
# nextTag.append("a")
# nextAttr.append("class")
# nextStr.append("comic-nav-base comic-nav-next")
# nextLinkParent = False
# total_pages = urlFinder.urlBuild(
#     urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
total_pages = 0
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Ctrl+Alt+Del
display = True
comic_name = "Ctrl+Alt+Del"
filename = "CADcomic"
# urlMain = "http://cad-comic.com/"
urlFirstPage = "http://cad-comic.com/comic/nice-melon/"
total_pages = urlCAD.urlBuild(urlFirstPage, filename)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))

# D20 Monkey
display = True
comic_name = "d20 Monkey"
filename = "d20"
urlMain = "http://www.d20monkey.com/"
urlFirstPage = "http://www.d20monkey.com/comic/welcome/"
nextTag.append("a")
nextAttr.append("class")
nextStr.append("navi comic-nav-next navi-next")
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Devilbear
display = True
comic_name = "Devilbear: The Grimoires of Bearalzebub"
filename = "Devilbear"
urlMain = "http://www.thedevilbear.com/index.html"
urlFirstPage = "http://www.thedevilbear.com/comics.php?p=1"
nextTag.append("a")
nextAttr.append("id")
nextStr.append('cg_next')
nextLinkParent = False
urlBase.append('http://www.thedevilbear.com/comics.php')
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Devilbear Shorts
display = True
comic_name = "Devilbear: The Shorts of Bearalzebub"
filename = "DevilbearShorts"
urlMain = "http://www.thedevilbear.com/"
urlFirstPage = "http://www.thedevilbear.com/b/comic/its-for-you/"
nextTag.append("a")
nextAttr.append("class_")
nextStr.append('comic-nav-base comic-nav-next')
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Depths of my Empty Soul
display = True
comic_name = "Depths Of My Empty Soul (Mature)"
filename = "Depths"
urlMain = "https://www.theduckwebcomics.com/Depths_of_My_Empty_Soul/"
urlFirstPage = "https://www.theduckwebcomics.com/Depths_of_My_Empty_Soul/5242309/"
nextTag.append("img")
nextAttr.append("class_")
nextStr.append('arrow_next')
urlBase.append('https://www.theduckwebcomics.com')
nextLinkParent = True
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Dreamscar
display = True
comic_name = "dream*scar"
filename = "dreamscar"
urlMain = "https://dream-scar.net/"
urlFirstPage = "https://dream-scar.net/?id=1"
nextTag.append("a")
nextAttr.append("title")
nextStr.append("next")
urlBase.append("https://dream-scar.net/")
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Druids
display = True
comic_name = "Druids (Mature)"
filename = "Druids"
urlMain = "http://druids.thecomicseries.com/"
urlFirstPage = "http://druids.thecomicseries.com/comics/first/"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append('next')
urlBase.append('http://druids.thecomicseries.com')
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Earthsong
display = True
comic_name = "Earthsong"
filename = "earthsong"
# urlMain = "http://earthsongsaga.com/index.php"
urlFirstPage = "http://earthsongsaga.com/vol1/vol1cover.php"
nextTag.append("li")
nextAttr.append("id")
nextStr.append("next")
nextTag.append("td")
nextAttr.append("width")
nextStr.append("71")
total_pages = urlEarthsong.urlBuild(urlFirstPage, filename, nextTag, nextAttr, nextStr)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Everblue
display = True
comic_name = "Everblue"
filename = "everblue"
urlMain = "http://www.everblue-comic.com/"
urlFirstPage = "http://www.everblue-comic.com/comic/1"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
urlBase.append("http://www.everblue-comic.com")
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Furthia High
display = True
comic_name = "Furthia High"
filename = "furthia"
urlMain = "http://furthiahigh.concessioncomic.com/"
urlFirstPage = "http://furthiahigh.concessioncomic.com/index.php?pid=20080128"
nextTag.append("img")
nextAttr.append("alt")
nextStr.append("Next")
nextLinkParent = True
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Greg
display = True
comic_name = "Greg"
filename = "Greg"
urlMain = "https://www.theduckwebcomics.com/Greg/"
urlFirstPage = "https://www.theduckwebcomics.com/Greg/5491003/"
nextTag.append("img")
nextAttr.append("src")
nextStr.append('next.png')
urlBase.append('https://www.theduckwebcomics.com')
nextLinkParent = True
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# HalfLight
display = True
comic_name = "HalfLight"
filename = "halflight"
urlMain = "http://halflightcomics.com/"
urlFirstPage = "http://halflightcomics.com/http:/halflightcomics.com/comic/chapter-1"
nextTag.append("a")
nextAttr.append("class")
nextStr.append('navi navi-next')
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Miamaska
display = True
comic_name = "Miamaska"
filename = "miamaska"
urlMain = "http://miamaska.com/index.php"
urlFirstPage = "http://miamaska.com/index.php?pn=0"
nextTag.append("a")
nextAttr.append("text")
nextStr.append('Next')
urlBase.append('http://miamaska.com/index.php')
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Misfile
display = True
comic_name = "Misfile"
filename = "misfile"
urlMain = "http://www.misfile.com/"
urlFirstPage = "http://www.misfile.com/?date=2004-02-22"
nextTag.append("img")
nextAttr.append("alt")
nextStr.append("Next Comic")
urlBase.append("http://www.misfile.com")
nextLinkParent = True
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Modest Medusa
display = True
comic_name = "Modest Medusa"
filename = "medusa"
urlMain = "http://modestmedusa.com/"
urlFirstPage = "http://modestmedusa.com/comic/christmas-eve-3/"
nextTag.append("a")
nextAttr.append("class")
nextStr.append("comic-nav-base comic-nav-next")
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Next Town Over
display = True
comic_name = "Next Town Over"
filename = "nexttown"
urlMain = "http://www.nexttownover.net/"
urlFirstPage = "http://www.nexttownover.net/?p=4"
nextTag.append("a")
nextAttr.append("class")
nextStr.append("navi navi-next")
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Questionable Content
display = True
comic_name = "Questionable Content"
filename = "questionable"
urlMain = "https://www.questionablecontent.net/"
urlFirstPage = "https://www.questionablecontent.net/view.php?comic=1"
nextTag.append("a")
nextAttr.append("text")
nextStr.append('Next')
urlBase.append('https://www.questionablecontent.net/')
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Red Moon Rising
display = True
comic_name = "Red Moon Rising"
filename = "redmoon"
urlMain = "http://www.redmoonrising.org/"
urlFirstPage = "http://www.redmoonrising.org/archive/red-moon-rising/"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Scout Crossing
display = True
comic_name = "Scout Crossing"
filename = "scout"
urlMain = "http://scoutcrossing.net/"
urlFirstPage = "http://scoutcrossing.net/comic/000-scoutcrossing/"
nextTag.append("a")
nextAttr.append("class")
nextStr.append("navi navi-next")
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Spinnerette
display = True
comic_name = "Spinnerette"
filename = "spinnerette"
urlMain = "https://www.spinnyverse.com/"
urlFirstPage = "https://www.spinnyverse.com/comic/02-09-2010"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Think before you Think
display = True
comic_name = "Think Before You Think"
filename = "think"
urlMain = "http://thinkbeforeyouthink.net/"
urlFirstPage = "http://thinkbeforeyouthink.net/?comic=20090612-coffee"
nextTag.append("a")
nextAttr.append("text")
nextStr.append('Next >')
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Toilet Genie
display = True
comic_name = "Toilet Genie"
filename = "toilet"
urlMain = "https://www.deviantart.com/blix-it/gallery/9792599/toilet-genie"
urlFirstPage = "https://www.deviantart.com/blix-it/art/D-0-0-R-Toilet-Genie-001-118248100"
nextTag.append("a")
nextAttr.append("text")
nextStr.append('Next')
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Two Guys and Guy
display = True
comic_name = "Two Guys and Guy"
filename = "twoguys"
urlMain = "http://www.twogag.com/"
urlFirstPage = "http://twogag.com/archives/4"
nextTag.append("a")  # use a, rel "next" if this doesn't work
nextAttr.append("class")
nextStr.append("cc-next")
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# TwoKinds
display = True
comic_name = "TwoKinds"
filename = "TwoKinds"
# urlMain = "http://twokinds.keenspot.com/"
urlFirstPage = "http://twokinds.keenspot.com/comic/1/"
total_pages = urlTwoKinds.urlBuild(urlFirstPage, filename)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))

# Looking for Group
display = True
comic_name = "Looking for Group"
filename = "LFG"
# urlMain = ""
urlFirstPage = 'https://www.lfg.co/page/1/'
total_pages = urlLFG.urlBuild(urlFirstPage, filename)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))

# Q2Q
display = True
comic_name = "Q2Q"
filename = "q2qcomic"
# urlMain = "https://q2qcomics.com/"
urlFirstPage = 'https://q2qcomics.com/comic/q2q1/'
total_pages = urlQ2Q.urlBuild(urlFirstPage, filename)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))

# Go Get a Roomie
# Can be used with an extension that makes browser ignore X-Frame options EX: Ignore X-Frame-Options for Firefox
display = True
comic_name = "Go Get a Roomie! (Mature) (Requires X-Frame option extension)"
filename = "roomie"
urlMain = "http://www.gogetaroomie.com/"
urlFirstPage = 'http://www.gogetaroomie.com/comic/and-so-it-begins'
total_pages = urlRoomie.urlBuild(urlFirstPage, filename, urlMain)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))

# Sandra and Woo
display = True
comic_name = "Sandra and Woo"
filename = "sandra"
urlMain = "http://www.sandraandwoo.com/"
urlFirstPage = "http://www.sandraandwoo.com/2000/01/01/welcome-to-sandra-and-woo/"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# A Redtail's Dream
display = True
comic_name = "A Redtail's Dream"
filename = "redtail"
urlMain = "http://www.minnasundberg.fi/comic/recent.php"
urlFirstPage = "http://www.minnasundberg.fi/comic/page00.php"
nextTag.append("img")
nextAttr.append("src")
nextStr.append(".*anext[.]jpg")
urlBase.append("http://www.minnasundberg.fi/comic/")
nextLinkParent = True
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Stand Still, Stay Silent
display = True
comic_name = "Stand Still. Stay Silent"
filename = "sssscomic"
urlMain = "http://www.sssscomic.com/"
urlFirstPage = "http://sssscomic.com/comic.php?page=1"
nextTag.append("img")
nextAttr.append("src")
nextStr.append("next.png")
urlBase.append('http://sssscomic.com/comic.php')
urlBase.append('http://sssscomic.com/comic2.php')
nextLinkParent = True
total_pages = urlFinder.urlBuild(
    urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent, baseChanges=True)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Sister Claire
display = True
comic_name = "Sister Claire Comic"
filename = "sisterClaire"
urlMain = "http://www.sisterclaire.com/"
urlFirstPage = "http://www.sisterclaire.com/comic/book-one"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Sister Claire - Missing Moments
display = True
comic_name = "Sister Claire Missing Moments"
filename = "sisterClaireMM"
urlMain = "http://www.sisterclaire.com/"
urlFirstPage = "http://www.sisterclaire.com/missing-moments/missing-moment-la-scoperta"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Tripp (web archive)
display = True
comic_name = "Tripp"
filename = "tripp"
urlMain = "https://web.archive.org/web/20150506105057/http://www.trippcomic.com/home"
urlFirstPage = "https://web.archive.org/web/20150507152639/http://www.trippcomic.com/archives/archive/poet-b5e016f"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Twilight Lady
display = True
comic_name = "Twilight Lady"
filename = "twilight"
urlMain = "http://corridorcomix.com/twilightlady/"
urlFirstPage = "http://corridorcomix.com/twilightlady/comic/the-secret-of-cass-corridor-2/"
nextTag.append("a")
nextAttr.append("class")
nextStr.append("comic-nav-base comic-nav-next")
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Corridor Realms - Twilight Lady
display = True
comic_name = "Corridor Realms - (new) Twilight Lady"
filename = "twilightnew"
urlMain = "http://corridorcomix.com/"
urlFirstPage = "http://corridorcomix.com/comic/twilight-ladys-house-concert/"
nextTag.append("a")
nextAttr.append("class")
nextStr.append("comic-nav-base comic-nav-next")
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Headless Bliss
display = True
comic_name = "Headless Bliss"
filename = "headbliss"
urlMain = "http://www.headlessbliss.com/"
urlFirstPage = "http://www.headlessbliss.com/comic/page-1"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# the end
display = True
comic_name = "the end"
filename = "endcomic"
urlMain = "http://www.endcomic.com/"
urlFirstPage = "http://www.endcomic.com/comic/book-one-cover/"
nextTag.append("a")
nextAttr.append("class_")
nextStr.append('comic-nav-base comic-nav-next')
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# Bedlam Genesis
display = True
comic_name = "Bedlam Genesis"
filename = "bedlam"
urlMain = "http://bedlamgenesis.com/index"
urlFirstPage = "http://bedlamgenesis.com/index?V=1&C=1&P=1"
nextTag.append("img")
nextAttr.append("src")
nextStr.append("next.png")
urlBase.append('http://bedlamgenesis.com/')
nextLinkParent = True
search_end = '#'
total_pages = urlFinder.urlBuild(
    urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent, search_end)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]


# FanFiction Stories

# FF Four Armed Bride
display = True
comic_name = "zFF Four Armed Bride"
filename = "fourarmed"
urlMain = "https://www.fanfiction.net/s/12103554/1/Four-Armed-Bride"
urlFirstPage = "https://www.fanfiction.net/s/12103554/1/Four-Armed-Bride"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# FF Hereafter
display = True
comic_name = "zFF Hereafter"
filename = "hereafter"
urlMain = "https://www.fanfiction.net/s/12711718/1/Hereafter"
urlFirstPage = "https://www.fanfiction.net/s/12711718/1/Hereafter"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# FF Love is a Kind of War
display = True
comic_name = "zFF Love is a Kind of War"
filename = "loveiswar"
urlMain = "https://www.fanfiction.net/s/8764528/1/Love-is-a-Kind-of-War"
urlFirstPage = "https://www.fanfiction.net/s/8764528/1/Love-is-a-Kind-of-War"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# FF Monster Falls
display = True
comic_name = "zFF Monster Falls"
filename = "monsterfalls"
urlMain = "https://www.fanfiction.net/s/11126659/1/Monster-Falls"
urlFirstPage = "https://www.fanfiction.net/s/11126659/1/Monster-Falls"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# FF One Hundred Kisses
display = True
comic_name = "zFF One Hundred Kisses"
filename = "100kisses"
urlMain = "https://www.fanfiction.net/s/11947059/1/One-Hundred-Kisses"
urlFirstPage = "https://www.fanfiction.net/s/11947059/1/One-Hundred-Kisses"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# FF Recovery and Resolutions
display = True
comic_name = "zFF Recovery and Resolutions"
filename = "recovery"
urlMain = "https://www.fanfiction.net/s/11958300/1/Recovery-and-Resolutions"
urlFirstPage = "https://www.fanfiction.net/s/11958300/1/Recovery-and-Resolutions"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# FF The Savage Dark
display = True
comic_name = "zFF The Savage Dark"
filename = "savagedark"
urlMain = "https://www.fanfiction.net/s/12086054/1/The-Savage-Dark"
urlFirstPage = "https://www.fanfiction.net/s/12086054/1/The-Savage-Dark"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# FF A Snowstorm of Secrets
display = True
comic_name = "zFF A Snowstorm of Secrets"
filename = "snowstormsecrets"
urlMain = "https://www.fanfiction.net/s/10023494/1/A-Snowstorm-of-Secrets"
urlFirstPage = "https://www.fanfiction.net/s/10023494/1/A-Snowstorm-of-Secrets"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# FF Swaw Mi Krr
display = True
comic_name = "zFF Swaw Mi Krr"
filename = "swawmikrr"
urlMain = "https://www.fanfiction.net/s/7121323/1/Swaw-M%C3%AC-Krr"
urlFirstPage = "https://www.fanfiction.net/s/7121323/1/Swaw-M%C3%AC-Krr"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# FF The fall of a king
display = True
comic_name = "zFF The Fall of a King"
filename = "kingfall"
urlMain = "https://www.fanfiction.net/s/11932949/1/The-fall-of-a-king"
urlFirstPage = "https://www.fanfiction.net/s/11932949/1/The-fall-of-a-king"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

# FF The True Self
display = True
comic_name = "zFF The True Self"
filename = "trueself"
urlMain = "https://www.fanfiction.net/s/11888755/1/The-True-Self"
urlFirstPage = "https://www.fanfiction.net/s/11888755/1/The-True-Self"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
total_pages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]


# Blocked by not allowing cross-origin framing

# WebToons - X-Frame extension doesn't allow these to work, more work required
# maybe separate program (using selenium?) to drive browser?
# best change is making page of links and allow manual setting/marking

# The Angel in the Forest
display = True
comic_name = "The Angel in the Forest"
filename = "angelForest"
# urlMain = "https://www.webtoons.com/en/challenge/the-angel-in-the-forest/list?title_no=230887"
urlFirstPage = ("https://www.webtoons.com/en/challenge/the-angel-in-the-forest/",
                "indebted-babysitter/viewer?title_no=230887&episode_no=1")
total_pages = urlWebToons.urlBuild(urlFirstPage, filename)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))

# Flow
display = True
comic_name = "Flow"
filename = "flow"
# urlMain = "https://www.webtoons.com/en/fantasy/flow/list?title_no=101"
urlFirstPage = "https://www.webtoons.com/en/fantasy/flow/ep-0/viewer?title_no=101&episode_no=1"
total_pages = urlWebToons.urlBuild(urlFirstPage, filename)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))

# Interspace Pirate Xuna
display = True
comic_name = "Interspace"
filename = "interspace"
# urlMain = "https://www.webtoons.com/en/challenge/interspace-pirate-xuna/list?title_no=282267"
urlFirstPage = ("https://www.webtoons.com/en/challenge/interspace-pirate-xuna/",
                "prologue/viewer?title_no=282267&episode_no=1")
total_pages = urlWebToons.urlBuild(urlFirstPage, filename)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))

# LionHeart
display = True
comic_name = "LionHeart"
filename = "lionheart"
# urlMain = "https://www.webtoons.com/en/challenge/lionheart/list?title_no=312965"
urlFirstPage = "https://www.webtoons.com/en/challenge/lionheart/ep-1/viewer?title_no=312965&episode_no=1"
total_pages = urlWebToons.urlBuild(urlFirstPage, filename)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))

# Lumine
display = True
comic_name = "Lumine"
filename = "lumine"
# urlMain = "https://www.webtoons.com/en/drama/lumine/list?title_no=1022"
urlFirstPage = "https://www.webtoons.com/en/drama/lumine/ep-1/viewer?title_no=1022&episode_no=1"
total_pages = urlWebToons.urlBuild(urlFirstPage, filename)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))

# Rise from Ashes
display = True
comic_name = "Rise from Ashes"
filename = "riseFromAshes"
# urlMain = "https://www.webtoons.com/en/fantasy/rise-from-ashes/list?title_no=959"
urlFirstPage = "https://www.webtoons.com/en/fantasy/rise-from-ashes/ep-1/viewer?title_no=959&episode_no=1"
total_pages = urlWebToons.urlBuild(urlFirstPage, filename)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))

# Seed
display = True
comic_name = "Seed"
filename = "seed"
# urlMain = "https://www.webtoons.com/en/sf/seed/list?title_no=1480"
urlFirstPage = "https://www.webtoons.com/en/sf/seed/prologue/viewer?title_no=1480&episode_no=1"
total_pages = urlWebToons.urlBuild(urlFirstPage, filename)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))

# Soleil
display = True
comic_name = "Soleil"
filename = "soleil"
# urlMain = "https://www.webtoons.com/en/fantasy/soleil/list?title_no=1823"
urlFirstPage = "https://www.webtoons.com/en/fantasy/soleil/episode-1/viewer?title_no=1823&episode_no=1"
total_pages = urlWebToons.urlBuild(urlFirstPage, filename)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))

# Space Vixen
display = True
comic_name = "Space Vixen - Deep Space K9"
filename = "spaceVixen"
# urlMain = "https://www.webtoons.com/en/challenge/space-vixen-deep-space-k9/list?title_no=207049"
urlFirstPage = ("https://www.webtoons.com/en/challenge/space-vixen-deep-space-k9/",
                "episode-0-prologue-pyramid-scheme/viewer?title_no=207049&episode_no=1")
total_pages = urlWebToons.urlBuild(urlFirstPage, filename)
comic_list.append(Webcomic(comic_name, filename, total_pages, display))


# Possibly defunct/dead

# Home
# display = False
# comic_name = "Home"
# filename = ""
# urlMain = ""
# urlFirstPage = "http://home-comic.smackjeeves.com/comics/2256824/page-1/"

# Mortal Half
# display = False
# comic_name = "Mortal Half"
# filename = ""
# urlMain = "http://www.mortalhalf.com/webcomic/"
# urlFirstPage = ""

# Succubus Justice--DEAD
# display = False
# comic_name = "Succubus Justice"
# filename = ""
# urlMain = ""
# urlFirstPage = "http://www.succubusjustice.com/page001.htm"


comic_list.sort(key=lambda comic: str.lower(comic.name))

comics = [comic.name for comic in comic_list]
files = [comic.file for comic in comic_list]
pages = [comic.pages for comic in comic_list]
visible = [comic.visible for comic in comic_list]

print("Full Comic List: (* hidden)")
for comic in comic_list:
    temp_str = ""
    if comic.visible:
        temp_str += "  "
    else:
        temp_str += "* "
    temp_str += comic.name + "  "
    print(temp_str)

buildMainPage(comics, files, pages, visible)


print('Main Page stored at:')
print(os.path.realpath(r'webcomic\webcomic.html'))
