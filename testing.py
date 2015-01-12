import xlrd

workbook = xlrd.open_workbook('itemDescriptions.xlsx')
worksheet = workbook.sheet_by_name('Stats')
num_rows = worksheet.nrows - 1
num_cells = worksheet.ncols - 1
curr_row = 1
ID = int(input("What item ID? >>> "))
queryType = input("What item details do you want? (name, stats, rarity) >>> ")
while curr_row < num_rows:
    if worksheet.cell_value(curr_row, 0) == ID:
        if queryType == 'name':
            print (worksheet.cell_value(curr_row, 1), worksheet.cell_value(curr_row, 2))
        elif queryType == "stats":
            print ("A: ", worksheet.cell_value(curr_row, 4), ". D: ", worksheet.cell_value(curr_row, 5), ". S: ", worksheet.cell_value(curr_row, 6))
        elif queryType == "rarity":
            print ("Rareness: ", worksheet.cell_value(curr_row, 3))
        else:
            print ("Make sure you select a proper option. Don't use any capitals!")
    curr_row += 1