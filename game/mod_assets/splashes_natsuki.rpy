image splash_natsuki_background:
    alpha 0
    2.35
    "mod_assets/splashes/menu_bg_natsuki.png"
    xtile 50 subpixel True
    crop_relative True
    yoffset -119.5
    crop (0.0,0.0,1.0,0.41)
    matrixcolor BrightnessMatrix(0.12)
    parallel:
        ease 0.25 alpha 1.0

    block:
        xoffset 0
        linear 80 xoffset 1280
        repeat

image splash_natsuki_1:

    contains:
        truecenter
        subpixel True
        Solid("#F85BFF") 
        crop_relative True
        xanchor 1
        xoffset -640
        
        crop (0.0,0.0,0.0,0.070)
        parallel:
            ease 1 crop (0.0,0.0,1.1, 0.070)
        parallel:
            1
            easein_quint 1 zoom 15

    contains:
        0.15
        truecenter
        subpixel True
        Solid("#F526FF")
        crop_relative True
        xanchor 1
        xoffset -640
        
        crop (0.0,0.0,0.0,0.070)
        parallel:
            ease 1 crop (0.0,0.0,1.1, 0.070)
        parallel:
            1
            easein_quint 1 zoom 15

    contains:
        0.3
        truecenter
        subpixel True
        Solid("#FA94FF")
        crop_relative True
        xanchor 1
        xoffset -640
        crop (0.0,0.0,0.0,0.070)
        parallel:
            ease 1 crop (0.0,0.0,1.1, 0.070)
        parallel:
            1
            easein_quint 1 zoom 15

    contains:
        0.6
        subpixel True
        Solid("#FBA1FF")
        crop_relative True
        xanchor 0.0
        yoffset -300
        crop (0.0,0.0,1.0, 0.195)
        ease 2 yoffset -30

    contains:
        0.6
        subpixel True
        Solid("#FBA1FF")
        crop_relative True
        xanchor 0.0
        yoffset 900
        crop (0.0,0.0,1.0, 0.195)
        ease 2 yoffset 600


image splash_natsuki_2:

    contains:
        2.95
        matrixcolor BrightnessMatrix(-0.25)
        "mod_assets/splashes/menu_art_n_pink.png"
        subpixel True
        truecenter
        
        alpha 0
        yoffset 300
        xoffset -290

        parallel:
            easein_quint 3 alpha 1.0 
        parallel:
            0.1
            ease 3 xoffset -325
            ease 3 xoffset -330
            ease 3 xoffset -320
            ease 3 xoffset -335
            repeat
        parallel:
            0.1
            ease 3 yoffset 305
            ease 3 yoffset 295
            ease 3 yoffset 301
            ease 3 yoffset 299
            repeat
        parallel:
            ease 10 rotate 2.5
            ease 10 rotate 0
            repeat
        parallel:
            ease 10 zoom 1.02
            ease 10 zoom 0.98
            repeat

    contains:
        2.9
        matrixcolor BrightnessMatrix(-0.1)
        "mod_assets/splashes/menu_art_n_pink.png"
        subpixel True
        truecenter
        
        alpha 0
        yoffset 300
        xoffset -290

        parallel:
            easein_quint 3 alpha 1.0 
        parallel:
            0.1
            ease 5 xoffset -310
            ease 3 xoffset -300
            ease 4 xoffset -295
            ease 3 xoffset -305
            repeat
        parallel:
            0.1
            ease 3 yoffset 308
            ease 3 yoffset 291
            repeat
        parallel:
            ease 10 rotate -2.5
            ease 10 rotate 0
            repeat
        parallel:
            ease 5 zoom 1.02
            ease 5 zoom 0.98
            repeat

    contains:
        1.75

        "mod_assets/splashes/menu_art_n_pink.png"
        subpixel True
        truecenter
        xoffset 800
        alpha 0
        yoffset 300
        easein_quint 1.75 xoffset -290 alpha 1
        parallel:
            ease 3 xoffset -285
            ease 3 xoffset -295
            ease 3 xoffset -300
            ease 3 xoffset -290
            repeat
        parallel:
            ease 3 yoffset 305
            ease 3 yoffset 295
            ease 3 yoffset 301
            ease 3 yoffset 297 
            repeat
        parallel:
            ease 6 zoom 1.02
            ease 4 zoom 0.98
            repeat

    contains:
        2.20
        'natsuki_name_pink'
        alpha 0
        subpixel True truecenter
        easein_quint 2 alpha 1 rotate -3 yoffset -15 zoom 1.1
        block:
            ease 3 zoom 1.14
            ease 3 zoom 1.1
            repeat

    contains:
        2.30
        'natsuki_name_pink_2'
        alpha 0
        subpixel True truecenter
        easein_quint 2 alpha 1 rotate 3 yoffset 45 zoom 1.1
        block:
            ease 3 zoom 1.14
            ease 3 zoom 1.1
            repeat   

    contains:
        2.25
        truecenter
        subpixel True
        yoffset 250
        xoffset 915
        ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
        particle_fadeout



image natsuki_name_pink:  
    
    truecenter subpixel True
    yoffset -75
    xoffset 350
    
    Text("Meanwhile,", size=50, slow_cps=0,  color="#fff", insensitive_outlines=[(4, "#F870FF", 0, 0), (2, "#F870FF", 2, 2)], outlines=[(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)])

image natsuki_name_pink_2:  
    
    truecenter subpixel True
    yoffset 0
    xoffset 360
    
    Text("with Merc, MGT\nand Retro...", size=50, text_align=0.5, slow_cps=0,  color="#fff", insensitive_outlines=[(4, "#F870FF", 0, 0), (2, "#F870FF", 2, 2)], outlines=[(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)])