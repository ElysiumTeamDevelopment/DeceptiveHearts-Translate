image mc_blink_a:
    alpha 0.0
    renpy.random.randint(20, 100)*0.1
    choice:
        alpha 1.0
        "mod_assets/MPT/mc/mc_turned_eyes_e1f.png"
        0.015
        "mod_assets/MPT/mc/mc_turned_eyes_e1e.png"
        0.035
        "mod_assets/MPT/mc/mc_turned_eyes_e1f.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/mc/mc_turned_eyes_e1f.png"
        0.015
        "mod_assets/MPT/mc/mc_turned_eyes_e1e.png"
        0.065
        "mod_assets/MPT/mc/mc_turned_eyes_e1f.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/mc/mc_turned_eyes_e1f.png"
        0.015
        "mod_assets/MPT/mc/mc_turned_eyes_e1e.png"
        0.095
        "mod_assets/MPT/mc/mc_turned_eyes_e1f.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/mc/mc_turned_eyes_e1f.png"
        0.015
        "mod_assets/MPT/mc/mc_turned_eyes_e1e.png"
        0.035
        "mod_assets/MPT/mc/mc_turned_eyes_e1f.png"
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        "mod_assets/MPT/mc/mc_turned_eyes_e1f.png"
        0.015
        "mod_assets/MPT/mc/mc_turned_eyes_e1e.png"
        0.035
        "mod_assets/MPT/mc/mc_turned_eyes_e1f.png"
        0.015
    repeat


