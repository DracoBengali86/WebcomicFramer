import os
#import webbrowser
import urlAvasDemon
import urlBladeBunny
import urlCAD
import urlEarthsong
import urlLFG
import urlQ2Q
import urlRoomie
import urlTwoKinds
import urlFinder
from htmlCreator import buildMainPage

os.makedirs('webcomic', exist_ok=True)

visible = []
comics = []
files = []
pages = []
nextTag = []
nextAttr = []
nextStr = []
urlBase = []


class Webcomic:
    def __init__(self, comicname, filename, totalpages, visibility):
        self.name = comicname
        self.file = filename
        self.pages = totalpages
        self.visible = visibility


comiclist = []

#XKCD
display = True
comicname = "XKCD"
filename = "xkcd"
urlMain = "http://www.xkcd.com/"
urlFirstPage = "http://xkcd.com/1/"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
urlBase.append('http://xkcd.com')
nextLinkParent = False
searchend = '#'
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent, searchend)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Ava's Demon
display = True
comicname = "Ava's Demon"
filename = "AvasDemon"
urlMain = "http://www.AvasDemon.com"
urlFirstPage = "http://www.AvasDemon.com/pages.php#0001"
totalpages = urlAvasDemon.urlBuild(urlFirstPage, filename, urlMain)
comiclist.append(Webcomic(comicname, filename, totalpages, display))

#Blade Bunny
#webpage doesn't like to reload...need to fix that
display = True
comicname = "Blade Bunny"
filename = "BladeBunny"
urlMain = "https://readcomiconline.to/Comic/Blade-Bunny"
urlFirstPage = "https://readcomiconline.to/Comic/Blade-Bunny/Issue-1?id=42534"
urlVol1End = "https://readcomiconline.to/Comic/Blade-Bunny/Issue-5?id=87724#29"
urlVol2 = "https://readcomiconline.to/Comic/Blade-Bunny-Vol-2/Issue-1?id=94715"
totalpages = urlBladeBunny.urlBuild(urlFirstPage, filename, urlMain, urlVol1End, urlVol2)
comiclist.append(Webcomic(comicname, filename, totalpages, display))

#Balazo
display = True
comicname = "Balazo - Stories in Pretty Pictures"
filename = "balazo"
urlMain = "http://balazo.net/"
urlFirstPage = "http://balazo.net/2010/08/starting-tomorrow/"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
#urlBase.append('')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Subnormality
display = True
comicname = "Subnromality"
filename = "Subnormality"
urlMain = "http://www.viruscomix.com/subnormality.html"
urlFirstPage = "http://www.viruscomix.com/page324.html"
# search 1
nextTag.append("img")
nextAttr.append("src")
nextStr.append('subnext.*')
#search 2
nextTag.append("img")
nextAttr.append("src")
nextStr.append("nextIIC.gif")
urlBase.append('http://www.viruscomix.com/')
nextLinkParent = True
searchend = 'subnormality.html'
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent, searchend)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]


# Will need something like Avas Demon for this (completely jQuery-button events for next page)
#Carciphona
display = False
comicname = "Carciphona"
filename = "carciphona"
# urlMain = "https://carciphona.com/"
# urlFirstPage = "https://carciphona.com/read.php#volume=1&chapter=1&page=-1&lang=en"
# nextTag.append("a")
# nextAttr.append("class")
# nextStr.append("comic-nav-base comic-nav-next")
# nextLinkParent = False
# totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
totalpages = 0
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Ctrl+Alt+Del
display = True
comicname = "Ctrl+Alt+Del"
filename = "CADcomic"
urlMain = "http://cad-comic.com/"
urlFirstPage = "http://cad-comic.com/comic/nice-melon/"
totalpages = urlCAD.urlBuild(urlFirstPage, filename)
comiclist.append(Webcomic(comicname, filename, totalpages, display))

