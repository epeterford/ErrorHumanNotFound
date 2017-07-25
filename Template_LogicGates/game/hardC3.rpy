init:
    image bg Logic_Gate = "LOGIC_GATE_BG.png"

label start:

    #loads background
    scene bg Logic_Gate
    
    #all sections are broken down into their rows
    #the first set of values declares images for the show call
    #the second set show the image at a certain positon
    #row 0
#    image tile00_00 = "r_elbow_tl.png"
#    image tile00_01 = "r_elbow_br.png"
#    image tile00_02 = "r_horizontal.png"
#    image tile00_03 = "g_elbow_br.png"
#    image tile00_04 = "g_elbow_bl.png"
#    image tile00_05 = "r_elbow_bl.png"
#    image tile00_06 = "g_horizontal.png"
#    image tile00_07 = "g_horizontal.png"
#    image tile00_08 = "g_horizontal.png"
#    image tile00_09 = "g_elbow_bl.png"
#    image tile00_10 = "g_horizontal.png"
#    image tile00_11 = "g_elbow_bl.png"
#    image tile00_12 = "r_elbow_tl.png"
#    image tile00_13 = "r_elbow_tl.png"
    
#    show tile00_00 at Position(xpos = 436, xanchor = 0, ypos = 233, yanchor = 0)
#    show tile00_01 at Position(xpos = 511, xanchor = 0, ypos = 233, yanchor = 0)
#    show tile00_02 at Position(xpos = 586, xanchor = 0, ypos = 233, yanchor = 0)
#    show tile00_03 at Position(xpos = 661, xanchor = 0, ypos = 233, yanchor = 0)
#    show tile00_04 at Position(xpos = 736, xanchor = 0, ypos = 233, yanchor = 0)
#    show tile00_05 at Position(xpos = 811, xanchor = 0, ypos = 233, yanchor = 0)
#    show tile00_06 at Position(xpos = 886, xanchor = 0, ypos = 233, yanchor = 0)
#    show tile00_07 at Position(xpos = 961, xanchor = 0, ypos = 233, yanchor = 0)
#    show tile00_08 at Position(xpos = 1036, xanchor = 0, ypos = 233, yanchor = 0)
#    show tile00_09 at Position(xpos = 1111, xanchor = 0, ypos = 233, yanchor = 0)
#    show tile00_10 at Position(xpos = 1186, xanchor = 0, ypos = 233, yanchor = 0)
#    show tile00_11 at Position(xpos = 1261, xanchor = 0, ypos = 233, yanchor = 0)
#    show tile00_12 at Position(xpos = 1336, xanchor = 0, ypos = 233, yanchor = 0)
#    show tile00_13 at Position(xpos = 1411, xanchor = 0, ypos = 233, yanchor = 0)
   
    #row 1 (row has a light)
    image tile01_00 = "r_horizontal.png"
    image tile01_01 = "r_elbow_bl.png"
#    image tile01_02 = "g_elbow_bl.png"
#    image tile01_03 = "g_vertical.png"
#    image tile01_04 = "g_r.png"
#    image tile01_05 = "NONE_Gate.png"
#    image tile01_06 = "y_horizontal.png"
#    image tile01_07 = "y_elbow_bl.png"
#    image tile01_08 = "g_horizontal.png"
#    image tile01_09 = "g_elbow_bl.png"
#    image tile01_10= "NONE_Gate.png"
#    image tile01_11 = "y_elbow_bl.png"
#    image tile01_12 = "y_elbow_br.png"
#    image tile01_13 = "y_horizontal.png"
    
    show tile01_00 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show tile01_01 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
