**How to use:**<br/>
Just run:
```
python arXiv-metadata-extract.py '2019-11-19' '2019-11-22'
```
First script downloads all the articles from arXiv via its API and creates xml file; second script makes a neat html out of xml.<br/>
'2019-11-19' '2019-11-22' means range of data (both inclusive).  If you want only one date, you can omit second date.<br/>
Feel free to change your own preferences (of what articles are of interest to you) in the second script.<br/>

**Possible errors:**
On some systems, scripts don't work until you change file paths to global. <br/>

**Other notes:**
File "arXiv-articles.html" is given for illustrative purposes. You can open the file in any browser.<br/>

**Credits:**
Much of content for downloading arXiv metadata has been taken from https://github.com/rocksonchang/arXiv-metadata
