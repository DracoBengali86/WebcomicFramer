import os
#import webbrowser
import urlXkcd
import urlAvasDemon
import urlCAD
import urlSubnorm
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

#XKCD
display = True
comicname = "XKCD"
filename = "xkcd"
urlMain = "http://www.xkcd.com/"
urlFirstPage = "http://xkcd.com/1/"
#totalpages = urlXkcd.urlBuild(urlFirstPage, filename)
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
urlnextBase = 'http://xkcd.com'
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlnextBase, nextTag, nextAttr, nextStr, nextLinkParent)
comics.append(comicname)
files.append(filename)
pages.append(totalpages)
visible.append(display)
del nextTag[:], nextAttr[:], nextStr[:]

#Ava's Demon
display = True
comicname = "Ava's Demon"
filename = "AvasDemon"
urlMain = "http://www.AvasDemon.com"
urlFirstPage = "http://www.AvasDemon.com/pages.php#0001"
totalpages = urlAvasDemon.urlBuild(urlFirstPage, filename, urlMain)
comics.append(comicname)
files.append(filename)
pages.append(totalpages)
visible.append(display)

#Subnormality
display = True
comicname = "Subnromality"
filename = "Subnormality"
urlMain = "http://www.viruscomix.com/subnormality.html"
urlFirstPage = "http://www.viruscomix.com/page324.html"
totalpages = urlSubnorm.urlBuild(urlFirstPage, filename)
comics.append(comicname)
files.append(filename)
pages.append(totalpages)
visible.append(display)

#Ctrl+Alt+Del
display = True
comicname = "Ctrl+Alt+Del"
filename = "CADcomic"
urlMain = "http://cad-comic.com/"
urlFirstPage = "http://cad-comic.com/comic/nice-melon/"
totalpages = urlCAD.urlBuild(urlFirstPage, filename)
comics.append(comicname)
files.append(filename)
pages.append(totalpages)
visible.append(display)

#TwoKinds
display = True
comicname = "TwoKinds"
filename = "TwoKinds"
urlMain = "http://twokinds.keenspot.com/"
urlFirstPage = "http://twokinds.keenspot.com/comic/1/"
totalpages = urlTwoKinds.urlBuild(urlFirstPage, filename)
comics.append(comicname)
files.append(filename)
pages.append(totalpages)
visible.append(display)

#Looking for Group
display = True
comicname = "Looking for Group"
filename = "LFG"
urlMain = ""
urlFirstPage = 'https://www.lfg.co/page/1/'
totalpages = urlLFG.urlBuild(urlFirstPage, filename)
comics.append(comicname)
files.append(filename)
pages.append(totalpages)
visible.append(display)

#Q2Q
display = True
comicname = "Q2Q"
filename = "q2qcomic"
urlMain = "https://q2qcomics.com/"
urlFirstPage = 'https://q2qcomics.com/comic/q2q1/'
totalpages = urlQ2Q.urlBuild(urlFirstPage, filename)
comics.append(comicname)
files.append(filename)
pages.append(totalpages)
visible.append(display)

#Go Get a Roomie
#Can be used with an extension that makes browser ignore X-Frame options EX: Ignore X-Frame-Options for Firefox
display = True
comicname = "Go Get a Roomie! (Requires X-Frame option extension)"
filename = "Roomie"
urlMain = "http://www.gogetaroomie.com/"
urlFirstPage = 'http://www.gogetaroomie.com/comic/and-so-it-begins'
totalpages = urlRoomie.urlBuild(urlFirstPage, filename, urlMain)
comics.append(comicname)
files.append(filename)
pages.append(totalpages)
visible.append(display)

#Sister Claire
display = True
comicname = "Sister Claire Comic"
filename = "sisterClaire"
urlMain = "http://www.sisterclaire.com/"
urlFirstPage = "http://www.sisterclaire.com/comic/book-one"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
urlnextBase = ''  # full url for next page is in href
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlnextBase, nextTag, nextAttr, nextStr, nextLinkParent)
comics.append(comicname)
files.append(filename)
pages.append(totalpages)
visible.append(display)
del nextTag[:], nextAttr[:], nextStr[:]

#Sister Claire - Missing Moments
display = True
comicname = "Sister Claire Missing Moments"
filename = "sisterClaireMM"
urlMain = "http://www.sisterclaire.com/"
urlFirstPage = "http://www.sisterclaire.com/missing-moments/missing-moment-la-scoperta"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
urlnextBase = ''  # full url for next page is in href
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlnextBase, nextTag, nextAttr, nextStr, nextLinkParent)
comics.append(comicname)
files.append(filename)
pages.append(totalpages)
visible.append(display)
del nextTag[:], nextAttr[:], nextStr[:]

