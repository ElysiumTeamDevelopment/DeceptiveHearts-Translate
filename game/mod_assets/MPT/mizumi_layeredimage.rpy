layeredimage mizumi base:
    at Flatten

    group hair:
        attribute lhair default null
        attribute shair null

    group outfit:
        attribute uniform default null
        attribute casual null

    group left:
        attribute ldown default if_all(["uniform", "lhair"]):
            "mod_assets/MPT/Mizumi/h1/1l.png"
        attribute ldown default if_all(["casual", "lhair"]):
            "mod_assets/MPT/Mizumi/h1/1bl.png"
        attribute ldown default if_all(["uniform", "shair"]):
            "mod_assets/MPT/Mizumi/h2/1l.png"
        attribute ldown default if_all(["casual", "shair"]):
            "mod_assets/MPT/Mizumi/h2/1bl.png"
        attribute lup if_all(["uniform", "lhair"]):
            "mod_assets/MPT/Mizumi/h1/2l.png"
        attribute lup if_all(["casual", "lhair"]):
            "mod_assets/MPT/Mizumi/h1/2bl.png"
        attribute lup if_all(["uniform", "shair"]):
            "mod_assets/MPT/Mizumi/h2/2l.png"
        attribute lup if_all(["casual", "shair"]):
            "mod_assets/MPT/Mizumi/h2/2bl.png"
        attribute lpoint if_all(["uniform", "lhair"]):
            "mod_assets/MPT/Mizumi/h1/3l.png"
        attribute lpoint if_all(["casual", "lhair"]):
            "mod_assets/MPT/Mizumi/h1/3bl.png"
        attribute lpoint if_all(["uniform", "shair"]):
            "mod_assets/MPT/Mizumi/h2/3l.png"
        attribute lpoint if_all(["casual", "shair"]):
            "mod_assets/MPT/Mizumi/h2/3bl.png"
            
    group right if_any(["lhair"]):
        attribute rdown default if_all(["uniform"]):
            "mod_assets/MPT/Mizumi/h1/1r.png"
        attribute rdown default if_all(["casual"]):
            "mod_assets/MPT/Mizumi/h1/1br.png"
        attribute rhip if_all(["uniform", "lhair"]):
            "mod_assets/MPT/Mizumi/h1/2r.png"
        attribute rhip if_all(["casual", "lhair"]):
            "mod_assets/MPT/Mizumi/h1/2br.png"

    group right if_any(["shair"]):
        attribute rdown default if_all(["uniform", "shair"]):
            "mod_assets/MPT/Mizumi/h2/1r.png"
        attribute rdown default if_all(["casual", "shair"]):
            "mod_assets/MPT/Mizumi/h2/1br.png"
        attribute rhip if_all(["uniform", "shair"]):
            "mod_assets/MPT/Mizumi/h2/2r.png"
        attribute rhip if_all(["casual", "shair"]):
            "mod_assets/MPT/Mizumi/h2/2br.png"

    group mood if_any(["lhair"]):
        attribute happ default: # happy w/ closed mouth
            "mod_assets/MPT/Mizumi/h1/E/a.png"
        attribute happ2: # happy w/ open mouth
            "mod_assets/MPT/Mizumi/h1/E/b.png"
        attribute nerv: # nervous w/ open eyes
            "mod_assets/MPT/Mizumi/h1/E/c.png"
        attribute worr: # worried
            "mod_assets/MPT/Mizumi/h1/E/d.png"
        attribute pani: # panic
            "mod_assets/MPT/Mizumi/h1/E/e.png"
        attribute surp: # surprised
            "mod_assets/MPT/Mizumi/h1/E/f.png"
        attribute laug: # laugh w/ closed eyes and open mouth
            "mod_assets/MPT/Mizumi/h1/E/g.png"
        attribute laug2: # laugh w/ closed eyes and small open mouth
            "mod_assets/MPT/Mizumi/h1/E/h.png"
        attribute scar: # scared
            "mod_assets/MPT/Mizumi/h1/E/i.png"
        attribute laug3: # laugh w/ closed eyes and smile
            "mod_assets/MPT/Mizumi/h1/E/j.png"
        attribute sad: # sad
            "mod_assets/MPT/Mizumi/h1/E/k.png"
        attribute nerv2: # nervous w/ closed eyes
            "mod_assets/MPT/Mizumi/h1/E/l.png"
        attribute sigh: # sigh
            "mod_assets/MPT/Mizumi/h1/E/m.png"
        attribute pout: # pout
            "mod_assets/MPT/Mizumi/h1/E/n.png"
        attribute angr: # angry
            "mod_assets/MPT/Mizumi/h1/E/o.png"
        attribute doub: # doubtful w/ open eyes
            "mod_assets/MPT/Mizumi/h1/E/p.png"
        attribute doub2: # doubtful w/ closed eyes
            "mod_assets/MPT/Mizumi/h1/E/q.png"
        attribute blush: # blush and open mouth
            "mod_assets/MPT/Mizumi/h1/E/r.png"
        attribute yand: # heart eyes and blush
            "mod_assets/MPT/Mizumi/h1/E/s.png"
        attribute blush2: # blush w/ closed eyes and smile
            "mod_assets/MPT/Mizumi/h1/E/u.png"
        attribute blush3: # blush w/ closed eyes and closed mouth
            "mod_assets/MPT/Mizumi/h1/E/v.png"
        attribute yand2: # heart eyes and mouth open
            "mod_assets/MPT/Mizumi/h1/E/w.png"
        attribute yand3: # heart eyes and mouth closed
            "mod_assets/MPT/Mizumi/h1/E/x.png"
        attribute exci: # sparkly eyes and mouth closed
            "mod_assets/MPT/Mizumi/h1/E/y.png"
        attribute exci2: # sparkly eyes and mouth open
            "mod_assets/MPT/Mizumi/h1/E/z.png"

    group mood if_any(["shair"]):
        attribute happ default: # happy w/ closed mouth
            "mod_assets/MPT/Mizumi/h2/E/a.png"
        attribute happ2: # happy w/ open mouth
            "mod_assets/MPT/Mizumi/h2/E/b.png"
        attribute nerv: # nervous w/ open eyes
            "mod_assets/MPT/Mizumi/h2/E/c.png"
        attribute worr: # worried
            "mod_assets/MPT/Mizumi/h2/E/d.png"
        attribute pani: # panic
            "mod_assets/MPT/Mizumi/h2/E/e.png"
        attribute surp: # surprised
            "mod_assets/MPT/Mizumi/h2/E/f.png"
        attribute laug: # laugh w/ closed eyes and open mouth
            "mod_assets/MPT/Mizumi/h2/E/g.png"
        attribute laug2: # laugh w/ closed eyes and small open mouth
            "mod_assets/MPT/Mizumi/h2/E/h.png"
        attribute scar: # scared
            "mod_assets/MPT/Mizumi/h2/E/i.png"
        attribute laug3: # laugh w/ closed eyes and smile
            "mod_assets/MPT/Mizumi/h2/E/j.png"
        attribute sad: # sad
            "mod_assets/MPT/Mizumi/h2/E/k.png"
        attribute nerv2: # nervous w/ closed eyes
            "mod_assets/MPT/Mizumi/h2/E/l.png"
        attribute sigh: # sigh
            "mod_assets/MPT/Mizumi/h2/E/m.png"
        attribute pout: # pout
            "mod_assets/MPT/Mizumi/h2/E/n.png"
        attribute angr: # angry
            "mod_assets/MPT/Mizumi/h2/E/o.png"
        attribute doub: # doubtful w/ open eyes
            "mod_assets/MPT/Mizumi/h2/E/p.png"
        attribute doub2: # doubtful w/ closed eyes
            "mod_assets/MPT/Mizumi/h2/E/q.png"
        attribute blush: # blush and open mouth
            "mod_assets/MPT/Mizumi/h2/E/r.png"
        attribute yand: # heart eyes and blush
            "mod_assets/MPT/Mizumi/h2/E/s.png"
        attribute blush2: # blush w/ closed eyes and smile
            "mod_assets/MPT/Mizumi/h2/E/u.png"
        attribute blush3: # blush w/ closed eyes and closed mouth
            "mod_assets/MPT/Mizumi/h2/E/v.png"
        attribute yand2: # heart eyes and mouth open
            "mod_assets/MPT/Mizumi/h2/E/w.png"
        attribute yand3: # heart eyes and mouth closed
            "mod_assets/MPT/Mizumi/h2/E/x.png"
        attribute exci: # sparkly eyes and mouth closed
            "mod_assets/MPT/Mizumi/h2/E/y.png"
        attribute exci2: # sparkly eyes and mouth open
            "mod_assets/MPT/Mizumi/h2/E/z.png"
    
    group extras1:
        attribute noglasses default null
        attribute glasses:
            "mod_assets/MPT/Mizumi/E1.png"
    
    group extras2:
        attribute nobeanie default null
        attribute beanie:
            "mod_assets/MPT/Mizumi/E2.png"