#    show tile01_02 at Position(xpos = 586, xanchor = 0, ypos = 308, yanchor = 0)
#    show tile01_03 at Position(xpos = 661, xanchor = 0, ypos = 308, yanchor = 0)
#    show tile01_04 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)
#    show tile01_05 at Position(xpos = 811, xanchor = 0, ypos = 308, yanchor = 0)
#    show tile01_06 at Position(xpos = 886, xanchor = 0, ypos = 308, yanchor = 0)
#    show tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
#    show tile01_08 at Position(xpos = 1036, xanchor = 0, ypos = 308, yanchor = 0)
#    show tile01_09 at Position(xpos = 1111, xanchor = 0, ypos = 308, yanchor = 0)
#    show tile01_10 at Position(xpos = 1186, xanchor = 0, ypos = 308, yanchor = 0)
#    show tile01_11 at Position(xpos = 1261, xanchor = 0, ypos = 308, yanchor = 0)
#    show tile01_12 at Position(xpos = 1336, xanchor = 0, ypos = 308, yanchor = 0)
#    show tile01_13 at Position(xpos = 1411, xanchor = 0, ypos = 308, yanchor = 0)
    
    #row 2
#    image tile02_00 = "r_elbow_tl.png"
    image tile02_01 = "r_r.png"
    image tile02_02 = "XOR_Gate.png"
    image tile02_03 = "r_horizontal.png"
    image tile02_04 = "r_horizontal.png"
    image tile02_05 = "r_t_down.png"
    image tile02_06 = "r_horizontal.png"
    image tile02_07 = "r_horizontal.png"
    image tile02_08 = "r_horizontal.png"
    image tile02_09 = "r_elbow_bl.png"
#    image tile02_10 = "y_horizontal.png"
#    image tile02_11 = "y_elbow_bl.png"
#    image tile02_12 = "y_vertical.png"
#    image tile02_13 = "y_vertical.png"
    
#    show tile02_00 at Position(xpos = 436, xanchor = 0, ypos = 383, yanchor = 0)
    show tile02_01 at Position(xpos = 511, xanchor = 0, ypos = 383, yanchor = 0)
    show tile02_02 at Position(xpos = 586, xanchor = 0, ypos = 383, yanchor = 0)
    show tile02_03 at Position(xpos = 661, xanchor = 0, ypos = 383, yanchor = 0)
    show tile02_04 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show tile02_05 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
    show tile02_06 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show tile02_07 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
    show tile02_08 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
    show tile02_09 at Position(xpos = 1111, xanchor = 0, ypos = 383, yanchor = 0)
#    show tile02_10 at Position(xpos = 1186, xanchor = 0, ypos = 383, yanchor = 0)
#    show tile02_11 at Position(xpos = 1261, xanchor = 0, ypos = 383, yanchor = 0)
#    show tile02_12 at Position(xpos = 1336, xanchor = 0, ypos = 383, yanchor = 0)
#    show tile02_13 at Position(xpos = 1411, xanchor = 0, ypos = 383, yanchor = 0)

    #row 3 (row has a light)
    image tile03_00 = "r_horizontal.png"
    image tile03_01 = "r_elbow_tl.png"
#    image tile03_02 = "r_horizontal.png"
#    image tile03_03 = "r_horizontal.png"
#    image tile03_04 = "g_g.png"
    image tile03_05 = "r_vertical.png"
#    image tile03_06 = "y_horizontal.png"
#    image tile03_07 = "y_horizontal.png"
#    image tile03_08 = "y_horizontal.png"
    image tile03_09 = "r_y.png"
    image tile03_10 = "OR_Gate.png"
    image tile03_11 = "y_elbow_bl.png"
#    image tile03_12 = "y_elbow_tl.png"
#    image tile03_13 = "y_elbow_br.png"
    
    show tile03_00 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show tile03_01 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
