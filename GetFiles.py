import  os, sys, requests, argparse

class GetFiles():

    def getFile(self, fromUrl, verbose=0):
        dlFile = fromUrl.split("/")[-1]
        print str(dlFile)
        print "this is the download file " + dlFile
        if dlFile == "":
            dlFile = "file-dummy"
        print "corrected download file " + dlFile
        head = requests.head(fromUrl)
       
        loop = 1
        existSize = 0
        overwrite_confirmed = False
        custom_header = {}
        webSize = int(head.headers['content-length'])
        if os.path.exists(dlFile):
            existSize = os.path.getsize(dlFile)
            if (existSize < webSize):
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
            custom_header = {"Range":"bytes=%s-%s" %((existSize, head.headers['content-length']))}
        else:
            if (overwrite_confirmed):
                os.remove(outputFile)
        outputFile = open(dlFile,"wb")
        response = requests.get(fromUrl, headers=custom_header, stream=True)
        #print "---->the output file" + outputFile
        if verbose:
            for k, v in response.headers.items():
                print k,"=", v
        numBytes = 0
    
        
        if webSize == existSize:
            if verbose: print "File (%s) was already downloaded from URL (%s)"%(dlFile, fromUrl)
        else:
            if verbose: print "Downloading %d more bytes" % (webSize-existSize)
            
            for chunk in response.iter_content(8192):
                outputFile.write(chunk)
                numBytes = numBytes + len(chunk)

        response.close(  )
        outputFile.close(  )
                    
        if verbose:
            print "downloaded", numBytes, "bytes from", fromUrl
        return numBytes

opener = GetFiles()
opener.getFile("http://speedtest.newark.linode.com/100MB-newark.bin",1)
