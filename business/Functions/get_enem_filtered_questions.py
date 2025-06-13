from interface.generate_pdf_artwork import generate_pdf_artwork


def get_enem_filtered_questions(dfResult_CN, prova, Habilidade, idom):
    dfResult_CN = dfResult_CN[dfResult_CN['OCRSearch']!='N/A']

    if (prova !='LC'):
        dfResult_CN = dfResult_CN.query("IN_ITEM_ABAN == 0 and TP_LINGUA not in [0, 1]")
    else: 
        dfResult_CN = dfResult_CN.query("IN_ITEM_ABAN == 0")
        if idom==-1: dfResult_CN = dfResult_CN.query("TP_LINGUA not in [0, 1]")
        else:
            alidom = 2 
            if idom == 0: alidom = 1
            else: alidom == 1
            dfResult_CN = dfResult_CN.query("TP_LINGUA not in ["+str(alidom)+']')

    cols_to_drop = ['TP_LINGUA', 'TX_MOTIVO_ABAN', 'IN_ITEM_ADAPTADO', 'NU_PARAM_A', 'NU_PARAM_B', 'NU_PARAM_C']

    dfResult_CN.drop(cols_to_drop, axis=1, inplace=True)
    dfResult_CN = dfResult_CN[dfResult_CN['SG_AREA'] == prova]
    dfResult_CN = dfResult_CN[dfResult_CN['IN_ITEM_ABAN'] == 0]
    dfResult_CN = dfResult_CN[dfResult_CN['CO_HABILIDADE'] == Habilidade]

    generate_pdf_artwork(dfResult_CN)

    dfResult_CN.sort_values('theta_065', ascending=True, inplace=True)
    dfResult_CN['indexacao'] = dfResult_CN.reset_index().index + 1

    return dfResult_CN