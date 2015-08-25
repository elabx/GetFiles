import urllib, os

class myURLOpener(urllib.FancyURLopener):
    
    def getFile(self, dlFile, fromUrl, verbose=0):
        loop = 1
        existSize = 0
        myUrlclass = myURLOpener(  )
        if os.path.exists(dlFile):
            outputFile = open(dlFile,"ab")
            existSize = os.path.getsize(dlFile)
            # If the file exists, then download only the remainder
            myUrlclass.addheader("Range","bytes=%s-" % (existSize))
        else:
            outputFile = open(dlFile,"wb")
        webPage = myUrlclass.open(fromUrl)
        if verbose:
            for k, v in webPage.headers.items(  ):
                print k,"=", v
            
    # If we already have the whole file, there is no need to download it again
        numBytes = 0
        webSize = int(webPage.headers['Content-Length'])
        if webSize == existSize:
            if verbose: print "File (%s) was already downloaded from URL (%s)"%(dlFile, fromUrl)
        else:
            if verbose: print "Downloading %d more bytes" % (webSize-existSize)
            while 1:
                data = webPage.read(8192)
                if not data:
                    break
                outputFile.write(data)
                numBytes = numBytes + len(data)
                
        webPage.close(  )
        outputFile.close(  )
                    
        if verbose:
            print "downloaded", numBytes, "bytes from", webPage.url
        return numBytes

opener = myURLOpener()
opener.getFile("100MB-newark.bin","http://www.oreilly.com/openbook/cgi/ch03_04.html",1)
