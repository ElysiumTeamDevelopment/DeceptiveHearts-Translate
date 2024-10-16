#change this here or in the script to change eye colors (1=green, 2=blue)
default nastya_eyes = 1

#change this here or in the script to change hair colors (1=black, 2=brown, and 3=edit)
default nastya_hair = 1

#hair and eye color script
init python:
    def nastya_adjust_attributes(name):
        names = set(name[1:])
        if nastya_hair == 1:
            names.add("black")
        if nastya_hair == 2:
            names.add("brown")
        if nastya_eyes == 1:
            names.add("green")
        if nastya_eyes == 2:
            names.add("blue")
        if nastya_hair == 3:
            names.add("edit")
        return (name[0],)+tuple(names)

define config.adjust_attributes["nastya"] = nastya_adjust_attributes

# all images are defined here to not have to change them in 2 places with the cross pose (similar to Natsuki's MPT)

image black_facebase:
    "mod_assets/MPT/nastya/black_facebase.png"
image black_hairpiece1:
    "mod_assets/MPT/nastya/black_hairpiece1.png"
image black_hairpiece2:
    "mod_assets/MPT/nastya/black_hairpiece2.png"
image black_hairpiece3:
    "mod_assets/MPT/nastya/black_hairpiece3.png"

image brown_facebase:
    "mod_assets/MPT/nastya/brown_facebase.png"
image brown_hairpiece1:
    "mod_assets/MPT/nastya/brown_hairpiece1.png"
image brown_hairpiece2:
    "mod_assets/MPT/nastya/brown_hairpiece2.png"
image brown_hairpiece3:
    "mod_assets/MPT/nastya/brown_hairpiece3.png"

image edit_facebase:
    "mod_assets/MPT/nastya/edit_facebase.png"
image edit_hairpiece1:
    "mod_assets/MPT/nastya/edit_hairpiece1.png"
image edit_hairpiece2:
    "mod_assets/MPT/nastya/edit_hairpiece2.png"
image edit_hairpiece3:
    "mod_assets/MPT/nastya/edit_hairpiece3.png"

image nose_n1:
    "mod_assets/MPT/nastya/n1.png"
image nose_n2:
    "mod_assets/MPT/nastya/n2.png"
image nose_n3:
    "mod_assets/MPT/nastya/n3.png"
image nose_n4:
    "mod_assets/MPT/nastya/n4.png"

image mouth_ma:
    "mod_assets/MPT/nastya/ma.png"
image mouth_mb:
    "mod_assets/MPT/nastya/mb.png"
image mouth_mc:
    "mod_assets/MPT/nastya/mc.png"
image mouth_md:
    "mod_assets/MPT/nastya/md.png"
image mouth_me:
    "mod_assets/MPT/nastya/me.png"
image mouth_mf:
    "mod_assets/MPT/nastya/mf.png"
image mouth_mg:
    "mod_assets/MPT/nastya/mg.png"
image mouth_mh:
    "mod_assets/MPT/nastya/mh.png"
image mouth_mi:
    "mod_assets/MPT/nastya/mi.png"
image mouth_mj:
    "mod_assets/MPT/nastya/mj.png"
image mouth_mk:
    "mod_assets/MPT/nastya/mk.png"
image mouth_ml:
    "mod_assets/MPT/nastya/ml.png"
image mouth_ml:
    "mod_assets/MPT/nastya/ml.png"
image mouth_mm:
    "mod_assets/MPT/nastya/mm.png"
image mouth_mn:
    "mod_assets/MPT/nastya/mn.png"
image mouth_mo:
    "mod_assets/MPT/nastya/mo.png"
image mouth_mp:
    "mod_assets/MPT/nastya/mp.png"
image mouth_mq:
    "mod_assets/MPT/nastya/mq.png"
image mouth_mr:
    "mod_assets/MPT/nastya/mr.png"
image mouth_ms:
    "mod_assets/MPT/nastya/ms.png"
image mouth_mt:
    "mod_assets/MPT/nastya/mt.png"
image mouth_mu:
    "mod_assets/MPT/nastya/mu.png"
image mouth_mv:
    "mod_assets/MPT/nastya/mv.png"
image mouth_mw:
    "mod_assets/MPT/nastya/mw.png"

image green_e1a:
    "mod_assets/MPT/nastya/e1a.png"
image green_e1b:
    "mod_assets/MPT/nastya/e1b.png"
image green_e1c:
    "mod_assets/MPT/nastya/e1c.png"
image green_e1d:
    "mod_assets/MPT/nastya/e1d.png"
image green_e1e:
    "mod_assets/MPT/nastya/e1e.png"
image green_e1f:
    "mod_assets/MPT/nastya/e1f.png"
image green_e1g:
    "mod_assets/MPT/nastya/e1g.png"
image green_e1h:
    "mod_assets/MPT/nastya/e1h.png"
image green_e1i:
    "mod_assets/MPT/nastya/e1i.png"
image green_e1j:
    "mod_assets/MPT/nastya/e1j.png"
image green_e2a:
    "mod_assets/MPT/nastya/e2a.png"
image green_e2b:
    "mod_assets/MPT/nastya/e2b.png"
image green_e2c:
    "mod_assets/MPT/nastya/e2c.png"
image green_e2d:
    "mod_assets/MPT/nastya/e2d.png"
image green_e3a:
    "mod_assets/MPT/nastya/e3a.png"
