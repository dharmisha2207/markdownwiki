import re
import os

def Text_Parse(mdstr):

    #Blank Lines

    if(mdstr == ""):
        mdstr="<br>"
        return mdstr

    #Bold and Italics
    bold_italics_patt=re.compile(r'\*\*\*.+\*\*\*|\_\_\*.+\_\_\*|\*\*\_.+\*\*\_')
    matches=bold_italics_patt.finditer(mdstr)
    for match in matches:
        str=match.group()
        l=len(str)
        t=str[3:(l-3)]
        mdstr=mdstr.replace(str,"<em><strong>"+t+"</em></strong>")

    # Bold
    bold_patt = re.compile(r'\*\*.+\*\*|\_\_.+\_\_')
    matches = bold_patt.finditer(mdstr)
    for match in matches:
        str = match.group()
        l = len(str)
        t=str[2:(l - 2)]
        mdstr=mdstr.replace(str, "<strong>" + t + "</strong>")

    # Italics
    italics_patt = re.compile(r'\*.+\*|\_.+\_')
    matches = italics_patt.finditer(mdstr)
    for match in matches:
        str = match.group()
        l = len(str)
        t = str[1:(l - 1)]
        x="<em>" + t + "</em>"
        mdstr=mdstr.replace(str,x)

    # Images

    image_patt = re.compile(r'!\[.*\]\(.+\)')
    matches = image_patt.finditer(mdstr)
    for match in matches:
        str = match.group()
        p = ""
        q = ""
        i = 2
        while str[i] != ']':
            p = p + str[i]
            i = i + 1
        i += 1
        if str[i] == '(':
            i += 1
            while str[i] != ')':
                q = q + str[i]
                i = i + 1

        x = "<img src= " + q + " alt= " + p + "><br>"
        mdstr = mdstr.replace(str, x)

    #Hyperlinks
    link_patt=re.compile(r'\[.*\]\(.+\)')
    matches = link_patt.finditer(mdstr)
    for match in matches:
        str = match.group()
        p=""
        q=""
        i=1
        while str[i]!=']':
            p=p+str[i]
            i=i+1
        i+=1
        if str[i]=='(':
            i += 1
            while str[i] != ')':
                q = q + str[i]
                i = i + 1

        x ="<a href=" +q+">"+p + "</a>"
        mdstr = mdstr.replace(str, x)


    return mdstr




def Ulist_Parse(ulist):
    htmlstr="<ul>\n"
    for element in ulist:
        htmlstr+="<li>"+Text_Parse(element)+"</li>\n"
    htmlstr+="</ul>\n"
    return htmlstr

def Olist_Parse(olist):
    htmlstr="<ol>\n"
    for element in olist:
        htmlstr+="<li>"+Text_Parse(element)+"</li>\n"
    htmlstr+="</ol>"
    return htmlstr




