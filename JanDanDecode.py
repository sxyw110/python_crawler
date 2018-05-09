#-*-coding:utf-8-*-
import hashlib
import base64
import sys

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

    m = m[q:];
    k = decode_base64(m);

    # h = [];
    # # for (g = 0; g < 256; g++) {
    # for g in range(256):
    #     h.append(g);
    h = list(range(256))


    # b = [];

    b = list(range(256));

    for g in range(0, 256):
        b[g] = ord(c[g % len(c)])

    # for g in range(256):
    #     b.append(ord(c[g % len(c)]));

    f = 0
    for g in range(256):
        # f = g;
        f = (f + h[g] + b[g]) % 256;
        tmp = h[g];
        h[g] = h[f];
        h[f] = tmp

    # f = 0
    # for g in range(0, 256):
    #     f = (f + h[g] + b[g]) % 256
    #     tmp = h[g]
    #     h[g] = h[f]
    #     h[f] = tmp


    # t = "";
    # # k = k.split(str="");
    # for g in range(len(k)):
    #     p = f = g
    #     p = (p + 1) % 256;
    #     f = (f + h[p]) % 256;
    #     tmp = h[p];
    #     h[p] = h[f];
    #     h[f] = tmp;
    #     t += chr(k[g] ^ (h[(h[p] + h[f]) % 256]))
    #
    # t = t[26:]

    result = ""
    p = 0
    f = 0
    for g in range(0, len(k)):
        p = (p + 1) % 256;
        f = (f + h[p]) % 256
        tmp = h[p]
        h[p] = h[f]
        h[f] = tmp
        result += chr(k[g] ^ (h[(h[p] + h[f]) % 256]))
    result = result[26:]


    return result;

def md5(value):
    m2 = hashlib.md5()
    m2.update(value.encode("utf-8"));
    return m2.hexdigest();


# def decode_base64(data):
#     """Decode base64, padding being optional.
#     :param data: Base64 data as an ASCII byte string
#     :returns: The decoded byte string.
#     """
#     missing_padding = 4 - len(data) % 4
#     data = bytes(data, encoding='utf-8');
#     if missing_padding:
#         data += b'=' * missing_padding
#     return base64.b64decode(data);

def decode_base64(data):
    missing_padding=4-len(data)%4
    if missing_padding:
        data += '='* missing_padding
    return base64.b64decode(data)



if __name__ == '__main__':
    # print(decode_base64("l+qjJijEfI4vQdQKRhvKB3UvuUhBY4pFbdk+50aTy+nczxMsvO0UBabIKu6eCKClOsAP/uGtLTZvUrVORjWPISVgYkFGnnJKZw1vMPPcrbuGdaKlWQ"));

    # result = parse("a8738jp66tFag/CR0lPCP5Z6j6xMLZ/EgsqGK7aDeib4bOd/q7QhFBfibMGo/D/T8htn4UNoQDa60crcpVXZBuK2VWA5ghjMD8azKLryqigCXSoQxtPf/A","H5C7UxNkap5ZxckFrL8PSljODZxgpH37");
    result = jiandanDecode("9b63zzCk1EIXqXbtmRX/TnUOGDBIchgGVh+Dwqko+FcSoKJWMKEyWw6AVIl01qp3n8MA0AVD+0+pggj5uDT9id+WZ1oRTMW/aWgrBAIsAixnSSclzu7Oaw","H5C7UxNkap5ZxckFrL8PSljODZxgpH37");
    print(result);
