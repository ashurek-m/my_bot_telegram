import pandas as pd


def item_filter(item, data):
    list_q = []
    df_exped_filtr = data[data['N° ITEM'] == item].reset_index(drop=True)
    tech_proc_order = df_exped_filtr.loc[0, 'Индекс RTB']
    tech_proc_name = df_exped_filtr.loc[0, 'Наименование детали']
    tech_proc_tp = df_exped_filtr.loc[0, 'Потенциальные проблемы']
    list_q.append(str(int(tech_proc_order)))
    list_q.append(str(tech_proc_name))
    list_q.append(str(tech_proc_tp))
    tech_proc = ', '.join(list_q)
    return tech_proc


def filter_by_orders():

    return

def text_1(t):
    return t


path = 'W:\\Theoretical Planning\\03 - План отгрузки (Planification)\\План отгрузки\\EXPED. IDM-Direct.xlsb'
df_exped = pd.read_excel(path, sheet_name='Текущий', engine='pyxlsb', header=4)
df_exped.dropna(subset=['Наименование детали'], inplace=True)
df_exped = df_exped.reset_index(drop=True)