#D20 Monkey
display = True
comicname = "d20 Monkey"
filename = "d20"
urlMain = "http://www.d20monkey.com/"
urlFirstPage = "http://www.d20monkey.com/comic/welcome/"
nextTag.append("a")
nextAttr.append("class")
nextStr.append("navi comic-nav-next navi-next")
#urlBase.append('')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Devilbear
display = True
comicname = "Devilbear: The Grimoires of Bearalzebub"
filename = "Devilbear"
urlMain = "http://www.thedevilbear.com/index.html"
urlFirstPage = "http://www.thedevilbear.com/comics.php?p=1"
nextTag.append("a")
nextAttr.append("id")
nextStr.append('cg_next')
nextLinkParent = False
urlBase.append('http://www.thedevilbear.com/comics.php')
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Devilbear Shorts
display = True
comicname = "Devilbear: The Shorts of Bearalzebub"
filename = "DevilbearShorts"
urlMain = "http://www.thedevilbear.com/"
urlFirstPage = "http://www.thedevilbear.com/b/comic/its-for-you/"
nextTag.append("a")
nextAttr.append("class_")
nextStr.append('comic-nav-base comic-nav-next')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Depths of my Empty Soul
display = True
comicname = "Depths Of My Empty Soul (Mature)"
filename = "Depths"
urlMain = "http://depthsofmyemptysoul.smackjeeves.com/"
urlFirstPage = "http://depthsofmyemptysoul.smackjeeves.com/comics/1629357/welcome/"
nextTag.append("a")
nextAttr.append("text")
nextStr.append('Next >')
urlBase.append('http://depthsofmyemptysoul.smackjeeves.com/mature.php?ref=')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Dreamscar
display = True
comicname = "dream*scar"
filename = "dreamscar"
urlMain = "https://dream-scar.net/"
urlFirstPage = "https://dream-scar.net/?id=1"
nextTag.append("a")
nextAttr.append("title")
nextStr.append("next")
urlBase.append("https://dream-scar.net/")
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Druids
display = True
comicname = "Druids (Mature)"
filename = "Druids"
urlMain = "http://druids.thecomicseries.com/"
urlFirstPage = "http://druids.thecomicseries.com/comics/first/"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append('next')
urlBase.append('http://druids.thecomicseries.com')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Earthsong
display = True
comicname = "Earthsong"
filename = "earthsong"
urlMain = "http://earthsongsaga.com/index.php"
urlFirstPage = "http://earthsongsaga.com/vol1/vol1cover.php"
nextTag.append("li")
nextAttr.append("id")
nextStr.append("next")
nextTag.append("td")
nextAttr.append("width")
nextStr.append("71")
totalpages = urlEarthsong.urlBuild(urlFirstPage, filename, nextTag, nextAttr, nextStr)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Everblue
display = True
comicname = "Everblue"
filename = "everblue"
urlMain = "http://www.everblue-comic.com/"
urlFirstPage = "http://www.everblue-comic.com/comic/1"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
urlBase.append("http://www.everblue-comic.com")
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Furthia High
display = True
comicname = "Furthia High"
filename = "furthia"
urlMain = "http://furthiahigh.concessioncomic.com/"
urlFirstPage = "http://furthiahigh.concessioncomic.com/index.php?pid=20080128"
nextTag.append("img")
nextAttr.append("alt")
nextStr.append("Next")
#urlBase.append('')
nextLinkParent = True
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Greg
display = True
comicname = "Greg"
filename = "Greg"
urlMain = "https://www.theduckwebcomics.com/Greg/"
urlFirstPage = "https://www.theduckwebcomics.com/Greg/5491003/"
nextTag.append("img")
nextAttr.append("src")
nextStr.append('next.png')
urlBase.append('https://www.theduckwebcomics.com')
nextLinkParent = True
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#HalfLight
display = True
comicname = "HalfLight"
filename = "halflight"
urlMain = "http://halflightcomics.com/"
urlFirstPage = "http://halflightcomics.com/http:/halflightcomics.com/comic/chapter-1"
nextTag.append("a")
nextAttr.append("class")
nextStr.append('navi navi-next')
#urlBase.append('')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Miamaska
display = True
comicname = "Miamaska"
filename = "miamaska"
urlMain = "http://miamaska.com/index.php"
urlFirstPage = "http://miamaska.com/index.php?pn=0"
nextTag.append("a")
nextAttr.append("text")
nextStr.append('Next')
urlBase.append('http://miamaska.com/index.php')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Misfile
display = True
comicname = "Misfile"
filename = "misfile"
urlMain = "http://www.misfile.com/"
urlFirstPage = "http://www.misfile.com/?date=2004-02-22"
nextTag.append("img")
nextAttr.append("alt")
nextStr.append("Next Comic")
urlBase.append("http://www.misfile.com")
nextLinkParent = True
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Modest Medusa
display = True
comicname = "Modest Medusa"
filename = "medusa"
urlMain = "http://modestmedusa.com/"
urlFirstPage = "http://modestmedusa.com/comic/christmas-eve-3/"
nextTag.append("a")
nextAttr.append("class")
nextStr.append("comic-nav-base comic-nav-next")
#urlBase.append("")
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Next Town Over
display = True
comicname = "Next Town Over"
filename = "nexttown"
urlMain = "http://www.nexttownover.net/"
urlFirstPage = "http://www.nexttownover.net/?p=4"
nextTag.append("a")
nextAttr.append("class")
nextStr.append("navi navi-next")
#urlBase.append("")
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Questionable Content
display = True
comicname = "Questionable Content"
filename = "questionable"
urlMain = "https://www.questionablecontent.net/"
urlFirstPage = "https://www.questionablecontent.net/view.php?comic=1"
nextTag.append("a")
nextAttr.append("text")
nextStr.append('Next')
urlBase.append('https://www.questionablecontent.net/')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Red Moon Rising
display = True
comicname = "Red Moon Rising"
filename = "redmoon"
urlMain = "http://www.redmoonrising.org/"
urlFirstPage = "http://www.redmoonrising.org/archive/red-moon-rising/"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
#urlBase.append("")
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Scout Crossing
display = True
comicname = "Scout Crossing"
filename = "scout"
urlMain = "http://scoutcrossing.net/"
urlFirstPage = "http://scoutcrossing.net/comic/000-scoutcrossing/"
nextTag.append("a")
nextAttr.append("class")
nextStr.append("navi navi-next")
#urlBase.append("")
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Think before you Think
display = True
comicname = "Think Before You Think"
filename = "think"
urlMain = "http://thinkbeforeyouthink.net/"
urlFirstPage = "http://thinkbeforeyouthink.net/?comic=20090612-coffee"
nextTag.append("a")
nextAttr.append("text")
nextStr.append('Next >')
#urlBase.append('')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Toilet Genie
display = True
comicname = "Toilet Genie"
filename = "toilet"
urlMain = "https://www.deviantart.com/blix-it/gallery/9792599/toilet-genie"
urlFirstPage = "https://www.deviantart.com/blix-it/art/D-0-0-R-Toilet-Genie-001-118248100"
nextTag.append("a")
nextAttr.append("text")
nextStr.append('Next')
#urlBase.append('')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Two Guys and Guy
display = True
comicname = "Two Guys and Guy"
filename = "twoguys"
urlMain = "http://www.twogag.com/"
urlFirstPage = "http://twogag.com/archives/4"
nextTag.append("a")  # use a, rel "next" if this doesn't work
nextAttr.append("class")
nextStr.append("cc-next")
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#TwoKinds
display = True
comicname = "TwoKinds"
filename = "TwoKinds"
urlMain = "http://twokinds.keenspot.com/"
urlFirstPage = "http://twokinds.keenspot.com/comic/1/"
totalpages = urlTwoKinds.urlBuild(urlFirstPage, filename)
comiclist.append(Webcomic(comicname, filename, totalpages, display))

