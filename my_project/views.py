# I have created this file - Rohit
from django.http import HttpResponse
from django.shortcuts import render

#Text Utils
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home")

def about(request):
    s='''<h2> This is a place where you do text formating.</h2><br>
    Text Utils is developed by Rohit Agrawal, B.Tech CSE, 3rd Year.<br>
    Please do visit his codechef profile: <a href="https://www.codechef.com/users/rohit_1402">rohi_1402</a>.<br>
    Please connect with him in <a href="https://www.linkedin.com/in/rohit-agrawal-10313917b/">linkedin</a>.<br><br>
    <button onclick="goBack()">Go Back</button>
        <script>
          function goBack() {
            window.history.back();
          }
        </script>'''
    return HttpResponse(s)


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    #Check Checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    input = djtext

    #check which box is on

    #Remove Punctuations
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc == "on":
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext=analyzed
        params = {'purpose':'Removed Punctuations', 'original_text': input,'analyzed_text': djtext}
        
    #UPPER CASE
    if fullcaps =='on':
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext=analyzed
        params = {'purpose':'Changed to Upper Case', 'original_text': input,'analyzed_text': djtext}
        
    if newlineremover == 'on':
        analyzed =""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        djtext=analyzed
        params = {'purpose':'New Line Removed', 'original_text': input,'analyzed_text': djtext}
        
    if extraspaceremover == 'on':
        analyzed =""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        djtext=analyzed
        params = {'purpose':'Extra Space Removed', 'original_text': input,'analyzed_text': djtext}

    if charcounter == 'on':
        analyzed =""
        cnt=0
        for char in djtext:
            cnt=cnt+1
        s=" and Character count = " + str(cnt)
        djtext=djtext+s
        params = {'purpose':'Character Counter', 'original_text': input,'analyzed_text': djtext}

    if (charcounter != 'on' and extraspaceremover != 'on' and newlineremover != 'on' and fullcaps != 'on' and removepunc != "on"):
        return HttpResponse("""<h2> You have Not selected any option!!! Please try again. </h2><br>
        <button onclick="goBack()">Go Back</button>
        <script>
          function goBack() {
            window.history.back();
          }
        </script>""")
   
    else:
        return render(request, 'analyze.html', params)