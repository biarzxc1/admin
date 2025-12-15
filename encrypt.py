#!/usr/bin/env python3
import os
import sys
import subprocess
import random
import time
import marshal
import lzma
import gzip
import bz2
import zlib
import binascii
from typing import Optional
import py_compile
try:
    import requests
    import tqdm
    import colorama
    import pyfiglet
except ModuleNotFoundError:
    requests = tqdm = colorama = pyfiglet = None
def prett(text: str) -> str:
    try:
        return text.title().center(os.get_terminal_size().columns)
    except OSError:
        return text.title()
PYTHON_VERSION = "python" + ".".join(str(i) for i in sys.version_info[:2])
if colorama:
    colorama.init(autoreset=True)
    BLU = colorama.Style.BRIGHT + colorama.Fore.BLUE
    CYA = colorama.Style.BRIGHT + colorama.Fore.CYAN
    GRE = colorama.Style.BRIGHT + colorama.Fore.GREEN
    YEL = colorama.Style.BRIGHT + colorama.Fore.YELLOW
    RED = colorama.Style.BRIGHT + colorama.Fore.RED
    WHI = colorama.Style.BRIGHT + colorama.Fore.WHITE
    MAG = colorama.Style.BRIGHT + colorama.Fore.MAGENTA
    LIYEL = colorama.Style.BRIGHT + colorama.Fore.LIGHTYELLOW_EX
    LIRED = colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX
    LIMAG = colorama.Style.BRIGHT + colorama.Fore.LIGHTMAGENTA_EX
    LIBLU = colorama.Style.BRIGHT + colorama.Fore.LIGHTBLUE_EX
    LICYA = colorama.Style.BRIGHT + colorama.Fore.LIGHTCYAN_EX
    LIGRE = colorama.Style.BRIGHT + colorama.Fore.LIGHTGREEN_EX
else:
    BLU = CYA = GRE = YEL = RED = MAG = LIYEL = LIRED = LIMAG = LIBLU = LICYA = LIGRE = ""
CLEAR = "cls" if os.name == "nt" else "clear"
COLORS = (BLU, CYA, GRE, YEL, RED, MAG, LIYEL, LIRED, LIMAG, LIBLU, LICYA, LIGRE)
FONTS = ("basic", "o8", "cosmic", "graffiti", "chunky", "epic", "poison", "doom", "avatar")
try:
    GZ_DECOMP = gzip.decompress
    ZL_DECOMP = zlib.decompress
    BZ_DECOMP = bz2.decompress
    LZ_DECOMP = lzma.decompress
    UNHEX = binascii.unhexlify
    A2B_QP = binascii.a2b_qp
    A2B_B64 = binascii.a2b_base64
except Exception:
    GZ_DECOMP = ZL_DECOMP = BZ_DECOMP = LZ_DECOMP = UNHEX = A2B_QP = A2B_B64 = None

MODES = [lzma, gzip, bz2, zlib, binascii]

def encode(source: str, layers: int = 10, seed: Optional[int] = None) -> str:
    if seed is not None:
        random.seed(seed)
    data = marshal.dumps(compile(source, "<x>", "exec"))
    stack = []
    current = data
    for _ in range(layers):
        mode = random.choice(MODES)
        stack.append(mode)
        if mode is binascii:
            current = binascii.b2a_base64(current)
        else:
            current = mode.compress(current)
    innermost = stack[-1]
    if innermost is binascii:
        expr = f"binascii.a2b_base64({repr(current)})"
    else:
        expr = f"{innermost.__name__}.decompress({repr(current)})"
    for mode in reversed(stack[:-1]):
        if mode is binascii:
            expr = f"binascii.a2b_base64({expr})"
        else:
            expr = f"{mode.__name__}.decompress({expr})"
    final_code = f"import marshal,lzma,gzip,bz2,zlib,binascii;exec(marshal.loads({expr}))"
    return final_code

def logo() -> None:
    try:
        subprocess.run([CLEAR], shell=True)
    except Exception:
        pass
    if pyfiglet:
        font = random.choice(FONTS)
        color1, color2 = random.choice(COLORS), random.choice(COLORS)
        while color1 == color2:
            color2 = random.choice(COLORS)
        width = 80
        try:
            width = os.get_terminal_size().columns
        except OSError:
            pass
        print(WHI + prett("______________________________________________________________________"))
        print(color2 + pyfiglet.figlet_format("ENCRYPTION", font=font, justify="center", width=width), end="")
        print(WHI + prett("______________________________________________________________________"))
        print("         AUTHOR : ERROR X ETHAN | TYPE : ENCRYPTION TOOL/SCRIPT\n         SATUTS : FREE | VERSION : 1.0")
        print(WHI + prett("______________________________________________________________________"))
    else:
        pass

def read_speed(prompt: str = "SPEED (SECONDS DELAY, 0 FOR NONE) [DEFAULT 0.1]: ") -> float:
    s = input(prompt).strip()
    if s == "":
        return 0.1
    try:
        v = float(s)
    except ValueError:
        print(f"{RED}INVALID SPEED — USING DEFAULT 0.1S.")
        return 0.1
    if v < 0:
        v = 0.0
    elif v > 5.0:
        v = 5.0
    return v

def main():
    logo()
    inp = input("INPUT FILE PATH: ").strip()
    print(WHI + prett("______________________________________________________________________"))
    if not inp:
        print(f"{RED}INPUT PATH IS REQUIRED")
        sys.exit(1)
    outp = input("OUTPUT FILE PATH: ").strip()
    print(WHI + prett("______________________________________________________________________"))
    if not outp:
        print("{RED}OUTPUT PATH IS REQUIRED")
        sys.exit(1)
    # safe speed parsing (replaces the raw speed=input("") line)
    print(WHI + prett("______________________________________________________________________"))
    delay = read_speed()
    comp_input = input("COMPLEXITY (e.g. 10) [default 10]: ").strip()
    print(WHI + prett("______________________________________________________________________"))
    try:
        complexity = int(comp_input) if comp_input else 10
    except ValueError:
        complexity = 10
    if complexity < 1:
        complexity = 1
    elif complexity > 50:
        complexity = 50
    print(random.choice(COLORS) + "ENCODING ".title() + inp)
    try:
        with open(inp, "r", encoding="utf-8") as iput:
            src = iput.read()
    except Exception as e:
        print(f"{RED}COULD NOT READ INPUT FILE: {e}")
        sys.exit(1)
    encoded_snippet = src
    if tqdm:
        pbar = tqdm.tqdm(total=1)
    else:
        pbar = None
    try:
        encoded_snippet = encode(src, layers=complexity)
        if pbar:
            pbar.update(1)
        if delay:
            time.sleep(delay)
    finally:
        if pbar:
            pbar.close()
    try:
        data = f'# Obfuscate By Error x Ethan\ntry:\n\t{encoded_snippet}\nexcept KeyboardInterrupt:\n\texit()\n'
        z = [ord(c) for c in data]
        sata = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z
        with open(outp, "w", encoding="utf-8") as f:
            f.write(sata)
        py_compile.compile(outp,outp)
    except Exception as e:
        print(f"{RED}COULD NOT WRITE OUTPUT FILE: {e}")
        sys.exit(1)
    print(f"{LIGRE}ENCODING SUCCESSFULLY!\n{WHI}______________________________________________________________________\n{LIGRE}SAVED AS ".title() + outp)

if __name__ == "__main__":
    main()
