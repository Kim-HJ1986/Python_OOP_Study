def copyright(func):
    def new_func():
        print("@Copyright")
        func()
        return "end!"

    return new_func


def smile():
    print("๐")


def sunglass():
    print("๐")


def angry():
    print("๐คฌ")


def doggy():
    print("๐ถ")


def madness():
    print("๐น")


def scary():
    print("๐ซ")


def hmm():
    print("๐ค")


def surprise():
    print("๐จ")


# ์๋ก์ด ํจ์๋ก ์ฌ์ ์ ํด์ค๋ค. ์ด ๋, ๊ฐ object๋ ์๋ก์ด ํจ์๋ก ์ฌ์ ์ ๋๋ค.
# ์๋ฅผ ๋ค์ด, smile์ ๊ฒฝ์ฐ copyright()๋ก ์ฌ์ ์ ๋๋ค.
# ์ด๋ smile์ ์ฌ์ ์๋ ํจ์์ด๋ฉฐ,
# ์๊ดํธ ()๋ฅผ ๋ถ์ผ ๊ฒฝ์ฐ ์คํํ๋ผ๋ ๋ป์ด ๋์ด,
# smile()์ return ๊ฐ์ธ None์ด ์ธ์๋ก ๋์ด๊ฐ not callable ์ค๋ฅ๊ฐ ๋ฐ์ํ๋ค.
smile = copyright(smile)
sunglass = copyright(sunglass)
angry = copyright(angry)
doggy = copyright(doggy)
madness = copyright(madness)
scary = copyright(scary)
hmm = copyright(hmm)
surprise = copyright(surprise)

# smile()
# sunglass()
# angry()
# doggy()
# madness()
# scary()
# hmm()
# surprise()

print(smile)
# ํจ์ ์์ฒด๋ฅผ printํ๋ฉด smile์ด ๋จผ์  ์คํ๋๊ณ  -> copyright(smile)
# ํด๋น ํจ์์ return ๊ฐ์ printํ๋ค. ์ฌ๊ธฐ์์  copyright์ return ๊ฐ์ด ์์ผ๋ฏ๋ก None ์ด ์ฐํ๋ค.
# ํ์ฌ๋ return ๊ฐ์ end! ๋ก ์ง์ ํ์ฌ, end! ๊ฐ ์ฐํ๋ค.
print(smile())
