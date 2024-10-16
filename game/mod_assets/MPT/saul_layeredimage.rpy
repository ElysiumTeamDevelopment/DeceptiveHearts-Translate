layeredimage braethan:

    at renpy.partial(Flatten, drawable_resolution = False)
    
    always "mod_assets/MPT/saul/saul_turned_facebase.png" #Always need this face.

    group outfit: #These attributes are here only to determine which set of "body" sprites to use later.  "null" is what lets us just use these attributes as logic and nothing else.
        attribute suit default null
        attribute black null
        attribute circus null

    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute cry null  #crying
        attribute curi null #curious
        attribute dist null #distant
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute lsur null #surprised (lightly)
        attribute nerv null #nervous
        attribute pani null #panicked
        attribute pout null #pouting
        attribute sad null  #sad
        attribute sedu null #seductive
        attribute shoc null #shocked
        attribute vang null #VERY angry
        attribute vsur null #surprised (very)
        attribute worr null #worried
        attribute yand null #yandere
        attribute blnk null
        #attribute xxxx null #xxxx #Do you want to define a new mood?  Here, have a template!



    group blush: #Have to separate these out, they can't share moods.
        attribute nobl null #No blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n



    #Left arm variants
    group left if_any(["suit"]):
        attribute ldown default:
            "mod_assets/MPT/saul/saul_turned_suit_left_down.png"
        attribute lpoint:
            "mod_assets/MPT/saul/saul_turned_suit_left_point.png"
        attribute lphone:
            "mod_assets/MPT/saul/saul_turned_suit_left_phone.png"

    group left if_any(["black"]):
        attribute ldown default:
            "mod_assets/MPT/saul/saul_turned_black_left_down.png"
        attribute lpoint:
            "mod_assets/MPT/saul/saul_turned_black_left_point.png"
        attribute lphone:
            "mod_assets/MPT/saul/saul_turned_black_left_phone.png"

    group left if_any(["circus"]):
        attribute ldown default:
            "mod_assets/MPT/saul/saul_turned_circus_left_down.png"
        attribute lpoint:
            "mod_assets/MPT/saul/saul_turned_circus_left_point.png"
        attribute lphone:
            "mod_assets/MPT/saul/saul_turned_circus_left_phone.png"


    #Right arm variants
    group right if_any(["suit"]):
        attribute rdown default:
            "mod_assets/MPT/saul/saul_turned_suit_right_down.png"
        attribute rpoint:
            "mod_assets/MPT/saul/saul_turned_suit_right_point.png"

    group right if_any(["black"]):
        attribute rdown default:
            "mod_assets/MPT/saul/saul_turned_black_right_down.png"
        attribute rpoint:
            "mod_assets/MPT/saul/saul_turned_black_right_point.png"

    group right if_any(["circus"]):
        attribute rdown default:
            "mod_assets/MPT/saul/saul_turned_circus_right_down.png"
        attribute rpoint:
            "mod_assets/MPT/saul/saul_turned_circus_right_point.png"

    group nose:

        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            "mod_assets/MPT/saul/saul_turned_nose_n1.png"
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            "mod_assets/MPT/saul/saul_turned_nose_n2.png"
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            "mod_assets/MPT/saul/saul_turned_nose_n3.png"
        attribute nose default if_any(["blaw"]):#default nose when "blushing and awkward"
            "mod_assets/MPT/saul/saul_turned_nose_n4.png"
        attribute nose default if_any(["blnk"]):
            "mod_assets/MPT/saul/saul_turned_nose_n1.png"


        #All noses - truncated tags:
        attribute n1:
            "mod_assets/MPT/saul/saul_turned_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/saul/saul_turned_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/saul/saul_turned_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/saul/saul_turned_nose_n4.png"
        attribute nl:
            "mod_assets/MPT/saul/saul_turned_nose_nl.png"



    group mouth:

        #Default Closed Mouths:
        attribute cm default if_any(["happ","sedu","nerv"]):
            "mod_assets/MPT/saul/saul_turned_mouth_ma.png"
        attribute cm default if_any(["neut","anno","worr","curi"]):
            "mod_assets/MPT/saul/saul_turned_mouth_md.png"
        attribute cm default if_any(["dist","flus"]):
            "mod_assets/MPT/saul/saul_turned_mouth_me.png"
        attribute cm default if_any(["lsur","shoc"]):
            "mod_assets/MPT/saul/saul_turned_mouth_mf.png"
        attribute cm default if_any(["sad","angr","pout","doub"]):
            "mod_assets/MPT/saul/saul_turned_mouth_mj.png"
        attribute cm default if_any(["cry","pani","vsur"]):
            "mod_assets/MPT/saul/saul_turned_mouth_mk.png"
        attribute cm default if_any(["vang"]):
            "mod_assets/MPT/saul/saul_turned_mouth_mm.png"
        attribute cm default if_any(["laug"]):
            "mod_assets/MPT/saul/saul_turned_mouth_mn.png"
        attribute cm default if_any(["yand"]):
            "mod_assets/MPT/saul/saul_turned_mouth_mo.png"
        attribute cm default if_any(["blnk"]):
            "mod_assets/MPT/saul/saul_turned_nose_n1.png"

        #Open Mouths:
        attribute om if_any(["happ","laug"]):
            "mod_assets/MPT/saul/saul_turned_mouth_mb.png"
        attribute om if_any(["yand","nerv"]):
            "mod_assets/MPT/saul/saul_turned_mouth_mc.png"
        attribute om if_any(["pout","sedu"]):
            "mod_assets/MPT/saul/saul_turned_mouth_mf.png"
        attribute om if_any(["sad","lsur","dist"]):
            "mod_assets/MPT/saul/saul_turned_mouth_mg.png"
        attribute om if_any(["neut","anno","shoc","worr"]):
            "mod_assets/MPT/saul/saul_turned_mouth_mh.png"
        attribute om if_any(["curi","doub"]):
            "mod_assets/MPT/saul/saul_turned_mouth_mi.png"
        attribute om if_any(["flus"]):
            "mod_assets/MPT/saul/saul_turned_mouth_mk.png"
        attribute om if_any(["cry","vsur"]):
            "mod_assets/MPT/saul/saul_turned_mouth_ml.png"
        attribute om if_any(["angr","pani","vang"]):
            "mod_assets/MPT/saul/saul_turned_mouth_mq.png"
        attribute om if_any(["blnk"]):
            "mod_assets/MPT/saul/saul_turned_nose_n1.png"


        ###All mouths - truncated tags:
        attribute ma:
            "mod_assets/MPT/saul/saul_turned_mouth_ma.png"
        attribute mb:
            "mod_assets/MPT/saul/saul_turned_mouth_mb.png"
        attribute mc:
            "mod_assets/MPT/saul/saul_turned_mouth_mc.png"
        attribute md:
            "mod_assets/MPT/saul/saul_turned_mouth_md.png"
        attribute me:
            "mod_assets/MPT/saul/saul_turned_mouth_me.png"
        attribute mf:
            "mod_assets/MPT/saul/saul_turned_mouth_mf.png"
        attribute mg:
            "mod_assets/MPT/saul/saul_turned_mouth_mg.png"
        attribute mh:
            "mod_assets/MPT/saul/saul_turned_mouth_mh.png"
        attribute mi:
            "mod_assets/MPT/saul/saul_turned_mouth_mi.png"
        attribute mj:
            "mod_assets/MPT/saul/saul_turned_mouth_mj.png"
        attribute mk:
            "mod_assets/MPT/saul/saul_turned_mouth_mk.png"
        attribute ml:
            "mod_assets/MPT/saul/saul_turned_mouth_ml.png"
        attribute mm:
            "mod_assets/MPT/saul/saul_turned_mouth_mm.png"
        attribute mn:
            "mod_assets/MPT/saul/saul_turned_mouth_mn.png"
        attribute mo:
            "mod_assets/MPT/saul/saul_turned_mouth_mo.png"
        attribute mp:
            "mod_assets/MPT/saul/saul_turned_mouth_mp.png"
        attribute mq:
            "mod_assets/MPT/saul/saul_turned_mouth_mq.png"
        attribute mr:
            "mod_assets/MPT/saul/saul_turned_mouth_mr.png"

    group eyes:

        #Default Opened eyes:
        attribute oe default if_any(["neut","angr","happ","laug","sad"]):
            "mod_assets/MPT/saul/saul_turned_eyes_e1a.png"
        attribute oe default if_any(["dist","worr","pout"]):
            "mod_assets/MPT/saul/saul_turned_eyes_e1b.png"
        attribute oe default if_any(["anno","sedu","doub"]):
            "mod_assets/MPT/saul/saul_turned_eyes_e1d.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/saul/saul_turned_eyes_e1g.png"
        attribute oe default if_any(["lsur","flus","vsur","curi"]):
            "mod_assets/MPT/saul/saul_turned_eyes_e2a.png"
        attribute oe default if_any(["nerv"]):
            "mod_assets/MPT/saul/saul_turned_eyes_e2b.png"
        attribute oe default if_any(["pani","vang","shoc"]):
            "mod_assets/MPT/saul/saul_turned_eyes_e2d.png"
        attribute oe default if_any(["yand"]):
            "mod_assets/MPT/saul/saul_turned_eyes_e3a.png"

        #Default Closed eyes:
        attribute ce if_any(["sad","anno","angr","dist","shoc","worr","nerv","curi","doub"]):
            "mod_assets/MPT/saul/saul_turned_eyes_e4a.png"
        attribute ce if_any(["neut","happ","lsur","laug","vsur","yand","pout","sedu"]):
            "mod_assets/MPT/saul/saul_turned_eyes_e4b.png"
        attribute ce if_any(["vang","flus","pani"]):
            "mod_assets/MPT/saul/saul_turned_eyes_e4c.png"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/saul/saul_turned_eyes_e4d.png"


        ###All eyes - truncated tags:
        attribute e1a:
            "mod_assets/MPT/saul/saul_turned_eyes_e1a.png"
        attribute e1b:
            "mod_assets/MPT/saul/saul_turned_eyes_e1b.png"
        attribute e1c:
            "mod_assets/MPT/saul/saul_turned_eyes_e1c.png"
        attribute e1d:
            "mod_assets/MPT/saul/saul_turned_eyes_e1d.png"
        attribute e1e:
            "mod_assets/MPT/saul/saul_turned_eyes_e1e.png"
        attribute e1f:
            "mod_assets/MPT/saul/saul_turned_eyes_e1f.png"
        attribute e1g:
            "mod_assets/MPT/saul/saul_turned_eyes_e1g.png"
        attribute e1h:
            "mod_assets/MPT/saul/saul_turned_eyes_e1h.png"
        attribute e2a:
            "mod_assets/MPT/saul/saul_turned_eyes_e2a.png"
        attribute e2b:
            "mod_assets/MPT/saul/saul_turned_eyes_e2b.png"
        attribute e2c:
            "mod_assets/MPT/saul/saul_turned_eyes_e2c.png"
        attribute e2d:
            "mod_assets/MPT/saul/saul_turned_eyes_e2d.png"
        attribute e3a:
            "mod_assets/MPT/saul/saul_turned_eyes_e3a.png"
        attribute e3b:
            "mod_assets/MPT/saul/saul_turned_eyes_e3b.png"
        attribute e4a:
            "mod_assets/MPT/saul/saul_turned_eyes_e4a.png"
        attribute e4b:
            "mod_assets/MPT/saul/saul_turned_eyes_e4b.png"
        attribute e4c:
            "mod_assets/MPT/saul/saul_turned_eyes_e4c.png"
        attribute e4d:
            "mod_assets/MPT/saul/saul_turned_eyes_e4d.png"
        attribute e4e:
            "mod_assets/MPT/saul/saul_turned_eyes_e4e.png"
        attribute e0a:
            "mod_assets/MPT/saul/saul_turned_eyes_e0a.png"
        attribute e0b:
            "mod_assets/MPT/saul/saul_turned_eyes_e0b.png"
        attribute ela:
            "mod_assets/MPT/saul/saul_turned_eyes_ela.png"

    group nosebleed:
        attribute nb:
            "mod_assets/MPT/saul/saul_turned_nosebleed.png"

    group eyebrows:

        #Default Eyebrows:
        attribute brow default if_any(["neut","happ","lsur","flus","shoc"]):
            "mod_assets/MPT/saul/saul_turned_eyebrows_b1a.png"
        attribute brow default if_any(["sad","cry","pani","yand","nerv"]):
            "mod_assets/MPT/saul/saul_turned_eyebrows_b1b.png"
        attribute brow default if_any(["laug","vsur","worr","sedu"]):
            "mod_assets/MPT/saul/saul_turned_eyebrows_b1c.png"
        attribute brow default if_any(["anno","pout"]):
            "mod_assets/MPT/saul/saul_turned_eyebrows_b1d.png"
        attribute brow default if_any(["angr","vang"]):
            "mod_assets/MPT/saul/saul_turned_eyebrows_b1e.png"
        attribute brow default if_any(["curi","doub"]):
            "mod_assets/MPT/saul/saul_turned_eyebrows_b1f.png"
        attribute brow if_any(["blnk"]):
            "mod_assets/MPT/saul/saul_turned_nose_n1.png"

        #The following brows are for moods that differ between open and closed eyes:
        attribute brow default if_any(["dist"]) if_all(["oe"]) if_not(["ce"]):
            "mod_assets/MPT/saul/saul_turned_eyebrows_b2a.png"
        attribute brow default if_any(["dist"]) if_all(["ce"]) if_not(["oe"]):
            "mod_assets/MPT/saul/saul_turned_eyebrows_b2a.png"


        ###All eyebrows - truncated tags:
        attribute b1a:
            "mod_assets/MPT/saul/saul_turned_eyebrows_b1a.png"
        attribute b1b:
            "mod_assets/MPT/saul/saul_turned_eyebrows_b1b.png"
        attribute b1c:
            "mod_assets/MPT/saul/saul_turned_eyebrows_b1c.png"
        attribute b1d:
            "mod_assets/MPT/saul/saul_turned_eyebrows_b1d.png"
        attribute b1e:
            "mod_assets/MPT/saul/saul_turned_eyebrows_b1e.png"
        attribute b1f:
            "mod_assets/MPT/saul/saul_turned_eyebrows_b1f.png"
        attribute b2a:
            "mod_assets/MPT/saul/saul_turned_eyebrows_b2a.png"
        attribute b2b:
            "mod_assets/MPT/saul/saul_turned_eyebrows_b2b.png"
        attribute b2c:
            "mod_assets/MPT/saul/saul_turned_eyebrows_b2c.png"

    group special:

        attribute ok:
            "mod_assets/MPT/saul/saul_ok.png"
        attribute okt:
            "mod_assets/MPT/saul/saul_ok_transparent.png"