#    show tile03_02 at Position(xpos = 586, xanchor = 0, ypos = 458, yanchor = 0)
#    show tile03_03 at Position(xpos = 661, xanchor = 0, ypos = 458, yanchor = 0)
#    show tile03_04 at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show tile03_05 at Position(xpos = 811, xanchor = 0, ypos = 458, yanchor = 0)
#    show tile03_06 at Position(xpos = 886, xanchor = 0, ypos = 458, yanchor = 0)
#    show tile03_07 at Position(xpos = 961, xanchor = 0, ypos = 458, yanchor = 0)
#    show tile03_08 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
    show tile03_09 at Position(xpos = 1111, xanchor = 0, ypos = 458, yanchor = 0)
    show tile03_10 at Position(xpos = 1186, xanchor = 0, ypos = 458, yanchor = 0)
    show tile03_11 at Position(xpos = 1261, xanchor = 0, ypos = 458, yanchor = 0)
#    show tile03_12 at Position(xpos = 1336, xanchor = 0, ypos = 458, yanchor = 0)
#    show tile03_13 at Position(xpos = 1411, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4 
#    image tile04_00 = "g_vertical.png"
#    image tile04_01 = "r_g.png"
#    image tile04_02 = "NAND_Gate.png"
#    image tile04_03 = "g_horizontal.png"
#    image tile04_04 = "g_t_left.png"
    image tile04_05 = "r_r.png"
    image tile04_06 = "NONE_Gate.png"
    image tile04_07 = "y_horizontal.png"
    image tile04_08 = "y_horizontal.png"
    image tile04_09 = "y_elbow_tl.png"
#    image tile04_10 = "y_y.png"
    image tile04_11 = "y_vertical.png"
#    image tile04_12 = "y_elbow_bl.png"
#    image tile04_13 = "y_elbow_tl.png"
    
#    show tile04_00 at Position(xpos = 436, xanchor = 0, ypos = 533, yanchor = 0)
#    show tile04_01 at Position(xpos = 511, xanchor = 0, ypos = 533, yanchor = 0)
#    show tile04_02 at Position(xpos = 586, xanchor = 0, ypos = 533, yanchor = 0)
#    show tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
#    show tile04_04 at Position(xpos = 736, xanchor = 0, ypos = 533, yanchor = 0)
    show tile04_05 at Position(xpos = 811, xanchor = 0, ypos = 533, yanchor = 0)
    show tile04_06 at Position(xpos = 886, xanchor = 0, ypos = 533, yanchor = 0)
    show tile04_07 at Position(xpos = 961, xanchor = 0, ypos = 533, yanchor = 0)
    show tile04_08 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
    show tile04_09 at Position(xpos = 1111, xanchor = 0, ypos = 533, yanchor = 0)
#    show tile04_10 at Position(xpos = 1186, xanchor = 0, ypos = 533, yanchor = 0)
    show tile04_11 at Position(xpos = 1261, xanchor = 0, ypos = 533, yanchor = 0)
#    show tile04_12 at Position(xpos = 1336, xanchor = 0, ypos = 533, yanchor = 0)
#    show tile04_13 at Position(xpos = 1411, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5 (row has a light)
    image tile05_00 = "r_horizontal.png"
    image tile05_01 = "r_t_down.png"
    image tile05_02 = "r_horizontal.png"
    image tile05_03 = "r_horizontal.png"
    image tile05_04 = "r_horizontal.png"
    image tile05_05 = "r_t_up.png"
    image tile05_06 = "r_horizontal.png"
    image tile05_07 = "r_horizontal.png"
    image tile05_08 = "r_elbow_bl.png"
#    image tile05_09 = "y_vertical.png"
#    image tile05_10 = "y_vertical.png"
    image tile05_11 = "y_y.png"
    image tile05_12 = "AND_Gate.png"
    image tile05_13 = "y_horizontal.png"
    
    show tile05_00 at Position(xpos = 436, xanchor = 0, ypos = 608, yanchor = 0)
    show tile05_01 at Position(xpos = 511, xanchor = 0, ypos = 608, yanchor = 0)
    show tile05_02 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show tile05_03 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
    show tile05_04 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    show tile05_05 at Position(xpos = 811, xanchor = 0, ypos = 608, yanchor = 0)
    show tile05_06 at Position(xpos = 886, xanchor = 0, ypos = 608, yanchor = 0)
    show tile05_07 at Position(xpos = 961, xanchor = 0, ypos = 608, yanchor = 0)
    show tile05_08 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
