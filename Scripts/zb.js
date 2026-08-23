/*
  ============================================================
  逆向抓包脚本（考试宝 / anki）— 全量记录接口与权益字段
  仅限本公司产品【授权】安全自测；仅用测试账号；禁止外传。
  用法：QX「重写」引用本文件；浏览 App 各功能，去「脚本日志」看输出。
  ============================================================
*/
/*
[rewrite_local]
^https?:\/\/(ksbapi\.jxedt\.com|ge-api\.jxedt\.com|userapi\.ksedt\.com|api\.ankianki\.com|search-api\.yisouti\.com)\/.* url script-response-body 全量抓包_log.js

[mitm]
hostname = ksbapi.jxedt.com, ge-api.jxedt.com, userapi.ksedt.com, api.ankianki.com, search-api.yisouti.com
*/
const url = $request.url;
const body = $response.body;

// 递归扫描：找出所有“权益相关”字段（vip/price/limit/status/buy/...）
function scan(o, path, out) {
    if (o === null || typeof o !== "object") return;
    for (let k in o) {
        if (!o.hasOwnProperty(k)) continue;
        const p = path ? path + "." + k : k;
        const kl = k.toLowerCase();
        if (/vip|price|sell|buy|limit|status|expir|ad|package|member|paid|unlock|free|point|number/.test(kl)) {
            out.push(p + "=" + JSON.stringify(o[k]).slice(0, 60));
        }
        scan(o[k], p, out);
    }
}

try {
    const obj = JSON.parse(body);
    const d = obj.data || obj;
    const out = [];
    scan(d, "", out);
    const pathOnly = url.replace(/\?.*$/, "").replace(/^https?:\/\/[^/]+/, "");
    console.log("\n===== " + pathOnly + "\n  host=" + url.replace(/^(https?:\/\/[^/]+).*$/, "$1") + "  code=" + obj.code + "\n  权益字段(" + out.length + "): " + (out.join(" | ") || "无"));
} catch (e) {
    console.log("\n===== " + url.replace(/\?.*$/, "").replace(/^https?:\/\/[^/]+/, "") + "\n  (非JSON响应)");
}
$done({});
