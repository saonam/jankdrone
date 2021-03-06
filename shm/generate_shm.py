#!/usr/bin/env python3

from lib.pyratemp import pyratemp
import shm

templates = [
    ('../drone/src/shm.cpp.template', '../drone/src/shm.cpp'),
    ('../drone/src/shm.h.template', '../drone/src/shm.h'),
    ('../handheld/src/shm.h.template', '../handheld/src/shm.h'),
    ('../client/shmdef.go.template', '../client/shmdef.go'),
]

if __name__ == '__main__':
    for t in templates:
        pt = pyratemp.Template(filename=t[0])
        with open(t[1], 'w') as out:
            out.write(pt(shm=shm.shm))
