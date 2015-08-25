import  os, sys, requests

class GetFiles():

    def getFile(self, dlFile, fromUrl, verbose=0):
        head = requests.head(fromUrl)
        #print head.headers
        #req = urllib2.Request(fromUrl)
        #header_request = req.get_method = lambda : 'HEAD'
        #header_response = urllib2.urlopen(header_request)
        loop = 1
        existSize = 0
        overwrite_confirmed = False
        ##myUrlclass = GetFiles(  )
        custom_header = {}
        webSize = int(head.headers['content-length'])
        if os.path.exists(dlFile):
            existsSize = os.path.getsize(dlFile)
            if (existsSize < webSize):
                print "The file named %s already exists in this directory and seems to be incomplete. Do you want to continue downloading?" % (dlFile)
            else:
                print "The file named %s already exists in this directory. Do you want to overwrite it?" % (dlFile)
            print "Type 'yes' to continue or type 'no' to cancel"
            while(overwrite_confirmed == False):
                answer = raw_input('-->')
                if answer == "yes":
                    break
                elif answer == "no":
                    exit()
                else:
                    print "Please write a correct answer."
                    continue
            outputFile = open(dlFile,"ab")

            # If the file exists, then download only the remainder
            #req.add_header("Range","bytes={}-{}".format([existSize, header_response.info()['Content-Length']]))
            ##myUrlclass.addheader("Range","bytes=%s-" % (existSize))
            custom_header = {"Range":"bytes=%s-%s" %((existSize, head.headers['content-length']))}
        else:
            if (overwrite_confirmed):
                os.remove(outputFile)
            outputFile = open(dlFile,"wb")
        ##webPage = myUrlclass.open(fromUrl)
        #print custom_header
        response = requests.get(fromUrl, headers=custom_header, stream=True)
        #print response.headers
        if verbose:
            for k, v in response.headers.items():
                print k,"=", v
            
        #If we already have the whole file, there is no need to download it again
        numBytes = 0
        ##webSize = int(webPage.headers['Content-Length'])
        #webSize = int(head.headers['content-length'])
        if webSize == existSize:
            if verbose: print "File (%s) was already downloaded from URL (%s)"%(dlFile, fromUrl)
        else:
            if verbose: print "Downloading %d more bytes" % (webSize-existSize)
            #while 1:
            for chunk in response.iter_content(8192):
                outputFile.write(chunk)
                numBytes = numBytes + len(chunk)
               
                #data = response.content(8192)
                #if not data:
                #    break
                #outputFile.write(data)
                #numBytes = numBytes + len(data)
                
        response.close(  )
        outputFile.close(  )
                    
        if verbose:
            print "downloaded", numBytes, "bytes from", fromUrl
        return numBytes

opener = GetFiles()
opener.getFile("100MB-newark.bin","http://speedtest.newark.linode.com/100MB-newark.bin",1)
