javascript:(function(){
    Game.LoadMod("https://github.erbkaiser.com/FrozenCookies/frozen_cookies.js");
    Game.LoadMod('https://rawgit.com/yannprada/cookie-garden-helper/master/cookie-garden-helper.js');
    /*Game.LoadMod("https://windswell.github.io/autosacrifice/main.js");*/

    /* Stock Selling Tool*/
    console.log("Load Stock Selling Tool");
    const id_end = 17;
    let pre1_val_of = [...Array(id_end)].map( e => 0 );
    let pre2_val_of = [...Array(id_end)].map( e => 0 );
    let pre3_val_of = [...Array(id_end)].map( e => 0 );
    function checkState(id, cur_val) {
        /* 3回前と比べて上昇していたら1, 下落していたら-1を返す。 更新されていなかったら0を返す*/
        var pre1_val = pre1_val_of[id];
        var pre2_val = pre2_val_of[id];
        var pre3_val = pre3_val_of[id];
        if(pre1_val == cur_val) {
            return 0;
        }
        pre3_val_of[id] = pre2_val;
        pre2_val_of[id] = pre1_val;
        pre1_val_of[id] = cur_val;
        if(pre3_val == 0) {
            return 0;
        }
        if(cur_val >= pre3_val) {
            return 1;
        } else {
            return -1;
        }
    }

    function autoStock() {
        const buyRate = 0.6;
        const sellRate = 1.0;
        const bankLvl = 1;
        var M = Game.ObjectsById[5].minigame;
        for(var id = 0; id < id_end; id++) {
            var me = M.goodsById[id];
            var stdValue = (id + 1) * 10 + bankLvl - 1;
            var value = M.getGoodPrice(me);
            var state = checkState(id, value);
            if(value <= stdValue * buyRate && me.stock < M.getGoodMaxStock(me) && state == 1) {
                /* 下落時に買う。下落トレンドは続く傾向があるので、反転して上昇したタイミングで買う*/
                console.log("buy " + id + " " + value + " pre1_val: " + pre1_val_of[id] + " pre3_val: " + pre3_val_of[id]);
                M.buyGood(id, 10000);
            } else if(value >= stdValue * sellRate && me.stock > 0 && state == -1) {
                console.log("sell " + id + " " + value + " pre1_val: " + pre1_val_of[id] + " pre3_val: " + pre3_val_of[id]);
                M.sellGood(id, 10000);
            }
        }
    }
    setInterval(function() {autoStock();}, 59000);

    }());