layeredimage headlock turned: #turned definitions.

    #This makes the sprite one single texture, instead of multiple textures on top of each other.
    #This fixes certain problems like alpha fadein/fadeout looking strange, at the cost of some performance.
    at renpy.partial(Flatten, drawable_resolution = False)

    always "mod_assets/MPT/mc/mc_turned_facebase.png" #Always need this face.

    group outfit: #These attributes are here only to determine which set of "body" sprites to use later.  "null" is what lets us just use these attributes as logic and nothing else.
        attribute uniform default null
        attribute casual null


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
        #attribute xxxx null #xxxx #Do you want to define a new mood?  Here, have a template!



    group blush: #Have to separate these out, they can't share moods.
        attribute nobl null #No blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n


    #Turned arm variants
    group center if_any(["uniform"]) if_all(["turned"]):
        attribute turned default:
            "mod_assets/MPT/mc/mc_turned_uniform.png"

    group center if_any(["casual"]) if_all(["turned"]):
        attribute turned default:
            "mod_assets/MPT/mc/mc_turned_casual.png"



    group nose:

        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            "mod_assets/MPT/mc/mc_turned_nose_n1.png"
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            "mod_assets/MPT/mc/mc_turned_nose_n2.png"
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            "mod_assets/MPT/mc/mc_turned_nose_n3.png"
        attribute nose default if_any(["blaw"]):#default nose when "blushing and awkward"
            "mod_assets/MPT/mc/mc_turned_nose_n4.png"


        #All noses - truncated tags:
        attribute n1:
            "mod_assets/MPT/mc/mc_turned_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/mc/mc_turned_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/mc/mc_turned_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/mc/mc_turned_nose_n4.png"
        attribute nl:
            "mod_assets/MPT/mc/mc_turned_nose_nl.png"



    group mouth:

        #Default Closed Mouths:
        attribute cm default if_any(["happ","sedu","nerv"]):
            "mod_assets/MPT/mc/mc_turned_mouth_mb.png"
        attribute cm default if_any(["neut","anno","worr","curi","dist","doub"]):
            "mod_assets/MPT/mc/mc_turned_mouth_ma.png"
        attribute cm default if_any(["lsur","shoc"]):
            "mod_assets/MPT/mc/mc_turned_mouth_mf.png"
        attribute cm default if_any(["sad","angr","pout","flus"]):
            "mod_assets/MPT/mc/mc_turned_mouth_md.png"
        attribute cm default if_any(["cry","pani"]):
            "mod_assets/MPT/mc/mc_turned_mouth_me.png"
        attribute cm default if_any(["vang","vsur"]):
            "mod_assets/MPT/mc/mc_turned_mouth_mh.png"
        attribute cm default if_any(["laug", "yand"]):
            "mod_assets/MPT/mc/mc_turned_mouth_mi.png"

        #Open Mouths:
        attribute om if_any(["happ","laug","yand",]):
            "mod_assets/MPT/mc/mc_turned_mouth_mc.png"
        attribute om if_any(["pout","sedu"]):
            "mod_assets/MPT/mc/mc_turned_mouth_mf.png"
        attribute om if_any(["sad","lsur","dist","anno","shoc","worr","flus","vsur","vang","pani"]):
            "mod_assets/MPT/mc/mc_turned_mouth_mg.png"
        attribute om if_any(["curi","doub","angr","neut"]):
            "mod_assets/MPT/mc/mc_turned_mouth_me.png"
        attribute om if_any(["cry","nerv"]):
            "mod_assets/MPT/mc/mc_turned_mouth_md.png"


        ###All mouths - truncated tags:
        attribute ma:
            "mod_assets/MPT/mc/mc_turned_mouth_ma.png"
        attribute mb:
            "mod_assets/MPT/mc/mc_turned_mouth_mb.png"
        attribute mc:
            "mod_assets/MPT/mc/mc_turned_mouth_mc.png"
        attribute md:
            "mod_assets/MPT/mc/mc_turned_mouth_md.png"
        attribute me:
            "mod_assets/MPT/mc/mc_turned_mouth_me.png"
        attribute mf:
            "mod_assets/MPT/mc/mc_turned_mouth_mf.png"
        attribute mg:
            "mod_assets/MPT/mc/mc_turned_mouth_mg.png"
        attribute mh:
            "mod_assets/MPT/mc/mc_turned_mouth_mh.png"
        attribute mi:
            "mod_assets/MPT/mc/mc_turned_mouth_mi.png"



    group eyes:

        #Default Opened eyes:
        attribute oe default if_any(["neut","angr","happ","laug","sad","dist","worr","pout","anno","sedu","doub","nerv","curi"]):
            "mod_assets/MPT/mc/mc_turned_eyes_e1a.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/mc/mc_turned_eyes_e1b.png"
        attribute oe default if_any(["lsur","flus","vsur","pani","vang","shoc"]):
            "mod_assets/MPT/mc/mc_turned_eyes_e1c.png"
        attribute oe default if_any(["yand"]):
            "mod_assets/MPT/mc/mc_turned_eyes_e1d.png"

        #Default Closed eyes:
        attribute ce if_any(["sad","anno","angr","dist","shoc","worr","nerv","curi","doub","vang"]):
            "mod_assets/MPT/mc/mc_turned_eyes_e1e.png"
        attribute ce if_any(["neut","happ","lsur","laug","vsur","yand","pout","sedu","flus","pani"]):
            "mod_assets/MPT/mc/mc_turned_eyes_e1f.png"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/mc/mc_turned_eyes_e1i.png"


        ###All eyes - truncated tags:
        attribute e1a:
            "mod_assets/MPT/mc/mc_turned_eyes_e1a.png"
        attribute e1b:
            "mod_assets/MPT/mc/mc_turned_eyes_e1b.png"
        attribute e1c:
            "mod_assets/MPT/mc/mc_turned_eyes_e1c.png"
        attribute e1d:
            "mod_assets/MPT/mc/mc_turned_eyes_e1d.png"
        attribute e1e:
            "mod_assets/MPT/mc/mc_turned_eyes_e1e.png"
        attribute e1f:
            "mod_assets/MPT/mc/mc_turned_eyes_e1f.png"
        attribute e1g:
            "mod_assets/MPT/mc/mc_turned_eyes_e1g.png"
        attribute e1h:
            "mod_assets/MPT/mc/mc_turned_eyes_e1h.png"
        attribute e1i:
            "mod_assets/MPT/mc/mc_turned_eyes_e1i.png"


    group blink:

        anchor (0,0) subpixel (True)

        attribute blink if_not(["ce","e1e","e1f", "e1g","e1h","e1i"]):
            "mc_blink_a"
        attribute no_blink default null


    group eyebrows:

        #Default Eyebrows:
        attribute brow default if_any(["neut","happ","lsur","flus","shoc","laug","vsur","dist"]):
            "mod_assets/MPT/mc/mc_turned_eyebrows_b1a.png"
        attribute brow default if_any(["sad","cry","pani","nerv","worr","sedu","pout"]):
            "mod_assets/MPT/mc/mc_turned_eyebrows_b1b.png"
        attribute brow default if_any(["angr","vang","anno","yand"]):
            "mod_assets/MPT/mc/mc_turned_eyebrows_b1c.png"
        attribute brow default if_any(["curi","doub"]):
            "mod_assets/MPT/mc/mc_turned_eyebrows_b1d.png"


        ###All eyebrows - truncated tags:
        attribute b1a:
            "mod_assets/MPT/mc/mc_turned_eyebrows_b1a.png"
        attribute b1b:
            "mod_assets/MPT/mc/mc_turned_eyebrows_b1b.png"
        attribute b1c:
            "mod_assets/MPT/mc/mc_turned_eyebrows_b1c.png"
        attribute b1d:
            "mod_assets/MPT/mc/mc_turned_eyebrows_b1d.png"

    #This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group special:

        attribute s_scream:
            "mod_assets/MPT/mc/mc_turned_special_scream.png"

