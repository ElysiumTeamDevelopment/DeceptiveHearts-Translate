image splash_monika_background:
    alpha 0
    2.35
    "mod_assets/splashes/menu_bg_monika.png"
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

#1 AND 2

image splash_monika_1:
    contains:
        truecenter
        subpixel True
        Solid("#268E1E") 
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
        Solid("#35BB2A")
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
        Solid("#6BD562")
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
        Solid("#6FE865")
        crop_relative True
        xanchor 0.0
        yoffset -300
        crop (0.0,0.0,1.0, 0.195)
        ease 2 yoffset -30

    contains:
        0.6
        subpixel True
        Solid("#6FE865")
        crop_relative True
        xanchor 0.0
        yoffset 900
        crop (0.0,0.0,1.0, 0.195)
        ease 2 yoffset 600

image splash_monika_2:
    contains:
        2.95
        matrixcolor BrightnessMatrix(-0.35)
        "mod_assets/splashes/menu_art_m_green.png"
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
        matrixcolor BrightnessMatrix(-0.2)
        "mod_assets/splashes/menu_art_m_green.png"
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
        matrixcolor BrightnessMatrix(-0.1)
        "mod_assets/splashes/menu_art_m_green.png"
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
        'first_monika_appearance'
        alpha 0
        subpixel True truecenter
        easein_quint 2 alpha 1 rotate -3 yoffset -15 zoom 1.1
        block:
            ease 3 zoom 1.14
            ease 3 zoom 1.1
            repeat

    contains:
        2.30
        'first_monika_appearance_2'
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


#CUSTOM ASSETS
image first_monika_appearance:  
    
    truecenter subpixel True
    yoffset 0
    xoffset 375
    
    Text(_("A few days later"), size=50, slow_cps=0,  color="#fff", insensitive_outlines=[(4, "#45AA3C", 0, 0), (2, "#45AA3C", 2, 2)], outlines=[(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)])

image first_monika_appearance_2:  
    
    truecenter subpixel True
    yoffset 30
    xoffset 375
    
    Text(_("At the park"), size=50, slow_cps=0,  color="fff", insensitive_outlines=[(4, "#45AA3C", 0, 0), (2, "#45AA3C", 2, 2)], outlines=[(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)])



image second_monika_appearance:  
    
    truecenter subpixel True
    yoffset 0
    xoffset 375
    
    Text(_("Two years"), size=50, slow_cps=0,  color="#fff", insensitive_outlines=[(4, "#45AA3C", 0, 0), (2, "#45AA3C", 2, 2)], outlines=[(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)])

image second_monika_appearance_2:  
    
    truecenter subpixel True
    yoffset 30
    xoffset 375
    
    Text(_("later..."), size=50, slow_cps=0,  color="fff", insensitive_outlines=[(4, "#45AA3C", 0, 0), (2, "#45AA3C", 2, 2)], outlines=[(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)])


image splash_monika_second_appearance:

    contains:
        2.95
        matrixcolor BrightnessMatrix(-0.35)
        "mod_assets/splashes/menu_art_m_green.png"
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
        matrixcolor BrightnessMatrix(-0.2)
        "mod_assets/splashes/menu_art_m_green.png"
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
        matrixcolor BrightnessMatrix(-0.1)
        "mod_assets/splashes/menu_art_m_green.png"
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
        'second_monika_appearance'
        alpha 0
        subpixel True truecenter
        easein_quint 2 alpha 1 rotate -3 yoffset -15 zoom 1.1
        block:
            ease 3 zoom 1.14
            ease 3 zoom 1.1
            repeat

    contains:
        2.30
        'second_monika_appearance_2'
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

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#3 AND 4

image splash_monika_background_2:
    alpha 0
    2.35
    "mod_assets/splashes/menu_bg_monika.png"
    xtile 50 subpixel True
    crop_relative True
    yoffset -119.5
    crop (0.0,0.0,1.0,0.41)
    matrixcolor BrightnessMatrix(-0.3)
    parallel:
        ease 0.25 alpha 1.0

    block:
        xoffset 0
        linear 80 xoffset 1280
        repeat

image first_monika_appearance_3:  
    
    truecenter subpixel True
    yoffset 0
    xoffset 375
    
    Text("A few days later...", size=50, slow_cps=0,  color="#ffffff", insensitive_outlines=[(4, "#000", 0, 0), (2, "#000", 2, 2)], outlines=[(4, "#000", 0, 0), (2, "#000", 2, 2)])

image splash_monika_3:
    contains:
        truecenter
        subpixel True
        Solid("#1f7819") 
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
        Solid("#268E1E")
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
        Solid("#35BB2A")
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
        Solid("#387932")
        crop_relative True
        xanchor 0.0
        yoffset -300
        crop (0.0,0.0,1.0, 0.195)
        ease 2 yoffset -30

    contains:
        0.6
        subpixel True
        Solid("#387932")
        crop_relative True
        xanchor 0.0
        yoffset 900
        crop (0.0,0.0,1.0, 0.195)
        ease 2 yoffset 600

image splash_monika_4:
    contains:
        2.95
        matrixcolor BrightnessMatrix(-0.8)
        "mod_assets/splashes/menu_art_m_green.png"
        subpixel True
        truecenter
        
        alpha 0
        yoffset 300
        xoffset -290

        parallel:
            easein_quint 3 alpha 1
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
        matrixcolor BrightnessMatrix(-0.7)
        "mod_assets/splashes/menu_art_m_green.png"
        subpixel True
        truecenter
        
        alpha 0
        yoffset 300
        xoffset -290

        parallel:
            easein_quint 3 alpha 0.7
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
        matrixcolor BrightnessMatrix(-0.6)
        "mod_assets/splashes/menu_art_m_green.png"
        subpixel True
        truecenter
        xoffset 800
        alpha 0
        yoffset 300
        easein_quint 1.75 xoffset -290 alpha 0.7
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
        'first_monika_appearance_3'
        alpha 0
        subpixel True truecenter
        easein_quint 2 alpha 1 rotate -3 yoffset -15 zoom 1.1
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
        ParticleBurst("gui/menu_particle.png", explodeTime=0.5, numParticles=0, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
        particle_fadeout

###

image splash_monika_5:
    contains:
        2.95
        matrixcolor BrightnessMatrix(-0.35)
        "mod_assets/splashes/menu_art_m_green.png"
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
        matrixcolor BrightnessMatrix(-0.2)
        "mod_assets/splashes/menu_art_m_green.png"
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
        matrixcolor BrightnessMatrix(-0.1)
        "mod_assets/splashes/menu_art_m_green.png"
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
        'first_monika_appearance_4'
        alpha 0
        subpixel True truecenter
        easein_quint 2 alpha 1 rotate -3 yoffset -15 zoom 1.1
        block:
            ease 3 zoom 1.14
            ease 3 zoom 1.1
            repeat

    contains:
        2.30
        'first_monika_appearance_5'
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


image first_monika_appearance_4:  
    
    truecenter subpixel True
    yoffset 0
    xoffset 375
    
    Text(_("6 months"), size=50, slow_cps=0,  color="#fff", insensitive_outlines=[(4, "#45AA3C", 0, 0), (2, "#45AA3C", 2, 2)], outlines=[(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)])

image first_monika_appearance_5:  
    
    truecenter subpixel True
    yoffset 30
    xoffset 375
    
    Text(_("later..."), size=50, slow_cps=0,  color="#fff", insensitive_outlines=[(4, "#45AA3C", 0, 0), (2, "#45AA3C", 2, 2)], outlines=[(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)])
