# GetFiles

## Description

GetFiles is a small python program that saves the contents of a URL to
a file or resumes the download if previously incomplete. It uses the
[Requests](http://www.python-requests.org/en/latest/) HTTP library.

GetFiles works by making a request to the URL and saving its contents
to a file. The not so secret sauce lies in checking up the file size in bytes
in a HEAD request, to later compare it to the current file size on
disk (if existent). If file already exists on path, a Range header is sent
along the request and the reponse object's content returned is streamed
according to the Range header values.

##Requirements

- Python 2.7.10 installed
- [Requests](http://www.python-requests.org/en/latest/)

##Usage

Download the GetFiles.py file to any directory on your computer. On
the command line terminal, navigate to the downloaded file location
and run the script according to following arguments:

```
python GetFiles.py url --v
```
If the URL doesn't end with a file name, the program will default the
file name to "file-dummy".

###Arguments:

`url`: The url you want to download. Must inlcude `http://`.

`--v`: Verbose. Prints the headers of the response, how many bytes are
left for download and total bytes transfered when finished.

###Example

```
python GetFiles.py http://google.com --v
```

##To-do

  - HTTP Error handling.
  - Catch keyboard interrumption.
  - Use hash for file content check.
  - Verbose adittions: Download bar, percentage complete update, size complete.
  - File dummy auto incremental value.
  - Detect content type and react accodingly.

## Sources

- [Requests library](http://www.python-requests.org/en/latest/)
- https://bytedebugger.wordpress.com/2014/05/19/tutorial-how-to-download-and-resume-files-using-python-and-urllib/
- https://www.safaribooksonline.com/library/view/python-cookbook/0596001673/ch11s06.html
- https://docs.python.org/2/library/argparse.html?highlight=argparse#type