def Parse_Markdown(mdstr):
    htmlstr=""
    line_list=mdstr.splitlines()
    i=0
    while i<len(line_list):
        #paragraph_patt=re.compile()
        #code_patt=re.compile()

        currline = line_list[i]

        #Heading Parsing

        heading1_patt = re.compile(r'# +')
        heading2_patt = re.compile(r'## +')
        heading3_patt = re.compile(r'### +')
        heading4_patt = re.compile(r'#### +')
        heading5_patt = re.compile(r'##### +')
        heading6_patt = re.compile(r'###### +')


        if re.search(heading6_patt, currline, flags=0)!=None:
            Heading=re.split(r'###### +', currline, flags=re.IGNORECASE)
            htmlstr+="<h6>"+Heading[1]+"</h6>"
            i+=1
            continue
        if re.search(heading5_patt, currline, flags=0)!=None:
            Heading=re.split(r'##### +', currline, flags=re.IGNORECASE)
            htmlstr+="<h5>"+Heading[1]+"</h5>"
            i += 1
            continue
        if re.search(heading4_patt, currline, flags=0)!=None:
            Heading=re.split(r'#### +', currline, flags=re.IGNORECASE)
            htmlstr+="<h4>"+Heading[1]+"</h4>"
            i += 1
            continue
        if re.search(heading3_patt, currline, flags=0)!=None:
            Heading=re.split(r'### +', currline, flags=re.IGNORECASE)
            htmlstr+="<h3>"+Heading[1]+"</h3>"
            i += 1
            continue
        if re.search(heading2_patt, currline, flags=0)!=None:
            Heading=re.split(r'## +', currline, flags=re.IGNORECASE)
            htmlstr+="<h2>"+Heading[1]+"</h2>"
            i += 1
            continue
        if re.search(heading1_patt, currline, flags=0)!=None:
            Heading=re.split(r'# +', currline, flags=re.IGNORECASE)
            htmlstr+="<h1>"+Heading[1]+"</h1>"
            i += 1
            continue

        #Horizontal Rule Parsing

        horizontal_line_patt=re.compile(r'\*\*\*+ *|---+ *|___+ *')
        if re.search(horizontal_line_patt, currline, flags=0) != None:
            HR = re.split(r'\*\*\*+ *|---+ *|___+ *', currline, flags=re.IGNORECASE)
            if HR[0]=='' and HR[1]=='':
                htmlstr +="\n<hr>\n"
                i += 1
                continue
        #Blockquote Parsing

        #if(currline[0]=='>'):
        #    bq_text=""+currline[1:]

        #    if(i<len(line_list)-1):
        #        nextline = line_list[i + 1]
        #        while(nextline[0]== '>'):
        #            bq_text=bq_text+ "\n"+nextline[1:]
        #            if(i<len(line_list)-1):
        #                i=i+1
        #                nextline=line_list[i]
        #            else:
        #                break
        #        if(i<len(line_list)-1):
        #            i=i-1
        #    htmlstr=htmlstr+"\n<blockquote>\n"+Parse_Markdown(bq_text)+"\n</blockquote>"
        #    continue

        #Unordered List Parsing

        ulist_patt=re.compile(r'-.+|\+.+')
        #scount=0
        #for c in currline:
        #    if c=='*':
        #        scount+=1
        #if (scount%2==1):
        #    ele_list=[]
        #    nextline=line_list[i]
        #    if i< len(line_list)-1:
        #        while (scount%2==1) and i< len(line_list)-1:
        #            ele_list.append(nextline[1:])
        #            i+=1
        #            nextline = line_list[i]
        #            scount=0
        #            for c in nextline:
        #                if c == '*':
        #                    scount += 1
        #        if i== len(line_list)-1:
        #            scount = 0
        #            for c in nextline:
        #                if c == '*':
        #                    scount += 1
        #            if(scount%2==1):
        #                ele_list.append(nextline[1:])
        #            else:
        #                i=i-1
        #        else:
        #            i=i-1
        #    else:
        #        ele_list.append(currline[1:])

        #    htmlstr+=Ulist_Parse(ele_list)
        #    i += 1
        #    continue


        if ((re.search(ulist_patt, currline, flags=0) != None)):
            UL = re.split(r'-.+|\+.+', currline, flags=re.IGNORECASE)
            if (UL[0]=='' and UL[1]==''):
                ele_list=[]
                #nextline=currline
                #if i< len(line_list)-1:
                    #while (nextline[1]=='-' or nextline[1]=='+') and i< len(line_list)-1:
                        #ele_list.append(nextline[1:])
                        #i+=1
                        #nextline = line_list[i]
                    #if i== len(line_list)-1:
                        #if (nextline[0]=='-' or nextline[0]=='+'):
                            #ele_list.append(nextline[1:])
                        #else:
                            #i=i-1
                    #else:
                        #i=i-1
                #else:
                    #ele_list.append(currline[1:])

                ele_list.append(currline[1:])
                htmlstr+=Ulist_Parse(ele_list)
                i += 1
                continue


        #Ordered List Parsing

        #htmlstr += Olist_Parse()


        #Text Parsing
        htmlstr += Text_Parse(currline)+"\n"
        i+=1



    return htmlstr




#Creates a html file with same name given a Markdown file

def Parse_File(fname):
    f=open(fname,"r")
    markdown_text= f.read()
    html_text="<html>\n"+Parse_Markdown(markdown_text)+"\n</html>"
    f_html_name="Html_Articles/"+fname[18:]
    f_html=open(f_html_name[:-2]+"html","w")
    f_html.write(html_text)
    

def Parse_Markdown_str(mdstr):
    html_text="<html>\n"+Parse_Markdown(mdstr)+"\n</html>"
    return html_text

directory="Markdown_Articles"

for fname in os.listdir(directory):
    f=os.path.join(directory,fname)

    if os.path.isfile(f):
        print(f)
        Parse_File(f)





