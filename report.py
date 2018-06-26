from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import inch, A4
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
# pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
# pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
# pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))
#
doc = SimpleDocTemplate("static/3.pdf", pagesize=A4, )
#
canvas.setFont('Vera', 32)
canvas.drawString(10, 150, "Some text encoded in UTF-8")
canvas.drawString(10, 100, "In the Vera TT Font!")


# MyFontObject = ttfonts.TTFont('Arial', 'arial.ttf')
# pdfmetrics.registerFont(MyFontObject)

# Canvas.setFont(MyFontObject, 'Arial', 12)

m = {'customer': 'Pak', 'contacts': '89161234567', 'place': 'Rostov', 'datetime': '18-00', 'count_tables': '50',
     'count_peoples': '100', 'payer': 'Pak', 'type': 'Marriage', 'comment': 'test',
     'menu': [{'name': 'Суп', 'value': 23, 'price': '500', 'weight': '300', 'photo': '1.jpg'},
              {'name': 'Салат', 'value': 2, 'price': '200', 'weight': '400', 'photo': '2.jpeg'},
              {'name': 'Десерт', 'value': 3, 'price': '600', 'weight': '300', 'photo': '3.jpg'}]}


elements = []

styleSheet = getSampleStyleSheet()


def report(order):

    data = [['Name', order['customer']],
            ['Contacts', order['contacts']],
            ['Place', order['place']],
            ['Datetime', order['datetime']],
            ['Count_tables', order['count_tables']],
            ['Count_people', order['count_peoples']],
            ['Payer', order['payer']],
            ['Type', order['type']],
            ['Comment', order['comment']]]

    t = Table(data, style=[('GRID', (0, 0), (1, 8), 1, colors.black)])

    return t


# def menu (order):
#
#     photo = Image('static/1.jpg')
#     photo.drawHeight = 1.25 * inch * I.drawHeight / I.drawWidth
#     photo.drawWidth = 1.25 * inch
#
#     menu = [[['Фото', order['photo']], ['Наименование', order[menu['name']]], ['Количество', order['value']], ['Цена', order['price']], ['Выход', order['weight']], ['Количество', order['value']]],
#            [['Фото', order['photo']], ['Наименование', order['name']], ['Количество', order['value']], ['Цена', order['price']], ['Выход', order['weight']], ['Количество', order['value']]],
#            [['Фото', order['photo']], ['Наименование', order['name']], ['Количество', order['value']], ['Цена', order['price']], ['Выход', order['weight']], ['Количество', order['value']]]]
#
#    t = Table(menu, style=[('GRID', (0, 0), (5, 2), 1, colors.black)])
#
#     return t

elements.append(report(m))
# elements.append(menu[menu(m)])
doc.build(elements)