#Looking for Group
display = True
comicname = "Looking for Group"
filename = "LFG"
urlMain = ""
urlFirstPage = 'https://www.lfg.co/page/1/'
totalpages = urlLFG.urlBuild(urlFirstPage, filename)
comiclist.append(Webcomic(comicname, filename, totalpages, display))

#Q2Q
display = True
comicname = "Q2Q"
filename = "q2qcomic"
urlMain = "https://q2qcomics.com/"
urlFirstPage = 'https://q2qcomics.com/comic/q2q1/'
totalpages = urlQ2Q.urlBuild(urlFirstPage, filename)
comiclist.append(Webcomic(comicname, filename, totalpages, display))

#Go Get a Roomie
#Can be used with an extension that makes browser ignore X-Frame options EX: Ignore X-Frame-Options for Firefox
display = True
comicname = "Go Get a Roomie! (Mature) (Requires X-Frame option extension)"
filename = "Roomie"
urlMain = "http://www.gogetaroomie.com/"
urlFirstPage = 'http://www.gogetaroomie.com/comic/and-so-it-begins'
totalpages = urlRoomie.urlBuild(urlFirstPage, filename, urlMain)
comiclist.append(Webcomic(comicname, filename, totalpages, display))

#Sanda and Woo
display = True
comicname = "Sandra and Woo"
filename = "sandra"
urlMain = "http://www.sandraandwoo.com/"
urlFirstPage = "http://www.sandraandwoo.com/2000/01/01/welcome-to-sandra-and-woo/"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
#urlBase.append("")
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#A Redtail's Dream
display = True
comicname = "A Redtail's Dream"
filename = "redtail"
urlMain = "http://www.minnasundberg.fi/comic/recent.php"
urlFirstPage = "http://www.minnasundberg.fi/comic/page00.php"
nextTag.append("img")
nextAttr.append("src")
nextStr.append(".*anext[.]jpg")
urlBase.append("http://www.minnasundberg.fi/comic/")
nextLinkParent = True
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Stand Still, Stay Silent
display = True
comicname = "Stand Still. Stay Silent"
filename = "sssscomic"
urlMain = "http://www.sssscomic.com/"
urlFirstPage = "http://sssscomic.com/comic.php?page=1"
nextTag.append("img")
nextAttr.append("src")
nextStr.append("next.png")
urlBase.append('http://sssscomic.com/comic.php')
urlBase.append('http://sssscomic.com/comic2.php')
nextLinkParent = True
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent, baseChanges=True)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Sister Claire
display = True
comicname = "Sister Claire Comic"
filename = "sisterClaire"
urlMain = "http://www.sisterclaire.com/"
urlFirstPage = "http://www.sisterclaire.com/comic/book-one"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
#urlBase.append("")  # full url for next page is in href
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Sister Claire - Missing Moments
display = True
comicname = "Sister Claire Missing Moments"
filename = "sisterClaireMM"
urlMain = "http://www.sisterclaire.com/"
urlFirstPage = "http://www.sisterclaire.com/missing-moments/missing-moment-la-scoperta"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
#urlBase.append("")  # full url for next page is in href
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Twilight Lady
display = True
comicname = "Twilight Lady"
filename = "twilight"
urlMain = "http://corridorcomix.com/twilightlady/"
urlFirstPage = "http://corridorcomix.com/twilightlady/comic/the-secret-of-cass-corridor-2/"
nextTag.append("a")
nextAttr.append("class")
nextStr.append("comic-nav-base comic-nav-next")
#urlBase.append("")
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Corridor Realms - Twilight Lady
display = True
comicname = "Corridor Realms - (new) Twilight Lady"
filename = "twilightnew"
urlMain = "http://corridorcomix.com/"
urlFirstPage = "http://corridorcomix.com/comic/twilight-ladys-house-concert/"
nextTag.append("a")
nextAttr.append("class")
nextStr.append("comic-nav-base comic-nav-next")
#urlBase.append("")
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Headless Bliss
display = True
comicname = "Headless Bliss"
filename = "headbliss"
urlMain = "http://www.headlessbliss.com/"
urlFirstPage = "http://www.headlessbliss.com/comic/page-1"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
#urlBase.append("")  # full url for next page is in href
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#the end
display = True
comicname = "the end"
filename = "endcomic"
urlMain = "http://www.endcomic.com/"
urlFirstPage = "http://www.endcomic.com/comic/book-one-cover/"
nextTag.append("a")
nextAttr.append("class_")
nextStr.append('comic-nav-base comic-nav-next')
#urlBase = ''  # full url for next page is in href
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#Bedlam Genesis
display = True
comicname = "Bedlam Genesis"
filename = "bedlam"
urlMain = "http://bedlamgenesis.com/index"
urlFirstPage = "http://bedlamgenesis.com/index?V=1&C=1&P=1"
nextTag.append("img")
nextAttr.append("src")
nextStr.append("next.png")
urlBase.append('http://bedlamgenesis.com/')
nextLinkParent = True
searchend = '#'
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent, searchend)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]