#    show tile05_09 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
#    show tile05_10 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
    show tile05_11 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    show tile05_12 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
    show tile05_13 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row 6
#    image tile06_00 = "g_elbow_tr.png"
    image tile06_01 = "r_g.png"
    image tile06_02 = "NONE_Gate.png"
    image tile06_03 = "y_horizontal.png"
    image tile06_04 = "y_horizontal.png"
    image tile06_05 = "y_elbow_bl.png"
#    image tile06_06 = "y_elbow_bl.png"
#    image tile06_07 = "y_elbow_bl.png"
    image tile06_08 = "r_vertical.png"
#    image tile06_09 = "NONE_Gate.png"
#    image tile06_10 = "y_elbow_tl.png"
    image tile06_11 = "y_vertical.png"
#    image tile06_12 = "r_elbow_tl.png"
#    image tile06_13 = "r_elbow_tl.png"
    
#    show tile06_00 at Position(xpos = 436, xanchor = 0, ypos = 683, yanchor = 0)
    show tile06_01 at Position(xpos = 511, xanchor = 0, ypos = 683, yanchor = 0)
    show tile06_02 at Position(xpos = 586, xanchor = 0, ypos = 683, yanchor = 0)
    show tile06_03 at Position(xpos = 661, xanchor = 0, ypos = 683, yanchor = 0)
    show tile06_04 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show tile06_05 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
#    show tile06_06 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
#    show tile06_07 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
    show tile06_08 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
#    show tile06_09 at Position(xpos = 1111, xanchor = 0, ypos = 683, yanchor = 0)
#    show tile06_10 at Position(xpos = 1186, xanchor = 0, ypos = 683, yanchor = 0)
    show tile06_11 at Position(xpos = 1261, xanchor = 0, ypos = 683, yanchor = 0)
#    show tile06_12 at Position(xpos = 1336, xanchor = 0, ypos = 683, yanchor = 0)
#    show tile06_13 at Position(xpos = 1411, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row 7 (row has a light)
    image tile07_00 = "g_horizontal.png"
    image tile07_01 = "g_t_up.png"
    image tile07_02 = "g_elbow_bl.png"
#    image tile07_03 = "g_horizontal.png"
#    image tile07_04 = "g_horizontal.png"
    image tile07_05 = "y_vertical.png"
#    image tile07_06 = "g_horizontal.png"
#    image tile07_07 = "g_horizontal.png"
    image tile07_08 = "r_y.png"
    image tile07_09 = "NONE_Gate.png"
    image tile07_10 = "y_horizontal.png"
    image tile07_11 = "y_elbow_tl.png"
#    image tile07_12 = "y_horizontal.png"
#    image tile07_13 = "y_horizontal.png"
    
    show tile07_00 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show tile07_01 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show tile07_02 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
#    show tile07_03 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
#    show tile07_04 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
    show tile07_05 at Position(xpos = 811, xanchor = 0, ypos = 758, yanchor = 0)
#    show tile07_06 at Position(xpos = 886, xanchor = 0, ypos = 758, yanchor = 0)
#    show tile07_07 at Position(xpos = 961, xanchor = 0, ypos = 758, yanchor = 0)
    show tile07_08 at Position(xpos = 1036, xanchor = 0, ypos = 758, yanchor = 0)
    show tile07_09 at Position(xpos = 1111, xanchor = 0, ypos = 758, yanchor = 0)
    show tile07_10 at Position(xpos = 1186, xanchor = 0, ypos = 758, yanchor = 0)
    show tile07_11 at Position(xpos = 1261, xanchor = 0, ypos = 758, yanchor = 0)
