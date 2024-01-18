"""
Phuong Anh Nguyen
This very slow program is to create websites base on the user input.
The program could be faster if I can use a queue or at least more dataclasses.
The design is bad but the programmer is too exhausted and it's 11:24pm with the last edit, the programmer chose not to
erased everything and do it again.
"""
import sys
from dataclasses import dataclass
from typing import Any, Union, List
import turtle
FONTS= {"Arial":0,"Comic Sans Ms":1,"Lucida Grande":2,"Tahoma":3,"Verdana":4,"Helvetica":5,"Times New Roman":6}
COLORS={'peachpuff', 'slateblue', 'powderblue', 'lightcyan', 'chartreuse', 'moccasin', 'mediumseagreen', 'lawngreen', 'seagreen', 'mintcream', 'azure', 'goldenrod', 'lightblue', 'firebrick', 'lightseagreen', 'chocolate', 'yellowgreen', 'darkolivegreen', 'violet', 'ivory', 'sandybrown', 'wheat', 'mediumvioletred', 'bisque', 'lightgreen', 'cyan', 'hotpink', 'gray', 'indianred', 'antiquewhite', 'royalblue', 'yellow', 'indigo', 'lightcoral', 'darkslategrey', 'sienna', 'lightslategray', 'mediumblue', 'red', 'khaki', 'darkviolet', 'mediumorchid', 'darkblue', 'lightskyblue', 'turquoise', 'lightyellow', 'grey', 'whitesmoke', 'blueviolet', 'orchid', 'mediumslateblue', 'darkturquoise', 'coral', 'forestgreen', 'gainsboro', 'darkorange', 'cornflowerblue', 'lightsteelblue', 'plum', 'lavender', 'palegreen', 'darkred', 'dimgray', 'floralwhite', 'orangered', 'oldlace', 'darksalmon', 'lavenderblush', 'darkslategray', 'tan', 'cadetblue', 'silver', 'tomato', 'darkkhaki', 'slategray', 'maroon', 'olive', 'deeppink', 'linen', 'magenta', 'crimson', 'mistyrose', 'lime', 'saddlebrown', 'blanchedalmond', 'black', 'snow', 'seashell', 'darkcyan', 'gold', 'midnightblue', 'darkgoldenrod', 'palevioletred', 'fuchsia', 'teal', 'lightpink', 'darkgrey', 'mediumspringgreen', 'aquamarine', 'lightsalmon', 'navajowhite', 'darkgreen', 'burlywood', 'rosybrown', 'springgreen', 'purple', 'olivedrab', 'lightslategrey', 'orange', 'aliceblue', 'mediumaquamarine', 'navy', 'salmon', 'rebeccapurple', 'darkmagenta', 'limegreen', 'deepskyblue', 'pink', 'mediumpurple', 'skyblue', 'aqua', 'blue', 'slategrey', 'darkslateblue', 'honeydew', 'darkseagreen', 'paleturquoise', 'brown', 'thistle', 'lemonchiffon', 'peru', 'cornsilk', 'papayawhip', 'green', 'lightgoldenrodyellow', 'mediumturquoise', 'steelblue', 'lightgray', 'lightgrey', 'beige', 'palegoldenrod', 'darkgray', 'white', 'ghostwhite', 'dodgerblue', 'greenyellow', 'dimgrey', 'darkorchid'}
@dataclass
class Image:
    """
    A dataclass for Image, contain url and width
    """
    url: str
    width: Union[int,str]
class Paragraph:
    """
    A dataclass for paragraph, contains a title, content and a list of images
    """
    title: str
    content: str
    image: List
class Style:
    """
    A dataclass for style
    """
    font_color: str
    back_color: str
    head_color: str
    font_style: str
def write_image(image):
    """
    This function is to process one image to html
    :param image:
    :return: html string of the image
    """
    image_lines=''
    image_lines= "<img src="+image.url+" "+"width="+str(image.width)+"%"+" "+"class='center'>"+"\n"
    return image_lines
def get_list():
    """
    This function is get a list of images from the user
    :return: a list
    """
    choice=""
    image_lst=[]
    while choice=="":
        choice= input("Do you want to add image? [yes]")
        if choice =="yes":
            Image.url= input("Image file name:")
            image_lst.append(Image)
            choice=""
        else:
            return image_lst
    return image_lst
