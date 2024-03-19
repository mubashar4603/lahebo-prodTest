import openpyxl
from openpyxl.workbook import Workbook


def getRows(file, sheetName):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return sheet.max_row


def getColumns(file, sheetName):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return sheet.max_column


# read single value in a cell of excell
def readData(file, sheetName, rowno, columnno):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return sheet.cell(row=rowno, column=columnno).value


# write single value in a cell of excell
def writeData(file, sheetName, rowno, columnno, data):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    workbook.save(file)
    return sheet.cell(row=rowno, column=columnno, value=data)


#write list data into excel in rows
def data_to_excel(data, filename):
    """
    Converts a list of lists to an Excel file.
    Args:
    - data (list of lists): The data to be written to the Excel file.
    - filename (str): The name of the Excel file to be saved.
    """
    # Create a new Excel workbook
    wb = Workbook()
    # Get the active worksheet
    ws = wb.active
    # Write the data to the worksheet
    for row in data:
        ws.append(row)
    # Save the workbook to a file
    wb.save(filename)

