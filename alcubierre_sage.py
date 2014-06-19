
{{{id=1|
ftophat(s,r, R)=((tanh(s*(r+R)))-(tanh(s*(r-R))))/(2*tanh(s*R))
///
}}}

{{{id=2|
print ftophat
///
(s, r, R) |--> 1/2*(tanh((R + r)*s) - tanh(-(R - r)*s))/tanh(R*s)
}}}

{{{id=3|
plot(ftophat(8, r, 1))
///
<html><font color='black'><img src='cell://sage0.png'></font></html>
}}}

{{{id=4|
derivative(f)
///
cosh(x)
}}}

{{{id=5|
@interact
def _(sigma=(1..23)):
  ftp = ftophat(sigma, r, 1)
  pt = plot(ftp, -2, 2,color='blue', thickness=2)
  show(pt, ymin = -0.1, ymax = 1.1)
///
}}}

{{{id=6|
dtophat = diff(ftophat, r)
///
}}}

{{{id=8|
dtophat
///
(s, r, R) |--> -1/2*((tanh((R + r)*s)^2 - 1)*s - (tanh(-(R - r)*s)^2 - 1)*s)/tanh(R*s)
}}}

{{{id=9|
plot(dtophat(8, r, 1), -2, 2)
///
<html><font color='black'><img src='cell://sage0.png'></font></html>
}}}

{{{id=10|
shift = x+2
///
}}}

{{{id=11|
plot(ftophat(8, shift(x), 1), -4, 1)
///
<html><font color='black'><img src='cell://sage0.png'></font></html>
}}}

{{{id=12|
r_rho(x, xs, rho) = ((x-xs)^2 + rho^2)^(1/2)
///
}}}

{{{id=13|
x_offset(x, xs) = x-xs
///
}}}

{{{id=14|
xs = 27
warp(x, rho) = (x_offset(x, xs)/r_rho(x, xs, rho))*(dtophat(8, r_rho(x, xs, rho), 1))
plot3d(warp(x, rho), (x, 25.5, 28.5), (rho, -1.5, 1.5), color='brown')
///
}}}

{{{id=15|

///
}}}