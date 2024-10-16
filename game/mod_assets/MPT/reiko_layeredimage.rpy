layeredimage reiko base:

    at renpy.partial(Flatten, drawable_resolution=False)

    always "mod_assets/MPT/reiko/reiko_turned_facebase.png"

    group outfit:
        attribute uniform default null
        attribute uniform_c null
        attribute casual null
        attribute casual2 null

    ### Right Half
    group right:
        anchor (0,0)
        subpixel True
        attribute rdown default if_any(["uniform"]):
            "mod_assets/MPT/reiko/body/reiko_turned_uniform_right_down.png"
        attribute rdown default if_any(["casual"]):
            "mod_assets/MPT/reiko/body/reiko_turned_casual_right_down.png"
        attribute rdown default if_any(["uniform_c"]):
            "mod_assets/MPT/reiko/body/reiko_turned_uniformc_right_down.png"
        attribute rdown default if_any(["casual2"]):
            "mod_assets/MPT/reiko/body/reiko_turned_casual2_right_down.png"
        attribute rup if_any(["uniform"]):
            "mod_assets/MPT/reiko/body/reiko_turned_uniform_right_up.png"
        attribute rup if_any(["casual"]):
            "mod_assets/MPT/reiko/body/reiko_turned_casual_right_up.png"
        attribute rup if_any(["uniform_c"]):
            "mod_assets/MPT/reiko/body/reiko_turned_uniformc_right_up.png"
        attribute rup if_any(["casual2"]):
            "mod_assets/MPT/reiko/body/reiko_turned_casual2_right_up.png"    
        attribute rthink if_any(["uniform"]):
            "mod_assets/MPT/reiko/body/reiko_turned_uniform_right_think.png"
        attribute rthink if_any(["casual"]):
            "mod_assets/MPT/reiko/body/reiko_turned_casual_right_think.png"
        attribute rthink if_any(["uniform_c"]):
            "mod_assets/MPT/reiko/body/reiko_turned_uniformc_right_think.png"
        attribute rthink if_any(["casual2"]):
            "mod_assets/MPT/reiko/body/reiko_turned_casual2_right_think.png"   

    ### Left Half
    group left:
        anchor (0,0)
        subpixel True
        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/reiko/body/reiko_turned_uniform_left_down.png"
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/reiko/body/reiko_turned_casual_left_down.png"
        attribute ldown default if_any(["uniform_c"]):
            "mod_assets/MPT/reiko/body/reiko_turned_uniformc_left_down.png"
        attribute ldown default if_any(["casual2"]):
            "mod_assets/MPT/reiko/body/reiko_turned_casual2_left_down.png"   
        attribute lpoint if_any(["uniform"]):
            "mod_assets/MPT/reiko/body/reiko_turned_uniform_left_point.png"
        attribute lpoint if_any(["casual"]):
            "mod_assets/MPT/reiko/body/reiko_turned_casual_left_point.png"
        attribute lpoint if_any(["uniform_c"]):
            "mod_assets/MPT/reiko/body/reiko_turned_uniformc_left_point.png"
        attribute lpoint if_any(["casual2"]):
            "mod_assets/MPT/reiko/body/reiko_turned_casual2_left_point.png"   
        attribute lhip if_any(["uniform"]):
            "mod_assets/MPT/reiko/body/reiko_turned_uniform_left_hip.png"
        attribute lhip if_any(["casual"]):
            "mod_assets/MPT/reiko/body/reiko_turned_casual_left_hip.png"
        attribute lhip if_any(["uniform_c"]):
            "mod_assets/MPT/reiko/body/reiko_turned_uniformc_left_hip.png"
        attribute lhip if_any(["casual2"]):
            "mod_assets/MPT/reiko/body/reiko_turned_casual2_left_hip.png"  

    group nose:

        ### Simple Syntax
        attribute nose1:
            "mod_assets/MPT/reiko/nose/reiko_turned_nose_n1.png"
        attribute nose2:
            "mod_assets/MPT/reiko/nose/reiko_turned_nose_n2.png"

        ### Old MPT Syntax
        attribute n1:
            "mod_assets/MPT/reiko/nose/reiko_turned_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/reiko/nose/reiko_turned_nose_n2.png"   

    group mouth:

        ### Simple Syntax
        attribute mouth_a:
            "mod_assets/MPT/reiko/mouth/reiko_turned_mouth_ma.png"
        attribute mouth_b:
            "mod_assets/MPT/reiko/mouth/reiko_turned_mouth_mb.png"
        attribute mouth_c:
            "mod_assets/MPT/reiko/mouth/reiko_turned_mouth_mc.png"
        attribute mouth_d:
            "mod_assets/MPT/reiko/mouth/reiko_turned_mouth_md.png"     
        attribute mouth_e:
            "mod_assets/MPT/reiko/mouth/reiko_turned_mouth_me.png"
        attribute mouth_f:
            "mod_assets/MPT/reiko/mouth/reiko_turned_mouth_mf.png"
        attribute mouth_g:
            "mod_assets/MPT/reiko/mouth/reiko_turned_mouth_mg.png"    

        ### Old MPT Syntax
        attribute ma:
            "mod_assets/MPT/reiko/mouth/reiko_turned_mouth_ma.png"
        attribute mb:
            "mod_assets/MPT/reiko/mouth/reiko_turned_mouth_mb.png"
        attribute mc:
            "mod_assets/MPT/reiko/mouth/reiko_turned_mouth_mc.png"
        attribute md:
            "mod_assets/MPT/reiko/mouth/reiko_turned_mouth_md.png"     
        attribute me: #Windows ME Moment
            "mod_assets/MPT/reiko/mouth/reiko_turned_mouth_me.png"
        attribute mf:
            "mod_assets/MPT/reiko/mouth/reiko_turned_mouth_mf.png"
        attribute mg:
            "mod_assets/MPT/reiko/mouth/reiko_turned_mouth_mg.png"     

    group eyes:
        
        ### Simple Syntax
        attribute eyes_a:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e1.png"
        attribute eyes_b:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e2.png"
        attribute eyes_c:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e3.png"
        attribute eyes_d:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e4.png"       
        attribute eyes_e:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e5.png"
        attribute eyes_f:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e6.png"
        attribute eyes_g:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e7.png"      

        ### New MPT Syntax
        attribute ea:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e1.png"
        attribute eb:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e2.png"
        attribute ec:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e3.png"
        attribute ed:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e4.png"       
        attribute ee:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e5.png"
        attribute ef:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e6.png"
        attribute eg:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e7.png"     

        ### Old MPT Syntax
        attribute e1a:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e1.png"
        attribute e1b:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e2.png"
        attribute e1c:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e3.png"
        attribute e1d:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e4.png"       
        attribute e1e:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e5.png"
        attribute e1f:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e6.png"
        attribute e1g:
            "mod_assets/MPT/reiko/eyes/reiko_turned_eyes_e7.png"    

    group eyebrows:

        ### Simple Syntax
        attribute brow_a:
            "mod_assets/MPT/reiko/eyebrows/reiko_turned_eyebrows_b1a.png"
        attribute brow_b:
            "mod_assets/MPT/reiko/eyebrows/reiko_turned_eyebrows_b1b.png"
        attribute brow_c:
            "mod_assets/MPT/reiko/eyebrows/reiko_turned_eyebrows_b1c.png"

        ### New MPT Syntax
        attribute ba:    
            "mod_assets/MPT/reiko/eyebrows/reiko_turned_eyebrows_b1a.png"   
        attribute bb:
            "mod_assets/MPT/reiko/eyebrows/reiko_turned_eyebrows_b1b.png"
        attribute bc:
            "mod_assets/MPT/reiko/eyebrows/reiko_turned_eyebrows_b1c.png"  

        ### Old MPT Syntax
        attribute b1a:    
            "mod_assets/MPT/reiko/eyebrows/reiko_turned_eyebrows_b1a.png"   
        attribute b1b:
            "mod_assets/MPT/reiko/eyebrows/reiko_turned_eyebrows_b1b.png"
        attribute b1c:
            "mod_assets/MPT/reiko/eyebrows/reiko_turned_eyebrows_b1c.png"     


