#-*-coding:utf-8-*-
import hashlib
import base64

def jiandanDecode(m, r):
    # r = r ? r: "";
    # d = d ? d: 0;
    d = 0;
    q = 4;
    r = md5(r);
    print(r)
    # 571b3caa7376811c7f1182be421ad2d3
    o = md5(r[0:16]);
    print(r[16:32]);
    n = md5(r[16: 32]);

    l = m[0:q];
    c = o + md5(o + l);

    m = m[0:q];
    k = base64.b64decode(m);

    h = [];
    # for (g = 0; g < 256; g++) {
    for g in range(256):
        h.append(g);

    b = [];
    for g in range(256):
        b.append(ord(c[g % len(c)]));

    for g in range(256):
        f = g;
        f = (f + h[g] + b[g]) % 256;
        tmp = h[g];
        h[g] = h[f];
        h[f] = tmp

    t = "";
    k = k.split(str="");
    for g in range(k.length):
        p = f = g
        p = (p + 1) % 256;
        f = (f + h[p]) % 256;
        tmp = h[p];
        h[p] = h[f];
        h[f] = tmp;
        t += chr(ord(k[g]) ^ (h[(h[p] + h[f]) % 256]))

    t = t[0:26];
    return t;

def md5(value):
    m2 = hashlib.md5()
    m2.update(value.encode("utf-8"));
    return m2.hexdigest();

if __name__ == '__main__':
    # r = 'zE4N6eHuAQP8vkQPb0wcuEcWnLzHYVhy';
    # print(md5(r));
    jiandanDecode("f276JkGIddwi3GvYyeh1wHUqPmpj4CXihNFX69eSyu3a+V+dehKirBRRWdKQGirys2SqU5zmouMLHbt7LZafTHHLRl1DKVCvZtcnp9jSF0en3cgoEf/now","zE4N6eHuAQP8vkQPb0wcuEcWnLzHYVhy");