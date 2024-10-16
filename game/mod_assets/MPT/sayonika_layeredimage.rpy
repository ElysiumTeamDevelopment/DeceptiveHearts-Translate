layeredimage sayonika turned:

    at renpy.partial(Flatten, drawable_resolution=False)

    always "mod_assets/MPT/sayonika/turned_facebase.png"

    group outfit:
        attribute uniform default null
        attribute casual null

    group left:
        subpixel True
        anchor (0.0, 0.0)
        yoffset 0.1

        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/sayonika/outfits/turned_uniform_ldown.png"
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/sayonika/outfits/turned_casual_ldown.png"

        attribute lpoint if_any(["uniform"]):
            "mod_assets/MPT/sayonika/outfits/turned_uniform_lpoint.png"
        attribute lpoint if_any(["casual"]):
            "mod_assets/MPT/sayonika/outfits/turned_casual_lpoint.png"
    
    group right:
        subpixel True
        anchor (0.0, 0.0)
        yoffset 0.1

        attribute rdown default if_any(["uniform"]):
            "mod_assets/MPT/sayonika/outfits/turned_uniform_rdown.png"
        attribute rdown default if_any(["casual"]):
            "mod_assets/MPT/sayonika/outfits/turned_casual_rdown.png"

        attribute rhip if_any(["uniform"]):
            "mod_assets/MPT/sayonika/outfits/turned_uniform_rhip.png"
        attribute rhip if_any(["casual"]):
            "mod_assets/MPT/sayonika/outfits/turned_casual_rhip.png"

    group nose:
        attribute na default null
        attribute nb:
            "mod_assets/MPT/sayonika/turned_nose_b.png"     # sweat drop
        attribute nc:
            "mod_assets/MPT/sayonika/turned_nose_c.png"     # blush

    group eyes:
        attribute ea default:
            "mod_assets/MPT/sayonika/turned_eyes_a.png"     # neutral
        attribute eb:
            "mod_assets/MPT/sayonika/turned_eyes_b.png"     # surprised
        attribute ec:
            "mod_assets/MPT/sayonika/turned_eyes_c.png"     # distant
        attribute ed:
            "mod_assets/MPT/sayonika/turned_eyes_d.png"     # tears
        attribute ee:
            "mod_assets/MPT/sayonika/turned_eyes_e.png"     # closed
        attribute ef:
            "mod_assets/MPT/sayonika/turned_eyes_f.png"     # closed + happy
        attribute eg:
            "mod_assets/MPT/sayonika/turned_eyes_g.png"     # crazy
        attribute eh:
            "mod_assets/MPT/sayonika/turned_eyes_h.png"     # >_<
        
    group eyebrows:
        attribute ba default:
            "mod_assets/MPT/sayonika/turned_eyebrows_a.png" # neutral
        attribute bb:
            "mod_assets/MPT/sayonika/turned_eyebrows_b.png" # serious
        attribute bc:
            "mod_assets/MPT/sayonika/turned_eyebrows_c.png" # raised eyebrow *vine boom*
        attribute bd:
            "mod_assets/MPT/sayonika/turned_eyebrows_d.png" # bit worried
        attribute be:
            "mod_assets/MPT/sayonika/turned_eyebrows_e.png" # worried
        attribute bf:
            "mod_assets/MPT/sayonika/turned_eyebrows_f.png" # anger
    
    group mouth:
        attribute ma default:
            "mod_assets/MPT/sayonika/turned_mouth_a.png"    # smiling
        attribute mb:
            "mod_assets/MPT/sayonika/turned_mouth_b.png"    # talking + happy
        attribute mc:
            "mod_assets/MPT/sayonika/turned_mouth_c.png"    # talking + very happy
        attribute md:
            "mod_assets/MPT/sayonika/turned_mouth_d.png"    # closed
        attribute me:
            "mod_assets/MPT/sayonika/turned_mouth_e.png"    # closed + bit opened
        attribute mf:
            "mod_assets/MPT/sayonika/turned_mouth_f.png"    # .
        attribute mg:
            "mod_assets/MPT/sayonika/turned_mouth_g.png"    # talking
        attribute mh:
            "mod_assets/MPT/sayonika/turned_mouth_h.png"    # embarassed / worried
        attribute mi:
            "mod_assets/MPT/sayonika/turned_mouth_i.png"    # anger


layeredimage sayonika lean:
    at Flatten

    always "mod_assets/MPT/sayonika/lean_facebase.png"

    group center:
        subpixel True
        anchor (0.0, 0.0)
        yoffset -0.7

        attribute uniform default:
            "mod_assets/MPT/sayonika/outfits/lean_uniform.png"
        attribute casual:
            "mod_assets/MPT/sayonika/outfits/lean_casual.png"
    
    group nose:
        attribute na default null
        attribute nb:
            "mod_assets/MPT/sayonika/lean_nose_b.png"     # sweat drop
        attribute nc:
            "mod_assets/MPT/sayonika/lean_nose_c.png"     # blush
    
    group eyes:
        attribute ea default:
            "mod_assets/MPT/sayonika/lean_eyes_a.png"     # neutral
        attribute eb:
            "mod_assets/MPT/sayonika/lean_eyes_b.png"     # looking a bit to the side
        attribute ec:
            "mod_assets/MPT/sayonika/lean_eyes_c.png"     # closed + happy
        
    group eyebrows:
        attribute ba default:
            "mod_assets/MPT/sayonika/lean_eyebrows_a.png" # neutral
        attribute bb:
            "mod_assets/MPT/sayonika/lean_eyebrows_b.png" # serious
        attribute bc:
            "mod_assets/MPT/sayonika/lean_eyebrows_c.png" # worried
    
    group mouth:
        attribute ma default:
            "mod_assets/MPT/sayonika/lean_mouth_a.png"    # smiling
        attribute mb:
            "mod_assets/MPT/sayonika/lean_mouth_b.png"    # talking + happy
        attribute mc:
            "mod_assets/MPT/sayonika/lean_mouth_c.png"    # closed
        attribute md:
            "mod_assets/MPT/sayonika/lean_mouth_d.png"    # closed but a bit opened