layeredimage headlock cross: #crossed definitions.

    #This makes the sprite one single texture, instead of multiple textures on top of each other.
    #This fixes certain problems like alpha fadein/fadeout looking strange, at the cost of some performance.
    at renpy.partial(Flatten, drawable_resolution = False)

    always "mod_assets/MPT/mc/mc_turned_facebase.png" #Always need this face.

    group outfit: #These attributes are here only to determine which set of "body" sprites to use later.  "null" is what lets us just use these attributes as logic and nothing else.
        attribute uniform default null
        attribute casual null


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
        #attribute xxxx null #xxxx #Do you want to define a new mood?  Here, have a template!



    group blush: #Have to separate these out, they can't share moods.
        attribute nobl null #No blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n

    #Crossed arm variants
    group center if_any(["uniform"]) if_all(["cross"]):
        attribute cross default:
            "mod_assets/MPT/mc/mc_crossed_uniform.png"

    group center if_any(["casual"]) if_all(["cross"]):
        attribute cross default:
            "mod_assets/MPT/mc/mc_crossed_casual.png"



    group nose:

        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            "mod_assets/MPT/mc/mc_turned_nose_n1.png"
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            "mod_assets/MPT/mc/mc_turned_nose_n2.png"
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            "mod_assets/MPT/mc/mc_turned_nose_n3.png"
        attribute nose default if_any(["blaw"]):#default nose when "blushing and awkward"
            "mod_assets/MPT/mc/mc_turned_nose_n4.png"


        #All noses - truncated tags:
        attribute n1:
            "mod_assets/MPT/mc/mc_turned_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/mc/mc_turned_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/mc/mc_turned_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/mc/mc_turned_nose_n4.png"
        attribute nl:
            "mod_assets/MPT/mc/mc_turned_nose_nl.png"



    group mouth:

        #Default Closed Mouths:
        attribute cm default if_any(["happ","sedu","nerv"]):
            "mod_assets/MPT/mc/mc_turned_mouth_mb.png"
        attribute cm default if_any(["neut","anno","worr","curi","dist","doub"]):
            "mod_assets/MPT/mc/mc_turned_mouth_ma.png"
        attribute cm default if_any(["lsur","shoc"]):
            "mod_assets/MPT/mc/mc_turned_mouth_mf.png"
        attribute cm default if_any(["sad","angr","pout","flus"]):
            "mod_assets/MPT/mc/mc_turned_mouth_md.png"
        attribute cm default if_any(["cry","pani"]):
            "mod_assets/MPT/mc/mc_turned_mouth_me.png"
        attribute cm default if_any(["vang","vsur"]):
            "mod_assets/MPT/mc/mc_turned_mouth_mh.png"
        attribute cm default if_any(["laug", "yand"]):
            "mod_assets/MPT/mc/mc_turned_mouth_mi.png"

        #Open Mouths:
        attribute om if_any(["happ","laug","yand","nerv"]):
            "mod_assets/MPT/mc/mc_turned_mouth_mc.png"
        attribute om if_any(["pout","sedu"]):
            "mod_assets/MPT/mc/mc_turned_mouth_mf.png"
        attribute om if_any(["sad","lsur","dist","anno","shoc","worr","flus","vsur","vang","pani"]):
            "mod_assets/MPT/mc/mc_turned_mouth_mg.png"
        attribute om if_any(["curi","doub","angr","neut"]):
            "mod_assets/MPT/mc/mc_turned_mouth_me.png"
        attribute om if_any(["cry"]):
            "mod_assets/MPT/mc/mc_turned_mouth_md.png"


        ###All mouths - truncated tags:
        attribute ma:
            "mod_assets/MPT/mc/mc_turned_mouth_ma.png"
        attribute mb:
            "mod_assets/MPT/mc/mc_turned_mouth_mb.png"
        attribute mc:
            "mod_assets/MPT/mc/mc_turned_mouth_mc.png"
        attribute md:
            "mod_assets/MPT/mc/mc_turned_mouth_md.png"
        attribute me:
            "mod_assets/MPT/mc/mc_turned_mouth_me.png"
        attribute mf:
            "mod_assets/MPT/mc/mc_turned_mouth_mf.png"
        attribute mg:
            "mod_assets/MPT/mc/mc_turned_mouth_mg.png"
        attribute mh:
            "mod_assets/MPT/mc/mc_turned_mouth_mh.png"
        attribute mi:
            "mod_assets/MPT/mc/mc_turned_mouth_mi.png"



    group eyes:

        #Default Opened eyes:
        attribute oe default if_any(["neut","angr","happ","laug","sad","dist","worr","pout","anno","sedu","doub","nerv","curi"]):
            "mod_assets/MPT/mc/mc_turned_eyes_e1a.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/mc/mc_turned_eyes_e1b.png"
        attribute oe default if_any(["lsur","flus","vsur","pani","vang","shoc"]):
            "mod_assets/MPT/mc/mc_turned_eyes_e1c.png"
        attribute oe default if_any(["yand"]):
            "mod_assets/MPT/mc/mc_turned_eyes_e1d.png"

        #Default Closed eyes:
        attribute ce if_any(["sad","anno","angr","dist","shoc","worr","nerv","curi","doub","vang"]):
            "mod_assets/MPT/mc/mc_turned_eyes_e1e.png"
        attribute ce if_any(["neut","happ","lsur","laug","vsur","yand","pout","sedu","flus","pani"]):
            "mod_assets/MPT/mc/mc_turned_eyes_e1f.png"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/mc/mc_turned_eyes_e1i.png"


        ###All eyes - truncated tags:
        attribute e1a:
            "mod_assets/MPT/mc/mc_turned_eyes_e1a.png"
        attribute e1b:
            "mod_assets/MPT/mc/mc_turned_eyes_e1b.png"
        attribute e1c:
            "mod_assets/MPT/mc/mc_turned_eyes_e1c.png"
        attribute e1d:
            "mod_assets/MPT/mc/mc_turned_eyes_e1d.png"
        attribute e1e:
            "mod_assets/MPT/mc/mc_turned_eyes_e1e.png"
        attribute e1f:
            "mod_assets/MPT/mc/mc_turned_eyes_e1f.png"
        attribute e1g:
            "mod_assets/MPT/mc/mc_turned_eyes_e1g.png"
        attribute e1h:
            "mod_assets/MPT/mc/mc_turned_eyes_e1h.png"
        attribute e1i:
            "mod_assets/MPT/mc/mc_turned_eyes_e1i.png"


    group eyebrows:

        #Default Eyebrows:
        attribute brow default if_any(["neut","happ","lsur","flus","shoc","laug","vsur","dist"]):
            "mod_assets/MPT/mc/mc_turned_eyebrows_b1a.png"
        attribute brow default if_any(["sad","cry","pani","nerv","worr","sedu","pout"]):
            "mod_assets/MPT/mc/mc_turned_eyebrows_b1b.png"
        attribute brow default if_any(["angr","vang","anno","yand"]):
            "mod_assets/MPT/mc/mc_turned_eyebrows_b1c.png"
        attribute brow default if_any(["curi","doub"]):
            "mod_assets/MPT/mc/mc_turned_eyebrows_b1d.png"


        ###All eyebrows - truncated tags:
        attribute b1a:
            "mod_assets/MPT/mc/mc_turned_eyebrows_b1a.png"
        attribute b1b:
            "mod_assets/MPT/mc/mc_turned_eyebrows_b1b.png"
        attribute b1c:
            "mod_assets/MPT/mc/mc_turned_eyebrows_b1c.png"
        attribute b1d:
            "mod_assets/MPT/mc/mc_turned_eyebrows_b1d.png"

    #This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group special:

        attribute s_scream:
            "mod_assets/MPT/mc/mc_turned_special_scream.png"