#FanFiction Stories

#FF Four Armed Bride
display = True
comicname = "zFF Four Armed Bride"
filename = "fourarmed"
urlMain = "https://www.fanfiction.net/s/12103554/1/Four-Armed-Bride"
urlFirstPage = "https://www.fanfiction.net/s/12103554/1/Four-Armed-Bride"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#FF Hereafter
display = True
comicname = "zFF Hereafter"
filename = "hereafter"
urlMain = "https://www.fanfiction.net/s/12711718/1/Hereafter"
urlFirstPage = "https://www.fanfiction.net/s/12711718/1/Hereafter"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#FF Love is a Kind of War
display = True
comicname = "zFF Love is a Kind of War"
filename = "loveiswar"
urlMain = "https://www.fanfiction.net/s/8764528/1/Love-is-a-Kind-of-War"
urlFirstPage = "https://www.fanfiction.net/s/8764528/1/Love-is-a-Kind-of-War"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#FF Monster Falls
display = True
comicname = "zFF Monster Falls"
filename = "monsterfalls"
urlMain = "https://www.fanfiction.net/s/11126659/1/Monster-Falls"
urlFirstPage = "https://www.fanfiction.net/s/11126659/1/Monster-Falls"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#FF One Hundred Kisses
display = True
comicname = "zFF One Hundred Kisses"
filename = "100kisses"
urlMain = "https://www.fanfiction.net/s/11947059/1/One-Hundred-Kisses"
urlFirstPage = "https://www.fanfiction.net/s/11947059/1/One-Hundred-Kisses"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#FF Recovery and Resolutions
display = True
comicname = "zFF Recovery and Resolutions"
filename = "recovery"
urlMain = "https://www.fanfiction.net/s/11958300/1/Recovery-and-Resolutions"
urlFirstPage = "https://www.fanfiction.net/s/11958300/1/Recovery-and-Resolutions"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#FF The Savage Dark
display = True
comicname = "zFF The Savage Dark"
filename = "savagedark"
urlMain = "https://www.fanfiction.net/s/12086054/1/The-Savage-Dark"
urlFirstPage = "https://www.fanfiction.net/s/12086054/1/The-Savage-Dark"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#FF A Snowstorm of Secrets
display = True
comicname = "zFF A Snowstorm of Secrets"
filename = "snowstormsecrets"
urlMain = "https://www.fanfiction.net/s/10023494/1/A-Snowstorm-of-Secrets"
urlFirstPage = "https://www.fanfiction.net/s/10023494/1/A-Snowstorm-of-Secrets"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#FF Swaw Mi Krr
display = True
comicname = "zFF Swaw Mi Krr"
filename = "swawmikrr"
urlMain = "https://www.fanfiction.net/s/7121323/1/Swaw-M%C3%AC-Krr"
urlFirstPage = "https://www.fanfiction.net/s/7121323/1/Swaw-M%C3%AC-Krr"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#FF The fall of a king
display = True
comicname = "zFF The Fall of a King"
filename = "kingfall"
urlMain = "https://www.fanfiction.net/s/11932949/1/The-fall-of-a-king"
urlFirstPage = "https://www.fanfiction.net/s/11932949/1/The-fall-of-a-king"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]

