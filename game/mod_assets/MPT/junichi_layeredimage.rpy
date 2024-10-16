


layeredimage junichi base:

    at renpy.partial(Flatten, drawable_resolution = False)

    always "mod_assets/MPT/Junichi/Expressions/base.png"

    group outfit:
        attribute uniform default null
        attribute casual null

    group mood:
        attribute neut default null
        attribute angr null
        attribute cry null
        attribute flus null
        attribute happ null
        attribute laug null
        attribute nerv null
        attribute pani null
        attribute sad null
        attribute sedu null
        attribute shoc null
        attribute vang null
        attribute surp null
        attribute worr null
        attribute yand null

    
    group left:
        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/Junichi/Poses/1l.png"
        attribute lup if_any(["uniform"]):
            "mod_assets/MPT/Junichi/Poses/2l.png"
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/Junichi/Poses/1bl.png"
        attribute lup if_all(["casual"]):
            "mod_assets/MPT/Junichi/Poses/2bl.png"

    
    group right:
        attribute rdown default if_any(["uniform"]):
            "mod_assets/MPT/Junichi/Poses/1r.png"
        attribute rup if_any(["uniform"]):
            "mod_assets/MPT/Junichi/Poses/2r.png"
        attribute rdown if_any(["casual"]):
            "mod_assets/MPT/Junichi/Poses/1br.png"
        attribute rup if_any(["casual"]):
            "mod_assets/MPT/Junichi/Poses/2br.png"


    group nose:
        attribute nose default if_any(["neut", "angr", "cry", "happ", "laug", "sad", "shoc", "vang", "surp", "worr", "yand"]):
            "mod_assets/MPT/Junichi/Expressions/Nose/blush1.png" # default blush
        attribute blush default if_any(["flus", "nerv", "pani", "sedu"]):
            "mod_assets/MPT/Junichi/Expressions/Nose/blush2.png" # flustered blush
        attribute noblush:
            null

        attribute n1:
            "mod_assets/MPT/Junichi/Expressions/Nose/blush1.png" # default blush
        attribute n2:
            "mod_assets/MPT/Junichi/Expressions/Nose/blush2.png" # flustered blush
            
    group mouth:
        attribute cm default if_any(["neut", "flus", "sad"]):
            "mod_assets/MPT/Junichi/Expressions/Mouth/mn.png" # neutral mouth
        attribute cm default if_any(["happ", "nerv"]):
            "mod_assets/MPT/Junichi/Expressions/Mouth/ms.png" # smiling mouth
        attribute om if_any(["happ", "laug", "sedu"]):
            "mod_assets/MPT/Junichi/Expressions/Mouth/ml.png" # laughing mouth
        attribute om if_any(["neut", "worr", "sad", "flus", "nerv", ""]):
            "mod_assets/MPT/Junichi/Expressions/Mouth/mo.png" # open mouth
        attribute om if_any(["yand", "pani", "surp", "cry"]):
            "mod_assets/MPT/Junichi/Expressions/Mouth/my.png" # wide mouth
        attribute cm default if_any(["laug", "pani", "sedu", "yand"]):
            "mod_assets/MPT/Junichi/Expressions/Mouth/mf.png" # smiling teeth mouth
        attribute cm default if_any(["angr", "cry", "shoc", "vang", "surp","worr"]):
            "mod_assets/MPT/Junichi/Expressions/Mouth/mm.png" # gitted teeth mouth
        attribute om if_any(["angr", "vang", "shoc"]):
            "mod_assets/MPT/Junichi/Expressions/Mouth/mt.png" # wide mouth (angry)

        attribute ms:
            "mod_assets/MPT/Junichi/Expressions/Mouth/ms.png" # smiling mouth
        attribute mn:
            "mod_assets/MPT/Junichi/Expressions/Mouth/mn.png" # neutral mouth
        attribute ml:
            "mod_assets/MPT/Junichi/Expressions/Mouth/ml.png" # laughing mouth
        attribute mo:
            "mod_assets/MPT/Junichi/Expressions/Mouth/mo.png" # open mouth
        attribute my:
            "mod_assets/MPT/Junichi/Expressions/Mouth/my.png" # wide mouth
        attribute mf:
            "mod_assets/MPT/Junichi/Expressions/Mouth/mf.png" # smiling teeth mouth
        attribute mm:
            "mod_assets/MPT/Junichi/Expressions/Mouth/mm.png" # gitted teeth mouth
        attribute mt:
            "mod_assets/MPT/Junichi/Expressions/Mouth/mt.png" # wide mouth (angry)
    
    group eyes:
        attribute oe default if_any(["neut", "angr", "flus", "happ", "laug", "nerv", "sad", "sedu", "worr"]):
            "mod_assets/MPT/Junichi/Expressions/Eyes/en.png" # neutral eyes
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/Junichi/Expressions/Eyes/ec.png" # crying eyes
        attribute oe default if_any(["pani", "shoc", "vang", "surp", "yand"]):
            "mod_assets/MPT/Junichi/Expressions/Eyes/es.png" # wide eyes
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/Junichi/Expressions/Eyes/em.png" # closed eyes (crying)
        attribute ce if_any(["neut", "angr", "flus", "happ", "laug", "nerv", "sad", "sedu", "worr"]):
            "mod_assets/MPT/Junichi/Expressions/Eyes/er.png" # closed eyes
        attribute ce if_any(["pani", "shoc", "vang", "surp", "yand"]):
            "mod_assets/MPT/Junichi/Expressions/Eyes/eh.png" # closed eyes (squinted)

        attribute en:
            "mod_assets/MPT/Junichi/Expressions/Eyes/en.png" # neutral eyes
        attribute ec:
            "mod_assets/MPT/Junichi/Expressions/Eyes/ec.png" # crying eyes
        attribute es:
            "mod_assets/MPT/Junichi/Expressions/Eyes/es.png" # wide eyes
        attribute em:
            "mod_assets/MPT/Junichi/Expressions/Eyes/em.png" # closed eyes (crying)
        attribute er:
            "mod_assets/MPT/Junichi/Expressions/Eyes/er.png" # closed eyes
        attribute eh:
            "mod_assets/MPT/Junichi/Expressions/Eyes/eh.png" # closed eyes (squinted)

    
    group eyebrows:
        attribute brow default if_any(["neut", "happ", "laug", "nerv", "sedu", "shoc", "flus"]):
            "mod_assets/MPT/Junichi/Expressions/Eyebrows/bn.png" # neutral eyebrows
        attribute brow default if_any(["cry", "pani", "sad", "surp", "worr", "yand"]):
            "mod_assets/MPT/Junichi/Expressions/Eyebrows/br.png" # raised eyebrows
        attribute brow default if_any(["angr", "vang"]):
            "mod_assets/MPT/Junichi/Expressions/Eyebrows/ba.png" # lowered eyebrows

        attribute bn:
            "mod_assets/MPT/Junichi/Expressions/Eyebrows/bn.png" # neutral eyebrows
        attribute br:
            "mod_assets/MPT/Junichi/Expressions/Eyebrows/br.png" # raised eyebrows
        attribute ba:
            "mod_assets/MPT/Junichi/Expressions/Eyebrows/ba.png" # lowered eyebrows



