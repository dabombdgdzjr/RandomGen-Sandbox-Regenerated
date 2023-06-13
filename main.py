import time, random,

WHITE,CYAN,GREEN,ORANGE,PINK,BLUE,PURPLE,DARKCYAN,YELLOW,RED,BLACK, MAGENTA,BRIGHT_BLACK,BRIGHT_RED,BRIGHT_GREEN,BRIGHT_YELLOW,BRIGHT_BLUE,BRIGHT_MAGENTA,BRIGHT_CYAN,BRIGHT_WHITE = "\033[0;37m","\033[1;36m","\033[0;32m","\033[0;33m","\033[1;31m","\033[0;34m","\033[95m","\033[36m","\033[93m","\033[91m","\033[0;30m","\033[0;35m","\033[0;90m","\033[0;91m","\033[0;92m","\033[0;93m","\033[0;94m","\033[0;95m","\033[0;96m","\033[0;97m"
#bg = Background colors
bg_black = '\x1b[40m'
bg_red = '\x1b[41m'
bg_green = '\x1b[42m'
bg_yellow = '\x1b[43m'
bg_blue = '\x1b[44m'
bg_magenta = '\x1b[45m'
bg_cyan = '\x1b[46m'
bg_white = '\x1b[47m'
bg_grey = '\x1b[100m'
bg_bright_red = '\x1b[101m'
bg_bright_green = '\x1b[102m'
bg_bright_yellow = '\x1b[103m'
bg_bright_blue = '\x1b[104m'
bg_bright_magenta = '\x1b[105m'
bg_bright_cyan = '\x1b[106m'
bg_bright_white = '\x1b[107m'
#Extras
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'
CLEAR = '\033[H'
#--- MENU HERE --- #
# --- OR NOT LOL IM LAZY --- #
rnd = ["#", " ", " ", " "]
wall = f"{WHITE}█{BLUE}{bg_black}"
a = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],wall,]
b = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],wall,rnd[1],rnd[1],rnd[1],rnd[1],wall,]
c = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],wall,]
d = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],wall,rnd[1],rnd[1],rnd[1],rnd[1],wall,]
e = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],wall,]
f = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],wall,]
g = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],wall,rnd[1],rnd[1],rnd[1],rnd[1],wall,]
h = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],wall,]
i = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],wall,rnd[1],rnd[1],rnd[1],rnd[1],wall,]
j = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],wall,rnd[1],rnd[1],rnd[1],rnd[1],wall,]
k = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],wall,rnd[1],rnd[1],rnd[1],rnd[1],wall,]
l = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],wall,]
m = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],wall,rnd[1],rnd[1],rnd[1],rnd[1],wall,]
n = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],wall,]
o = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],wall,]
p = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],wall,rnd[1],rnd[1],rnd[1],rnd[1],wall,]
q = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],wall,]
r = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],wall,]
s = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],wall,rnd[1],rnd[1],rnd[1],rnd[1],wall,]
t = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],wall,]
u = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],wall,]
v = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],wall,rnd[1],rnd[1],rnd[1],rnd[1],wall,]
w = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],wall,]
x = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],wall,]
y = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],wall,rnd[1],rnd[1],rnd[1],wall,]
z = [random.choice(rnd),rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],rnd[1],wall,]