#FF The True Self
display = True
comicname = "zFF The True Self"
filename = "trueself"
urlMain = "https://www.fanfiction.net/s/11888755/1/The-True-Self"
urlFirstPage = "https://www.fanfiction.net/s/11888755/1/The-True-Self"
nextTag.append("button")
nextAttr.append("text")
nextStr.append("Next >")
urlBase.append('https://www.fanfiction.net')
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent)
comiclist.append(Webcomic(comicname, filename, totalpages, display))
del nextTag[:], nextAttr[:], nextStr[:], urlBase[:]


#Blocked by not allowing cross-origin framing

#WebToons - X-Frame extension doesn't allow these to work, more work required
#maybe seperate program (using selenium?) to drive browser?
#The Angel in the Forest
display = False
comicname = "The Angel in the Forest"
filename = "AngelForest"
urlMain = "http://www.webtoons.com/en/challenge/the-angel-in-the-forest/list?title_no=230887"
urlFirstPage = "http://www.webtoons.com/en/challenge/the-angel-in-the-forest/indebted-babysitter/viewer?title_no=230887&episode_no=1"
#totalpages = urlAngelForest.urlBuild(urlFirstPage, filename)
totalpages = 0
comiclist.append(Webcomic(comicname, filename, totalpages, display))

#Seed
display = False
comicname = "Seed"
filename = "Seed"
urlMain = "http://www.webtoons.com/en/sf/seed/list?title_no=1480"
urlFirstPage = "http://www.webtoons.com/en/sf/seed/prologue/viewer?title_no=1480&episode_no=1"
#totalpages = urlSeed.urlBuild(urlFirstPage, filename)
totalpages = 0
comiclist.append(Webcomic(comicname, filename, totalpages, display))