def write_images(image_list):
    """
    This function is to process  images to html
    :param image:
    :return: html string of the images
    """

    line=""
    lines=""
    if image_list==[]:
        return line
    else:
        for i in image_list:
            line= write_image(i)
            lines+=line
        return lines


def write_title(paragraph):
    """
    This function takes the input paragraph dataclass and create the html title
    :param paragraph:
    :return: a string of the paragraph title
    """
    title_line=''
    title_line= "<h2>"+paragraph.title+"\n</h2>"
    return title_line
def write_paragraph_with_images(paragraph):
    """
    This function takes a paragraph dataclass and turn it into a html string of paragraph and images
    :param paragraph:
    :return: a html format string
    """
    para_line=""
    para_line+= write_title(paragraph)
    para_line+= "<p>"+paragraph.content+"\n</p>\n"
    image_list=get_list()
    image_lines= write_images(image_list)
    para_line+=image_lines
    return para_line
def write_paragraphs_with_images():
    """
    This function loop and turn  into  html strings of paragraph and images until the user say something other than yes
    :param paragraph:
    :return: a html format string
    """

    para_lines=""
    para= Paragraph()
    choice=""
    while choice=="":
        choice=input("Do you wanna add another paragraph?[yes]")
        if choice=="yes":
            para.title= input("Title of your paragraph:")
            para.content= input("Content of your paragraph(single line):")
            para_lines+= write_paragraph_with_images(para)
            choice=""
        else:
            break
    return para_lines
def front_display():
    """
    This function shows the fonts options in turtle
    :return:
    """
    turtle.speed(0)
    turtle.up()
    turtle.goto(-140,130)
    turtle.setup(340,340)
    turtle.hideturtle()
    for i in FONTS:
        turtle.write(i,move=False,align="left",font=(i,14,"normal"))
        turtle.up()
        turtle.right(90)
        turtle.forward(40)
        turtle.left(90)
        turtle.down()
    turtle.done()
def create_style(style):
    """
    This function takes the style and create the head base on style_template.txt
    :param style:
    :return: a string
    """
    file_fix=open("style_template.txt")
    lines= file_fix.read()
    lines =lines .replace("@BACKCOLOR",style.back_color)
    lines =lines .replace("@HEADCOLOR",style.head_color)
    lines = lines .replace("@FONTCOLOR",style.font_color)
    lines =lines .replace("@FONTSTYLE",style.font_style)
    return lines
def create_head(head_title,style):
    """
    This function take the head title and the style to create the head string
    :param head_title:
    :param style:
    :return: a string
    """
    head_lines="<head>\n<title>"+head_title
    style_line= create_style(style)
    head_lines+="\n</title>"+style_line+"\n</head>\n"
    return head_lines
def choose_color():
    """
    This function prompt and check for the user input color
    :return: a color string
    """
    color=""
    while color=="":
        color= input("Choose the name of a color, or in format '#XXXXXX:")
        if color[0]=='#':
            if not len(color)==7:
                color=""
            else:
                return color

        else:
            if not color in COLORS:
                color=""
            else:
                return color
    return color
def choose_font():
    """
    This function get the fonts from the number the user input
    :return:
    """
    number=choose_font_number()
    font = ""
    for i in FONTS.keys():
        if FONTS[i] == number:
            font += i
            return font
    return font
def choose_font_number():
    """
    This function ask for the user input of the right number
    :return:
    """
    number= None
    while number is None:
        number= int(input("""Choose a font by its number.
        0: Arial, size 14
        1: Comic Sans MS, size 14
        2: Lucida Grande, size 14
        3: Tahoma, size 14
        4: Verdana, size 14
        5: Helvetica, size 14
        6: Times New Roman, size 14)\n"""))
        if 0<= number <= 6:
            return number
        else:
            return None
def wizard_mode():
    """
    This function ask the user everything to created an website
    :return: a html file
    """
    image=Image
    image.width=100
    style=Style()
    html_text="<!DOCTYPE html>\n<html>\n"
    head_title=input("What is the title of your website:")
    head= create_head(head_title,style)
    html_text+=head+"<body>\n"+"<h1>"+head_title+"\n</h1>\n<hr/>\n"
    para= Paragraph()
    para.title= input("Title of your paragraph:")
    para.content= input("Content of your paragraph(single line):")
    para_text= write_paragraph_with_images(para)
    html_text+=para_text
    para_next= write_paragraphs_with_images()
    html_text+=para_next+"\n</body>\n</html>"
    out_file= open("index.html","wt")
    for line in html_text:
        out_file.write(line)
    out_file.close()
    return out_file