image green_e3b:
    "mod_assets/MPT/nastya/e3b.png"
image green_e4a:
    "mod_assets/MPT/nastya/e4a.png"
image green_e4b:
    "mod_assets/MPT/nastya/e4b.png"
image green_e4c:
    "mod_assets/MPT/nastya/e4c.png"
image green_e4d:
    "mod_assets/MPT/nastya/e4d.png"
image green_e4e:
    "mod_assets/MPT/nastya/e4e.png"
image green_e0a:
    "mod_assets/MPT/nastya/e0a.png"
image green_e0b:
    "mod_assets/MPT/nastya/e0b.png"

image blue_e1a:
    "mod_assets/MPT/nastya/e1a_blue.png"
image blue_e1b:
    "mod_assets/MPT/nastya/e1b_blue.png"
image blue_e1c:
    "mod_assets/MPT/nastya/e1c_blue.png"
image blue_e1d:
    "mod_assets/MPT/nastya/e1d_blue.png"
image blue_e1e:
    "mod_assets/MPT/nastya/e1e_blue.png"
image blue_e1f:
    "mod_assets/MPT/nastya/e1f_blue.png"
image blue_e1g:
    "mod_assets/MPT/nastya/e1g_blue.png"
image blue_e1h:
    "mod_assets/MPT/nastya/e1h_blue.png"
image blue_e1i:
    "mod_assets/MPT/nastya/e1i_blue.png"
image blue_e1j:
    "mod_assets/MPT/nastya/e1j_blue.png"
image blue_e2a:
    "mod_assets/MPT/nastya/e2a_blue.png"
image blue_e2b:
    "mod_assets/MPT/nastya/e2b_blue.png"
image blue_e2c:
    "mod_assets/MPT/nastya/e2c_blue.png"
image blue_e2d:
    "mod_assets/MPT/nastya/e2d_blue.png"
image blue_e3a:
    "mod_assets/MPT/nastya/e3a_blue.png"
image blue_e3b:
    "mod_assets/MPT/nastya/e3b_blue.png"
image blue_e4a:
    "mod_assets/MPT/nastya/e4a_blue.png"
image blue_e4b:
    "mod_assets/MPT/nastya/e4b_blue.png"
image blue_e4c:
    "mod_assets/MPT/nastya/e4c_blue.png"
image blue_e4d:
    "mod_assets/MPT/nastya/e4d_blue.png"
image blue_e4e:
    "mod_assets/MPT/nastya/e4e_blue.png"
image blue_e0a:
    "mod_assets/MPT/nastya/e0a_blue.png"
image blue_e0b:
    "mod_assets/MPT/nastya/e0b_blue.png"

image black_b1a:
    "mod_assets/MPT/nastya/b1a.png"
image black_b1b:
    "mod_assets/MPT/nastya/b1b.png"
image black_b1c:
    "mod_assets/MPT/nastya/b1c.png"
image black_b1d:
    "mod_assets/MPT/nastya/b1d.png"
image black_b1e:
    "mod_assets/MPT/nastya/b1e.png"
image black_b1f:
    "mod_assets/MPT/nastya/b1f.png"
image black_b1g:
    "mod_assets/MPT/nastya/b1g.png"
image black_b1h:
    "mod_assets/MPT/nastya/b1h.png"
image black_b2a:
    "mod_assets/MPT/nastya/b2a.png"
image black_b2b:
    "mod_assets/MPT/nastya/b2b.png"
image black_b2c:
    "mod_assets/MPT/nastya/b2c.png"
image black_b3a:
    "mod_assets/MPT/nastya/b3a.png"
image black_b3b:
    "mod_assets/MPT/nastya/b3b.png"
image black_b3c:
    "mod_assets/MPT/nastya/b3c.png"

image brown_b1a:
    "mod_assets/MPT/nastya/b1a_brown.png"
image brown_b1b:
    "mod_assets/MPT/nastya/b1b_brown.png"
image brown_b1c:
    "mod_assets/MPT/nastya/b1c_brown.png"
image brown_b1d:
    "mod_assets/MPT/nastya/b1d_brown.png"
image brown_b1e:
    "mod_assets/MPT/nastya/b1e_brown.png"
image brown_b1f:
    "mod_assets/MPT/nastya/b1f_brown.png"
image brown_b2a:
    "mod_assets/MPT/nastya/b2a_brown.png"
image brown_b2b:
    "mod_assets/MPT/nastya/b2b_brown.png"
image brown_b2c:
    "mod_assets/MPT/nastya/b2c_brown.png"
image brown_b3a:
    "mod_assets/MPT/nastya/b3a_brown.png"
image brown_b3b:
    "mod_assets/MPT/nastya/b3b_brown.png"
image brown_b3c:
    "mod_assets/MPT/nastya/b3c_brown.png"

image 0la:
    "mod_assets/MPT/nastya/0la.png"
image 0lb:
    "mod_assets/MPT/nastya/0lb.png"
image 0lc:
    "mod_assets/MPT/nastya/0lc.png"
image 0ld:
    "mod_assets/MPT/nastya/0ld.png"
image 0le:
    "mod_assets/MPT/nastya/0le.png"
image 1la:
    "mod_assets/MPT/nastya/1la.png"
image 1lb:
    "mod_assets/MPT/nastya/1lb.png"
image 1lc:
    "mod_assets/MPT/nastya/1lc.png"