layeredimage reiko sad:
    

    group outfit:
        attribute uniform default null
        attribute casual null    
        attribute uniform_c null   
        attribute casual2 null   

    group body:
        attribute body default if_any(["uniform"]):
            "mod_assets/MPT/reiko/body/reiko_shy_uniform_bodybase.png"
        attribute body default if_any(["casual"]):
            "mod_assets/MPT/reiko/body/reiko_shy_casual_bodybase.png"    
        attribute body default if_any(["uniform_c"]):
            "mod_assets/MPT/reiko/body/reiko_shy_uniformc_bodybase.png"
        attribute body default if_any(["casual2"]):
            "mod_assets/MPT/reiko/body/reiko_shy_casual2_bodybase.png"  


        ### Old MPT Syntax
        attribute n1:
            "mod_assets/MPT/reiko/nose/reiko_tough_nose_n1.png"

    group mouth:
        ### Simple Syntax
        attribute mouth_a:
            "mod_assets/MPT/reiko/mouth/reiko_shy_mouth_m1.png"
        attribute mouth_b:
            "mod_assets/MPT/reiko/mouth/reiko_shy_mouth_m2.png"
        attribute mouth_c:
            "mod_assets/MPT/reiko/mouth/reiko_shy_mouth_m3.png"
            
        ### New MPT Syntax
        attribute ma:
            "mod_assets/MPT/reiko/mouth/reiko_shy_mouth_m1.png"
        attribute mb:
            "mod_assets/MPT/reiko/mouth/reiko_shy_mouth_m2.png"
        attribute mc:
            "mod_assets/MPT/reiko/mouth/reiko_shy_mouth_m3.png"

        ### Old MPT Syntax
        attribute m1:
            "mod_assets/MPT/reiko/mouth/reiko_shy_mouth_m1.png"
        attribute m2:
            "mod_assets/MPT/reiko/mouth/reiko_shy_mouth_m2.png"
        attribute m3:
            "mod_assets/MPT/reiko/mouth/reiko_shy_mouth_m3.png"

    group eyes:
        ### Simple Syntax
        attribute eyes_a:
            "mod_assets/MPT/reiko/eyes/reiko_shy_eyes_e1.png"
        attribute eyes_b:
            "mod_assets/MPT/reiko/eyes/reiko_shy_eyes_e2.png"
        attribute eyes_c:
            "mod_assets/MPT/reiko/eyes/reiko_shy_eyes_e3.png"
        attribute eyes_d:
            "mod_assets/MPT/reiko/eyes/reiko_shy_eyes_e4.png"
            
        ### New MPT Syntax
        attribute ea:
            "mod_assets/MPT/reiko/eyes/reiko_shy_eyes_e1.png"
        attribute eb:
            "mod_assets/MPT/reiko/eyes/reiko_shy_eyes_e2.png"
        attribute ec:
            "mod_assets/MPT/reiko/eyes/reiko_shy_eyes_e3.png"
        attribute ed:
            "mod_assets/MPT/reiko/eyes/reiko_shy_eyes_e4.png"
            
        ### Old MPT Syntax
        attribute e1:
            "mod_assets/MPT/reiko/eyes/reiko_shy_eyes_e1.png"
        attribute e2:
            "mod_assets/MPT/reiko/eyes/reiko_shy_eyes_e2.png"
        attribute e3:
            "mod_assets/MPT/reiko/eyes/reiko_shy_eyes_e3.png"
        attribute e4:
            "mod_assets/MPT/reiko/eyes/reiko_shy_eyes_e4.png"

    group eyebrows:
        
        ### Simple Syntax
        attribute brow_a:
            "mod_assets/MPT/reiko/eyebrows/reiko_shy_eyebrows_b1.png"
        attribute brow_b:
            "mod_assets/MPT/reiko/eyebrows/reiko_shy_eyebrows_b2.png"

        ### New MPT Syntax
        attribute ba:
            "mod_assets/MPT/reiko/eyebrows/reiko_shy_eyebrows_b1.png"
        attribute bb:
            "mod_assets/MPT/reiko/eyebrows/reiko_shy_eyebrows_b2.png"
            
        ### New MPT Syntax
        attribute b1:
            "mod_assets/MPT/reiko/eyebrows/reiko_shy_eyebrows_b1.png"
        attribute b2:
            "mod_assets/MPT/reiko/eyebrows/reiko_shy_eyebrows_b2.png"

    group special:
        attribute shyside1:
            "mod_assets/MPT/reiko/special/reiko_shyside_1.png"
        attribute shyside2:
            "mod_assets/MPT/reiko/special/reiko_shyside_2.png"

