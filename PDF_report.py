# -*- coding: utf-8 -*-
PATH = 'static/fonts/'

import os
import datetime
from reportlab.platypus import Image, BaseDocTemplate, SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib import colors
from reportlab.lib.units import inch, cm
# для шрифтов
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import ttfonts

# размеры страниц
from reportlab.lib.pagesizes import A4, landscape

class genPDF(object):
    Title = u"Привет, Мир!"
    styles = getSampleStyleSheet()
    font_name = 'Times New Roman'
    font_size = 9

    def __init__(self):
        #self._set_registerFont()
        self.setStyle()

    def _set_registerFont(self):
        Times_New_Roman = ttfonts.TTFont('Times New Roman', PATH + "times.ttf")
        pdfmetrics.registerFont(Times_New_Roman)

        Times_New_Roman_Bold = ttfonts.TTFont('Times New Roman Bold', PATH + "timesbd.ttf")
        pdfmetrics.registerFont(Times_New_Roman_Bold)

    def _set_font(self, canvas):
        canvas.setFont(self.font_name, self.font_size)

    def myFirstPage(self, canvas, doc):
        canvas.saveState()
        self._set_font(canvas)
        canvas.restoreState()

    def myLaterPages(self, canvas, doc):
        canvas.saveState()
        self._set_font(canvas)
        canvas.restoreState()

    def run(self, m):
        # m = {'customer': 'Pak', 'contacts': '89161234567', 'place': 'Rostov', 'datetime': '18-00', 'count_tables': '50',
        #      'count_peoples': '100', 'payer': 'Pak', 'type': 'Marriage', 'comment': 'test',
        #      'menu': [{'name': 'Суп', 'value': 2, 'price': '500', 'weight': '300', 'photo': '1.jpg'},
        #               {'name': 'Салат', 'value': 2, 'price': '200', 'weight': '400', 'photo': '2.jpeg'},
        #               {'name': 'Десерт', 'value': 3, 'price': '600', 'weight': '300', 'photo': '3.jpg'}]}

        DocName = datetime.datetime.now().strftime('genpdf_%Y%m%d_%H%M.pdf')
        doc = SimpleDocTemplate(DocName,
                                pagesize=A4,# размер страницы == портретный A4
                                leftMargin=1 * cm,# отступ слева
                                rightMargin=2 * cm,# отступ справа
                                bottomMargin=2 * cm,# отступ сверху
                                topMargin=2 * cm,# отступ снизу
                                )
        style = self.styles["Normal"]


        DataTable = [['ФИО', m['customer']],
                     ['Контакт', m['contacts']],
                     ['Место', m['place']],
                     ['Дата и время', m['datetime']],
                     ['Количество столов', m['count_tables']],
                     ['Количество людей', m['count_peoples']],
                     ['Плательщик', m['payer']],
                     ['Вид мероприятия', m['type']],
                     ['Примечания', m['comment']]]

        GridObj = Table(DataTable,
                        colWidths = [100, 300],
                        rowHeights = None,
                        style = self._style,
                        splitByRow = 1,
                        #repeatRows = 1,
                        #repeatCols = 0,
                        )


        DataTable1 = [ [ "Название","Кол-во","Цена","Вес" ] ]

        for i in m["menu"]:

            I = Image(f"static/{i['photo']}")
            I.drawHeight = 1 * inch * I.drawHeight / I.drawWidth
            I.drawWidth = 1 * inch

            buf = []

            buf.append(i["name"])
            buf.append(i["value"])
            buf.append(i["price"])
            buf.append(i["weight"])

            buf.append(I)

            DataTable1.append(buf)


        GridObj1 = Table(DataTable1,
                        colWidths = [80, 80, 80, 80, 80],
                        rowHeights = None,
                        style = self._style,
                        splitByRow = 1,
                        #repeatRows = 1,
                        #repeatCols = 0,
                        )


        total = sum([int(i["value"]) * int(i["price"]) for i in m['menu']])

        # s = []
        # for i in m["menu"]:
        #     s.append( int(i["value"]) * int(i["price"]))
        # total = sum(s)


        tips = total/10
        total_with_tips = total + tips
        total_for_person = total_with_tips/int(m["count_peoples"])


        DataTable2 = [['Итого по мероприятию', total],
                      ['Обслуживание 10%', tips],
                      ['Итого по мероприятию с обслуживанием', total_with_tips],
                      ['Сумма на человека', total_for_person]]

        GridObj2 = Table(DataTable2,
             colWidths=[300, 100],
             rowHeights=None,
             style=self._style,
             splitByRow=1,
             # repeatRows = 1,
             # repeatCols = 0,
             )

        # насколько я понял этот код создает вторую таблицу и в тогда надо вставить в doc.build([BGridObj])
        # BGridObj = Table([[GridObj,GridObj]],
        #                 colWidths = [320,320,],
        #                 rowHeights = None,
        #                 style = self._style,
        #                 splitByRow = 1,
        #                 repeatRows = 1,
        #                 #repeatCols = 0,
        #                 )
        doc.build([GridObj, GridObj1, GridObj2], onFirstPage = self.myFirstPage, onLaterPages = self.myLaterPages)
    #----------------------------------------------------------------------------------------------------------
    # установка стилей и шрифтов
    def setStyle(self, style = None):
        self._set_registerFont()
        if not style:
            self._style = [('TEXTCOLOR', (0,0), (0,-1), colors.blue),
                           ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                           ('VALIGN', (0,0), (0,-1), 'TOP'),
                           ('TEXTCOLOR', (0,0), (-1,-1), colors.black),
                           ('INNERGRID', (0,0), (-1,-1), 0.1, colors.black),
                           ('BOX',(0,0),(-1,-1),0.1,colors.black),
                           ('FONTNAME', (0,0),(-1,-1), self.font_name),
                           ('FONTSIZE', (0,0),(-1,-1), self.font_size),
                          ]
        else:
            self._style = style


if __name__ == '__main__':
    genPDF().run()