#    show tile07_12 at Position(xpos = 1336, xanchor = 0, ypos = 758, yanchor = 0)
#    show tile07_13 at Position(xpos = 1411, xanchor = 0, ypos = 758, yanchor = 0)
    
    #row 8
#    image tile08_00 = "g_elbow_tr.png"
#    image tile08_01 = "g_horizontal.png"
    image tile08_02 = "g_vertical.png"
#    image tile08_03 = "y_elbow_tr.png"
#    image tile08_04 = "y_horizontal.png"
    image tile08_05 = "y_g.png"
    image tile08_06 = "NONE_Gate.png"
    image tile08_07 = "y_horizontal.png"
    image tile08_08 = "y_elbow_tl.png"
#    image tile08_09 = "y_horizontal.png"
#    image tile08_10 =  "y_elbow_tl.png"
#    image tile08_11 = "y_elbow_tl.png"
#    image tile08_12 = "NONE_Gate.png"
#    image tile08_13 = "y_elbow_tl.png"
    
#    show tile08_00 at Position(xpos = 436, xanchor = 0, ypos = 833, yanchor = 0)
#    show tile08_01 at Position(xpos = 511, xanchor = 0, ypos = 833, yanchor = 0)
    show tile08_02 at Position(xpos = 586, xanchor = 0, ypos = 833, yanchor = 0)
#    show tile08_03 at Position(xpos = 661, xanchor = 0, ypos = 833, yanchor = 0)
#    show tile08_04 at Position(xpos = 736, xanchor = 0, ypos = 833, yanchor = 0)
    show tile08_05 at Position(xpos = 811, xanchor = 0, ypos = 833, yanchor = 0)
    show tile08_06 at Position(xpos = 886, xanchor = 0, ypos = 833, yanchor = 0)
    show tile08_07 at Position(xpos = 961, xanchor = 0, ypos = 833, yanchor = 0)
    show tile08_08 at Position(xpos = 1036, xanchor = 0, ypos = 833, yanchor = 0)
#    show tile08_09 at Position(xpos = 1111, xanchor = 0, ypos = 833, yanchor = 0)
#    show tile08_10 at Position(xpos = 1186, xanchor = 0, ypos = 833, yanchor = 0)
#    show tile08_11 at Position(xpos = 1261, xanchor = 0, ypos = 833, yanchor = 0)
#    show tile08_12 at Position(xpos = 1336, xanchor = 0, ypos = 833, yanchor = 0)
#    show tile08_13 at Position(xpos = 1411, xanchor = 0, ypos = 833, yanchor = 0)
    
    #row 9
#    image tile09_00 = "g_elbow_tr.png"
#    image tile09_01 = "g_elbow_tl.png"
    image tile09_02 = "g_elbow_tr.png"
    image tile09_03 = "g_horizontal.png"
    image tile09_04 = "g_horizontal.png"
    image tile09_05 = "g_elbow_tl.png"
#    image tile09_06 = "r_elbow_tr.png"
#    image tile09_07 = "r_horizontal.png"
#    image tile09_08 = "r_horizontal.png"
#    image tile09_09 = "r_horizontal.png"
#    image tile09_10 = "r_horizontal.png"
#    image tile09_11 = "r_elbow_tl.png"
#    image tile09_12 = "r_elbow_tl.png"
#    image tile09_13 = "r_elbow_tl.png"
    
#    show tile09_00 at Position(xpos = 436, xanchor = 0, ypos = 908, yanchor = 0)
#    show tile09_01 at Position(xpos = 511, xanchor = 0, ypos = 908, yanchor = 0)
    show tile09_02 at Position(xpos = 586, xanchor = 0, ypos = 908, yanchor = 0)
    show tile09_03 at Position(xpos = 661, xanchor = 0, ypos = 908, yanchor = 0)
    show tile09_04 at Position(xpos = 736, xanchor = 0, ypos = 908, yanchor = 0)
    show tile09_05 at Position(xpos = 811, xanchor = 0, ypos = 908, yanchor = 0)