layeredimage reiko tough:
    

    group outfit:
        attribute uniform default null
        attribute casual null    
        attribute uniform_c null   
        attribute casual2 null   

    group body:
        attribute body default if_any(["uniform"]):
            "mod_assets/MPT/reiko/body/reiko_tough_uniform_bodybase.png"
        attribute body default if_any(["casual"]):
            "mod_assets/MPT/reiko/body/reiko_tough_casual_bodybase.png"    
        attribute body default if_any(["uniform_c"]):
            "mod_assets/MPT/reiko/body/reiko_tough_uniformc_bodybase.png"
        attribute body default if_any(["casual2"]):
            "mod_assets/MPT/reiko/body/reiko_tough_casual2_bodybase.png"  

    group nose:
        ### Simple Syntax
        attribute nose1:
            "mod_assets/MPT/reiko/nose/reiko_tough_nose_n1.png"              

    group mouth:
        ### Simple Syntax
        attribute mouth_a:
            "mod_assets/MPT/reiko/mouth/reiko_tough_mouth_m1.png"
        attribute mouth_b:
            "mod_assets/MPT/reiko/mouth/reiko_tough_mouth_m2.png"
        attribute mouth_c:
            "mod_assets/MPT/reiko/mouth/reiko_tough_mouth_m3.png"
        attribute mouth_d:
            "mod_assets/MPT/reiko/mouth/reiko_tough_mouth_m4.png"
            
        ### New MPT Syntax
        attribute ma:
            "mod_assets/MPT/reiko/mouth/reiko_tough_mouth_m1.png"
        attribute mb:
            "mod_assets/MPT/reiko/mouth/reiko_tough_mouth_m2.png"
        attribute mc:
            "mod_assets/MPT/reiko/mouth/reiko_tough_mouth_m3.png"
        attribute md:
            "mod_assets/MPT/reiko/mouth/reiko_tough_mouth_m4.png"

        ### Old MPT Syntax
        attribute m1:
            "mod_assets/MPT/reiko/mouth/reiko_tough_mouth_m1.png"
        attribute m2:
            "mod_assets/MPT/reiko/mouth/reiko_tough_mouth_m2.png"
        attribute m3:
            "mod_assets/MPT/reiko/mouth/reiko_tough_mouth_m3.png"  
        attribute m4:
            "mod_assets/MPT/reiko/mouth/reiko_tough_mouth_m4.png"

    group eyes:
        ### Simple Syntax
        attribute eyes_a:
            "mod_assets/MPT/reiko/eyes/reiko_tough_eyes_e1.png"
            
        ### New MPT Syntax
        attribute ea:
            "mod_assets/MPT/reiko/eyes/reiko_tough_eyes_e1.png"
            
        ### Old MPT Syntax
        attribute e1:
            "mod_assets/MPT/reiko/eyes/reiko_tough_eyes_e1.png"

    group eyebrows:
        
        ### Simple Syntax
        attribute brow_a:
            "mod_assets/MPT/reiko/eyebrows/reiko_tough_eyebrows_b1.png"
        attribute brow_b:
            "mod_assets/MPT/reiko/eyebrows/reiko_tough_eyebrows_b2.png"

        ### New MPT Syntax
        attribute ba:
            "mod_assets/MPT/reiko/eyebrows/reiko_tough_eyebrows_b1.png"
        attribute bb:
            "mod_assets/MPT/reiko/eyebrows/reiko_tough_eyebrows_b2.png"
            
        ### New MPT Syntax
        attribute b1:
            "mod_assets/MPT/reiko/eyebrows/reiko_tough_eyebrows_b1.png"
        attribute b2:
            "mod_assets/MPT/reiko/eyebrows/reiko_tough_eyebrows_b2.png"

    group special:
        attribute coy1:
            "mod_assets/MPT/reiko/special/reiko_coy_1.png"
        attribute coy2:
            "mod_assets/MPT/reiko/special/reiko_coy_2.png"
        attribute coy3:
            "mod_assets/MPT/reiko/special/reiko_coy_3.png"
            

# Thanks for reading all the way down here~ 