def write_head_website(filename,style):
    """
    This function takes the filename and style dataclass to create the head string of the html file
    :param filename:
    :param style:
    :return: a string
    """
    head_title=""
    para=Paragraph
    para.title=''
    para.content=''
    lst_para=[]
    para.image=[]
    html_text = "<!DOCTYPE html>\n<html>\n"
    file=open(filename)
    for line in file:
        if head_title=="":
            head_title=line
            html_text+=create_head(head_title,style)
    file.close()
    return html_text
def write_body(filename,filename_list):
    """
    This function takes the filename and list of the filenames  to create the body string of the html file
    :param filename:
    :param filename_list: a list
    :return: a string
    """

    html_text="<body>\n"
    head_title=""
    para=Paragraph
    para.title=''
    para.content=''
    lst_para=[]
    para.image=[]
    file=open(filename)
    for line in file:
        if head_title=="":
            head_title=line
            html_text+="<h1>"+head_title+"</h1>\n"+ website_link(filename_list)
        elif line.strip()[:15]=="!new_paragraph":
            if len(line)>15:
                print(line+"\nContent error")
                raise SyntaxError
            elif para.title=="":
                pass
            else:
                para_line = ""
                para_line += write_title(para)+"\n"
                para_line+="<p>"+para.content+"\n</p>\n"
                html_text+= para_line
                html_text+= write_images(para.image)
                para.title=""
                para.content=""
                para.image=[]
        elif line[0:6]=="!title":
            para.title=line[6:]
        elif line[0:6]=="!image":
            line=line.split()
            image=Image
            image.url=line[1]
            if len(line)==3:
                image.width= line[2]
            else:
                image.width=100
            para.image.append(image)
        else:
            para.content+=line
    html_text+= write_title(para)+"\n"+"<p>"+para.content+"\n</p>\n"+write_images(para.image)
    file.close()
    return html_text
def website_mode(filename,style,filename_list):
    """
    This function takes the user in put in the command line, and return one html file
    """
    html_text=""
    html_text+= write_head_website(filename,style)
    html_text+= write_body(filename,filename_list)
    html_text+="\n</body>\n</html>"
    name=filename[:-4]+".html"
    out_file= open(name,"wt")
    for line in html_text:
        out_file.write(line)
    out_file.close()
    return out_file
def get_title(filename):
    """
    This function get the title of a file
    :param filename:
    :return: a stirng
    """
    title=""
    file=open(filename)
    for i in file:
        title= i
        return title
    return title
def website_link(filename_list):
    """
    This function returns a string to link the websites
    :param filename_list:
    :return:
    """
    title=""
    lines="<hr/>\n"
    if len(filename_list)>1:
        lines += "<p align='center'>"
        for i in filename_list:
            lines+='<a '
            title=get_title(i)
            lines+="href="+i[:-4]+".html"+">"+title+"</a>---"
        return lines+"\n</p>\n"
    else:
        return lines
def generate_filenames(filename_list):
    """
    This function return a list of html file names
    :param filename_list:
    :return:
    """
    names=[]
    for i in filename_list:
        name=i[:-4]+".html"
        names.append(name)
    return names
def main():
    """
    This function choose to use wizard or website mode base on the user input.
    :return:
    """
    style = Style
    print("Background Color")
    style.back_color= choose_color()
    print("You will now choose a font.")
    choice= input("Do you want to see what the fonts look like? [yes]")
    if choice=='yes':
        print("Close the window when you have made your choice")
        front_display()
    style.font_style= choose_font()
    print("Paragraph Text Color")
    style.font_color= choose_color()
    print("Heading Color")
    style.head_color=choose_color()
    if len(sys.argv)>1:
        if len(sys.argv)==2:
            file_name_list=sys.argv[1:]
            names= generate_filenames(file_name_list)
            file_name=sys.argv[1]
            website_mode(file_name,style,file_name_list)
            print("Your web page has been save as "+str(names).strip("[]"))
        else:
            file_name_list=sys.argv[1:]
            for i in range(1,len(sys.argv)):
                file_name= sys.argv[i]
                website_mode(file_name,style,file_name_list)
            names= generate_filenames(file_name_list)
            print("Your web page has been save as "+str(names).strip("[]"))
    else:
        wizard_mode()
        print("Your web page has been save as index.html ")
if __name__ == "__main__":
    main()