#Soleil
display = False
comicname = "Soleil"
filename = "Soleil"
urlMain = "http://www.webtoons.com/en/challenge/soleil/list?title_no=192734"
urlFirstPage = "http://www.webtoons.com/en/challenge/soleil/intro/viewer?title_no=192734&episode_no=1"
#totalpages = urlSoleil.urlBuild(urlFirstPage, filename)
totalpages = 0
comiclist.append(Webcomic(comicname, filename, totalpages, display))

#Flow
display = False
comicname = "Flow"
filename = "Flow"
urlMain = "http://www.webtoons.com/en/fantasy/flow/list?title_no=101"
urlFirstPage = "http://www.webtoons.com/en/fantasy/flow/ep-0/viewer?title_no=101&episode_no=1"
#totalpages = urlFlow.urlBuild(urlFirstPage, filename)
totalpages = 0
comiclist.append(Webcomic(comicname, filename, totalpages, display))

#Lumine
display = False
comicname = "Lumine"
filename = "Lumine"
urlMain = "http://www.webtoons.com/en/drama/lumine/list?title_no=1022"
urlFirstPage = "http://www.webtoons.com/en/drama/lumine/episode-1/viewer?title_no=1022&episode_no=1"
#totalpages = urlLumine.urlBuild(urlFirstPage, filename)
totalpages = 0
comiclist.append(Webcomic(comicname, filename, totalpages, display))

#Rise from Ashes
display = False
comicname = "Rise from Ashes"
filename = "RisefromAshes"
urlMain = "http://www.webtoons.com/en/fantasy/rise-from-ashes/list?title_no=959"
urlFirstPage = "http://www.webtoons.com/en/fantasy/rise-from-ashes/ep-1/viewer?title_no=959&episode_no=1"
#totalpages = urlRisefromAshes.urlBuild(urlFirstPage, filename)
totalpages = 0
comiclist.append(Webcomic(comicname, filename, totalpages, display))


#Possibly defunct/dead


#Home
display = False
comicname = "Home"
filename = ""
urlMain = ""
urlFirstPage = "http://home-comic.smackjeeves.com/comics/2256824/page-1/"

#Mortal Half
display = False
comicname = "Mortal Half"
filename = ""
urlMain = "http://www.mortalhalf.com/webcomic/"
urlFirstPage = ""

#Succubus Justice--DEAD
display = False
comicname = "Succubus Justice"
filename = ""
urlMain = ""
urlFirstPage = "http://www.succubusjustice.com/page001.htm"


comiclist.sort(key=lambda comic: str.lower(comic.name))

comics = [comic.name for comic in comiclist]
files = [comic.file for comic in comiclist]
pages = [comic.pages for comic in comiclist]
visible = [comic.visible for comic in comiclist]

print("Full Comic List: (* hidden)")
for comic in comiclist:
    tempstr = ""
    if comic.visible:
        tempstr += "  "
    else:
        tempstr += "* "
    tempstr += comic.name + "  "
    #tempstr += str(comic.pages)
    print(tempstr)

buildMainPage(comics, files, pages, visible)


print('Main Page stored at:')
print(os.path.realpath('webcomic\webcomic.html'))
#print('Opening Webcomic Main Page')
#webbrowser.open('file://' + os.path.realpath('webcomic\webcomic.html'))