image 1ld:
    "mod_assets/MPT/nastya/1ld.png"
image 1le:
    "mod_assets/MPT/nastya/1le.png"
image 2la:
    "mod_assets/MPT/nastya/2la.png"
image 2lb:
    "mod_assets/MPT/nastya/2lb.png"
image 2lc:
    "mod_assets/MPT/nastya/2lc.png"
image 2ld:
    "mod_assets/MPT/nastya/2ld.png"
image 2le:
    "mod_assets/MPT/nastya/2le.png"

image 0ra:
    "mod_assets/MPT/nastya/0ra.png"
image 0rb:
    "mod_assets/MPT/nastya/0rb.png"
image 0rc:
    "mod_assets/MPT/nastya/0rc.png"
image 0rd:
    "mod_assets/MPT/nastya/0rd.png"
image 0re:
    "mod_assets/MPT/nastya/0re.png"
image 1ra:
    "mod_assets/MPT/nastya/1ra.png"
image 1rb:
    "mod_assets/MPT/nastya/1rb.png"
image 1rc:
    "mod_assets/MPT/nastya/1rc.png"
image 1rd:
    "mod_assets/MPT/nastya/1rd.png"
image 1re:
    "mod_assets/MPT/nastya/1re.png"
image 2ra:
    "mod_assets/MPT/nastya/2ra.png"
image 2rb:
    "mod_assets/MPT/nastya/2rb.png"
image 2rc:
    "mod_assets/MPT/nastya/2rc.png"
image 2rd:
    "mod_assets/MPT/nastya/2rd.png"
image 2re:
    "mod_assets/MPT/nastya/2re.png"

image 3a:
    "mod_assets/MPT/nastya/3a.png"
image 3b:
    "mod_assets/MPT/nastya/3b.png"
image 3c:
    "mod_assets/MPT/nastya/3c.png"
image 3d:
    "mod_assets/MPT/nastya/3d.png"
image 3e:
    "mod_assets/MPT/nastya/3e.png"
image 4a:
    "mod_assets/MPT/nastya/4a.png"
image 4b:
    "mod_assets/MPT/nastya/4b.png"
image 4c:
    "mod_assets/MPT/nastya/4c.png"
image 4d:
    "mod_assets/MPT/nastya/4d.png"
image 4e:
    "mod_assets/MPT/nastya/4e.png"

image glasses:
    "mod_assets/MPT/nastya/glasses.png"

