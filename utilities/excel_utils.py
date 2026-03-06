import openpyxl


def get_excel_data(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row[0] is not None and row[1] is not None:
            data.append((row[0], row[1]))

    return data