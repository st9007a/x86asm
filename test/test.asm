.DATA
ALPHA   DB 1
BETA    DW A1
.CODE
        MOV AX, BX
        ADD AH, 1
LABEL1  MOV DL, [AL]
        ADD DL, LABEL1
