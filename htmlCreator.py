import os


def buildComicPage(pagecount, filename, reloadrequired=False):
    print("Building " + filename + " webpage")

    htmlfile = open(os.path.join('webcomic', filename + '.html'), 'w')

    comicheader(htmlfile, pagecount, filename)
    comicbody(htmlfile)
    comicscripts(htmlfile, pagecount, filename, reloadrequired)

    htmlfile.close()
    print("Done building " + filename + " webpage\n")


def buildMainPage(comicnames, filenames, totalpages, displayonpage):
    print("Building Main webpage")

    htmlfile = open('webcomic\\Webcomic.html', 'w')

    #common head banner code
    #removed "overflow:hidden" from body style
    htmlfile.write('<!DOCTYPE html>\n' +
                   '<html style="height:100%">\n' +
                   '<head>\n' +
                   '<title>Webcomic</title>\n' +
                   '</head>\n' +
                   '<body style="height:100%" onload="updateProgress()">\n' +
                   '<div style="left:8px; right:12px; height:65px; background-color: grey">\n' +
                   '<input type="file" name="names[]" id="name" />\n' +
                   '<button onclick="restoredata()" type="button">Upload Progress</button>\n' +
                   '<p />\n' +
                   '<button onclick="backupdata()" type="button">Save Progress</button>\n' +
                   '</div>\n' +
                   '<div style="position:absolute; top:73px; bottom:9px; left:8px; right:12px">\n')

    #iterate through creating comic displays
    for i in range(len(comicnames)):
        if (displayonpage[i]):
            strtotal = str(totalpages[i])
            htmlfile.write('<p />\n' +
                           '<a href="' + filenames[i] + '.html">' + comicnames[i] + '</a>\n' +
                           '<br />\n' +
                           '<progress id="' + filenames[i] + '" style="width:25%" max="' + strtotal + '" ' +
                           'value="1"><span>1</span>/' + strtotal + '</progress>\n' +
                           '<br />\n' +
                           '<a id="page' + filenames[i] + '">Page 1</a>/' + strtotal + '\n')

    #common closing and scripts
    htmlfile.write('</div>\n' +
                   '</body>\n' +
                   '</html>\n' +
                   '<script type="text/javascript">\n' +
                   'function updateProgress() {\n' +
                   '  for (var i = 0; i < localStorage.length; i++) {\n' +
                   '    var key = localStorage.key(i)\n' +
                   '    var progressBar = document.getElementById(key);\n' +
                   '    var myposition = localStorage.getItem(key);\n' +
                   '    \n' +
                   '	if (progressBar !== null) {\n' +
                   '      progressBar.value = myposition;\n' +
                   '      progressBar.getElementsByTagName(\'span\')[0].textContent = myposition\n' +
                   '      if (myposition == progressBar.max) {\n' +
                   '        document.getElementById(\'page\' + key).innerHTML = "No New Pages ";\n' +
                   '      } else {\n' +
                   '        document.getElementById(\'page\' + key).innerHTML = "Page " + myposition;\n' +
                   '      }\n' +
                   '	}\n' +
                   '  }\n' +
                   '}\n' +
                   '\n' +
                   '// Setup file reading\n' +
                   'var reader = new FileReader();\n' +
                   'reader.onload = handleFileRead;\n' +
                   '\n' +
                   'function restoredata() {\n' +
                   '  var inputName = document.getElementById("name").files[0];\n' +
                   '  //console.log(inputName);\n' +
                   '  reader.readAsText(inputName);\n' +
                   '}\n' +
                   '\n' +
                   'function handleFileRead(event) {\n' +
                   '  var save = JSON.parse(reader.result);\n' +
                   '  //console.log(save)\n' +
                   '  for (var i in save) {\n' +
                   '    //console.log(\'Key \' + i + \': \' + save[i])\n' +
                   '    window.localStorage.setItem(i, save[i]);\n' +
                   '  }\n' +
                   '  window.location.reload(false);\n' +
                   '}\n' +
                   '\n' +
                   'function backupdata() {\n' +
                   '  save = {}\n' +
                   '  for (var i = 0; i < localStorage.length; i++) {\n' +
                   '    var key = localStorage.key(i)\n' +
                   '    save[key] = localStorage.getItem(key);\n' +
                   '    console.log(save)\n' +
                   '  }\n' +
                   '  var a = window.document.createElement(\'a\');\n' +
                   '  a.href = window.URL.createObjectURL(new Blob([JSON.stringify(save)], {type: \'text/plain\'}));\n' +
                   '  a.download = \'save.json\';\n' +
                   '  document.body.appendChild(a);\n' +
                   '  a.click();\n' +
                   '  document.body.removeChild(a);\n' +
                   '}\n' +
                   '</script>')

    htmlfile.close()
    print("Done building Main webpage\n")


