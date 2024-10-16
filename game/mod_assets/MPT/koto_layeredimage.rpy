layeredimage kotonoha toward:

    at renpy.partial(Flatten, drawable_resolution=False)

    always if_any(["uniform"]) if_not(["casual", "bikini"]):
        "mod_assets/MPT/kotonoha/bases/base1.png"

    always if_any(["bikini"]) if_not(["casual", "uniform"]):
        "mod_assets/MPT/kotonoha/bases/base3.png"

    always if_any(["casual"]) if_not(["uniform", "bikini"]):
        "mod_assets/MPT/kotonoha/bases/base2.png"

    group outfit:

        attribute uniform default null
        attribute casual null
        attribute bikini null

    group mood:

        attribute neut default null #neutral
        attribute angr null #angry
        attribute curi null #curious
        attribute daub null #daubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute surp null #surprised
        attribute nerv null #nervouse
        attribute sad null #sad
        attribute worr null #worried



    
    group eyes:

        attribute oe default if_any(["neut", "curi", "happ", "laug", "surp"]):
            "mod_assets/MPT/kotonoha/eyes/e1a.png"
        attribute oe default if_any(["angr"]):
            "mod_assets/MPT/kotonoha/eyes/e1d.png"
        attribute oe default if_any(["flus", "nerv", "daub", "sad", "worr"]):
            "mod_assets/MPT/kotonoha/eyes/e1c.png"

        attribute ce if_any(["neut", "angr", "daub", "sad", "worr"]):
            "mod_assets/MPT/kotonoha/eyes/e2b.png"
        attribute ce if_any(["curi", "flus", "happ", "laug", "surp", "nerv"]):
            "mod_assets/MPT/kotonoha/eyes/e2a.png"

        attribute e1a:
            "mod_assets/MPT/kotonoha/eyes/e1a.png"
        attribute e1b:
            "mod_assets/MPT/kotonoha/eyes/e1b.png"
        attribute e1c:
            "mod_assets/MPT/kotonoha/eyes/e1c.png"
        attribute e1d:
            "mod_assets/MPT/kotonoha/eyes/e1d.png"
        attribute e2a:
            "mod_assets/MPT/kotonoha/eyes/e2a.png"
        attribute e2b:
            "mod_assets/MPT/kotonoha/eyes/e2b.png"
        attribute e3a:
            "mod_assets/MPT/kotonoha/eyes/e3a.png"
        attribute e3b:
            "mod_assets/MPT/kotonoha/eyes/e3b.png"

    group brows:

        attribute brow default if_any(["neut", "happ"]):
            "mod_assets/MPT/kotonoha/brows/b1a.png"
        attribute brow default if_any(["angr"]):
            "mod_assets/MPT/kotonoha/brows/b1c.png"
        attribute brow default if_any(["curi", "daub"]):
            "mod_assets/MPT/kotonoha/brows/b1e.png"
        attribute brow default if_any(["flus", "laug", "nerv", "sad", "worr"]):
            "mod_assets/MPT/kotonoha/brows/b1b.png"
        attribute brow default if_any(["surp"]):
            "mod_assets/MPT/kotonoha/brows/b1d.png"

        attribute b1a:
            "mod_assets/MPT/kotonoha/brows/b1a.png"
        attribute b1b:
            "mod_assets/MPT/kotonoha/brows/b1b.png"
        attribute b1c:
            "mod_assets/MPT/kotonoha/brows/b1c.png"
        attribute b1d:
            "mod_assets/MPT/kotonoha/brows/b1d.png"
        attribute b1e:
            "mod_assets/MPT/kotonoha/brows/b1e.png"

    group mouths:

        attribute cm default if_any(["neut", "angr", "flus", "daub", "sad", "worr"]):
            "mod_assets/MPT/kotonoha/mouths/me.png"
        attribute cm default if_any(["curi", "surp"]):
            "mod_assets/MPT/kotonoha/mouths/mf.png"
        attribute cm default if_any(["happ", "laug", "nerv"]):
            "mod_assets/MPT/kotonoha/mouths/ma.png"
        
        attribute om if_any(["neut", "worr"]):
            "mod_assets/MPT/kotonoha/mouths/mf.png"
        attribute om if_any(["angr", "sad"]):
            "mod_assets/MPT/kotonoha/mouths/mg.png"
        attribute om if_any(["curi", "flus", "surp", "daub"]):
            "mod_assets/MPT/kotonoha/mouths/mb.png"
        attribute om if_any(["happ"]):
            "mod_assets/MPT/kotonoha/mouths/md.png"
        attribute om if_any(["laug", "nerv"]):
            "mod_assets/MPT/kotonoha/mouths/mc.png"

        attribute ma:
            "mod_assets/MPT/kotonoha/mouths/ma.png"
        attribute mb:
            "mod_assets/MPT/kotonoha/mouths/mb.png"
        attribute mc:
            "mod_assets/MPT/kotonoha/mouths/mc.png"
        attribute md:
            "mod_assets/MPT/kotonoha/mouths/md.png"
        attribute me:
            "mod_assets/MPT/kotonoha/mouths/me.png"
        attribute mf:
            "mod_assets/MPT/kotonoha/mouths/mf.png"
        attribute mg:
            "mod_assets/MPT/kotonoha/mouths/mg.png"

    group noses:

        attribute nose default if_any(["neut", "angr", "curi", "daub", "flus", "happ", "laug", "surp", "sad"]):
            "mod_assets/MPT/kotonoha/noses/n1.png"
        attribute nose default if_any(["worr"]):
            "mod_assets/MPT/kotonoha/noses/n2.png"
        attribute nose default if_any(["nerv"]):
            "mod_assets/MPT/kotonoha/noses/n3.png"
        
        attribute n1:
            "mod_assets/MPT/kotonoha/noses/n1.png"
        attribute n2:
            "mod_assets/MPT/kotonoha/noses/n2.png"
        attribute n3:
            "mod_assets/MPT/kotonoha/noses/n3.png"

    group left:
        anchor (0,0) subpixel (True)
        yoffset (-0.5) xoffset(-0.5)

        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/ldown.png"
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/ldown.png"
        attribute ldown default if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/ldown.png"

        attribute lchest if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/lchest.png"
        attribute lchest if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/lchest.png"
        attribute lchest if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/lchest.png"

        attribute lup if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/lup.png"
        attribute lup if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/lup.png"
        attribute lup if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/lup.png"

    group right:
        anchor (0,0) subpixel (True)
        yoffset (-1.0) xoffset(-1.0)

        attribute rdown default if_any("uniform"):
            "mod_assets/MPT/kotonoha/clothes/uniform/rdown.png"
        attribute rdown default if_any("casual"):
            "mod_assets/MPT/kotonoha/clothes/casual/rdown.png"
        attribute rdown default if_any("bikini"):
            "mod_assets/MPT/kotonoha/clothes/bikini/rdown.png"

        attribute rbehind if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/rbehind.png"
        attribute rbehind if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/rbehind.png"
        attribute rbehind if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/rbehind.png"

        attribute rchip if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/rchip.png"
        attribute rchip if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/rchip.png"
        attribute rchip if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/rchip.png"

    