#    show tile09_06 at Position(xpos = 886, xanchor = 0, ypos = 908, yanchor = 0)
#    show tile09_07 at Position(xpos = 961, xanchor = 0, ypos = 908, yanchor = 0)
#    show tile09_08 at Position(xpos = 1036, xanchor = 0, ypos = 908, yanchor = 0)
#    show tile09_09 at Position(xpos = 1111, xanchor = 0, ypos = 908, yanchor = 0)
#    show tile09_10 at Position(xpos = 1186, xanchor = 0, ypos = 908, yanchor = 0)
#    show tile09_11 at Position(xpos = 1261, xanchor = 0, ypos = 908, yanchor = 0)
#    show tile09_12 at Position(xpos = 1336, xanchor = 0, ypos = 908, yanchor = 0)
#    show tile09_13 at Position(xpos = 1411, xanchor = 0, ypos = 908, yanchor = 0)

    #start points
    image start1 = "light_r_on.png"
    show start1 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image start2 = "light_r_on.png"
    show start2 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image start3 = "light_r_on.png"
    show start3 at Position(xpos = 238, xanchor = 0, ypos = 608, yanchor = 0)
    image start4 = "light_g_on.png"
    show start4 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    
    #end points (only use one of these
#    image end1 = "light_g_off.png"
#    show end1 at Position(xpos = 1595, xanchor = 0, ypos = 308, yanchor = 0)
#    image end2 = "light_g_off.png"
#    show end2 at Position(xpos = 1595, xanchor = 0, ypos = 458, yanchor = 0)
#    image end3 = "YELLOW.png"
#    show end3 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)
#    image end4 = "YELLOW.png"
#    show end4 at Position(xpos = 1595, xanchor = 0, ypos = 758, yanchor = 0)
    
    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************

    
    #makes gray backgrounds for tiles
    image and_gray = "AND_Gray.png"
    image or_gray = "OR_Gray.png"
    image nand_gray = "NAND_Gray.png"
    image nor_gray = "NOR_Gray.png"
    show and_gray at Position(xpos = 586, xanchor = 0, ypos = 88, yanchor = 0)
    show or_gray at Position(xpos = 812, xanchor = 0, ypos = 88, yanchor = 0)
    show nand_gray at Position(xpos = 1035, xanchor = 0, ypos = 88, yanchor = 0)
    show nor_gray at Position(xpos = 1261, xanchor = 0, ypos = 88, yanchor = 0)



    #initial value assignment for dragables
    $ and1x = 586
    $ and1y = 88
   
    # check conditons for locations
    $ and1in1 = False
   
    #attempts for players
    $ attempts = 6
 
    jump gamefile2
    
    
label gamefile2:
    
#    calls game screen
    call screen logicGates2
    
#    the first logic gate *******************************************************************************
    if gate_name == "and_gate":
#        gate slot numeber one *******************************
        if slot_name == "gate slot one":
#            sets values for checks
            $ and1x = 1111
            $ and1y = 608
            $ and1in1 = True


#*******************************************
#************image zone********************* 
#*******************************************

#first slot for and 1
    if and1in1 == True:
        image tile39 = "GREEN-HORIZ-LINE.png"
        image tile40 = "GREEN-HORIZ-LINE.png"
        image tile41 = "GREEN-HORIZ-LINE.png"
        image tile42 = "GREEN-HORIZ-LINE.png"
        image end2 = "GREEN.png"

        #shows tiles
        show tile39 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
        show tile40 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        show tile41 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
        show tile42 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        show end2 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)
        
    if slot_name == "null":
        $attempts +=1
        
#win conditions ********
    if and1in1 == True: 
        "game"
        
        jump start

   
    
    $ attempts -= 1
    if attempts == 0:
        "you lose try again"
        jump start
    
    jump gamefile2
