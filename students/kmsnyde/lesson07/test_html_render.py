# -*- coding: utf-8 -*-
"""
Created on Wed May  2 18:03:36 2018

@author: Karl M. Snyder
"""

"""
test code for html_render.py

This is just a start -- you will need more tests!
"""

import io
import pytest

# import * is often bad form, but makes some sense for testing.
from html_render import *


# utility function for testing render methods
# needs to be used in multiple tests, so we write it once here.
def render_result(element, ind=""):
    """
    calls the element's render method, and returns what got rendered as a
    string
    """
    # the StringIO object is a "file-like" object -- something that
    # provides the methods of a file, but keeps everything in memory
    # so it can be used to test code that writes to a file, without
    # having to actually write to disk.
    outfile = io.StringIO()
    element.render(outfile, ind)
    return outfile.getvalue()

########
# Step 1
########

#def test_init():
#    """
#    This only tests that it can be initialized with and without
#    some content -- but it's a start
#    """
#    e = Element()
#    e = Element("this is some text")
#test_init()
#
#def test_append():
#    """
#    This tests that you can append text
#
#    It doesn't test if it works --
#    that will be covered by the render test later
#    """
#    e = Element("this is some text")
#    e.append("some more text")
#test_append()
#
#def test_render_element():
#    """
#    Tests whether the Element can render two pieces of text
#    So it is also testing that the append method works correctly.
#
#    It is not testing whether indentation or line feeds are correct.
#    """
#    e = Element("this is some text")
#    e.append("and this is some more text")
#
#    # This uses the render_results utility above
#    file_contents = render_result(e).strip()
#
#    # making sure the content got in there.
#    assert("this is some text") in file_contents
#    assert("and this is some more text") in file_contents
#
#    # make sure it's in the right order
#    assert file_contents.index("this is") < file_contents.index("and this")
#
#    # making sure the opening and closing tags are right.
#    assert file_contents.startswith("<html>")
#    assert file_contents.endswith("</html>")
#test_render_element()



# ########
# # Step 2
# ########


#tests for the new tags
#def test_html():
#    e = Html("this is some text")
#    e.append("and this is some more text")
#    file_contents = render_result(e).strip()
#    assert("this is some text") in file_contents
#    assert("and this is some more text") in file_contents
#    print(file_contents)
#    assert file_contents.endswith("</html>")
#test_html()
#
#
#
#def test_body():
#    e = Body("this is some text")
#    e.append("and this is some more text")
#    file_contents = render_result(e).strip()
#    assert("this is some text") in file_contents
#    assert("and this is some more text") in file_contents
#    print(file_contents)
#    assert file_contents.startswith("<body>")
#    assert file_contents.endswith("</body>")
#test_body()
#
#
#
#
#def test_sub_element():
#    """
#    tests that you can add another element and still render properly
#    """
#    page = Html()
#    page.append("some plain text.")
#    page.append(P("A simple paragraph of text"))
#    page.append("Some more plain text.")
#
#    file_contents = render_result(page)
#    print(file_contents) # so we can see it if the test fails
#
#     # note: The previous tests should make sure that the tags are getting
#     #       properly rendered, so we don't need to test that here.
#    assert "some plain text" in file_contents
#    assert "A simple paragraph of text" in file_contents
#    assert "Some more plain text." in file_contents
#    assert "some plain text" in file_contents
#    # but make sure the embedded element's tags get rendered!
#    print(file_contents)
#    assert "<p>" in file_contents
#    assert "</p>" in file_contents
#test_sub_element()


# #####################
# # indentation testing
# #####################


#def test_indent():
#     """
#     Tests that the indentation gets passed through to the renderer
#     """
#     html = Html("some content")
#     file_contents = render_result(html, ind="   ")
#
#     print(file_contents)
#     lines = file_contents.split("\n")
#     assert lines[0].startswith("   <")
#     assert lines[-1].startswith("   <")
#test_indent()
#
#
#def test_indent_contents():
#     """
#     The contents in a element should be indented more than the tag
#     by the amount in the indent class attribute
#     """
#     html = Element("some content")
#     file_contents = render_result(html, ind="")
#
#     print(file_contents)
#     lines = file_contents.split("\n")
#     assert lines[1].startswith(Element.indent)
#test_indent_contents()

#def test_multiple_indent():
#     """
#     make sure multiple levels get indented fully
#     """
#     body = Body()
#     body.append(P("some text"))
#     html = Html(body)
#
#     file_contents = render_result(html)
#
#     print(file_contents)
#     lines = file_contents.split("\n")
#     for i in range(3):  # this needed to be adapted to the <DOCTYPE> tag
#         assert lines[i + 1].startswith(i * Element.indent + "<")
#
#     assert lines[4].startswith(3 * Element.indent + "some")
#test_multiple_indent()

