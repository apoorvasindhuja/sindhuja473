from xlwt import Workbook
wb= Workbook()
s1=wb.add_sheet('sheet1')
s2=wb.add_sheet('sheet2')
sheet1.write(1,0,"sindhu sanju")
wb.save('xlwt1.xls')
