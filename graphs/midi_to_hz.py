import matplotlib.pyplot as plt
import numpy as np

"""
The standard mineiro function is the only viable fast option
for accuracy, although the speed improvements are only minor.
If accuracy at high frequencies isn't nececarry, then the
fast mineiro function is a great choice.

The following table compares the speed and error margin of
different pow(2, x) approxiamtions used in the following formula:
    440 * pow(2, (midi - 69) / 12)

SEC      xSPEED ERROR  NAME
0.055522               pass
0.085976 1      0      stl64
0.084367 1.05   bad    desoras64
0.073314 1.71   bad    ankerl64
0.081256 1      0      stl32
0.091158 0.72   bad    ekmett_fast_precise
0.090583 0.73   bad    ekmett_fast_better_precise
0.077771 1.15   0.005  mineiro            -- amazing at all ranges
0.065949 2.46   bad    exp - ekmett_ub
0.063300 3.3    400    shraudolph         -- very similar to mineiro_faster. More accurate at
0.063001 3.43   bad    ekmett_fast_ub
0.062901 3.47   bad    ekmett_fast
0.062841 3.5    35     ekmett_fast_lb     -- really bad between 500 - 1000Hz. Quite accurate at any other frequency
0.061775 4.09   400    mineiro_faster     -- ~0.4hz error at 50hz, 4Hz error at 500hz, 120Hz error at 5kHz. Quite good


- pass = no processing
- stl = std::pow(2, x)
- xSpeed of the pow2 function calculated: (stl_sec - pass) / (other_sec - pass)
- Error is in Hz
"""

class Styles:
    idx = 0
    types = ['solid', 'dotted', 'dashed', 'dashdot']

    def get(self):
        s = self.types[self.idx]
        self.idx = (self.idx + 1) & 3
        return s

linestyles = Styles()

fig, ax = plt.subplots()

x_labels = [1,     2,    5,
            10,    20,   50,
            100,   200,  500,
            1000,  2000, 5000,
            10000, 20000]
x_ticks = [i for i in range(len(x_labels))]

plt.xlabel('Frequencyy in Hz')
plt.xticks(ticks=x_ticks, labels=x_labels)
plt.ylabel('Hz')

stl64 = [1.00000023842,2.00000047684,4.99999856949,9.99999713898,20,50.0000076294,100.000015259,200.000030518,500.000061035,1000.00012207,2000.00024414,5000.00048828,10000.0009766,20000.0019531,]
ankerl64 = [0.709617733955,1.46906578541,3.80887722969,8.01639652252,16.8300914764,44.62109375,92.4313278198,191.240936279,500.338775635,1051.70385742,2205.45996094,5813.92041016,12036.0507812,24888.5195312,]
stl32 = [1.00000011921,2.00000071526,4.99999809265,9.9999961853,19.9999980927,50.0000038147,100.000007629,200.000030518,500.000061035,1000.00012207,2000.00024414,5000,10000.0009766,20000.0019531,]
ekmett_fast = [0.709617733955,1.46906495094,3.80886077881,8.01640987396,16.8300914764,44.6212005615,92.4314880371,191.241149902,500.340881348,1051.70043945,2205.45166016,5813.94042969,12036.0839844,24888.5742188,]
ekmett_fast_lb = [0.973300933838,1.94660186768,4.99981164932,9.99962329865,19.9992465973,48.8515663147,97.7031326294,195.406265259,483.274230957,966.541748047,1933.08349609,4999.36035156,9998.72070312,19997.4414062,]
ekmett_fast_ub = [0.628553032875,1.33107662201,3.41102480888,7.36081123352,15.9051513672,43.7922477722,92.318611145,194.104614258,528.13293457,1132.01171875,2415.48828125,6364.69238281,13335.3515625,27882.421875,]
ekmett_fast_precise = [0.964854419231,1.92970883846,4.71072864532,9.42145729065,18.8429145813,48.3514556885,96.702911377,193.405822754,521.147155762,1042.29431152,2084.58862305,5302.37060547,10604.7412109,21209.4824219,]
ekmett_fast_better_precise = [0.786740005016,1.573480010033,4.347667217255,8.695334434509,17.390668869019,48.672134399414,97.344268798828,194.688537597656,522.970275878906,1045.940551757812,2091.881103515625,5836.787109375,11673.57421875,23347.1484375,]
mineiro = [0.99995970726,1.99991941452,4.99999523163,9.99999046326,19.9999809265,49.997959137,99.9959182739,199.991836548,499.974975586,999.963378906,1999.92675781,5000.00488281,10000.0097656,20000.0195312,]
mineiro_faster = [0.998025536537,1.99605107307,5.09871006012,10.1974201202,20.3948402405,49.6427536011,99.2855072021,198.571014404,495.933227539,991.866455078,1983.73291016,5100.65917969,10201.3183594,20402.6367188,]
schraudolph = [0.997442007065,1.994884014130,5.096375942230,10.192751884460,20.385503768921,49.624080657959,99.248161315918,198.496322631836,495.634460449219,991.262207031250,1982.524414062500,5098.242187500000,10196.484375000000,20392.968750000000,]
desoras = [1.047268986702,2.094537973404,5.295701980591,10.591403961182,21.182815551758,51.218658447266,102.437316894531,204.874633789062,521.146850585938,1042.293823242188,2084.587890625000,5302.362304687500,10604.724609375000,21209.449218750000,]
exp_ekmett_ub = [1.047271490097,2.094542980194,5.295693874359,10.591387748718,21.182775497437,51.218624114990,102.437248229980,204.874496459961,521.147155761719,1042.28759765625,2084.5751953125,5302.34375,10604.6875,21209.375,]

x = [i for i in range(len(stl64))]

# ax.plot(stl64, label='stl64', linestyle=linestyles.get())
# ax.plot(ankerl64, label='ankerl64', linestyle=linestyles.get())
ax.plot(stl32, label='stl32', linestyle=linestyles.get())
# ax.plot(ekmett_fast, label='ekmett_fast', linestyle=linestyles.get())
# ax.plot(ekmett_fast_lb, label='ekmett_fast_lb', linestyle=linestyles.get())
# ax.plot(ekmett_fast_ub, label='ekmett_fast_ub', linestyle=linestyles.get())
# ax.plot(ekmett_fast_precise, label='ekmett_fast_precise', linestyle=linestyles.get())
# ax.plot(ekmett_fast_better_precise, label='ekmett_fast_better_precise', linestyle=linestyles.get())
# ax.plot(mineiro, label='mineiro', linestyle=linestyles.get())
ax.plot(schraudolph, label='schraudolph', linestyle=linestyles.get())
ax.plot(mineiro_faster, label='mineiro_faster', linestyle=linestyles.get())
# ax.plot(exp_ekmett_ub, label='exp_ekmett_ub', linestyle=linestyles.get())
ax.plot(desoras, label='desoras', linestyle=linestyles.get())

ax.legend()
plt.show()
