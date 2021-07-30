import glob
import pandas as pd
path_to_excel_files = glob.glob('D:\\xls_to_csv\Customer.xlsx')
for excel in path_to_excel_files:
    xl = pd.ExcelFile(excel)

    for sheet in xl.sheet_names:
        out = excel.split('.')[0] +'_'+ sheet + '.csv'
        print(out)
        df_tmp = xl.parse(sheet)
        #print(out)
        #df = pd.read_excel(excel.sheet)
        df_tmp.to_csv(out)