#Headless Bliss
display = True
comicname = "Headless Bliss"
filename = "headbliss"
urlMain = "http://www.headlessbliss.com/"
urlFirstPage = "http://www.headlessbliss.com/comic/page-1"
nextTag.append("a")
nextAttr.append("rel")
nextStr.append("next")
urlnextBase = ''  # full url for next page is in href
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlnextBase, nextTag, nextAttr, nextStr, nextLinkParent)
comics.append(comicname)
files.append(filename)
pages.append(totalpages)
visible.append(display)
del nextTag[:], nextAttr[:], nextStr[:]

#the end
display = True
comicname = "the end"
filename = "endcomic"
urlMain = "http://www.endcomic.com/"
urlFirstPage = "http://www.endcomic.com/comic/book-one-cover/"
nextTag.append("a")
nextAttr.append("class_")
nextStr.append('comic-nav-base comic-nav-next')
urlnextBase = ''  # full url for next page is in href
nextLinkParent = False
totalpages = urlFinder.urlBuild(urlFirstPage, filename, urlMain, urlnextBase, nextTag, nextAttr, nextStr, nextLinkParent)
comics.append(comicname)
files.append(filename)
pages.append(totalpages)
visible.append(display)
del nextTag[:], nextAttr[:], nextStr[:]


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
comics.append(comicname)
files.append(filename)
pages.append(totalpages)
visible.append(display)

#Seed
display = False
comicname = "Seed"
filename = "Seed"
urlMain = "http://www.webtoons.com/en/sf/seed/list?title_no=1480"
urlFirstPage = "http://www.webtoons.com/en/sf/seed/prologue/viewer?title_no=1480&episode_no=1"
#totalpages = urlSeed.urlBuild(urlFirstPage, filename)
comics.append(comicname)
files.append(filename)
pages.append(totalpages)
visible.append(display)

#Soleil
display = False
comicname = "Soleil"
filename = "Soleil"
urlMain = "http://www.webtoons.com/en/challenge/soleil/list?title_no=192734"
urlFirstPage = "http://www.webtoons.com/en/challenge/soleil/intro/viewer?title_no=192734&episode_no=1"
#totalpages = urlSoleil.urlBuild(urlFirstPage, filename)
comics.append(comicname)
files.append(filename)
pages.append(totalpages)
visible.append(display)

#Flow
display = False
comicname = "Flow"
filename = "Flow"
urlMain = "http://www.webtoons.com/en/fantasy/flow/list?title_no=101"
urlFirstPage = "http://www.webtoons.com/en/fantasy/flow/ep-0/viewer?title_no=101&episode_no=1"
#totalpages = urlFlow.urlBuild(urlFirstPage, filename)
comics.append(comicname)
files.append(filename)
pages.append(totalpages)
visible.append(display)

#Lumine
display = False
comicname = "Lumine"
filename = "Lumine"
urlMain = "http://www.webtoons.com/en/drama/lumine/list?title_no=1022"
urlFirstPage = "http://www.webtoons.com/en/drama/lumine/episode-1/viewer?title_no=1022&episode_no=1"
#totalpages = urlLumine.urlBuild(urlFirstPage, filename)
comics.append(comicname)
files.append(filename)
pages.append(totalpages)
visible.append(display)

#Rise from Ashes
display = False
comicname = "Rise from Ashes"
filename = "RisefromAshes"
urlMain = "http://www.webtoons.com/en/fantasy/rise-from-ashes/list?title_no=959"
urlFirstPage = "http://www.webtoons.com/en/fantasy/rise-from-ashes/ep-1/viewer?title_no=959&episode_no=1"
#totalpages = urlRisefromAshes.urlBuild(urlFirstPage, filename)
comics.append(comicname)
files.append(filename)
pages.append(totalpages)
visible.append(display)


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
urlMain = ""
urlFirstPage = ""

#Succubus Justice--DEAD
display = False
comicname = "Succubus Justice"
filename = ""
urlMain = ""
urlFirstPage = "http://www.succubusjustice.com/page001.htm"


buildMainPage(comics, files, pages, visible)

print('Main Page stored at:')
print(os.path.realpath('webcomic\webcomic.html'))
#print('Opening Webcomic Main Page')
#webbrowser.open('file://' + os.path.realpath('webcomic\webcomic.html'))