layeredimage junichi corrupted:
    
    at renpy.partial(Flatten, drawable_resolution = False)

    always "mod_assets/MPT/Junichi/Expressions/basec.png"

    group outfit:
        attribute uniform default null
        attribute casual null
    

    group left:
        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/Junichi/Poses/1lc.png"
        attribute lup if_any(["uniform"]):
            "mod_assets/MPT/Junichi/Poses/2lc.png"
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/Junichi/Poses/1blc.png"
        attribute lup if_any(["casual"]):
            "mod_assets/MPT/Junichi/Poses/2blc.png"
    

    group right:
        attribute rdown default if_any(["uniform"]):
            "mod_assets/MPT/Junichi/Poses/1rc.png"
        attribute rup if_any(["uniform"]):
            "mod_assets/MPT/Junichi/Poses/2rc.png"
        attribute rdown default if_any(["casual"]):
            "mod_assets/MPT/Junichi/Poses/1brc.png"
        attribute rup if_any(["casual"]):
            "mod_assets/MPT/Junichi/Poses/2brc.png"
    

    group nose:
        attribute nose default if_any(["neut", "angr", "cry", "happ", "laug", "sad", "shoc", "vang", "surp", "worr", "yand"]):
            "mod_assets/MPT/Junichi/Expressions/Nose/blush1c.png" # default blush
        attribute blush default if_any(["flus", "nerv", "pani", "sedu"]):
            "mod_assets/MPT/Junichi/Expressions/Nose/blush2c.png" # flustered blush
        attribute noblush:
            null

        attribute n1:
            "mod_assets/MPT/Junichi/Expressions/Nose/blush1c.png"
        attribute n2:
            "mod_assets/MPT/Junichi/Expressions/Nose/blush2c.png"
    
    group mouth:
        attribute cm default if_any(["neut", "flus", "sad"]):
            "mod_assets/MPT/Junichi/Expressions/Mouth/mnc.png" # neutral mouth
        attribute cm default if_any(["happ", "nerv"]):
            "mod_assets/MPT/Junichi/Expressions/Mouth/msc.png" # smiling mouth
        attribute om:
            "mod_assets/MPT/Junichi/Expressions/Mouth/mlc.png" # laughing mouth
        attribute om:
            "mod_assets/MPT/Junichi/Expressions/Mouth/moc.png" # open mouth
        attribute om:
            "mod_assets/MPT/Junichi/Expressions/Mouth/myc.png" # wide mouth
        attribute cm default if_any(["laug", "pani", "sedu", "yand"]):
            "mod_assets/MPT/Junichi/Expressions/Mouth/mfc.png" # smiling teeth mouth
        attribute cm default if_any(["angr", "cry", "shoc", "vang", "surp","worr"]):
            "mod_assets/MPT/Junichi/Expressions/Mouth/mmc.png" # gitted teeth mouth
        attribute om:
            "mod_assets/MPT/Junichi/Expressions/Mouth/mtc.png" # wide mouth (angry)

        attribute ms:
            "mod_assets/MPT/Junichi/Expressions/Mouth/msc.png"
        attribute mn:
            "mod_assets/MPT/Junichi/Expressions/Mouth/mnc.png"
        attribute ml:
            "mod_assets/MPT/Junichi/Expressions/Mouth/mlc.png"
        attribute mo:
            "mod_assets/MPT/Junichi/Expressions/Mouth/moc.png"
        attribute my:
            "mod_assets/MPT/Junichi/Expressions/Mouth/myc.png"
        attribute mf:
            "mod_assets/MPT/Junichi/Expressions/Mouth/mfc.png"
        attribute mm:
            "mod_assets/MPT/Junichi/Expressions/Mouth/mmc.png"
        attribute mt:
            "mod_assets/MPT/Junichi/Expressions/Mouth/mtc.png"
    
    group eyes:
        attribute oe default if_any(["neut", "angr", "flus", "happ", "laug", "nerv", "sad", "sedu", "worr"]):
            "mod_assets/MPT/Junichi/Expressions/Eyes/enc.png" # neutral eyes
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/Junichi/Expressions/Eyes/ecc.png" # crying eyes
        attribute oe default if_any(["pani", "shoc", "vang", "surp", "yand"]):
            "mod_assets/MPT/Junichi/Expressions/Eyes/esc.png" # wide eyes
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/Junichi/Expressions/Eyes/emc.png" # closed eyes (crying)
        attribute ce if_any(["neut", "angr", "flus", "happ", "laugh", "nerv", "sad", "sedu", "worr"]):
            "mod_assets/MPT/Junichi/Expressions/Eyes/erc.png" # closed eyes
        attribute ce if_any(["pani", "shoc", "vang", "surp", "yand"]):
            "mod_assets/MPT/Junichi/Expressions/Eyes/ehc.png" # closed eyes (squinted)

        attribute en:
            "mod_assets/MPT/Junichi/Expressions/Eyes/enc.png"
        attribute ec:
            "mod_assets/MPT/Junichi/Expressions/Eyes/ecc.png"
        attribute es:
            "mod_assets/MPT/Junichi/Expressions/Eyes/esc.png"
        attribute em:
            "mod_assets/MPT/Junichi/Expressions/Eyes/emc.png"
        attribute er:
            "mod_assets/MPT/Junichi/Expressions/Eyes/erc.png"
        attribute eh:
            "mod_assets/MPT/Junichi/Expressions/Eyes/ehc.png"
    
    group eyebrows:
        attribute brow default if_any(["neut", "happ", "laug", "nerv", "sedu", "shoc", "flus"]):
            "mod_assets/MPT/Junichi/Expressions/Eyebrows/bnc.png" # neutral eyebrows
        attribute brow default if_any(["cry", "pani", "sad", "surp", "worr", "yand"]):
            "mod_assets/MPT/Junichi/Expressions/Eyebrows/brc.png" # raised eyebrows
        attribute brow default if_any(["angr", "vang"]):
            "mod_assets/MPT/Junichi/Expressions/Eyebrows/bac.png" # lowered eyebrows

        attribute bn:
            "mod_assets/MPT/Junichi/Expressions/Eyebrows/bnc.png"
        attribute br:
            "mod_assets/MPT/Junichi/Expressions/Eyebrows/brc.png"
        attribute ba:
            "mod_assets/MPT/Junichi/Expressions/Eyebrows/bac.png"
