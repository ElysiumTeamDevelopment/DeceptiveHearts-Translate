
define chadmc = DynamicCharacter('player', image='chadmc', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

layeredimage chadmc turned:

    at renpy.partial(Flatten, drawable_resolution=False)

    group outfit:

        attribute uniform default null
        attribute casual null



    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute curi null #curious
        attribute dist null #distant
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute lsur null
        attribute nerv null #nervous
        attribute pani null #panicked
        attribute pout null #pouting
        attribute sad null  #sad
        attribute shoc null #shocked
        attribute vang null #VERY angry
        attribute vsur null #surprised (very)
        attribute worr null #worried
        attribute yand null #yandere
        #attribute xxxx null #xxxx #Do you want to define a new mood?  Here, have a template!



    group blush: #These are intentionally separate from mood; the idea being that these aren't consciously controlled by the character - rather, they're a result of their emotions making them blush/sweat/etc.
        attribute nobl default null #Default, no blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n


    always "mod_assets/MPT/chadmc/chadmc_uniform_facebase.png"  if_all(["uniform"])
    always "mod_assets/MPT/chadmc/chadmc_casual_facebase.png"  if_all(["casual"])

    group left:
        anchor (0,0) subpixel (True)
        yoffset (-0.5)
        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/chadmc/chadmc_uniform_left_down.png"
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/chadmc/chadmc_casual_left_down.png"
        attribute lhip if_any(["uniform"]):
            "mod_assets/MPT/chadmc/chadmc_uniform_left_hip.png"
        attribute lshrug if_any(["uniform"]):
            "mod_assets/MPT/chadmc/chadmc_uniform_left_shrug.png"
        attribute lthink if_any(["uniform"]):
            "mod_assets/MPT/chadmc/chadmc_uniform_left_think.png"



    group right:
        anchor (0,0) subpixel (True)
        yoffset (-0.5)
        attribute rdown default if_any(["uniform"]):
            "mod_assets/MPT/chadmc/chadmc_uniform_right_down.png"
        attribute rdown default if_any(["casual"]):
            "mod_assets/MPT/chadmc/chadmc_casual_right_down.png"
        attribute rhip if_any(["uniform"]):
            "mod_assets/MPT/chadmc/chadmc_uniform_right_hip.png"
        attribute rshrug if_any(["uniform"]):
            "mod_assets/MPT/chadmc/chadmc_uniform_right_shrug.png"



    group nose:

        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            "mod_assets/MPT/chadmc/chadmc_nose_n1.png"
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            "mod_assets/MPT/chadmc/chadmc_nose_n2.png"
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            "mod_assets/MPT/chadmc/chadmc_nose_n3.png"
        attribute nose default if_any(["blaw"]):#default nose when "blushing and awkward"
            "mod_assets/MPT/chadmc/chadmc_nose_n4.png"


        #All noses - truncated tags:
        attribute n1:
            "mod_assets/MPT/chadmc/chadmc_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/chadmc/chadmc_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/chadmc/chadmc_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/chadmc/chadmc_nose_n4.png"

    group mouth:

        ###All mouths - truncated tags:
        attribute cm default if_any(["happ", "laug", "nerv"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_ma.png"
        attribute cm default if_any(["yand", "yandere"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_mc.png"
        attribute cm default if_any(["neut", "angr", "anno", "curi", "dist", "flus", "sad", "worr"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_md.png"
        attribute cm default if_any(["pout", "lsur", "vsur"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_me.png"
        attribute cm default if_any(["shoc"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_mi.png"
        attribute cm default if_any(["vang", "pani"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_mk.png"

        attribute om if_any(["happ", "laug", "nerv", "yand"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_mb.png"
        attribute om if_any(["neut", "curi", "dist", "pout", "vsur", "worr"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_mf.png"
        attribute om if_any(["angr", "anno"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_mg.png"
        attribute om if_any(["pani", "vang"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_mh.png"
        attribute om if_any(["flus", "lsur"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_mi.png"
        attribute om if_any(["sad", "shoc"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_mj.png"

        attribute ma:
            "mod_assets/MPT/chadmc/chadmc_mouth_ma.png"
        attribute mb:
            "mod_assets/MPT/chadmc/chadmc_mouth_mb.png"
        attribute mc:
            "mod_assets/MPT/chadmc/chadmc_mouth_mc.png"
        attribute md:
            "mod_assets/MPT/chadmc/chadmc_mouth_md.png"
        attribute me:
            "mod_assets/MPT/chadmc/chadmc_mouth_me.png"
        attribute mf:
            "mod_assets/MPT/chadmc/chadmc_mouth_mf.png"
        attribute mg:
            "mod_assets/MPT/chadmc/chadmc_mouth_mg.png"
        attribute mh:
            "mod_assets/MPT/chadmc/chadmc_mouth_mh.png"
        attribute mi:
            "mod_assets/MPT/chadmc/chadmc_mouth_mi.png"
        attribute mj:
            "mod_assets/MPT/chadmc/chadmc_mouth_mj.png"
        attribute mk:
            "mod_assets/MPT/chadmc/chadmc_mouth_mk.png"

    group eyes:

        attribute oe default if_any(["neut", "angr", "anno", "curi", "happ", "laug", "lsur", "pani", "pout", "sad", "shoc", "vang", "vsur", "yand"]):
            "mod_assets/MPT/chadmc/chadmc_eyes_e1.png"
        attribute oe default if_any(["dist", "flus", "nerv", "worr"]):
            "mod_assets/MPT/chadmc/chadmc_eyes_e2.png"

        attribute ce if_any(["neut", "angr", "anno", "curi", "dist", "flus", "lsur", "pani", "pout", "sad", "shoc", "vang", "vsur", "worr"]):
            "mod_assets/MPT/chadmc/chadmc_eyes_e3.png"
        attribute ce if_any(["happ", "laug", "nerv", "yand"]):
            "mod_assets/MPT/chadmc/chadmc_eyes_e4.png"

        attribute e1a:
            "mod_assets/MPT/chadmc/chadmc_eyes_e1.png"
        attribute e1b:
            "mod_assets/MPT/chadmc/chadmc_eyes_e2.png"
        attribute e1c:
            "mod_assets/MPT/chadmc/chadmc_eyes_e3.png"
        attribute e1d:
            "mod_assets/MPT/chadmc/chadmc_eyes_e4.png"
        attribute e1e:
            "mod_assets/MPT/chadmc/chadmc_eyes_e5.png"
        attribute e1f:
            "mod_assets/MPT/chadmc/chadmc_eyes_e6.png"
        attribute e1g:
            "mod_assets/MPT/chadmc/chadmc_eyes_e7.png"

    group eyebrows:

        attribute brow default if_any(["neut", "dist", "happ", "lsur"]):
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b1.png"
        attribute brow default if_any(["anno", "pout"]):
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b2.png"
        attribute brow default if_any(["angr", "vang"]):
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b3.png"
        attribute brow default if_any(["yand"]):
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b4.png"
        attribute brow default if_any(["flus", "laug", "nerv", "pani", "sad", "shoc", "vsur", "worr"]):
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b5.png"
        attribute brow default if_any(["curi"]):
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b6.png"

        attribute b1a:
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b1.png"
        attribute b1b:
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b2.png"
        attribute b1c:
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b3.png"
        attribute b1d:
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b4.png"
        attribute b1e:
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b5.png"
        attribute b1f:
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b6.png"

    #This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group special:

        attribute s_scream:
            "mod_assets/MPT/chadmc/chadmc_special_scream.png"

layeredimage chadmc cross:

    at Flatten

    group outfit:
        attribute uniform default null

    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute curi null #curious
        attribute dist null #distant
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute lsur null
        attribute nerv null #nervous
        attribute pani null #panicked
        attribute pout null #pouting
        attribute sad null  #sad
        attribute shoc null #shocked
        attribute vang null #VERY angry
        attribute vsur null #surprised (very)
        attribute worr null #worried
        attribute yand null #yandere
        #attribute xxxx null #xxxx #Do you want to define a new mood?  Here, have a template!

    group blush: #These are intentionally separate from mood; the idea being that these aren't consciously controlled by the character - rather, they're a result of their emotions making them blush/sweat/etc.
        attribute nobl default null #Default, no blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n


    always "mod_assets/MPT/povmc/povmc_uniform_facebase.png"  if_all(["uniform"])

    always "mod_assets/MPT/povmc/povmc_uniform_cross.png"  if_all(["uniform"])

    group nose:

        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            "mod_assets/MPT/chadmc/chadmc_nose_n1.png"
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            "mod_assets/MPT/chadmc/chadmc_nose_n2.png"
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            "mod_assets/MPT/chadmc/chadmc_nose_n3.png"
        attribute nose default if_any(["blaw"]):#default nose when "blushing and awkward"
            "mod_assets/MPT/chadmc/chadmc_nose_n4.png"


        #All noses - truncated tags:
        attribute n1:
            "mod_assets/MPT/chadmc/chadmc_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/chadmc/chadmc_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/chadmc/chadmc_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/chadmc/chadmc_nose_n4.png"

    group mouth:

        ###All mouths - truncated tags:
        attribute cm default if_any(["happ", "laug", "nerv"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_ma.png"
        attribute cm default if_any(["yand", "yandere"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_mc.png"
        attribute cm default if_any(["neut", "angr", "anno", "curi", "dist", "flus", "sad", "worr"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_md.png"
        attribute cm default if_any(["pout", "lsur", "vsur"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_me.png"
        attribute cm default if_any(["shoc"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_mi.png"
        attribute cm default if_any(["vang", "pani"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_mk.png"

        attribute om if_any(["happ", "laug", "nerv", "yand"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_mb.png"
        attribute om if_any(["neut", "curi", "dist", "pout", "vsur", "worr"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_mf.png"
        attribute om if_any(["angr", "anno"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_mg.png"
        attribute om if_any(["pani", "vang"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_mh.png"
        attribute om if_any(["flus", "lsur"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_mi.png"
        attribute om if_any(["sad", "shoc"]):
            "mod_assets/MPT/chadmc/chadmc_mouth_mj.png"

        attribute ma:
            "mod_assets/MPT/chadmc/chadmc_mouth_ma.png"
        attribute mb:
            "mod_assets/MPT/chadmc/chadmc_mouth_mb.png"
        attribute mc:
            "mod_assets/MPT/chadmc/chadmc_mouth_mc.png"
        attribute md:
            "mod_assets/MPT/chadmc/chadmc_mouth_md.png"
        attribute me:
            "mod_assets/MPT/chadmc/chadmc_mouth_me.png"
        attribute mf:
            "mod_assets/MPT/chadmc/chadmc_mouth_mf.png"
        attribute mg:
            "mod_assets/MPT/chadmc/chadmc_mouth_mg.png"
        attribute mh:
            "mod_assets/MPT/chadmc/chadmc_mouth_mh.png"
        attribute mi:
            "mod_assets/MPT/chadmc/chadmc_mouth_mi.png"
        attribute mj:
            "mod_assets/MPT/chadmc/chadmc_mouth_mj.png"
        attribute mk:
            "mod_assets/MPT/chadmc/chadmc_mouth_mk.png"

    group eyes:

        attribute oe default if_any(["neut", "angr", "anno", "curi", "happ", "laug", "lsur", "pani", "pout", "sad", "shoc", "vang", "vsur", "yand"]):
            "mod_assets/MPT/chadmc/chadmc_eyes_e1.png"
        attribute oe default if_any(["dist", "flus", "nerv", "worr"]):
            "mod_assets/MPT/chadmc/chadmc_eyes_e2.png"

        attribute ce if_any(["neut", "angr", "anno", "curi", "dist", "flus", "lsur", "pani", "pout", "sad", "shoc", "vang", "vsur", "worr"]):
            "mod_assets/MPT/chadmc/chadmc_eyes_e3.png"
        attribute ce if_any(["happ", "laug", "nerv", "yand"]):
            "mod_assets/MPT/chadmc/chadmc_eyes_e4.png"

        attribute e1a:
            "mod_assets/MPT/chadmc/chadmc_eyes_e1.png"
        attribute e1b:
            "mod_assets/MPT/chadmc/chadmc_eyes_e2.png"
        attribute e1c:
            "mod_assets/MPT/chadmc/chadmc_eyes_e3.png"
        attribute e1d:
            "mod_assets/MPT/chadmc/chadmc_eyes_e4.png"
        attribute e1e:
            "mod_assets/MPT/chadmc/chadmc_eyes_e5.png"
        attribute e1f:
            "mod_assets/MPT/chadmc/chadmc_eyes_e6.png"
        attribute e1g:
            "mod_assets/MPT/chadmc/chadmc_eyes_e7.png"

    group eyebrows:

        attribute brow default if_any(["neut", "dist", "happ", "lsur"]):
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b1.png"
        attribute brow default if_any(["anno", "pout"]):
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b2.png"
        attribute brow default if_any(["angr", "vang"]):
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b3.png"
        attribute brow default if_any(["yand"]):
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b4.png"
        attribute brow default if_any(["flus", "laug", "nerv", "pani", "sad", "shoc", "vsur", "worr"]):
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b5.png"
        attribute brow default if_any(["curi"]):
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b6.png"

        attribute b1a:
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b1.png"
        attribute b1b:
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b2.png"
        attribute b1c:
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b3.png"
        attribute b1d:
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b4.png"
        attribute b1e:
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b5.png"
        attribute b1f:
            "mod_assets/MPT/chadmc/chadmc_eyebrows_b6.png"

    #This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group special:

        attribute s_scream:
            "mod_assets/MPT/chadmc/chadmc_special_scream.png"
