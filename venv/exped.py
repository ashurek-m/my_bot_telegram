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


def filter_by_orders(order, data):
    filter_list = []
    filter_list.append(order)
    filter_list.append(int('8' + str(order)))
    df_exped_filtr = data[data['Индекс RTB'].isin(filter_list)].reset_index(drop=True)
    return df_exped_filtr


def text_filter_by_order(order, data):
    df = filter_by_orders(order, data)
    if df.shape[0] !=0:
        list_2 = []
        list_3 = []
        for i in range(df.shape[0]):
            list_1 = []
            list_1.append(str(int(df.loc[i, 'Индекс RTB'])))
            list_1.append(str(df.loc[i, 'Наименование детали']))
            list_1.append(str(df.loc[i, 'Отметка о выполнении']))
            list_1.append(str(df.loc[i, 'Потенциальные проблемы']))
            list_1.append(str(int(df.loc[i, 'N° ITEM'])))
            list_2.append(list_1)
        for j in range(len(list_2)):
            text_proc = ', '.join(list_2[j])
            list_3.append(text_proc)
        text_proc_1 = ';\n\n'.join(list_3)
    else:
        text_proc_1 = 'такого заказа нет в базе'
    return text_proc_1


path = 'W:\\Theoretical Planning\\03 - План отгрузки (Planification)\\План отгрузки\\EXPED. IDM-Direct.xlsb'
df_exped = pd.read_excel(path, sheet_name='Текущий', engine='pyxlsb', header=4)
df_exped.dropna(subset=['Наименование детали'], inplace=True)
df_exped = df_exped.reset_index(drop=True)
