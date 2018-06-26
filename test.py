
# # def hello (c):
# #     c.drawString(100,800,"Hello World")
# #
# # c = canvas.Canvas("hello.pdf")
# #
# # hello(c)
# # c.showPage()
# # c.save()
#
#
#
# from reportlab.pdfgen import canvas
# from reportlab.lib import colors
# from reportlab.lib.pagesizes import inch, A4
# from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table
# from reportlab.lib.styles import getSampleStyleSheet
#
# doc = SimpleDocTemplate("static/3.pdf", pagesize=A4)
#
# elements = []
#
# styleSheet = getSampleStyleSheet()
#
# I = Image('static/1.jpg')
# I.drawHeight = 1.25*inch*I.drawHeight / I.drawWidth
# I.drawWidth = 1.25*inch
#
#
# P0 = Paragraph('''
#                <b>A pa<font color=red>r</font>a<i>graph</i></b>
#                <super><font color=yellow>1</font></super>''',
#                styleSheet["BodyText"])
#
# P = Paragraph('''
#     <para align=center spaceb=3>The <b>Pak Left
#     <font color=red>Logo</font></b>
#     Image</para>''',
#     styleSheet["BodyText"])
#
# data = [['A', 'B', 'C', P0, 'D'],
#         ['00', '01', '', [I,P], '04'],
#         ['10', '11', '12', [P,I], '14'],
#         ['20', '21', '22', '23', '24'],
#         ['30', '31', '32', '33', '34']]
#
# t = Table(data, style=[('GRID', (0, 0), (4, 4), 1, colors.green)])
#
# elements.append(t)
#
# # write the document to disk
# doc.build(elements)

print("test ",__name__)

if __name__ == "__main__":
    print("Hello")