def comicheader(htmlfile, pagecount, filename):
    htmlfile.write('<!DOCTYPE html>\n' +
                   '<html style="height:100%">\n' +
                   '<head>\n' +
                   '<title>' + filename + '</title>\n' +
                   '<script>\n' +
                   '  window.addEventListener("load", function() {\n' +
                   '    loadVars();\n' +
                   '  });\n' +
                   '</script>\n' +
                   '</head>\n' +
                   '<body style="overflow:hidden; height:100%">\n' +
                   '<div style="left:8px; right:12px; height:55px; background-color:grey; text-align:center">\n' +
                   '  <a href="javascript:progressFirst()">First</a>\n' +
                   '  <label for="' + filename + '">1</label>\n' +
                   '  <progress id="' + filename + '" style="width:75%" max="' + str(pagecount) + '" value="1"><span>1</span>/' + str(pagecount) + '</progress>\n' +
                   '  ' + str(pagecount) + '\n' +
                   '  <a href="javascript:progressLast()">Last</a>\n' +
                   '  <br />\n' +
                   '  <a id="page">Page 1</a>\n' +
                   '  <br />\n' +
                   '  <div style="left:8px; height:10px; width:300px; float:left">\n' +
                   '    <a href="Webcomic.html">Home</a>\n' +
                   '  </div>\n' +
                   '  <a href="javascript:progressPrevious()"><- Prev</a>\n' +
                   '  <a href="javascript:progressNext()">Next -></a>\n' +
                   '  <div style="right:12px; height:10px; width:300px; float:right">\n' +
                   '  </div>\n' +
                   '</div>\n')


def comicbody(htmlfile):
    htmlfile.write('<div style="position:absolute; top:63px; bottom:9px; left:8px; right:12px">\n' +
                   # left off allow-forms and allow-popups. Could probably be added, but likely not necessary
                   # allow-top-navigation is what allowed Sister Claire to break out of iframe
                   '<iframe sandbox="allow-same-origin allow-scripts allow-pointer-lock" ' +
                   'src="" name="ifrm" width="100%" height="100%">\n' +
                   '  <p>Your browser does not support iframes.</p>\n' +
                   '</iframe>\n' +
                   '</div>\n' +
                   '</body>\n' +
                   '</html>\n')


def comicscripts(htmlfile, pagecount, filename, reloadrequired=False):
    htmlfile.write('<script type="text/javascript">\n' +
                   'var progressBar = document.getElementById(\'' + filename + '\');\n' +
                   'var myposition = progressBar.value;\n' +
                   'var myframe = document.getElementsByName(\'ifrm\')[0];\n' +
                   'function progressNext() {\n' +
                   '  if (myposition + 1 > comics[0]) {\n' +
                   '    //alert(\'no more comics\');\n' +
                   '    window.location.href = \'Webcomic.html\'\n' +
                   '    return;\n' +
                   '  }\n' +
                   '  myposition = myposition + 1;\n' +
                   '  updateProgress();\n' +
                   '}\n' +
                   'function progressPrevious() {\n' +
                   '  if (myposition - 1 < 1) {\n' +
                   '    alert(\'Already at first comic\');\n' +
                   '    return;\n' +
                   '  }\n' +
                   '  myposition = myposition - 1;\n' +
                   '  updateProgress();\n' +
                   '}\n' +
                   'function progressFirst() {\n' +
                   '  myposition = 1;\n' +
                   '  updateProgress();\n' +
                   '}\n' +
                   'function progressLast() {\n' +
                   '  myposition = comics[0];\n' +
                   '  updateProgress();\n' +
                   '}\n' +
                   'function updateProgress() {\n' +
                   '  progressBar.value = myposition;\n' +
                   '  progressBar.getElementsByTagName(\'span\')[0].textContent = myposition\n' +
                   '  document.getElementById(\'page\').innerHTML = "Page " + myposition;\n' +
                   '  localStorage.setItem(\'' + filename + '\', myposition);\n' +
                   '  myframe.src = comics[myposition];\n')

    if (reloadrequired):
        htmlfile.write('  myframe.reload(true);\n')

    htmlfile.write('}\n' +
                   'function loadVars() {\n' +
                   '  myposition = localStorage.getItem(\'' + filename + '\');\n' +
                   '  if (myposition == null) {\n' +
                   '    myposition = 1;\n' +
                   '  } else {\n' +
                   '    myposition = parseInt(myposition, 10);\n' +
                   '  }\n' +
                   '  window.comics = [\n' +
                   '    ' + str(pagecount))  # comma and newline are part of loop

    with open(os.path.join('webcomic', filename), 'r') as f:
        for line in f:
            if line != "":
                htmlfile.write(',\n    "' + line.rstrip('\n') + '"')

    htmlfile.write('\n' +
                   '  ];\n' +
                   '  updateProgress();\n' +
                   '}\n' +
                   '</script>')


if __name__ == "__main__":
    import sys
    #arg1 = pagecount int
    #arg2 = filename str
    #arg3 = reloadrequired bool
    arguments = len(sys.argv) - 1

    pages = sys.argv[1]
    file = sys.argv[2]
    reload = sys.argv[3]

    if (pages in ['-h', '--help', 'h', 'help', '/?']):
        print("<number of pages> <filename containing links> [True or False if reload if required]", file=sys.stderr)
        raise SystemExit
    elif (arguments < 2) or (arguments > 3):
        print("<number of pages> <filename containing links> [True or False if reload if required]", file=sys.stderr)
        raise SystemExit

    pages = int(pages)

    if reload is None:
        reload = False
    else:
        reload = True

    buildComicPage(pages, file, reload)
    #htmlTwoKinds(50, 'TwoKinds')