layeredimage nastya turned:

    #This makes the sprite one single texture, instead of multiple textures on top of each other.
    #This fixes certain problems like alpha fadein/fadeout looking strange, at the cost of some performance.
    at renpy.partial(Flatten, drawable_resolution = False)

    group eyes:
        attribute green default null
        attribute blue null

    group hair:
        attribute black default null
        attribute brown null
        attribute edit null

    group outfit:
        attribute uniform default null
        attribute pajamas null
        attribute sweater null
        attribute coat null
        attribute swim null
   
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
        #attribute xxxx null #xxxx #Do you want to define a new mood?  Here, have a template! #who the FUCK uses moods unironically
    
    group blush: #These are intentionally separate from mood; the idea being that these aren't consciously controlled by the character - rather, they're a result of their emotions making them blush/sweat/etc. #this implies emotions are consciously controlled which can be wrong #also it would work the exact same i think if you didnt use moods and most people dont use moods
        attribute nobl default null #Default, no blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n
        attribute pale null #no color in cheeks. defaults for n
    
    group left:
        anchor (0,0) subpixel (True)
        yoffset (-0.5)
        attribute ldown default if_any(["uniform"]):
            "0la"
        attribute ldown default if_any(["pajamas"]):
            "0lb"
        attribute ldown default if_any(["sweater"]):
            "0lc"
        attribute ldown default if_any(["coat"]):
            "0ld"
        attribute ldown default if_any(["swim"]):
            "0le"
        attribute lfist if_any(["uniform"]):
            "1la"
        attribute lfist if_any(["pajamas"]):
            "1lb"
        attribute lfist if_any(["sweater"]):
            "1lc"
        attribute lfist if_any(["coat"]):
            "1ld"
        attribute lfist if_any(["swim"]):
            "1le"
        attribute lhip if_any(["uniform"]):
            "2la"
        attribute lhip if_any(["pajamas"]):
            "2lb"
        attribute lhip if_any(["sweater"]):
            "2lc"
        attribute lhip if_any(["coat"]):
            "2ld"
        attribute lhip if_any(["swim"]):
            "2le"
    
    group right:
        anchor (0,0) subpixel (True)
        yoffset (-0.5)
        attribute rdown default if_any(["uniform"]):
            "0ra"
        attribute rdown default if_any(["pajamas"]):
            "0rb"
        attribute rdown default if_any(["sweater"]):
            "0rc"
        attribute rdown default if_any(["coat"]):
            "0rd"
        attribute rdown default if_any(["swim"]):
            "0re"
        attribute rfist if_any(["uniform"]):
            "1ra"
        attribute rfist if_any(["pajamas"]):
            "1rb"
        attribute rfist if_any(["sweater"]):
            "1rc"
        attribute rfist if_any(["coat"]):
            "1rd"
        attribute rfist if_any(["swim"]):
            "1re"
        attribute rhip if_any(["uniform"]):
            "2ra"
        attribute rhip if_any(["pajamas"]):
            "2rb"
        attribute rhip if_any(["sweater"]):
            "2rc"
        attribute rhip if_any(["coat"]):
            "2rd"
        attribute rhip if_any(["swim"]):
            "2re"

    always:
        "black_facebase" if_any "black"
    always:
        "black_hairpiece1" if_all(["black"]) if_not(["pajamas"])
    always:
        "black_hairpiece2" if_all(["black"]) if_not(["pajamas","uniform"])
    always:
        "black_hairpiece3" if_all(["black","swim"])

    always:
        "brown_facebase" if_any "brown"
    always:
        "brown_hairpiece1" if_all(["brown"]) if_not(["pajamas"])
    always:
        "brown_hairpiece2" if_all(["brown"]) if_not(["pajamas","uniform"])
    always:
        "brown_hairpiece3" if_all(["brown","swim"])

    always:
        "edit_facebase" if_any "edit"
    always:
        "edit_hairpiece1" if_all(["edit"]) if_not(["pajamas"])
    always:
        "edit_hairpiece2" if_all(["edit"]) if_not(["pajamas","uniform"])
    always:
        "edit_hairpiece3" if_all(["edit","swim"])

    group nose: 
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            "nose_n1"
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            "nose_n2"
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            "nose_n3"
        attribute nose default if_any(["blaw"]):#default nose when "blushing and awkward"
            "nose_n4"
        attribute nose default if_any(["pale"]):#default nose when "no color in cheeks"
            null
        
        #All noses - truncated tags:
        attribute n1:
            "nose_n1"
        attribute n2:
            "nose_n2"
        attribute n3:
            "nose_n3"
        attribute n4:
            "nose_n4"
        attribute n0: #for if you want not even default blush
            null
    
    
    group mouth:
        #Default Closed Mouths:
        attribute cm default if_any(["happ","sedu"]):
            "mouth_ma"
        attribute cm default if_any(["neut","worr","anno","curi"]):
            "mouth_md"
        attribute cm default if_any(["dist","flus"]):
            "mouth_me"
        attribute cm default if_any(["lsur","shoc"]):
            "mouth_mf"
        attribute cm default if_any(["sad","angr","pout","doub"]):
            "mouth_mj"
        attribute cm default if_any(["cry","pani","vsur"]):
            "mouth_mk"
        attribute cm default if_any(["vang"]):
            "mouth_mm"
        attribute cm default if_any(["laug"]):
            "mouth_mn"
        attribute cm default if_any(["yand"]):
            "mouth_mo"
        attribute cm default if_any(["nerv"]):
            "mouth_mv"
        
        #Open Mouths:
        attribute om if_any(["laug"]):
            "mouth_mb"
        attribute om if_any(["yand","nerv"]):
            "mouth_mc"
        attribute om if_any(["pout","sedu"]):
            "mouth_mf"
        attribute om if_any(["sad","lsur","dist"]):
            "mouth_mg"
        attribute om if_any(["anno","shoc","worr"]):
            "mouth_mh"
        attribute om if_any(["doub","curi"]):
            "mouth_mi"
        attribute om if_any(["flus"]):
            "mouth_mk"
        attribute om if_any(["cry","vsur"]):
            "mouth_ml"
        attribute om if_any(["vang","pani"]):
            "mouth_mq"
        attribute om if_any(["happ"]):
            "mouth_ms"
        attribute om if_any(["neut"]):
            "mouth_mt"
        attribute om if_any(["angr"]):
            "mouth_mu"
        
        ###All mouths - truncated tags:
        attribute ma:
            "mouth_ma"
        attribute mb:
            "mouth_mb"
        attribute mc:
            "mouth_mc"
        attribute md:
            "mouth_md"
        attribute me:
            "mouth_me"
        attribute mf:
            "mouth_mf"
        attribute mg:
            "mouth_mg"
        attribute mh:
            "mouth_mh"
        attribute mi:
            "mouth_mi"
        attribute mj:
            "mouth_mj"
        attribute mk:
            "mouth_mk"
        attribute ml:
            "mouth_ml"
        attribute mm:
            "mouth_mm"
        attribute mn:
            "mouth_mn"
        attribute mo:
            "mouth_mo"
        attribute mp:
            "mouth_mp"
        attribute mq:
            "mouth_mq"
        attribute mr:
            "mouth_mr"
        attribute ms:
            "mouth_ms"
        attribute mt:
            "mouth_mt"
        attribute mu:
            "mouth_mu"
        attribute mv:
            "mouth_mv"
        attribute mw:
            "mouth_mw"
    
    group green if_not(["blue"]):
            #Default Opened eyes:
        attribute oe default if_any(["neut","happ","laug","sad","angr"]):
            "green_e1a"
        attribute oe default if_any(["pout","flus"]):
            "green_e1b"
        attribute oe default if_any(["anno","sedu","doub"]):
            "green_e1d"
        attribute oe default if_any(["cry"]):
            "green_e1g"
        attribute oe default if_any(["dist"]):
            "green_e1j"
        attribute oe default if_any(["flus","vsur","lsur","curi"]):
            "green_e2a"
        attribute oe default if_any(["nerv"]):
            "green_e2b"
        attribute oe default if_any(["pani","vang","shoc"]):
            "green_e2d"
        attribute oe default if_any(["yand"]):
            "green_e3a"
        
            #Default Closed eyes:
        attribute ce if_any(["anno","shoc","worr","sad","angr","dist","worr","nerv","curi"]):
            "green_e4a"
        attribute ce if_any(["happ","laug","neut","lsur","vsur","yand","pout","sedu"]):
            "green_e4b"
        attribute ce if_any(["vang","flus","pani"]):
            "green_e4c"
        attribute ce if_any(["cry"]):
            "green_e4d"
        
            ###All eyes - truncated tags:
        attribute e1a:
            "green_e1a"
        attribute e1b:
            "green_e1b"
        attribute e1c:
            "green_e1c"
        attribute e1d:
            "green_e1d"
        attribute e1e:
            "green_e1e"
        attribute e1f:
            "green_e1f"
        attribute e1g:
            "green_e1g"
        attribute e1h:
            "green_e1h"
        attribute e1i:
            "green_e1i"
        attribute e1j:
            "green_e1j"
        attribute e2a:
            "green_e2a"
        attribute e2b:
            "green_e2b"
        attribute e2c:
            "green_e2c"
        attribute e2d:
            "green_e2d"
        attribute e3a:
            "green_e3a"
        attribute e3b:
            "green_e3b"
        attribute e4a:
            "green_e4a"
        attribute e4b:
            "green_e4b"
        attribute e4c:
            "green_e4c"
        attribute e4d:
            "green_e4d"
        attribute e4e:
            "green_e4e"
        attribute e0a:
            "green_e0a"
        attribute e0b:
            "green_e0b"
    
    group blue if_not(["green"]):
        #Default Opened eyes:
        attribute oe default if_any(["neut","happ","laug","sad","angr"]):
            "blue_e1a"
        attribute oe default if_any(["pout","flus"]):
            "blue_e1b"
        attribute oe default if_any(["anno","sedu","doub"]):
            "blue_e1d"
        attribute oe default if_any(["cry"]):
            "blue_e1g"
        attribute oe default if_any(["dist"]):
            "blue_e1j"
        attribute oe default if_any(["flus","vsur","lsur","curi"]):
            "blue_e2a"
        attribute oe default if_any(["nerv"]):
            "blue_e2b"
        attribute oe default if_any(["pani","vang","shoc"]):
            "blue_e2d"
        attribute oe default if_any(["yand"]):
            "blue_e3a"
        
            #Default Closed eyes:
        attribute ce if_any(["anno","shoc","worr","sad","angr","dist","worr","nerv","curi"]):
            "blue_e4a"
        attribute ce if_any(["happ","laug","neut","lsur","vsur","yand","pout","sedu"]):
            "blue_e4b"
        attribute ce if_any(["vang","flus","pani"]):
            "blue_e4c"
        attribute ce if_any(["cry"]):
            "blue_e4d"
        
            ###All eyes - truncated tags:
        attribute e1a:
            "blue_e1a"
        attribute e1b:
            "blue_e1b"
        attribute e1c:
            "blue_e1c"
        attribute e1d:
            "blue_e1d"
        attribute e1e:
            "blue_e1e"
        attribute e1f:
            "blue_e1f"
        attribute e1g:
            "blue_e1g"
        attribute e1h:
            "blue_e1h"
        attribute e1i:
            "blue_e1i"
        attribute e1j:
            "blue_e1j"
        attribute e2a:
            "blue_e2a"
        attribute e2b:
            "blue_e2b"
        attribute e2c:
            "blue_e2c"
        attribute e2d:
            "blue_e2d"
        attribute e3a:
            "blue_e3a"
        attribute e3b:
            "blue_e3b"
        attribute e4a:
            "blue_e4a"
        attribute e4b:
            "blue_e4b"
        attribute e4c:
            "blue_e4c"
        attribute e4d:
            "blue_e4d"
        attribute e4e:
            "blue_e4e"
        attribute e0a:
            "blue_e0a"
        attribute e0b:
            "blue_e0b"

    group black if_not(["brown"]):
        #Default Eyebrows:
        attribute brow default if_any(["neut","happ","lsur","shoc","flus"]):
            "black_b1a"
        attribute brow default if_any(["cry","yand","sad","pani","nerv"]):
            "black_b1b"
        attribute brow default if_any(["worr","laug","sedu"]):
            "black_b1c"
        attribute brow default if_any(["anno","pout"]):
            "black_b1d"
        attribute brow default if_any(["angr","vang"]):
            "black_b1e"
        attribute brow default if_any(["curi","doub"]):
            "black_b1f"
        attribute brow default if_any(["vsur"]):
            "black_b1h"
        
        #The following brows are for moods that differ between open and closed eyes:
        attribute brow default if_any(["dist"]) if_all(["oe"]) if_not(["ce"]):
            "black_b2a"
        attribute brow default if_any(["dist"]) if_all(["ce"]) if_not(["oe"]):
            "black_b3c"
        
        #All eyebrows - truncated tags:
        attribute b1a:
            "black_b1a"
        attribute b1b:
            "black_b1b"
        attribute b1c:
            "black_b1c"
        attribute b1d:
            "black_b1d"
        attribute b1e:
            "black_b1e"
        attribute b1f:
            "black_b1f"
        attribute b1g:
            "black_b1g"
        attribute b1h:
            "black_b1h"
        attribute b2a:
            "black_b2a"
        attribute b2b:
            "black_b2b"
        attribute b2c:
            "black_b2c"
        attribute b3a if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "black_b31"
        attribute b3b if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "black_b3b"
        attribute b3c if_any(["b1d","e4a","e4b","e4c","e4d","e4e","ce"]):
            "black_b3c"

    group brown if_not(["black","edit"]):
        #Default Eyebrows:
        attribute brow default if_any(["neut","happ","lsur","shoc","flus"]):
            "brown_b1a"
        attribute brow default if_any(["cry","yand","sad","pani","nerv"]):
            "brown_b1b"
        attribute brow default if_any(["worr","laug","sedu"]):
            "brown_b1c"
        attribute brow default if_any(["anno","pout"]):
            "brown_b1d"
        attribute brow default if_any(["angr","vang"]):
            "brown_b1e"
        attribute brow default if_any(["curi","doub"]):
            "brown_b1f"
        attribute brow default if_any(["vsur"]):
            "brown_b1h"
        
        #The following brows are for moods that differ between open and closed eyes:
        attribute brow default if_any(["dist"]) if_all(["oe"]) if_not(["ce"]):
            "brown_b2a"
        attribute brow default if_any(["dist"]) if_all(["ce"]) if_not(["oe"]):
            "brown_b3c"
        
        #All eyebrows - truncated tags:
        attribute b1a:
            "brown_b1a"
        attribute b1b:
            "brown_b1b"
        attribute b1c:
            "brown_b1c"
        attribute b1d:
            "brown_b1d"
        attribute b1e:
            "brown_b1e"
        attribute b1f:
            "brown_b1f"
        attribute b1g:
            "brown_b1g"
        attribute b1h:
            "brown_b1h"
        attribute b2a:
            "brown_b2a"
        attribute b2b:
            "brown_b2b"
        attribute b2c:
            "brown_b2c"
        attribute b3a if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "brown_b3a"
        attribute b3b if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "brown_b3b"
        attribute b3c if_any(["b1d","e4a","e4b","e4c","e4d","e4e","ce"]):
            "brown_b3c"

    group eyewear:
        attribute glasses:
            "glasses"
        attribute noglasses null


