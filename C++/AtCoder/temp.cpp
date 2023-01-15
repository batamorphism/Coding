javascript:(function(){
Game.LoadMod("https://github.erbkaiser.com/FrozenCookies/frozen_cookies.js");
Game.LoadMod('https://rawgit.com/yannprada/cookie-garden-helper/master/cookie-garden-helper.js');

// Stock Selling Tool
var let pre1_val_of = [...Array(17)].map( e => 0 ); // => [0,0,0,0,0]
var let pre2_val_of = [...Array(17)].map( e => 0 ); // => [0,0,0,0,0]
function checkState(id, cur_val) {
    // 2回前と比べて上昇していたら1, 下落していたら-1を返す
    // 更新されていなかったら0を返す
    if (id == 16) {
        console.log(pre1_val_of);
        console.log(pre2_val_of);
    }
    var pre1_val = pre1_val_of[id];
    var pre2_val = pre2_val_of[id];
    if(pre1_val == cur_val) {
        return 0;
    }
    pre2_val_of[id] = pre1_val;
    pre1_val_of[id] = cur_val;
    if(pre2_val == 0) {
        return 0;
    }
    if(cur_val >= pre2_val) {
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
    for(var id = 0; id <= 16; id++) {
        var me = M.goodsById[id];
        var stdValue = (id + 1) * 10 + bankLvl - 1;
        var value = M.getGoodPrice(me);
        var state = checkState(id, value);
        if(value <= stdValue * buyRate && me.stock < M.getGoodMaxStock(me) && state == 1) {
            // 下落時に買う。下落トレンドは続く傾向があるので、反転して上昇したタイミングで買う
            console.log("buy " + id + " " + value);
            M.buyGood(id, 10000);
        } else if(value >= stdValue * sellRate && me.stock > 0 && state == -1) {
            console.log("sell " + id + " " + value);
            M.sellGood(id, 10000);
        }
    }
}
setInterval(function() {autoStock();}, 59000);

}());