# this is for testing indenting -- we'll wait 'till we get to that
# def test_element_indent1():
#     """
#     Tests whether the Element indents at least simple content

#     we are expecting to to look like this:

#     <html>
#         this is some text
#     <\html>

#     More complex indentation should be tested later.
#     """
#     e = Element("this is some text")

#     # This uses the render_results utility above
#     file_contents = render_result(e).strip()

#     # making sure the content got in there.
#     assert("this is some text") in file_contents

#     # break into lines to check indentation
#     lines = file_contents.split('\n')
#     # making sure the opening and closing tags are right.
#     assert lines[0] == "<html>"
#     # this line should be indented by the amount specified
#     # by the class attribute: "indent"
#     assert lines[1].startswith(Element.indent + "thi")
#     assert lines[2] == "</html>"
#     assert file_contents.endswith("</html>")


########
# Step 3
########

#def test_title():
#    e = Title("this is some text")
#    file_contents = render_result(e).strip()
#    assert("this is some text") in file_contents
#    print(file_contents)
#    assert file_contents.startswith("<title>")
#    assert file_contents.endswith("</title>")
#test_title()

########
# Step 4
########

#def test_dict_args():
#    age = hr.Html()
#    head = hr.Head()
#    head.append(hr.Title("PythonClass = Revision 1087:"))
#    page.append(head)
#    body = hr.Body()
#    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                      "but this is enough  to show that we can do some text",
#                   cable="Verizon", power="BGE"))
#    page.append(body)
#    file_contents = render_result(page)
#    assert "cable=Verizon" in file_contents
#test_dict_args()

########
# Step 5
########

#def test_dict_args():
#    age = hr.Html()
#    head = hr.Head()
#    head.append(hr.Title("PythonClass = Revision 1087:"))
#    page.append(head)
#    body = hr.Body()
#    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                      "but this is enough  to show that we can do some text",
#                   cable="Verizon", power="BGE"))
#    body.append(hr.Hr())
#    page.append(body)
#    file_contents = render_result(page)
#    assert "<hr />" in file_contents
#test_dict_args()

########
# Step 6
########

#def test_link():
#    age = hr.Html()
#    head = hr.Head()
#    head.append(hr.Title("PythonClass = Revision 1087:"))
#    page.append(head)
#    body = hr.Body()
#    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                      "but this is enough  to show that we can do some text",
#                   cable="Verizon", power="BGE"))
#    body.append(hr.A("http://google.com", "link"))
#    page.append(body)
#    file_contents = render_result(page)
#    assert "href=http://google.com" in file_contents
#test_link()

########
# Step 7
########

#def test_step7():
#    page = hr.Html()
#    head = hr.Head()
#    head.append(hr.Title("PythonClass = Revision 1087:"))
#    page.append(head)
#    body = hr.Body()
#    body.append( hr.H(2, "PythonClass - Class 6 example") )
#    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                      "but this is enough  to show that we can do some text",
#                   style="text-align: center; font-style: oblique;"))
#    body.append(hr.Hr())
#    list = hr.Ul(id="TheList", style="line-height:200%")
#    list.append( hr.Li("The first item in a list") )
#    list.append( hr.Li("This is the second item", style="color: red") )
#    item = hr.Li()
#    item.append("And this is a ")
#    item.append( hr.A("http://google.com", "link") )
#    item.append("to google")
#    list.append(item)
#    body.append(list)   
#    page.append(body)
#    file_contents = render_result(page)
#    #print(file_contents)
#    assert "<ui id=TheList style=line-height:200%>" in file_contents
#test_step7()

########
# Step 8
########

def test_8():
    page = hr.Html()
    head = hr.Head()
    head.append( hr.Meta(charset="UTF-8") )
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append( hr.H(2, "PythonClass - Example") )
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                      "but this is enough  to show that we can do some text",
                      style="text-align: center; font-style: oblique;"))
    body.append(hr.Hr())
    list = hr.Ul(id="TheList", style="line-height:200%")
    list.append( hr.Li("The first item in a list") )
    list.append( hr.Li("This is the second item", style="color: red") )
    item = hr.Li()
    item.append("And this is a ")
    item.append( hr.A("http://google.com", "link") )
    item.append("to google")
    list.append(item)
    body.append(list)
    page.append(body)
    render_page(page, "test_html_output8.html")
    file_contents = render_result(page)
    #print(file_contents)
    assert "<meta charset=UTF-8 />" in file_contents
test_8()                                                                                                                                                                                             