︠c2150ae0-d246-4f6d-9d7a-dbb45ad8ff68︠
ftophat(s,r, R)=((tanh(s*(r+R)))-(tanh(s*(r-R))))/(2*tanh(s*R))
xshift(x, xs) = x-xs
#fhts = [plot(c*sin(x), (-2*pi,2*pi), color=Color(c,0,0), ymin=-1,ymax=1) for c in sxrange(0,1,.2)]
fhts = [plot(ftophat(23, x-xs, 1), (1,17), color=Color(0,0,0), ymin=-0.1,ymax=1.1,xmin=0,xmax=18) for xs in sxrange(2.1,17,.2)]
b = animate(fhts)
b
b.show()
︡a35c99f7-6e77-4605-825b-f3326397759b︡{"once":false,"file":{"show":true,"uuid":"8d22a2bd-52d7-41c8-bc82-2793489cfc3c","filename":"/projects/fcf5aea1-72c1-4a0d-9b0d-2bff298bbe93/.sage/temp/compute3dc2/18433/tmp_t4MUS2.gif"}}︡{"once":false,"file":{"show":true,"uuid":"8d22a2bd-52d7-41c8-bc82-2793489cfc3c","filename":"/projects/fcf5aea1-72c1-4a0d-9b0d-2bff298bbe93/.sage/temp/compute3dc2/18433/tmp_rrfsiK.gif"}}︡
︠445d2966-4379-45d8-b9b2-8cb20d587e98︠









