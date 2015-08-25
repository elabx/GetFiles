# GetFiles

## Description

GetFiles is a small python program that saves the contents of a URL to
a file or resumes the download if previously incomplete. It uses the
[Requests](http://www.python-requests.org/en/latest/) HTTP library.

GetFiles works by making a request to the URL and saving its contents
to a file. The secret sauce lies in checking up the file size in bytes
in a HEAD request, to later compare it to the current file size on
disk (if existent). If file already exists on path, a Range header is sent
along the request and the reponse object's content returned is streamed
according to the Range header values.

##To-do

  - HTTP Error handling.
  - Catch keyboard interrumption.
  - Use hash for file content check.
  - Download bar, percentage complete update, size complete.
  - File dummy auto incremental value.

## Sources

- [Requests library](http://www.python-requests.org/en/latest/)
- https://bytedebugger.wordpress.com/2014/05/19/tutorial-how-to-download-and-resume-files-using-python-and-urllib/
- https://www.safaribooksonline.com/library/view/python-cookbook/0596001673/ch11s06.html
