from generate import *
import sys

# flags 
# Minion seq (+ how many processes)
# Minion parallel (+ how many processes)
# NBCMiniSAT
def test(testMinionSeq,testMinionPar,testNBCSAT):
    if testMinionSeq:
        run([0,5],5,[False],False)
    elif testMinionPar:
        run([0,5],5,[True,2],False)
    elif testNBCSAT:
        run([0,5],5,[False],True)

# test(True,False,False)
# test(False,True,False)
# test(False,False,True)


inargs = sys.argv[1:]
if len(inargs) == 0:
    print('Arguments need to be given')
    print('<Minimal permutations length> <Maximal perm length> <solver> <solver options, optional>')
    print('Solvers are minionseq , minionpar (which needs the number of processes as well), nbcsat')
    print('If no solver is given minionseq is standard')

if inargs[0] == 'testms':
    run([0,5],5,[False],False)
elif inargs[0] == 'testmp':
    run([0,5],5,[True,2],False)
elif inargs[0] == 'testnsat':
    run([0,5],5,[False],True)
elif inargs[2] == 'minionseq':
    run([0,comb(int(inargs[1]),2)],int(inargs[0]),int(inargs[1]),[False],False)
elif inargs[2] == 'minionpar':
    run([0,comb(int(inargs[1]),2)],int(inargs[0]),int(inargs[1]),[True,int(inargs[2])],False)
elif inargs[2] == 'nbcsat':
    run([0,comb(int(inargs[1]),2)],int(inargs[0]),int(inargs[1]),[False],True)