printToScreen = lambda:print(f"{bg_black}{a[0]}{b[0]}{c[0]}{d[0]}{e[0]}{f[0]}{g[0]}{h[0]}{i[0]}{j[0]}{k[0]}{l[0]}{m[0]}{n[0]}{o[0]}{p[0]}{q[0]}{r[0]}{s[0]}{t[0]}{u[0]}{v[0]}{w[0]}{x[0]}{y[0]}{z[0]}\n{a[1]}{b[1]}{c[1]}{d[1]}{e[1]}{f[1]}{g[1]}{h[1]}{i[1]}{j[1]}{k[1]}{l[1]}{m[1]}{n[1]}{o[1]}{p[1]}{q[1]}{r[1]}{s[1]}{t[1]}{u[1]}{v[1]}{w[1]}{x[1]}{y[1]}{z[1]}\n{a[2]}{b[2]}{c[2]}{d[2]}{e[2]}{f[2]}{g[2]}{h[2]}{i[2]}{j[2]}{k[2]}{l[2]}{m[2]}{n[2]}{o[2]}{p[2]}{q[2]}{r[2]}{s[2]}{t[2]}{u[2]}{v[2]}{w[2]}{x[2]}{y[2]}{z[2]}\n{a[3]}{b[3]}{c[3]}{d[3]}{e[3]}{f[3]}{g[3]}{h[3]}{i[3]}{j[3]}{k[3]}{l[3]}{m[3]}{n[3]}{o[3]}{p[3]}{q[3]}{r[3]}{s[3]}{t[3]}{u[3]}{v[3]}{w[3]}{x[3]}{y[3]}{z[3]}\n{a[4]}{b[4]}{c[4]}{d[4]}{e[4]}{f[4]}{g[4]}{h[4]}{i[4]}{j[4]}{k[4]}{l[4]}{m[4]}{n[4]}{o[4]}{p[4]}{q[4]}{r[4]}{s[4]}{t[4]}{u[4]}{v[4]}{w[4]}{x[4]}{y[4]}{z[4]}\n{a[5]}{b[5]}{c[5]}{d[5]}{e[5]}{f[5]}{g[5]}{h[5]}{i[5]}{j[5]}{k[5]}{l[5]}{m[5]}{n[5]}{o[5]}{p[5]}{q[5]}{r[5]}{s[5]}{t[5]}{u[5]}{v[5]}{w[5]}{x[5]}{y[5]}{z[5]}\n{a[6]}{b[6]}{c[6]}{d[6]}{e[6]}{f[6]}{g[6]}{h[6]}{i[6]}{j[6]}{k[6]}{l[6]}{m[6]}{n[6]}{o[6]}{p[6]}{q[6]}{r[6]}{s[6]}{t[6]}{u[6]}{v[6]}{w[6]}{x[6]}{y[6]}{z[6]}\n{a[7]}{b[7]}{c[7]}{d[7]}{e[7]}{f[7]}{g[7]}{h[7]}{i[7]}{j[7]}{k[7]}{l[7]}{m[7]}{n[7]}{o[7]}{p[7]}{q[7]}{r[7]}{s[7]}{t[7]}{u[7]}{v[7]}{w[7]}{x[7]}{y[7]}{z[7]}\n{a[8]}{b[8]}{c[8]}{d[8]}{e[8]}{f[8]}{g[8]}{h[8]}{i[8]}{j[8]}{k[8]}{l[8]}{m[8]}{n[8]}{o[8]}{p[8]}{q[8]}{r[8]}{s[8]}{t[8]}{u[8]}{v[8]}{w[8]}{x[8]}{y[8]}{z[8]}\n{a[9]}{b[9]}{c[9]}{d[9]}{e[9]}{f[9]}{g[9]}{h[9]}{i[9]}{j[9]}{k[9]}{l[9]}{m[9]}{n[9]}{o[9]}{p[9]}{q[9]}{r[9]}{s[9]}{t[9]}{u[9]}{v[9]}{w[9]}{x[9]}{y[9]}{z[9]}{END}")
vars = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
# --- ENGINE --- #
while True:
  for I in range(9):
    for item in vars:
      try:
        place = item.index("#")
        item[place] = f"{BLUE}{bg_black}*"
      except:
        pass
  for I in range(9):
    for item in vars:
      try:
        place = item.index(f"{BLUE}{bg_black}*")
        item[place] = f"{ORANGE}{BLUE}{bg_black}#"
        if item[place+1] == f"{WHITE}█{BLUE}{bg_black}":
          if item == vars[0]:
            vars[1][place] = "#"
          if item == vars[1]:
            vars[2][place] = "#"
            vars[0][place] = "#"
          if item == vars[2]:
            vars[3][place] = "#"
            vars[1][place] = "#"
          if item == vars[3]:
            vars[4][place] = "#"
            vars[2][place] = "#"
          if item == vars[4]:
            vars[5][place] = "#"
            vars[3][place] = "#"
          if item == vars[5]:
            vars[6][place] = "#"
            vars[4][place] = "#"
          if item == vars[6]:
            vars[7][place] = "#"
            vars[5][place] = "#"
          if item == vars[7]:
            vars[8][place] = "#"
            vars[6][place] = "#"
          if item == vars[8]:
            vars[9][place] = "#"
            vars[7][place] = "#"
          if item == vars[9]:
            vars[10][place] = "#"
            vars[8][place] = "#"
          if item == vars[10]:
            vars[11][place] = "#"
            vars[9][place] = "#"
          if item == vars[11]:
            vars[12][place] = "#"
            vars[10][place] = "#"
          if item == vars[12]:
            vars[13][place] = "#"
            vars[11][place] = "#"
          if item == vars[13]:
            vars[14][place] = "#"
            vars[12][place] = "#"
          if item == vars[14]:
            vars[15][place] = "#"
            vars[13][place] = "#"
          if item == vars[15]:
            vars[16][place] = "#"
            vars[14][place] = "#"
          if item == vars[16]:
            vars[17][place] = "#"
            vars[15][place] = "#"
          if item == vars[17]:
            vars[18][place] = "#"
            vars[16][place] = "#"
          if item == vars[18]:
            vars[19][place] = "#"
            vars[17][place] = "#"
          if item == vars[19]:
            vars[20][place] = "#"
            vars[18][place] = "#"
          if item == vars[20]:
            vars[21][place] = "#"
            vars[19][place] = "#"
          if item == vars[21]:
            vars[22][place] = "#"
            vars[20][place] = "#"
          if item == vars[22]:
            vars[23][place] = "#"
            vars[21][place] = "#"
          if item == vars[24]:
            vars[23][place] = "#"
            vars[25][place] = "#"
          if item == vars[25]:
            vars[26][place] = "#"
            vars[24][place] = "#"
          if item == vars[26]:
            vars[25][place] = "#"
        else:
          item[place+1] = "#"
      except:
        pass
  print(CLEAR)
  printToScreen()
  time.sleep(.5)
