import pandas as pd


def item_filter(item, data):
    df_exped_filtr = data[data['N° ITEM'] == item]
    print((df_exped_filtr))

path = 'W:\\Theoretical Planning\\03 - План отгрузки (Planification)\\План отгрузки\\EXPED. IDM-Direct.xlsb'
df_exped = pd.read_excel(path, sheet_name='Текущий', engine='pyxlsb', header=4)
df_exped.dropna(subset=['Наименование детали'], inplace=True)
df_exped = df_exped.reset_index(drop=True)