layeredimage nastya cross:

    #This makes the sprite one single texture, instead of multiple textures on top of each other.
    #This fixes certain problems like alpha fadein/fadeout looking strange, at the cost of some performance.
    at renpy.partial(Flatten, drawable_resolution = False)
    
    group outfit:
        attribute uniform default null
        attribute pajamas null
        attribute sweater null
        attribute coat null
        attribute swim null

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
        #attribute xxxx null #xxxx #Do you want to define a new mood?  Here, have a template! #who the FUCK uses moods unironically
    
    group eyes:
        attribute green default null
        attribute blue null
    
    group hair:
        attribute black default null
        attribute brown null
        attribute edit null
    
    group blush: #These are intentionally separate from mood; the idea being that these aren't consciously controlled by the character - rather, they're a result of their emotions making them blush/sweat/etc. #this implies emotions are consciously controlled which can be wrong #also it would work the exact same i think if you didnt use moods and most people dont use moods
        attribute nobl default null #Default, no blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n
        attribute pale null #no color in cheeks. defaults for n

    group leftright:
        attribute fold default if_any(["uniform"]):
            "3a"
        attribute fold default if_any(["pajamas"]):
            "3b"
        attribute fold default if_any(["sweater"]):
            "3c"
        attribute fold default if_any(["coat"]):
            "3d"
        attribute fold default if_any(["swim"]):
            "3e"
        attribute grab if_any(["uniform"]):
            "4a"
        attribute grab if_any(["pajamas"]):
            "4b"
        attribute grab if_any(["sweater"]):
            "4c"
        attribute grab if_any(["coat"]):
            "4d"
        attribute grab if_any(["swim"]):
            "4e"

    always:
        "black_facebase" if_any "black"
    always:
        "black_hairpiece1" if_all(["black"]) if_not(["pajamas"])
    always:
        "black_hairpiece2" if_all(["black"]) if_not(["pajamas","uniform"])
    always:
        "black_hairpiece3" if_all(["black","swim"])

    always:
        "brown_facebase" if_any "brown"
    always:
        "brown_hairpiece1" if_all(["brown"]) if_not(["pajamas"])
    always:
        "brown_hairpiece2" if_all(["brown"]) if_not(["pajamas","uniform"])
    always:
        "brown_hairpiece3" if_all(["brown","swim"])

    always:
        "edit_facebase" if_any "edit"
    always:
        "edit_hairpiece1" if_all(["edit"]) if_not(["pajamas"])
    always:
        "edit_hairpiece2" if_all(["edit"]) if_not(["pajamas","uniform"])
    always:
        "edit_hairpiece3" if_all(["edit","swim"])

    group nose: 
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            "nose_n1"
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            "nose_n2"
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            "nose_n3"
        attribute nose default if_any(["blaw"]):#default nose when "blushing and awkward"
            "nose_n4"
        attribute nose default if_any(["pale"]):#default nose when "no color in cheeks"
            null
        
        #All noses - truncated tags:
        attribute n1:
            "nose_n1"
        attribute n2:
            "nose_n2"
        attribute n3:
            "nose_n3"
        attribute n4:
            "nose_n4"
        attribute n0: #for if you want not even default blush
            null
    
    
    group mouth:
        #Default Closed Mouths:
        attribute cm default if_any(["happ","sedu"]):
            "mouth_ma"
        attribute cm default if_any(["neut","worr","anno","curi"]):
            "mouth_md"
        attribute cm default if_any(["dist","flus"]):
            "mouth_me"
        attribute cm default if_any(["lsur","shoc"]):
            "mouth_mf"
        attribute cm default if_any(["sad","angr","pout","doub"]):
            "mouth_mj"
        attribute cm default if_any(["cry","pani","vsur"]):
            "mouth_mk"
        attribute cm default if_any(["vang"]):
            "mouth_mm"
        attribute cm default if_any(["laug"]):
            "mouth_mn"
        attribute cm default if_any(["yand"]):
            "mouth_mo"
        attribute cm default if_any(["nerv"]):
            "mouth_mv"
        
        #Open Mouths:
        attribute om if_any(["laug"]):
            "mouth_mb"
        attribute om if_any(["yand","nerv"]):
            "mouth_mc"
        attribute om if_any(["pout","sedu"]):
            "mouth_mf"
        attribute om if_any(["sad","lsur","dist"]):
            "mouth_mg"
        attribute om if_any(["anno","shoc","worr"]):
            "mouth_mh"
        attribute om if_any(["doub","curi"]):
            "mouth_mi"
        attribute om if_any(["flus"]):
            "mouth_mk"
        attribute om if_any(["cry","vsur"]):
            "mouth_ml"
        attribute om if_any(["vang","pani"]):
            "mouth_mq"
        attribute om if_any(["happ"]):
            "mouth_ms"
        attribute om if_any(["neut"]):
            "mouth_mt"
        attribute om if_any(["angr"]):
            "mouth_mu"
        
        ###All mouths - truncated tags:
        attribute ma:
            "mouth_ma"
        attribute mb:
            "mouth_mb"
        attribute mc:
            "mouth_mc"
        attribute md:
            "mouth_md"
        attribute me:
            "mouth_me"
        attribute mf:
            "mouth_mf"
        attribute mg:
            "mouth_mg"
        attribute mh:
            "mouth_mh"
        attribute mi:
            "mouth_mi"
        attribute mj:
            "mouth_mj"
        attribute mk:
            "mouth_mk"
        attribute ml:
            "mouth_ml"
        attribute mm:
            "mouth_mm"
        attribute mn:
            "mouth_mn"
        attribute mo:
            "mouth_mo"
        attribute mp:
            "mouth_mp"
        attribute mq:
            "mouth_mq"
        attribute mr:
            "mouth_mr"
        attribute ms:
            "mouth_ms"
        attribute mt:
            "mouth_mt"
        attribute mu:
            "mouth_mu"
        attribute mv:
            "mouth_mv"
        attribute mw:
            "mouth_mw"
    
    group green if_not(["blue"]):
            #Default Opened eyes:
        attribute oe default if_any(["neut","happ","laug","sad","angr"]):
            "green_e1a"
        attribute oe default if_any(["pout","flus"]):
            "green_e1b"
        attribute oe default if_any(["anno","sedu","doub"]):
            "green_e1d"
        attribute oe default if_any(["cry"]):
            "green_e1g"
        attribute oe default if_any(["dist"]):
            "green_e1j"
        attribute oe default if_any(["flus","vsur","lsur","curi"]):
            "green_e2a"
        attribute oe default if_any(["nerv"]):
            "green_e2b"
        attribute oe default if_any(["pani","vang","shoc"]):
            "green_e2d"
        attribute oe default if_any(["yand"]):
            "green_e3a"
        
            #Default Closed eyes:
        attribute ce if_any(["anno","shoc","worr","sad","angr","dist","worr","nerv","curi"]):
            "green_e4a"
        attribute ce if_any(["happ","laug","neut","lsur","vsur","yand","pout","sedu"]):
            "green_e4b"
        attribute ce if_any(["vang","flus","pani"]):
            "green_e4c"
        attribute ce if_any(["cry"]):
            "green_e4d"
        
            ###All eyes - truncated tags:
        attribute e1a:
            "green_e1a"
        attribute e1b:
            "green_e1b"
        attribute e1c:
            "green_e1c"
        attribute e1d:
            "green_e1d"
        attribute e1e:
            "green_e1e"
        attribute e1f:
            "green_e1f"
        attribute e1g:
            "green_e1g"
        attribute e1h:
            "green_e1h"
        attribute e1i:
            "green_e1i"
        attribute e1j:
            "green_e1j"
        attribute e2a:
            "green_e2a"
        attribute e2b:
            "green_e2b"
        attribute e2c:
            "green_e2c"
        attribute e2d:
            "green_e2d"
        attribute e3a:
            "green_e3a"
        attribute e3b:
            "green_e3b"
        attribute e4a:
            "green_e4a"
        attribute e4b:
            "green_e4b"
        attribute e4c:
            "green_e4c"
        attribute e4d:
            "green_e4d"
        attribute e4e:
            "green_e4e"
        attribute e0a:
            "green_e0a"
        attribute e0b:
            "green_e0b"
    
    group blue if_not(["green"]):
        #Default Opened eyes:
        attribute oe default if_any(["neut","happ","laug","sad","angr"]):
            "blue_e1a"
        attribute oe default if_any(["pout","flus"]):
            "blue_e1b"
        attribute oe default if_any(["anno","sedu","doub"]):
            "blue_e1d"
        attribute oe default if_any(["cry"]):
            "blue_e1g"
        attribute oe default if_any(["dist"]):
            "blue_e1j"
        attribute oe default if_any(["flus","vsur","lsur","curi"]):
            "blue_e2a"
        attribute oe default if_any(["nerv"]):
            "blue_e2b"
        attribute oe default if_any(["pani","vang","shoc"]):
            "blue_e2d"
        attribute oe default if_any(["yand"]):
            "blue_e3a"
        
            #Default Closed eyes:
        attribute ce if_any(["anno","shoc","worr","sad","angr","dist","worr","nerv","curi"]):
            "blue_e4a"
        attribute ce if_any(["happ","laug","neut","lsur","vsur","yand","pout","sedu"]):
            "blue_e4b"
        attribute ce if_any(["vang","flus","pani"]):
            "blue_e4c"
        attribute ce if_any(["cry"]):
            "blue_e4d"
        
            ###All eyes - truncated tags:
        attribute e1a:
            "blue_e1a"
        attribute e1b:
            "blue_e1b"
        attribute e1c:
            "blue_e1c"
        attribute e1d:
            "blue_e1d"
        attribute e1e:
            "blue_e1e"
        attribute e1f:
            "blue_e1f"
        attribute e1g:
            "blue_e1g"
        attribute e1h:
            "blue_e1h"
        attribute e1i:
            "blue_e1i"
        attribute e1j:
            "blue_e1j"
        attribute e2a:
            "blue_e2a"
        attribute e2b:
            "blue_e2b"
        attribute e2c:
            "blue_e2c"
        attribute e2d:
            "blue_e2d"
        attribute e3a:
            "blue_e3a"
        attribute e3b:
            "blue_e3b"
        attribute e4a:
            "blue_e4a"
        attribute e4b:
            "blue_e4b"
        attribute e4c:
            "blue_e4c"
        attribute e4d:
            "blue_e4d"
        attribute e4e:
            "blue_e4e"
        attribute e0a:
            "blue_e0a"
        attribute e0b:
            "blue_e0b"

    group black if_not(["brown"]):
        #Default Eyebrows:
        attribute brow default if_any(["neut","happ","lsur","shoc","flus"]):
            "black_b1a"
        attribute brow default if_any(["cry","yand","sad","pani","nerv"]):
            "black_b1b"
        attribute brow default if_any(["worr","laug","sedu"]):
            "black_b1c"
        attribute brow default if_any(["anno","pout"]):
            "black_b1d"
        attribute brow default if_any(["angr","vang"]):
            "black_b1e"
        attribute brow default if_any(["curi","doub"]):
            "black_b1f"
        attribute brow default if_any(["vsur"]):
            "black_b1h"
        
        #The following brows are for moods that differ between open and closed eyes:
        attribute brow default if_any(["dist"]) if_all(["oe"]) if_not(["ce"]):
            "black_b2a"
        attribute brow default if_any(["dist"]) if_all(["ce"]) if_not(["oe"]):
            "black_b3c"
        
        #All eyebrows - truncated tags:
        attribute b1a:
            "black_b1a"
        attribute b1b:
            "black_b1b"
        attribute b1c:
            "black_b1c"
        attribute b1d:
            "black_b1d"
        attribute b1e:
            "black_b1e"
        attribute b1f:
            "black_b1f"
        attribute b1g:
            "black_b1g"
        attribute b1h:
            "black_b1h"
        attribute b2a:
            "black_b2a"
        attribute b2b:
            "black_b2b"
        attribute b2c:
            "black_b2c"
        attribute b3a if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "black_b31"
        attribute b3b if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "black_b3b"
        attribute b3c if_any(["b1d","e4a","e4b","e4c","e4d","e4e","ce"]):
            "black_b3c"

    group brown if_not(["black","edit"]):
        #Default Eyebrows:
        attribute brow default if_any(["neut","happ","lsur","shoc","flus"]):
            "brown_b1a"
        attribute brow default if_any(["cry","yand","sad","pani","nerv"]):
            "brown_b1b"
        attribute brow default if_any(["worr","laug","sedu"]):
            "brown_b1c"
        attribute brow default if_any(["anno","pout"]):
            "brown_b1d"
        attribute brow default if_any(["angr","vang"]):
            "brown_b1e"
        attribute brow default if_any(["curi","doub"]):
            "brown_b1f"
        attribute brow default if_any(["vsur"]):
            "brown_b1h"
        
        #The following brows are for moods that differ between open and closed eyes:
        attribute brow default if_any(["dist"]) if_all(["oe"]) if_not(["ce"]):
            "brown_b2a"
        attribute brow default if_any(["dist"]) if_all(["ce"]) if_not(["oe"]):
            "brown_b3c"
        
        #All eyebrows - truncated tags:
        attribute b1a:
            "brown_b1a"
        attribute b1b:
            "brown_b1b"
        attribute b1c:
            "brown_b1c"
        attribute b1d:
            "brown_b1d"
        attribute b1e:
            "brown_b1e"
        attribute b1f:
            "brown_b1f"
        attribute b1g:
            "brown_b1g"
        attribute b1h:
            "brown_b1h"
        attribute b2a:
            "brown_b2a"
        attribute b2b:
            "brown_b2b"
        attribute b2c:
            "brown_b2c"
        attribute b3a if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "brown_b3a"
        attribute b3b if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "brown_b3b"
        attribute b3c if_any(["b1d","e4a","e4b","e4c","e4d","e4e","ce"]):
            "brown_b3c"

    group eyewear:
        attribute glasses:
            "glasses"
        attribute noglasses null