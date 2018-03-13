
import os
from xlrd import open_workbook
from xlwt import Workbook
from xlutils.copy import copy
cardList = ['하나','신한','국민','삼성','현대','Tpay','롯데']
sheets = []

wkbk = Workbook()


for card in cardList:
  filelist = os.listdir(card+'/')
  idx = 0
  for file in filelist:
    try:
      outrow_idx = 0
      insheet = open_workbook(card + '/' + file).sheets()[0]
      outsheet = wkbk.add_sheet(card + str(idx))
      for row_idx in range(insheet.nrows):
        for col_idx in range(insheet.ncols):
          outsheet.write(outrow_idx, col_idx,
                         insheet.cell_value(row_idx, col_idx))
        outrow_idx += 1
    except:
      print(card + '/' + file, '오류')
    """
    try:
      rb = open_workbook(card + '/' + file, on_demand=True, formatting_info = True)
      # Copy into a new workbook
      wb = copy(rb)
      # Rename to 'test1' as the original post asked for
      ws = wb.get_sheet(0)
      ws.name = card+str(idx)
      idx += 1
      sheets.append(ws)
    except:
      print(card + '/' + file, '오류')

wb._Workbook__worksheets = sheets
wb.save("output.xls")
"""
wkbk.save(r'./합쳐진엑셀.xls')