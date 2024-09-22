# Начал писать по курсу Гэддиса, пока не нашёл уже готовую либу. 
# Выношу сюда.
# Расчёт склонений
sp_last_symbol = total_sausage_pack_needs - total_sausage_pack_needs // 10 * 10
bp_last_symbol = total_buns_pack_needs - total_buns_pack_needs // 10 * 10

if sp_last_symbol >= 5 or sp_last_symbol == 0 or (sp_last_symbol % 10) == 1:
    sp_declesion = 'ок'
elif sp_last_symbol >= 2:
    sp_declesion = 'ки'
elif sp_last_symbol == 1:
    sp_declesion = 'ка'
if sausages_left >= 5 or sausages_left == 0:
    s_declesion = 'ок'
elif sausages_left >= 2:
    s_declesion = 'ки'
elif sausages_left == 1:
    s_declesion = 'ка'
if bp_last_symbol >= 5 or bp_last_symbol == 0 or (bp_last_symbol % 10) == 1:
    bp_declesion = 'ок'
elif bp_last_symbol >= 2:
    bp_declesion = 'ки'
elif bp_last_symbol == 1:
    bp_declesion = 'ка'
if buns_left >= 5 or buns_left == 0:
    b_declesion = 'ок'
elif buns_left >= 2:
    b_declesion = 'ки'
elif buns_left == 1:
    b_declesion = 'ка'
if participants_num == 1:
    p_declesion = 'ка'
else:
    p_declesion = 'ков'