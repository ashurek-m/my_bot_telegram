import pandas as pd


def item_filter(item, data):
    df_exped_filtr = data[data['N° ITEM'] == item].reset_index(drop=True)
    tech_proc = df_exped_filtr.loc[0, 'Потенциальные проблемы']
    return tech_proc

path = 'W:\\Theoretical Planning\\03 - План отгрузки (Planification)\\План отгрузки\\EXPED. IDM-Direct.xlsb'
df_exped = pd.read_excel(path, sheet_name='Текущий', engine='pyxlsb', header=4)
df_exped.dropna(subset=['Наименование детали'], inplace=True)
df_exped = df_exped.reset_index(drop=True)
