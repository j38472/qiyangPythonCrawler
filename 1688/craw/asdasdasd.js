function sdasd () {
    "use strict";
    var a = location, e = document, o = function (o, n, t) {
        (void 0 === n && (n = 1), void 0 === t && (t = 1), 0 >= t || Math.random() < t) && function (a, e) {
            var o = [];
            for (var n in a) o.push(n + "=" + encodeURIComponent(a[n]));
            (new Image).src = e + o.join("&")
        }({
            code: n,
            msg: o + "",
            pid: "baxia-fast",
            page: a.href.split(/[#?]/)[0],
            query: a.search.substr(1),
            hash: a.hash,
            referrer: e.referrer,
            title: e.title,
            ua: navigator.userAgent
        }, "//gm.mmstat.com/fsp.1.1?")
    };
    var n = document, t = 1, r = function (a, e, i) {
        if (!a) return e();
        var s = n.getElementsByTagName("script")[0], d = n.createElement("script");
        if (d.async = !0, d.src = a, a.indexOf("alicdn") > -1 && (d.crossOrigin = !0), d.onerror = function (n) {
            5 > t ? (t++, r(a, e, i)) : (d.onerror = null, o("function:loadJS. msg:" + a + "load error。props：" + JSON.stringify(i)))
        }, e) {
            var c = !1;
            d.onload = d.onreadystatechange = function () {
                c || d.readyState && !/loaded|complete/.test(d.readyState) || (d.onload = d.onreadystatechange = null, c = !0, e())
            }
        }
        s.parentNode.insertBefore(d, s)
    }, i = function (a, e) {
        return !!a && a.indexOf(e) > -1
    }, s = location.href || "";
    try {
        var d = !1;
        if (s.indexOf("loadbaxiajs") > -1 || document.cookie.indexOf("loadbaxiajs") > -1) {
            var c = null;
            if (s.indexOf("_set_bx_v_") > -1) {
                var l = s.match(/_set_bx_v_=([^&]+)/);
                c = encodeURIComponent(l && l[1])
            }
            v(1, c), d = !0
        }
        var f = [];
        f.push("crm.simba.taobao.com");
        for (var m = 0; f.length > m; m++) i(s, f[m]) && (d = !0);
        if (!self.baxiaCommon && !d) {
            o("init", "aplus_js_load", .01);
            var u = [];
            u.push({path: ".", ratio: 1, jsv: "2.0.50"});
            for (m = 0; u.length > m; m++) i(s, u[m].path) && v(u[m].ratio, u[m].jsv)
        }
    } catch (h) {
        o("err" + h.message, "aplus_js_baxia_err", 1)
    }
    var _ = !1;

    function v(a, e) {
        if (void 0 === e && (e = "2.0.50"), a >= Math.random() && !_) {
            _ = !0, o("baxiajs", "aplus_js_load", .01);
            var n = "//g.alicdn.com", t = self.goldlog;
            if (t && t.getCdnPath && (n = t.getCdnPath()), s.indexOf("_set_bx_v_") > -1) {
                var i = s.match(/_set_bx_v_=([^&]+)/);
                e = encodeURIComponent(i && i[1])
            }
            o("/sd/baxia/" + e + "/baxiaCommon.js", 13, .01), n = n + "/sd/baxia/" + e + "/baxiaCommon.js", s.indexOf("_set_bx_v_=debug") > -1 && (n = "http://localhost:8064/build/baxiaCommon.js"), r(n, null, null)
        }
    }
};
