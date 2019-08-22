import os
#import webbrowser
import urlAvasDemon
import urlCAD
import urlTwoKinds
import urlLFG
import urlQ2Q
import urlRoomie
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

#Ctrl+Alt+Del
display = True
comicname = "Ctrl+Alt+Del"
filename = "CADcomic"
urlMain = "http://cad-comic.com/"
urlFirstPage = "http://cad-comic.com/comic/nice-melon/"
totalpages = urlCAD.urlBuild(urlFirstPage, filename)
comiclist.append(Webcomic(comicname, filename, totalpages, display))

#Devilbear
display = True
comicname = "Devilbear: The Grimoires of Bearalzebub"
filename = "Devilbear"
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

#Druids
display = False
comicname = "Druids (Mature)"
filename = "Druids"
urlMain = "http://druids.thecomicseries.com/"
urlFirstPage = "http://druids.thecomicseries.com/comics/first/"
nextTag.append("")
nextAttr.append("")
nextStr.append('')
#urlBase.append('')
nextLinkParent = False
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
